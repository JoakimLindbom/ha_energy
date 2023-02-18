# ha_energy
Energy optimisation package for Home Assistant

You can use the Nordpool integration in Home Assistant to get the electricity prioce for current hour and for all hours today and tomorrow. But how do you know when to utilise cheap hours to e.g. start the heat water boiler, or when to start your dish washer?
Likewise - how do you know when to stop running e.g. your floor heating during morning and evening peak hours?

This package is taking care of identifying these hours, either as single hour (1h) slots, or as consecutive timeslots. For a charging load needing 3 hours during the night, you can pick any 3 hours. But for a dishwasher this wouldn't work; you need three hours in a row, else the heated water would chill down and, most likely, the dishwasher wouldn't work as you'd expect.

To give you freedom in how you want to create your solution, I've created events for cheapest and most expensive hours in a day, in the morning, in the evening and the evening/night, as well as events for the cheapest and most expensive consecutive time slots (1h - 5h slots).




## Dashboard example:
You don't need the dashboards for this to work, but if you want to keep an eye at the prices etc. it's nice to have,

 ![Dashboard example](/images/Energy_package_UI_example_1.png)

If you want to avoid morning and evening peaks, you can use the morning and evening events to start and stop automations.

 ![Dashboard example](/images/Expensive_morning.png)

 ![Dashboard example](/images/Expensive_evening.png)

Workloads that can be run during evening and night (20-08) will benefit from:

 ![Dashboard example](/images/Cheapest_evening_night.png)

The ha_energy_ui folder contains some sample cards you can modify and include as per your needs.
My examples are using multiple-entity-row, but you can use whichever cards you like.

More info:
[Installation](documentation/installation.md)
[Event documentation](documentation/events.md)
