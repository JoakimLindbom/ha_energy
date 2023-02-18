# Event driven solution
# Intro
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

# List of events
## Consecutive time slots - you'll need e.g. 3 hours that are consecutive to run your dish washer; you cannot take 3 hours spread around in the day.

| Slot | Start                         | End                         |
|------|-------------------------------|-----------------------------|
| 1h   | start_cheapest_electricity_1h | end_cheapest_electricity_1h |
| 2h   | start_cheapest_electricity_2h | end_cheapest_electricity_2h |
| 3h   | start_cheapest_electricity_3h | end_cheapest_electricity_3h |    
| 4h   | start_cheapest_electricity_4h | end_cheapest_electricity_4h |    
| 5h   | start_cheapest_electricity_5h | end_cheapest_electricity_5h |    


| Slot | Start                          | End                          |
|------|--------------------------------|------------------------------|
| 1h   | start_expensive_electricity_1h | end_expensive_electricity_1h |
| 2h   | start_expensive_electricity_2h | end_expensive_electricity_2h |
| 3h   | start_expensive_electricity_3h | end_expensive_electricity_3h |    
| 4h   | start_expensive_electricity_4h | end_expensive_electricity_4h |    
| 5h   | start_expensive_electricity_5h | end_expensive_electricity_5h |    

## Single 1 hour time slots for today - if you need e.g. 3 hours to charge your bike, you'd subscribe to the three first in the list.

| Slot | Start                                 | End                                 |
|------|---------------------------------------|-------------------------------------|
| 1st  | start_cheapest_electricity_1h_slot_00 | end_cheapest_electricity_1h_slot_00 |
| 2nd  | start_cheapest_electricity_1h_slot_01 | end_cheapest_electricity_1h_slot_01 |
| 3rd  | start_cheapest_electricity_1h_slot_02 | end_cheapest_electricity_1h_slot_02 |    
| 4th  | start_cheapest_electricity_1h_slot_03 | end_cheapest_electricity_1h_slot_03 |    
| 5th  | start_cheapest_electricity_1h_slot_04 | end_cheapest_electricity_1h_slot_04 |    
| 6th  | start_cheapest_electricity_1h_slot_05 | end_cheapest_electricity_1h_slot_05 |    
| 7th  | start_cheapest_electricity_1h_slot_06 | end_cheapest_electricity_1h_slot_06 |    

## Single 1 hour time slots for today, one set for the morning and one set for the afternoon/evening

| Slot | Start                                          | End                                          |
|------|------------------------------------------------|----------------------------------------------|
| 1st  | start_expensive_electricity_1h_slot_morning_00 | end_expensive_electricity_1h_slot_morning_00 |
| 2nd  | start_expensive_electricity_1h_slot_morning_01 | end_expensive_electricity_1h_slot_morning_01 |
| 3rd  | start_expensive_electricity_1h_slot_morning_02 | end_expensive_electricity_1h_slot_morning_02 |    
| 4th  | start_expensive_electricity_1h_slot_morning_03 | end_expensive_electricity_1h_slot_morning_03 |    
| 5th  | start_expensive_electricity_1h_slot_morning_04 | end_expensive_electricity_1h_slot_morning_04 |    
| 6th  | start_expensive_electricity_1h_slot_morning_05 | end_expensive_electricity_1h_slot_morning_05 |    
| 7th  | start_expensive_electricity_1h_slot_morning_06 | end_expensive_electricity_1h_slot_morning_06 |    


| Slot | Start                                          | End                                          |
|------|------------------------------------------------|----------------------------------------------|
| 1st  | start_expensive_electricity_1h_slot_evening_00 | end_expensive_electricity_1h_slot_evening_00 |
| 2nd  | start_expensive_electricity_1h_slot_evening_01 | end_expensive_electricity_1h_slot_evening_01 |
| 3rd  | start_expensive_electricity_1h_slot_evening_02 | end_expensive_electricity_1h_slot_evening_02 |    
| 4th  | start_expensive_electricity_1h_slot_evening_03 | end_expensive_electricity_1h_slot_evening_03 |    
| 5th  | start_expensive_electricity_1h_slot_evening_04 | end_expensive_electricity_1h_slot_evening_04 |    
| 6th  | start_expensive_electricity_1h_slot_evening_05 | end_expensive_electricity_1h_slot_evening_05 |    
| 7th  | start_expensive_electricity_1h_slot_evening_06 | end_expensive_electricity_1h_slot_evening_06 |    

## Single 1 hour time slots for evening-/night (20-08)

| Slot | Start                                               | End                                               |
|------|-----------------------------------------------------|---------------------------------------------------|
| 1st  | start_cheapest_electricity_1h_slot_evening_night_00 | end_cheapest_electricity_1h_slot_evening_night_00 |
| 2nd  | start_cheapest_electricity_1h_slot_evening_night_01 | end_cheapest_electricity_1h_slot_evening_night_01 |
| 3rd  | start_cheapest_electricity_1h_slot_evening_night_02 | end_cheapest_electricity_1h_slot_evening_night_02 |    
| 4th  | start_cheapest_electricity_1h_slot_evening_night_03 | end_cheapest_electricity_1h_slot_evening_night_03 |    
| 5th  | start_cheapest_electricity_1h_slot_evening_night_04 | end_cheapest_electricity_1h_slot_evening_night_04 |    
| 6th  | start_cheapest_electricity_1h_slot_evening_night_05 | end_cheapest_electricity_1h_slot_evening_night_05 |    
| 7th  | start_cheapest_electricity_1h_slot_evening_night_06 | end_cheapest_electricity_1h_slot_evening_night_06 |    



You'll find some examples in the ha_energy/examples folder how to use these events for your own needs.
