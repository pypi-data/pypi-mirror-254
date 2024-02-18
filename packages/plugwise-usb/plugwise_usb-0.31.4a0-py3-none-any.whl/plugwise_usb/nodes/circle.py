"""Plugwise Circle node object."""
from datetime import datetime, timedelta
import logging

from ..constants import (
    FEATURE_ENERGY_CONSUMPTION_TODAY,
    FEATURE_PING,
    FEATURE_POWER_CONSUMPTION_CURRENT_HOUR,
    FEATURE_POWER_CONSUMPTION_PREVIOUS_HOUR,
    FEATURE_POWER_CONSUMPTION_TODAY,
    FEATURE_POWER_CONSUMPTION_YESTERDAY,
    FEATURE_POWER_PRODUCTION_CURRENT_HOUR,
    FEATURE_POWER_USE,
    FEATURE_POWER_USE_LAST_8_SEC,
    FEATURE_RELAY,
    FEATURE_RSSI_IN,
    FEATURE_RSSI_OUT,
    MAX_TIME_DRIFT,
    MESSAGE_TIME_OUT,
    PRIORITY_HIGH,
    PRIORITY_LOW,
    PULSES_PER_KW_SECOND,
    RELAY_SWITCHED_OFF,
    RELAY_SWITCHED_ON,
)
from ..messages.requests import (
    CircleCalibrationRequest,
    CircleClockGetRequest,
    CircleClockSetRequest,
    CircleEnergyCountersRequest,
    CirclePowerUsageRequest,
    CircleSwitchRelayRequest,
)
from ..messages.responses import (
    CircleCalibrationResponse,
    CircleClockResponse,
    CircleEnergyCountersResponse,
    CirclePowerUsageResponse,
    NodeAckLargeResponse,
)
from ..nodes import PlugwiseNode

_LOGGER = logging.getLogger(__name__)


