# Installation
## Prerequisites
You need to install the Nordpool integration in order for this package to work at all.
Note down the name of the Nordpool sensor.
If you want to use the sorted 1 hour slots, you need to have AppDaemon running.

## Copying files
Clone the files from this repo to some file location, e.g.:
```
git clone git@github.com:JoakimLindbom/ha_energy.git ~/proj/homeassistant
```
Since this is implemented as a Home Assistant package; it's easiest to create a packages folder and include the packages folder in this repo there: 
```
mkdir /HA_location/config/packages/energy
cp -r ~/proj/homeassistant/ha_energy/packages/* /HA_location/config/packages/
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

## AppDaemon
Copy energy_slot_sort.py to your AppDaemon apps directory, e.g.:
```
cp energy_slot_sort.py /HA_location/config/appdaemon/apps
```
Update your AddDaemon config file:
```
nano /HA_location/config/appdaemon/apps/apps.yaml
```
Include the lines below. If you don't need all energy sorting alternatives, you can just skip them.
```
energy_slot_sort:
  module: energy_slot_sort
  class: energy_slot_sort
  energy_sensor: sensor.nordpool_kwh_se4_sek_2_095_025
  time_slots_cheap_prefix: cheapest_electricity_1h_slot_
  time_slots_expensive_prefix: expensive_electricity_1h_slot_
  time_slots_expensive_morning_prefix: expensive_electricity_1h_slot_morning_
  time_slots_expensive_evening_prefix: expensive_electricity_1h_slot_evening_
  time_slots_cheap_evening_night_prefix: cheapest_electricity_1h_slot_evening_night_
  ```
Replace the Nordpool sensor with a value that you noted before.
