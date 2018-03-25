
# coding: utf-8

# In[2]:


import json
import random

# generate random cabs data

f = open("restaurant_names.txt","r")
restaurantNames = f.readlines()
f.close()

f = open("../../entities/cost.dat", "r")
costList = f.readlines()
f.close()

f = open("../../entities/cuisine.dat", "r")
cuisineList = f.readlines()
f.close()

f = open("../../entities/location.dat", "r")
locList = f.readlines()
f.close()


data = []
for i in range(10000):
    name = random.choice(restaurantNames).rstrip('\n')
    cuisine = random.choice(cuisineList).rstrip('\n')
    cost = random.choice(costList).rstrip('\n')
    location = random.choice(locList).rstrip('\n')
    data.append({
        'name': name,
        'cuisine': cuisine,
        'cost': cost,
        'location': location
    })

with open('./restaurant_data.json', 'w') as outfile:
    json.dump(data, outfile)

