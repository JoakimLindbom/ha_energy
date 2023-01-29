# ha_energy
Energy optimisation package for Home Assistant

This is implemented as a Home Assistant package; easiest is to create a packages folder and include the packages folder in this repo there, and then include it from your config.yaml file, e.g.
```
homeassistant:
  packages: !include_dir_named packages/
```
Dashboard example:

 ![Dashboard example](/images/Energy_package_UI_example_1.png)


The solution is based around events, where you can use these events to trigger automations. All events contain relevant data, e.g. the price or mean price for the time slot starting.

```
event_type: start_expensive_energy_3h
data:
  price: 249.8
origin: LOCAL
time_fired: "2023-01-27T18:00:00.031815+00:00"
context:
  id: 01GQZ0NMC3CFQ4S9RQKKH15Y5K
  parent_id: null
  user_id: null
```

## List of events
### Consecutive time slots - you'll need e.g. 3 hours that are consecutive to run yoiur dish washer; cou cannot take 3 hours spread around in the day.

| Slot | Start                    | End                     |
|------|--------------------------|-------------------------|
| 1h   | start_cheapest_energy_1h | end_cheapest_energy_1h  |
| 2h   | start_cheapest_energy_2h | end_cheapest_energy_2h  |
| 3h   | start_cheapest_energy_3h | end_cheapest_energy_3h  |    
| 4h   | start_cheapest_energy_4h | end_cheapest_energy_4h |    
| 5h   | start_cheapest_energy_5h | end_cheapest_energy_5h  |    

### Single 1 hour time slots - if you need e.g. 3 hours to charge your bike, you'd subscribe to the three first in the list.

| Slot | Start                            | End                            |
|------|----------------------------------|--------------------------------|
| 1st  | start_cheapest_energy_1h_slot_00 | end_cheapest_energy_1h_slot_00 |
| 2nd  | start_cheapest_energy_1h_slot_01 | end_cheapest_energy_1h_slot_01 |
| 3rd  | start_cheapest_energy_1h_slot_02 | end_cheapest_energy_1h_slot_02 |    
| 4th  | start_cheapest_energy_1h_slot_03 | end_cheapest_energy_1h_slot_03 |    
| 5th  | start_cheapest_energy_1h_slot_04 | end_cheapest_energy_1h_slot_04 |    
| 6th  | start_cheapest_energy_1h_slot_05 | end_cheapest_energy_1h_slot_05 |    
| 7th  | start_cheapest_energy_1h_slot_06 | end_cheapest_energy_1h_slot_06 |    

