from urllib import response
import requests

# defines base url - server location of API
BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "helloworld/bill")
print(response.json())

# returns [20/Oct/2022 10:43:42] "GET /helloworld HTTP/1.1" 200