class PlugwiseCircle(PlugwiseNode):
    """provides interface to the Plugwise Circle nodes and base class for Circle+ nodes"""

    def __init__(self, mac, address, message_sender):
        super().__init__(mac, address, message_sender)
        self._features = (
            FEATURE_ENERGY_CONSUMPTION_TODAY["id"],
            FEATURE_PING["id"],
            FEATURE_POWER_USE["id"],
            FEATURE_POWER_USE_LAST_8_SEC["id"],
            FEATURE_POWER_CONSUMPTION_CURRENT_HOUR["id"],
            FEATURE_POWER_CONSUMPTION_PREVIOUS_HOUR["id"],
            FEATURE_POWER_CONSUMPTION_TODAY["id"],
            FEATURE_POWER_CONSUMPTION_YESTERDAY["id"],
            FEATURE_POWER_PRODUCTION_CURRENT_HOUR["id"],
            # FEATURE_POWER_PRODUCTION_PREVIOUS_HOUR["id"],
            FEATURE_RSSI_IN["id"],
            FEATURE_RSSI_OUT["id"],
            FEATURE_RELAY["id"],
        )
        self._last_collected_address = None
        self._last_collected_address_slot = 0
        self._last_collected_address_timestamp = datetime(2000, 1, 1)
        self._energy_consumption_today_reset = datetime.now().replace(
            hour=0, minute=0, second=0, microsecond=0
        )
        self._energy_memory = {}
        self._energy_history = {}
        self._energy_history_failed_address = []
        self._energy_last_collected_timestamp = datetime(2000, 1, 1)
        self._energy_last_collected_count = 0
        self._energy_ratelimit_collection_timestamp = datetime.utcnow()
        self._energy_last_rollover_timestamp = datetime.utcnow()
        self._energy_pulses_midnight_rollover = datetime.utcnow()
        self._energy_last_local_hour = datetime.now().hour
        self._energy_last_populated_slot = 0
        self._energy_pulses_current_hour = None
        self._energy_pulses_prev_hour = None
        self._energy_pulses_today_hourly = None
        self._energy_pulses_today_now = None
        self._energy_pulses_yesterday = None
        self._new_relay_state = False
        self._new_relay_stamp = datetime.now() - timedelta(seconds=MESSAGE_TIME_OUT)
        self._pulses_1s = None
        self._pulses_8s = None
        self._pulses_produced_1h = None
        self.calibration = False
        self._gain_a = None
        self._gain_b = None
        self._off_noise = None
        self._off_tot = None
        self._measures_power = True
        self._last_log_collected = False
        self.timezone_delta = datetime.now().replace(
            minute=0, second=0, microsecond=0
        ) - datetime.utcnow().replace(minute=0, second=0, microsecond=0)
        self._clock_offset = None
        self._last_clock_sync_day = datetime.now().day
        self.get_clock(self.sync_clock)
        self._request_calibration()

    @property
    def current_power_usage(self):
        """Returns power usage during the last second in Watts
        Based on last received power usage information
        """
        if self._pulses_1s is not None:
            return self.pulses_to_kws(self._pulses_1s) * 1000
        return None

    @property
    def current_power_usage_8_sec(self):
        """Returns power usage during the last 8 second in Watts
        Based on last received power usage information
        """
        if self._pulses_8s is not None:
            return self.pulses_to_kws(self._pulses_8s, 8) * 1000
        return None

    @property
    def energy_consumption_today(self) -> float:
        """Returns total energy consumption since midnight in kWh"""
        if self._energy_pulses_today_now is not None:
            return self.pulses_to_kws(self._energy_pulses_today_now, 3600)
        return None

    @property
    def energy_consumption_today_last_reset(self):
        """Last reset of total energy consumption today"""
        return self._energy_consumption_today_reset

    @property
    def power_consumption_current_hour(self):
        """Returns the power usage during this running hour in kWh
        Based on last received power usage information
        """
        if self._energy_pulses_current_hour is not None:
            return self.pulses_to_kws(self._energy_pulses_current_hour, 3600)
        return None

    @property
    def power_consumption_previous_hour(self):
        """Returns power consumption during the previous hour in kWh"""
        if self._energy_pulses_prev_hour is not None:
            return self.pulses_to_kws(self._energy_pulses_prev_hour, 3600)
        return None

    @property
    def power_consumption_today(self):
        """Total power consumption during today in kWh"""
        if self._energy_pulses_today_hourly is not None:
            return self.pulses_to_kws(self._energy_pulses_today_hourly, 3600)
        return None

    @property
    def power_consumption_yesterday(self):
        """Total power consumption of yesterday in kWh"""
        if self._energy_pulses_yesterday is not None:
            return self.pulses_to_kws(self._energy_pulses_yesterday, 3600)
        return None

    @property
    def power_production_current_hour(self):
        """Returns the power production during this running hour in kWh
        Based on last received power usage information
        """
        if self._pulses_produced_1h is not None:
            return self.pulses_to_kws(self._pulses_produced_1h, 3600)
        return None

    @property
    def relay_state(self) -> bool:
        """Return last known relay state or the new switch state by anticipating
        the acknowledge for new state is getting in before message timeout.
        """
        if self._new_relay_stamp + timedelta(seconds=MESSAGE_TIME_OUT) > datetime.now():
            return self._new_relay_state
        return self._relay_state

    @relay_state.setter
    def relay_state(self, state):
        """Request the relay to switch state."""
        self._request_switch(state)
        self._new_relay_state = state
        self._new_relay_stamp = datetime.now()
        if state != self._relay_state:
            self.do_callback(FEATURE_RELAY["id"])

    def _request_calibration(self, callback=None):
        """Request calibration info"""
        self.message_sender(
            CircleCalibrationRequest(self._mac),
            callback,
            0,
            PRIORITY_HIGH,
        )

    def _request_switch(self, state, callback=None):
        """Request to switch relay state and request state info"""
        self.message_sender(
            CircleSwitchRelayRequest(self._mac, state),
            callback,
            0,
            PRIORITY_HIGH,
        )

    def request_power_update(self, callback=None):
        """Request power usage and update energy counters"""
        if self._available:
            self.message_sender(
                CirclePowerUsageRequest(self._mac),
                callback,
            )
            _timestamp_utcnow = datetime.utcnow()
            # Request new energy counters if last one is more than one hour ago
            if self._energy_last_collected_timestamp < _timestamp_utcnow.replace(
                minute=0, second=0, microsecond=0
            ):
                _LOGGER.info("Queue _last_log_address for %s at %s last_collected %s",
                              str(self.mac),str(self._last_log_address),
                             self._energy_last_collected_timestamp
                )
                self._request_info(self.push_last_log_address)

            if len(self._energy_history_failed_address) > 0:
                    _mem_address = self._energy_history_failed_address.pop(0)
                    if self._energy_memory.get(_mem_address, 0) < 4:
                        _LOGGER.info("Collect EnergyCounters for %s at %s",
                                     str(self.mac),
                                    str(_mem_address),
                        )
                        self.request_energy_counters(_mem_address)
                        self._energy_ratelimit_collection_timestamp = _timestamp_utcnow
                    else:
                        _LOGGER.info(
                            "Drop known request_energy_counters for %s at %s and clock sync",
                            str(self.mac),
                            str(_mem_address),
                        )
                        self.get_clock(self.sync_clock)
            if datetime.now().day != self._last_clock_sync_day:
                self._last_clock_sync_day = datetime.now().day
                self.get_clock(self.sync_clock)

    def push_last_log_address(self):
        if self._energy_history_failed_address.count(self._last_log_address) == 0:
            self._energy_history_failed_address.append(self._last_log_address)

    def message_for_circle(self, message):
        """Process received message
        """
        if isinstance(message, CirclePowerUsageResponse):
            if self.calibration:
                self._response_power_usage(message)
                _LOGGER.debug(
                    "Power update for %s, last update %s",
                    str(self.mac),
                    str(self._last_update),
                )
            else:
                _LOGGER.info(
                    "Received power update for %s before calibration information is known",
                    str(self.mac),
                )
                self._request_calibration(self.request_power_update)
        elif isinstance(message, NodeAckLargeResponse):
            self._node_ack_response(message)
        elif isinstance(message, CircleCalibrationResponse):
            self._response_calibration(message)
        elif isinstance(message, CircleEnergyCountersResponse):
            if self.calibration:
                self._response_energy_counters(message)
            else:
                _LOGGER.debug(
                    "Received power buffer log for %s before calibration information is known",
                    str(self.mac),
                )
                self._request_calibration(self.request_energy_counters)
        elif isinstance(message, CircleClockResponse):
            self._response_clock(message)
        else:
            self.message_for_circle_plus(message)

    def message_for_circle_plus(self, message):
        """Pass messages to PlugwiseCirclePlus class"""

    def _node_ack_response(self, message):
        """Process switch response message"""
        if message.ack_id == RELAY_SWITCHED_ON:
            if not self._relay_state:
                _LOGGER.debug(
                    "Switch relay on for %s",
                    str(self.mac),
                )
                self._relay_state = True
                self.do_callback(FEATURE_RELAY["id"])
        elif message.ack_id == RELAY_SWITCHED_OFF:
            if self._relay_state:
                _LOGGER.debug(
                    "Switch relay off for %s",
                    str(self.mac),
                )
                self._relay_state = False
                self.do_callback(FEATURE_RELAY["id"])
        else:
            _LOGGER.debug(
                "Unmanaged _node_ack_response %s received for %s",
                str(message.ack_id),
                str(self.mac),
            )

    def _response_power_usage(self, message: CirclePowerUsageResponse):
        # Sometimes the circle returns -1 for some of the pulse counters
        # likely this means the circle measures very little power and is suffering from
        # rounding errors. Zero these out. However, negative pulse values are valid
        # for power producing appliances, like solar panels, so don't complain too loudly.

        # Power consumption last second
        if message.pulse_1s.value == -1:
            message.pulse_1s.value = 0
            _LOGGER.debug(
                "1 sec power pulse counter for node %s has value of -1, corrected to 0",
                str(self.mac),
            )
        self._pulses_1s = message.pulse_1s.value
        if message.pulse_1s.value != 0:
            if message.nanosecond_offset.value != 0:
                pulses_1s = (
                    message.pulse_1s.value
                    * (1000000000 + message.nanosecond_offset.value)
                ) / 1000000000
            else:
                pulses_1s = message.pulse_1s.value
            self._pulses_1s = pulses_1s
        else:
            self._pulses_1s = 0
        self.do_callback(FEATURE_POWER_USE["id"])
        # Power consumption last 8 seconds
        if message.pulse_8s.value == -1:
            message.pulse_8s.value = 0
            _LOGGER.debug(
                "8 sec power pulse counter for node %s has value of -1, corrected to 0",
                str(self.mac),
            )
        if message.pulse_8s.value != 0:
            if message.nanosecond_offset.value != 0:
                pulses_8s = (
                    message.pulse_8s.value
                    * (1000000000 + message.nanosecond_offset.value)
                ) / 1000000000
            else:
                pulses_8s = message.pulse_8s.value
            self._pulses_8s = pulses_8s
        else:
            self._pulses_8s = 0
        self.do_callback(FEATURE_POWER_USE_LAST_8_SEC["id"])
        # Power consumption current hour
        if message.pulse_hour_consumed.value == -1:
            _LOGGER.debug(
                "1 hour consumption power pulse counter for node %s has value of -1, drop value",
                str(self.mac),
            )
        else:
            self._update_energy_current_hour(message.pulse_hour_consumed.value)

        # Power produced current hour
        if message.pulse_hour_produced.value == -1:
            message.pulse_hour_produced.value = 0
            _LOGGER.debug(
                "1 hour power production pulse counter for node %s has value of -1, corrected to 0",
                str(self.mac),
            )
        if self._pulses_produced_1h != message.pulse_hour_produced.value:
            self._pulses_produced_1h = message.pulse_hour_produced.value
            self.do_callback(FEATURE_POWER_PRODUCTION_CURRENT_HOUR["id"])

    def _response_calibration(self, message: CircleCalibrationResponse):
        """Store calibration properties"""
        for calibration in ("gain_a", "gain_b", "off_noise", "off_tot"):
            val = getattr(message, calibration).value
            setattr(self, "_" + calibration, val)
        self.calibration = True

    def pulses_to_kws(self, pulses, seconds=1):
        """Converts the amount of pulses to kWs using the calaboration offsets
        """
        if pulses is None:
            return None
        if pulses == 0 or not self.calibration:
            return 0.0
        pulses_per_s = pulses / float(seconds)
        corrected_pulses = seconds * (
            (
                (((pulses_per_s + self._off_noise) ** 2) * self._gain_b)
                + ((pulses_per_s + self._off_noise) * self._gain_a)
            )
            + self._off_tot
        )
        calc_value = corrected_pulses / PULSES_PER_KW_SECOND / seconds
        # Fix minor miscalculations
        if -0.001 < calc_value < 0.001:
            calc_value = 0.0
        return calc_value

    def _collect_energy_pulses(self, start_utc: datetime, end_utc: datetime):
        """Return energy pulses of given hours"""

        if start_utc == end_utc:
            hours = 0
        else:
            hours = int((end_utc - start_utc).seconds / 3600)
        _energy_pulses = 0
        for hour in range(0, hours + 1):
            _log_timestamp = start_utc + timedelta(hours=hour)
            if self._energy_history.get(_log_timestamp) is not None:
                _energy_pulses += self._energy_history[_log_timestamp]
                _LOGGER.debug(
                    "_collect_energy_pulses for %s | %s : %s, total = %s",
                    str(self.mac),
                    str(_log_timestamp),
                    str(self._energy_history[_log_timestamp]),
                    str(_energy_pulses),
                )
            else:
                _mem_address = self._energy_timestamp_memory_address(_log_timestamp)
                if (_mem_address is not None and _mem_address >= 0):
                    _LOGGER.info(
                        "_collect_energy_pulses for %s at %s | %s not found",
                        str(self.mac),
                        str(_log_timestamp),
                        str(_mem_address),
                    )
                    if self._energy_history_failed_address.count(_mem_address) == 0:
                        self._energy_history_failed_address.append(_mem_address)
                else:
                    _LOGGER.info(
                        "_collect_energy_pulses ignoring negative _mem_address %s",
                        str(_mem_address),
                    )


        # Validate all history values where present
        if len(self._energy_history_failed_address) == 0:
            return _energy_pulses
        return None

    def _update_energy_current_hour(self, _pulses_cur_hour):
        """Update energy consumption (pulses) of current hour"""
        _LOGGER.info(
            "_update_energy_current_hour for %s | counter = %s, update= %s",
            str(self.mac),
            str(self._energy_pulses_current_hour),
            str(_pulses_cur_hour),
        )
        if self._energy_pulses_current_hour is None:
            self._energy_pulses_current_hour = _pulses_cur_hour
            self.do_callback(FEATURE_POWER_CONSUMPTION_CURRENT_HOUR["id"])
        else:
            if self._energy_pulses_current_hour != _pulses_cur_hour:
                self._energy_pulses_current_hour = _pulses_cur_hour
                self.do_callback(FEATURE_POWER_CONSUMPTION_CURRENT_HOUR["id"])

        if self._last_collected_address_timestamp > datetime(2000, 1, 1):
            # Update today after lastlog has been retrieved
            self._update_energy_today_now()

    def _update_energy_today_now(self):
        """Update energy consumption (pulses) of today up to now"""

        _pulses_today_now = None

        # Regular update
        if (
            self._energy_pulses_today_hourly is not None
            and self._energy_pulses_current_hour is not None
        ):
            _pulses_today_now = (
                self._energy_pulses_today_hourly
                + self._energy_pulses_current_hour
            )

        _utc_hour_timestamp = datetime.utcnow().replace(
                minute=0, second=0, microsecond=0
        )
        _local_hour = datetime.now().hour
        _utc_midnight_timestamp = _utc_hour_timestamp - timedelta(hours=_local_hour)
        _local_midnight_timestamp = datetime.now().replace(
            hour=0, minute=0, second=0, microsecond=0
        )

        if _pulses_today_now is None:
            if self._energy_pulses_today_hourly is None:
                self._update_energy_today_hourly(
                    _utc_midnight_timestamp + timedelta(hours=1),
                    _utc_hour_timestamp,
                )
        elif (
             self._energy_pulses_today_now is not None
             and self._energy_pulses_today_now > _pulses_today_now
             and self._energy_pulses_midnight_rollover < _local_midnight_timestamp
        ):
            _LOGGER.info(
                "_update_energy_today_now for %s midnight rollover started old=%s, new=%s",
                str(self.mac),
                str(self._energy_pulses_today_now),
                str(_pulses_today_now),
            )
            self._energy_pulses_today_now = 0
            self._energy_pulses_midnight_rollover = _local_midnight_timestamp
            self._update_energy_today_hourly(
                _utc_midnight_timestamp + timedelta(hours=1),
                _utc_hour_timestamp,
            )
            self.do_callback(FEATURE_ENERGY_CONSUMPTION_TODAY["id"])
        elif (
             self._energy_pulses_today_now is not None
             and self._energy_pulses_today_now > _pulses_today_now
             and int((self._energy_pulses_today_now-_pulses_today_now)/(self._energy_pulses_today_now+1)*100) > 1
        ):
            _LOGGER.info(
                "_update_energy_today_now for %s hour rollover started old=%s, new=%s",
                str(self.mac),
                str(self._energy_pulses_today_now),
                str(_pulses_today_now),
            )
            self._update_energy_today_hourly(
                _utc_midnight_timestamp + timedelta(hours=1),
                _utc_hour_timestamp,
            )
        else:
            _LOGGER.info(
                "_update_energy_today_now for %s | counter = %s, update= %s (%s + %s)",
                str(self.mac),
                str(self._energy_pulses_today_now),
                str(_pulses_today_now),
                str(self._energy_pulses_today_hourly),
                str(self._energy_pulses_current_hour),
            )
            if self._energy_pulses_today_now is None:
                self._energy_pulses_today_now = _pulses_today_now
                if self._energy_pulses_today_now is not None:
                    self.do_callback(FEATURE_ENERGY_CONSUMPTION_TODAY["id"])
            else:
                if self._energy_pulses_today_now != _pulses_today_now:
                    self._energy_pulses_today_now = _pulses_today_now
                    self.do_callback(FEATURE_ENERGY_CONSUMPTION_TODAY["id"])

    def _update_energy_previous_hour(self, prev_hour: datetime):
        """Update energy consumption (pulses) of previous hour"""
        _pulses_prev_hour = self._collect_energy_pulses(prev_hour, prev_hour)
        _LOGGER.info(
            "_update_energy_previous_hour for %s | counter = %s, update= %s, timestamp %s",
            str(self.mac),
            str(self._energy_pulses_yesterday),
            str(_pulses_prev_hour),
            str(prev_hour),
        )
        if self._energy_pulses_prev_hour is None:
            self._energy_pulses_prev_hour = _pulses_prev_hour
            if self._energy_pulses_prev_hour is not None:
                self.do_callback(FEATURE_POWER_CONSUMPTION_PREVIOUS_HOUR["id"])
        else:
            if self._energy_pulses_prev_hour != _pulses_prev_hour:
                self._energy_pulses_prev_hour = _pulses_prev_hour
                self.do_callback(FEATURE_POWER_CONSUMPTION_PREVIOUS_HOUR["id"])

    def _update_energy_yesterday(
        self, start_yesterday: datetime, end_yesterday: datetime
    ):
        """Update energy consumption (pulses) of yesterday"""
        _pulses_yesterday = self._collect_energy_pulses(start_yesterday, end_yesterday)
        _LOGGER.debug(
            "_update_energy_yesterday for %s | counter = %s, update= %s, range %s to %s",
            str(self.mac),
            str(self._energy_pulses_yesterday),
            str(_pulses_yesterday),
            str(start_yesterday),
            str(end_yesterday),
        )
        if self._energy_pulses_yesterday is None:
            self._energy_pulses_yesterday = _pulses_yesterday
            if self._energy_pulses_yesterday is not None:
                self.do_callback(FEATURE_POWER_CONSUMPTION_YESTERDAY["id"])
        else:
            if self._energy_pulses_yesterday != _pulses_yesterday:
                self._energy_pulses_yesterday = _pulses_yesterday
                self.do_callback(FEATURE_POWER_CONSUMPTION_YESTERDAY["id"])

    def _update_energy_today_hourly(self, start_today: datetime, end_today: datetime):
        """Update energy consumption (pulses) of today up to last hour"""
        if start_today > end_today:
            _pulses_today_hourly = 0
        else:
            _pulses_today_hourly = self._collect_energy_pulses(start_today, end_today)
        _LOGGER.info(
            "_update_energy_today_hourly for %s | counter = %s, update= %s, range %s to %s",
            str(self.mac),
            str(self._energy_pulses_today_hourly),
            str(_pulses_today_hourly),
            str(start_today),
            str(end_today),
        )
        if self._energy_pulses_today_hourly is None:
            self._energy_pulses_today_hourly = _pulses_today_hourly
            if self._energy_pulses_today_hourly is not None:
                self.do_callback(FEATURE_POWER_CONSUMPTION_TODAY["id"])
        else:
            if self._energy_pulses_today_hourly != _pulses_today_hourly:
                self._energy_pulses_today_hourly = _pulses_today_hourly
                self.do_callback(FEATURE_POWER_CONSUMPTION_TODAY["id"])

    def request_energy_counters(self, log_address=None, callback=None):
        """Request power log of specified address"""
        _LOGGER.debug(
            "request_energy_counters for %s of address %s", str(self.mac), str(log_address)
        )
        if not self._available:
            _LOGGER.debug(
                    "Skip request_energy_counters for % is unavailable",
                    str(self.mac),
            )
            return
        if log_address is None:
            log_address = self._last_log_address
        if log_address is not None:
            # Energy history already collected
            if (
                log_address == self._last_log_address
                and self._energy_last_populated_slot == 4
            ):
                # Rollover of energy counter slot, get new memory address first
                self._energy_last_populated_slot = 0
                self._request_info(self.request_energy_counters)
            else:
                # Request new energy counters
                if self._energy_memory.get(log_address, 0) < 4:
                    self.message_sender(
                        CircleEnergyCountersRequest(self._mac, log_address),
                        None,
                        0,
                        PRIORITY_LOW,
                    )
                else:
                    _LOGGER.info(
                        "Drop known request_energy_counters for %s of address %s",
                        str(self.mac),
                        str(log_address),
                    )
        else:
            self._request_info(self.request_energy_counters)

    def _response_energy_counters(self, message: CircleEnergyCountersResponse):
        """Save historical energy information in local counters
        Each response message contains 4 log counters (slots)
        of the energy pulses collected during the previous hour of given timestamp
        """
        if message.logaddr.value == (self._last_log_address):
            self._energy_last_populated_slot = 0

        # Collect energy history pulses from received log address
        # Store pulse in self._energy_history using the timestamp in UTC as index
        _utc_hour_timestamp = datetime.utcnow().replace(
            minute=0, second=0, microsecond=0
        )
        _local_midnight_timestamp = datetime.now().replace(
            hour=0, minute=0, second=0, microsecond=0
        )
        _local_hour = datetime.now().hour
        _utc_midnight_timestamp = _utc_hour_timestamp - timedelta(hours=_local_hour)
        _midnight_rollover = False
        _history_rollover = False
        for _slot in range(1, 5):
            if (
                _log_timestamp := getattr(message, "logdate%d" % (_slot,)).value
            ) is None:
                break
            # Register collected history memory
            if _slot > self._energy_memory.get(message.logaddr.value, 0):
                self._energy_memory[message.logaddr.value] = _slot

            self._energy_history[_log_timestamp] = getattr(
                message, "pulses%d" % (_slot,)
            ).value

            _LOGGER.info("push _energy_memory for %s address %s slot %s stamp %s",
                         str(self.mac),
                         str(message.logaddr.value),
                         str(_slot),
                         str(_log_timestamp),
            )

            # Store last populated _slot
            if message.logaddr.value == (self._last_log_address):
                self._energy_last_populated_slot = _slot

            # Store most recent timestamp of collected pulses
            self._energy_last_collected_timestamp = max(
                self._energy_last_collected_timestamp, _log_timestamp
            )

            # Keep track of the most recent timestamp, _last_log_address might be corrupted
            if _log_timestamp > self._last_collected_address_timestamp:
                self._last_collected_address = message.logaddr.value
                self._last_collected_address_slot = _slot
                self._last_collected_address_timestamp = _log_timestamp

            # Trigger history rollover
            _LOGGER.info('history_rollover %s %s %s',str(_log_timestamp),
                         str(_utc_hour_timestamp),
                         str(self._energy_last_rollover_timestamp),
            )
            if (
                _log_timestamp == _utc_hour_timestamp
                and self._energy_last_rollover_timestamp < _utc_hour_timestamp
            ):
                self._energy_last_rollover_timestamp = _utc_hour_timestamp
                _history_rollover = True
                _LOGGER.info(
                    "_response_energy_counters for %s | history rollover, reset date to %s",
                    str(self.mac),
                    str(_utc_hour_timestamp),
                )

            # Trigger midnight rollover
            if (
                _log_timestamp == _utc_midnight_timestamp
                and self._energy_consumption_today_reset < _local_midnight_timestamp
            ):
                _LOGGER.info(
                    "_response_energy_counters for %s | midnight rollover, reset date to %s",
                    str(self.mac),
                    str(_local_midnight_timestamp),
                )
                self._energy_consumption_today_reset = _local_midnight_timestamp
                _midnight_rollover = True
        if self._energy_last_collected_timestamp == datetime.utcnow().replace(
                minute=0, second=0, microsecond=0
        ):
            self._update_energy_previous_hour(_utc_hour_timestamp)
            self._update_energy_today_hourly(
                _utc_midnight_timestamp + timedelta(hours=1),
                _utc_hour_timestamp,
            )
            self._update_energy_yesterday(
                _utc_midnight_timestamp - timedelta(hours=23),
                _utc_midnight_timestamp,
            )
        else:
            _LOGGER.info("CircleEnergyCounter failed for %s at %s|%s count %s",
                         str(self.mac),
                         str(message.logaddr.value),
                         str(self._last_log_address),
                         str(self._energy_last_collected_count),
            )
            self._energy_last_collected_count +=1

            if (
                    message.logaddr.value == self._last_log_address
                    and self._energy_last_collected_count > 3
            ):
                if self._energy_history_failed_address.count(self._last_log_address-1) == 0:
                    self._energy_history_failed_address.append(self._last_log_address-1)
                _LOGGER.info("Resetting CircleEnergyCounter due to logaddress offset")


        # Cleanup energy history for more than 48 hours 
        _48_hours_ago = datetime.utcnow().replace(
            minute=0, second=0, microsecond=0
        ) - timedelta(hours=48)
        for log_timestamp in list(self._energy_history.keys()):
            if log_timestamp < _48_hours_ago:
                del self._energy_history[log_timestamp]

    def _response_clock(self, message: CircleClockResponse):
        log_date = datetime(
            datetime.now().year,
            datetime.now().month,
            datetime.now().day,
            message.time.value.hour,
            message.time.value.minute,
            message.time.value.second,
        )
        clock_offset = message.timestamp.replace(microsecond=0) - (
            log_date + self.timezone_delta
        )
        if clock_offset.days == -1:
            self._clock_offset = clock_offset.seconds - 86400
        else:
            self._clock_offset = clock_offset.seconds
        _LOGGER.debug(
            "Clock of node %s has drifted %s sec",
            str(self.mac),
            str(self._clock_offset),
        )

    def get_clock(self, callback=None):
        """Get current datetime of internal clock of Circle."""
        self.message_sender(
            CircleClockGetRequest(self._mac),
            callback,
            0,
            PRIORITY_LOW,
        )

    def set_clock(self, callback=None):
        """Set internal clock of Circle."""
        self.message_sender(
            CircleClockSetRequest(self._mac, datetime.utcnow()),
            callback,
        )


    def sync_clock(self, max_drift=0):
        """Resync clock of node if time has drifted more than MAX_TIME_DRIFT"""
        if self._clock_offset is not None:
            if max_drift == 0:
                max_drift = MAX_TIME_DRIFT
            if (self._clock_offset > max_drift) or (self._clock_offset < -(max_drift)):
                _LOGGER.info(
                    "Reset clock of node %s because time has drifted %s sec",
                    str(self.mac),
                    str(self._clock_offset),
                )
                self.set_clock()

    def _energy_timestamp_memory_address(self, utc_timestamp: datetime):
        """Return memory address for given energy counter timestamp"""
        if self._last_collected_address is None:
            return None
        #Should already be hour timestamp, but just to be sure.
        _utc_now_timestamp = self._last_collected_address_timestamp.replace(
            minute=0, second=0, microsecond=0
        )
        if utc_timestamp > _utc_now_timestamp:
            return None

        _seconds_offset = (_utc_now_timestamp - utc_timestamp).total_seconds()
        _hours_offset = _seconds_offset / 3600

        if (_slot := self._last_collected_address_slot) == 0:
            _slot = 4
        _address = self._last_collected_address
        _sslot = _slot

        # last known
        _hours = 1
        while _hours <= _hours_offset:
            _slot -= 1
            if _slot == 0:
                _address -= 1
                _slot = 4
            _hours += 1
        _LOGGER.info("Calculated address %s at %s from %s at %s with %s|%s",
                     _address,
                     utc_timestamp,
                     self._last_log_address,
                     _utc_now_timestamp,
                     _sslot,
                     _hours_offset,
        )
        return _address
