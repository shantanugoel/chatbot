import os
import json
import random

#TODO: Convert to class

cab_types = ['regular', 'premium', 'xl']
cab_type_order = {
  'regular': 0,
  'premium': 1,
  'xl': 2
}
cabs = {}
cab_config = {
    "time_taken_per_km": 2,
    "fare_rate_regular": 7,
    "fare_rate_premium": 10,
    "fare_rate_xl": 15,
    "psgr_cap_regular": 4,
    "psgr_cap_premium": 5,
    "psgr_cap_xl": 8,
    "luggage_cap_regular": 2,
    "luggage_cap_premium": 3,
    "luggage_cap_xl": 5
  }

def CabsInit():
  global cabs
  with open('./db/cabs.json') as f:
    cabs = json.load(f)

def AssignCab(attributes, context):

  global cabs
  cab_type = None
  num_psgrs = int(attributes['num_passengers'])
  luggage = int(attributes['luggage'])

  if num_psgrs <= cab_config['psgr_cap_regular'] and luggage <= cab_config['luggage_cap_regular']:
    cab_type = 'regular'
  elif num_psgrs <= cab_config['psgr_cap_premium'] and luggage <= cab_config['luggage_cap_premium']:
    cab_type = 'premium'
  elif num_psgrs <= cab_config['psgr_cap_xl'] and luggage <= cab_config['luggage_cap_xl']:
    cab_type = 'xl'

  if cab_type_order[attributes['cab_type']] > cab_type_order[cab_type]:
    cab_type = attributes['cab_type']

  matches = []
  if cab_type:
    matches = list(filter(lambda x: x['cab_type'] == cab_type and
                          x['available'] == "True", cabs))

  # TODO: Retry matches with upgrade of cab type
  if len(matches) > 0:
    cab = random.choice(matches)
    cab['available'] = "False"
    return "Your cab to " + attributes['destination'] + " has been booked. Cab No: " + cab['license'] + \
      " Driver: " + cab['driver_name'] + " Driver Ph: " + cab['driver_phone']

  return "Sorry, no cab available for your requirements"

restaurants = []

def RestaurantsInit():
  global restaurants
  with open('./db/restaurants.json') as f:
    restaurants = json.load(f)

def BookRestaurant(attributes, context):

  global restaurants
  matches = list(filter(lambda x: x['cuisine'] == attributes['cuisine'] and
                        x['cost'] == attributes['cost'] and
                        x['location'] == attributes['location'],
                        restaurants))

  if len(matches) > 0:
    return 'Your reserveration has been confirmed at ' + random.choice(matches)['name']
  else:
    return 'Sorry, we couldn\'t find any restaurants matching your selection'
