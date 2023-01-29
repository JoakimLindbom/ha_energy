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
        self.energy_sensor = self.args["energy_sensor"]
        self.time_slots_prefix = self.args["time_slots_prefix"]
        self.listen_event(self.event_listener, "state_changed")
        self.get_todays_raw_prices()

    def event_listener(self, event, data, kwargs):
        entity = data['entity_id']
        if data["entity_id"] == self.energy_sensor:
            self.log(f'{self.energy_sensor}')

    def get_todays_raw_prices(self):
        prices = self.get_state(self.energy_sensor, attribute="raw_today")
        lst = []
        i = 0
        for item in prices:
            lst.append({"hour": i, "price": item["value"], "start": item["start"]})
            i += 1
        i = 0
        for item in sorted(lst, key=lambda k: k["price"]):
            self.log(f'{item["price"]} - {item["hour"]} - {item["start"]}')
            e = "sensor." + self.time_slots_prefix + f'{i:02d}'
            attr = {"price": item["price"], "order": i, "device_class": "timestamp"}
            self.log(f'e={e}')
            self.set_state(e, state=item["start"], attributes=attr)
            i += 1
