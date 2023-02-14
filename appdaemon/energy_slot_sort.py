# +---------------------------------------------------------------------------------------------
# |
# | Author: Joakim Lindbom
# | Date:   2023-01-28
# |
# | Licence: GPL V3
# | You know the drill - no warranty, no nothing except the good stuff you can get out of this
# |
# +---------------------------------------------------------------------------------------------

import hassapi as hass
import datetime

class energy_slot_sort(hass.Hass):
    """
    This class creates/updates a set of sensors, sorted by cheapest hourly electricity price
    24 senors (one per hour) are created, e.g. sensor.cheapest_electricity_1h_slot_00,
    sensor.cheapest_electricity_1h_slot_01, sensor.cheapest_electricity_1h_slot_02 etc.
    Each sensor contains an attribute (price) with the price for that hour.
    """

    def initialize(self):
        self.set_log_level("DEBUG")
        self.log("energy_slot_sort - initiated")
        self.tomorrow_data_available = False
        self.price_lst = []
        self.energy_sensor = self.args["energy_sensor"]

        try:
            self.time_slots_cheap_prefix = self.args["time_slots_cheap_prefix"]
        except KeyError:
            self.log('No key for cheap time slots present. Ignoring.')
            self.time_slots_cheap_prefix = None
        try:
            self.time_slots_expensive_prefix = self.args["time_slots_expensive_prefix"]
        except KeyError:
            self.log('No key for expensive time slots present. Ignoring.')
            self.time_slots_expensive_prefix = None
        try:
            self.time_slots_expensive_morning_prefix = self.args["time_slots_expensive_morning_prefix"]
        except KeyError:
            self.log('No key for expensive morning slots present. Ignoring.')
            self.time_slots_expensive_morning_prefix = None
        try:
            self.time_slots_expensive_evening_prefix = self.args["time_slots_expensive_evening_prefix"]
        except KeyError:
            self.log('No key for expensive evening slots present. Ignoring.')
            self.time_slots_expensive_evening_prefix = None
        try:
            self.time_slots_cheap_evening_night_prefix = self.args["time_slots_cheap_evening_night_prefix"]
        except KeyError:
            self.log('No key for cheap evening+night slots present. Ignoring.')
            self.time_slots_cheap_evening_night_prefix = None

        # self.listen_event(self.event_listener, "state_changed")
        handle = self.run_daily(self.create_evening_night_sensors, "13:30:10")
        handle = self.run_daily(self.create_morning_evening_sensors, "00:00:10")
        handle = self.run_daily(self.create_24h_sensors, "00:00:05")
        self.create_evening_night_sensors()
        self.create_morning_evening_sensors()
        self.create_24h_sensors()

    def event_listener(self, event, data, kwargs):
        entity = data['entity_id']
        if data["entity_id"] == self.energy_sensor:
            self.log(f'{self.energy_sensor}', level="DEBUG")

    def get_todays_raw_prices(self):
        prices = self.get_state(self.energy_sensor, attribute="raw_today")

        i = 0
        price_lst = []
        for item in prices:
            price = float('{:.0f}'.format(item["value"]))  # TODO: Will need some guardrail against bad or missing data
            price_lst.append({"hour": i, "price": price, "start": item["start"]})
            i += 1
        return price_lst

    def get_tomorrow_raw_prices(self):
        self.tomorrow_data_available = self.get_state(self.energy_sensor, attribute="tomorrow_valid")
        self.log (f'tomorrow_data_available={self.tomorrow_data_available}', level="DEBUG")
        if not self.tomorrow_data_available:
            return None

        prices = self.get_state(self.energy_sensor, attribute="raw_tomorrow")

        i = 0
        price_lst = []
        for item in prices:
            price = float('{:.0f}'.format(item["value"]))  # TODO: Will need some guardrail against bad or missing data
            price_lst.append({"hour": i, "price": price, "start": item["start"]})
            i += 1
        return price_lst


    def create_24h_sensors(self):
        self.price_lst = self.get_todays_raw_prices()
        i = 0
        if self.time_slots_cheap_prefix is not None:
            self.log(f'Creating 24h sensors, cheap hours', level="INFO")
            for item in sorted(self.price_lst, key=lambda k: k["price"]):
                self.log(f'{item["price"]} - {item["hour"]} - {item["start"]}', level="DEBUG")
                e = "sensor." + self.time_slots_cheap_prefix + f'{i:02d}'
                attr = {"price": item["price"], "order": i, "device_class": "timestamp"}
                self.log(f'e={e}', level="DEBUG")
                self.set_state(e, state=item["start"], attributes=attr)
                i += 1

        if self.time_slots_expensive_prefix is not None:
            self.log(f'Creating 24h sensors, expensive hours', level="INFO")
            i = 0
            for item in sorted(self.price_lst, key=lambda k: k["price"], reverse=True):
                self.log(f'{item["price"]} - {item["hour"]} - {item["start"]}', level="DEBUG")
                e = "sensor." + self.time_slots_expensive_prefix+ f'{i:02d}'
                attr = {"price": item["price"], "order": i, "device_class": "timestamp"}
                self.log(f'e={e}', level="DEBUG")
                self.set_state(e, state=item["start"], attributes=attr)
                i += 1

    def create_morning_evening_sensors(self):
        self.price_lst = self.get_todays_raw_prices()

        if self.time_slots_expensive_morning_prefix is not None:
            self.log(f'Creating morning sensors for expensive hours', level="INFO")
            i = 0
            for item in sorted(self.price_lst[:12], key=lambda k: k["price"], reverse=True):
                self.log(f'{item["price"]} - {item["hour"]} - {item["start"]}', level="DEBUG")
                e = "sensor." + self.time_slots_expensive_morning_prefix + f'{i:02d}'
                attr = {"price": item["price"], "order": i, "device_class": "timestamp"}
                self.log(f'e={e}', level="DEBUG")
                self.set_state(e, state=item["start"], attributes=attr)
                i += 1

        if self.time_slots_expensive_evening_prefix is not None:
            self.log(f'Creating evening sensors for expensive hours', level="INFO")
            i = 0
            for item in sorted(self.price_lst[12:], key=lambda k: k["price"], reverse=True):
                self.log(f'{item["price"]} - {item["hour"]} - {item["start"]}', level="DEBUG")
                e = "sensor." + self.time_slots_expensive_evening_prefix + f'{i:02d}'
                attr = {"price": item["price"], "order": i, "device_class": "timestamp"}
                self.log(f'e={e}', level="DEBUG")
                self.set_state(e, state=item["start"], attributes=attr)
                i += 1

    def create_evening_night_sensors(self):
        '''
        Calculates cheapest 1h slots between 20:00 and 8:00
        Will only run if tomorrow's data is available
        '''
        if self.time_slots_cheap_evening_night_prefix is not None:
            self.log(f'Creating evening and night sensors for expensive hours', level="INFO")
            today = self.get_todays_raw_prices()
            tomorrow = self.get_tomorrow_raw_prices()
            if tomorrow is None:
                self.log(">>>Data for tomorrow not available. Rerunning in 1h<<<", level="ERROR")
                handle = self.run_in(self.create_evening_night_sensors, 3600)
                return

            i = 0
            for item in sorted(today[20:]+tomorrow[:8], key=lambda k: k["price"]):
                self.log(f'{item["price"]} - {item["hour"]} - {item["start"]}', level="DEBUG")
                e = "sensor." + self.time_slots_cheap_evening_night_prefix + f'{i:02d}'
                attr = {"price": item["price"], "order": i, "device_class": "timestamp"}
                self.log(f'e={e}', level="DEBUG")
                self.set_state(e, state=item["start"], attributes=attr)
                i += 1
