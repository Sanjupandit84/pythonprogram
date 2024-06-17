
a=int(input("enter value"))
def length(a):
    a=a*12
    print(a)
length(a)

import requests
import json
 
url= ' https://v6.exchangerate-api.com/v6/20d36e1e15961f62ee030384/pair/INR/USD'
response = requests.get(url)
data = response.json()
y=json.dumps(data,indent=3)
# json object to file: output.json
print(y)
print (type(y))
with open("output.json","w")as f:
    f.write(y)

a = "ram"
y=json.dumps(a)
print (type(y))







