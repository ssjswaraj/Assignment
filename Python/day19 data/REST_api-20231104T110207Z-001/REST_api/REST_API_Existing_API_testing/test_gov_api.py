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



url = "https://api.data.gov.in/resource/352b3616-9d3d-42e5-80af-7d21a2a53fab?api-key=579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b&format=json"
 
headers = {
    "api-Key": "579b464db66ec23bdd000001cdd3946e44ce4aad7209ff7b23ac571b",
    "accept": "application/xml"
}
 
response = requests.request("GET", url, 
				headers=headers)
print(response)

myjson = response.json()
print(myjson['records'])


#writing data in csv format

data_csv = pd.DataFrame(myjson['records'])
data_csv.to_csv('inflation_rates.csv')




#### Another example
## POST method

"""
params = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1,
  }

url = 'https://jsonplaceholder.typicode.com/posts'


headers= {
    'Content-type': 'application/json; charset=UTF-8',
  }

response = requests.request("POST", url, 
				headers=headers, json=params)

print("After POST ")
print(response.json())

url = 'https://jsonplaceholder.typicode.com/posts'


headers= {
    'Content-type': 'application/json; charset=UTF-8',
  }

response = requests.request("GET", url, 
				headers=headers)

print("All current resources after GET")
print(response.json())
"""


## GET POST GET method

## First Start the fask server in app.py
'''
url = 'http://127.0.0.1:5000/countries'

headers= { 'Content-Type': 'application/json' }
params = {"name":"Germany", 
	"capital": "Berlin",
	"area": 357022}

response = requests.request("GET", url)#, 
				#headers=headers, json=params)

print("After GET ")
print(response.json())



response = requests.request("POST", url, 
				headers=headers, json=params)

print("After POST ")
print(response.json())

response = requests.request("GET", url)#, 
				#headers=headers, json=params)

print("After GET ")
print(response.json())


print("Completed!")
'''