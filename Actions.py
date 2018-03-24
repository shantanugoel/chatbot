import os
import json
import random

cab_types = ['regular', 'premium', 'xl']
cabs = {}

def CabsInit():

  for ct in cab_types:
    cabs[ct] = []

  for ct in cab_types:
    lines = open(os.path.join('./db/', 'cabs_'+ ct + '.dat')).readlines()
    for i, line in enumerate(lines):
      no, name, phone = line.split(',')
      cabs[ct].append({
        'no': no,
        'name': name,
        'phone': phone
      })

def AssignCab(attributes, context):
  print(attributes)
  return "executed"


def BookRestaurant(attributes, context):

  restaurants = []
  with open('./db/restaurants.json') as f:
    restaurants = json.load(f)

  matches = list(filter(lambda x: x['cuisine'] == attributes['cuisine'] and
                        x['cost'] == attributes['cost'] and
                        x['location'] == attributes['location'],
                        restaurants))

  return 'Your reserveration has been confirmed at ' + random.choice(matches)['name']
