import pytest
import requests


api_url = "http://192.168.1.8:5000/"
response = requests.get(api_url)
status_code= response.status_code
print("status code=",response.status_code)
if status_code==200:
    print ("Test is passed")
else:
    print("Test failed")