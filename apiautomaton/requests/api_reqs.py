import requests
import json

class Api_req:

    def get_req(self,url):
        responce= requests.get(url)
        return responce.json()

    def post_req(self,url,data,headers):
        responce= requests.post(url,data=data,headers=headers)
        return responce.json()

    def put_req(self,url,data):
        responce= requests.put(url,json=data)
        return responce.json()

    def delete_req(self,url):
        responce= requests.delete(url)
        return responce.json()