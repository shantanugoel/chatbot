Team No: 60
Domain Choice: Cab Booking
Bonus Task: Graceful Restart at any stage of the chat (Type 'start' or 'restart' to use. See bottom of readme.txt for more details)

Usage
=====
Run 'python Chatbot_v2.py'

The chat bot works for restaurant booking and cab booking skills.
Restaurant booking input attributes: Cuisine, Cost/budget, Location/area
Cab Booking input attributes: Destination, Number of passengers, number of luggage, Cab type (Cab type is optional and can be regular, premium or xl)


Files
====
Chatbot_v2.py - Main executable file to be run

entities/cab_type.dat -> Cab type (classes of cabs depending on how many passengers and luggage they can hold)
entities/destination.dat -> Destinations covered by cab booking program
entities/location.dat -> Locations to search for restaurant
entities/cuisine.dat -> Types of cuisines to search for restaurant
entities/cost.dat -> Budget range to search for restaurant

intents/BookCab.dat -> Utterances for cab booking intent
intents/BookRestaurant.dat -> Utterances for restaurant booking intent

params/newparams.cfg -> Parameters for the chatbot

Actions.py -> Action/DB query and internal configuration for cab and restaurant booking.
stoplist.txt -> List of stop words for cleaning the input data for better ngrammatch
utils.py -> Utils to convert text to numbers for some inputs to allow both english and numeric inputs


Database
=====
cabs.json -> Generated database containing 200 diverse entries of various cabs
restaurants.json -> Generated database containing 10000 diverse entries of various attributes of restaurants
raw/CabsDataGenerator.py -> A script we wrote to generate the cabs database using some raw names, attributes and entities
raw/RestaurantDataGenerator.py -> A script we wrote to generate teh restaurant data using some raw names, attributes and entities
raw/* -> Other input/output files for the data generation


Bonus Task
=====
Graceful restart at any stage of the chat
-----------------------------------------
At any stage of the chat, the user can write "start" or "restart" for a fresh start to the chat. Previous attributes, contexts and all states are appopriately cleaned up and a FreshGreeting context is setup to start the chat again.
Additionally, we added "bye" and "exit" keywords to exit the chat at anytime either with or without completing the chat fulfillment.
