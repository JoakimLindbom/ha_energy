# ha_energy
Energy optimisation package for Home Assistant

## Installation
### Prerequisites
You need to install the Nordpool integration in order for this package to work at all.
Note down the name of the Nordpool sensor.
If you want to use the sorted 1 hour slots, you need to have AppDaemon running.

### Copying files
Clone the files from this repo to some file location, e.g.:
```
git clone git@github.com:JoakimLindbom/ha_energy.git ~/proj/homeassistant
```
Since this is implemented as a Home Assistant package; it's easiest to create a packages folder and include the packages folder in this repo there: 
```
mkdir /HA_location/config/packages/energy
cp ~/proj/homeassistant/ha_energy/packages/* /location-to-HA/config/packages/
```
Next, check the name of the Nordpool sensor. If it differs from the name I'm having, run the following commands
```
cd /HA_location/config/packages/energy
sed -i 's/nordpool_kwh_se4_sek_2_095_025/the-name-you-noted-before/g' sensors.yaml
```
Last, include it from your configuration.yaml file, e.g.
```
homeassistant:
  packages: !include_dir_named packages/
```
Remember to restart HA after you've installed the files.

### AppDaemon
Copy energy_slot_sort.py to your AppDaemon apps directory, e.g.:
```
cp energy_slot_sort.py /HA_location/config/appdaemon/apps
```
Update your AddDaemon config file:
```
nano /HA_location/config/appdaemon/apps/apps.yaml
```
Include the lines below
```
energy_slot_sort:
  module: energy_slot_sort
  class: energy_slot_sort
  energy_sensor: sensor.nordpool_kwh_se4_sek_2_095_025
  time_slots_prefix: cheapest_electricity_1h_slot_
```
Replace the Nordpool sensor with a value that you noted before.

## Dashboard example:
You don't need the dashboards for this to work, but if you want to keep an eye at the prices etc. it's nice to have,

 ![Dashboard example](/images/Energy_package_UI_example_1.png)
The ha_energy_ui folder contains some sample cards you can modify and include as per your needs.
My examples are using multiple-entity-row, but you can use whichever cards you like.

## Event driven solution
## Intro
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

You'll find some examples in the ha_energy/examples folder how to use these events for your own needs.
