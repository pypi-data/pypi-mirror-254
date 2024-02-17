import requests
from ..config import base_url,api_token

# Creates an account  Organization/Client
def create_account(name,email,username,password):
    url = f"{base_url}/client/" 
    data = {        
    "name": name,
    "email":email,
    "username": username,       
    "password": password
    }
    headers = {"Authorization":api_token}
    response = requests.post(url,data=data,headers=headers)
    return response.text


def create_app(name,client_id,access_token):
    data = {
    "name": name,                  
    "client": client_id  
    }
    url = f"{base_url}/app/"
    access_token = "Bearer "+ access_token
    headers = {"Authorization": access_token}
    response = requests.post(url,json=data,headers=headers)
    return response.json()


def login(username,password):
    data = {
    "username": username,                  
    "password": password  
    }
    url = f"{base_url}/login"
    headers = {"Authorization":api_token}
    response = requests.post(url,json=data,headers=headers)
    output = response.json()
    try:
        del output["refresh"]
    except:
        return response.json()
    return output
