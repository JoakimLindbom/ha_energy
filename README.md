# ha_energy
Energy optimisation package for Home Assistant

This is implemented as a Home Assistant package; easiest is to create a packages folder and include it from your config.yaml file, e.g.

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
