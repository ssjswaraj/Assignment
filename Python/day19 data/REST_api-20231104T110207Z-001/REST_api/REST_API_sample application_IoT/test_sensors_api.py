import requests
import pandas as pd
import json

"""
1. Select right URL
2. Check GET / POST method
3. In case of GET method, 
parameters to be sent directly in URL
4. In case of POST method,
"""

## GET POST GET method

## First Start the fask server in app.py

url = 'http://127.0.0.1:5000/sensors'

headers= { 'Content-Type': 'application/json' }
params = {"SensorID":"10", 
	"Value": "45",
	}

response = requests.request("GET", url)

print("After GET ")
print(response.json())

response = requests.request("POST", url, 
				headers=headers, json=params)

print("After POST ")
print(response.json())

response = requests.request("GET", url)

print("After GET ")
print(response.json())


print("Completed!")