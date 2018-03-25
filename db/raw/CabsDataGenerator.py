# coding: utf-8

import json
import random

# generate random cabs data

f = open("names.txt","r")
driverNames = f.readlines()
f.close()

nums = [0,1, 2, 3, 4, 5, 6, 7, 8, 9]
cabTypes = ["regular", "premium", "xl"]
availability = "True"
#random.sample(nums, 10)
data = []
for i in range(200):
    name = random.choice(driverNames).rstrip('\n')
    phoneNumber = ''.join(str(e) for e in random.sample(nums, 10))
    license = ''.join(str(e) for e in random.sample(nums, 4))
    cabType = random.choice(cabTypes)
    available = availability
    data.append({
        'license': 'LC'+license,
        'driver_name': name,
        'driver_phone': phoneNumber,
        'cab_type': cabType,
        'available': available
    })

with open('./cabs_data.json', 'w') as outfile:
    json.dump(data, outfile)

