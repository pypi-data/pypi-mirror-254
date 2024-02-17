import requests
from ..config import base_url, api_token

def read_file(file_path):
    with open(file_path, "rb") as file:
        uploaded_filename = file_path.split('\\')[-1]
        content = file.read()
        return uploaded_filename, content

def aicloud_model_monitoring(token,deployment_id,file_path,modelling_mode):
    if modelling_mode.lower() == 'aipilot':
        data = {
        'res_type':'base64',
        'deployment_id': deployment_id
        }
        url = f"{base_url}/training/aipilot/monitor-model"
        # Get The Monitor Graph Of The Deployed Model
        access_token = 'Bearer '+ token
        headers = {"Authorization": access_token}
        uploaded_filename, content = read_file(file_path)
        files = {'file': (uploaded_filename, content)}
        # Send the POST request
        response = requests.post(url, data=data, headers=headers,files=files)
        response_json = response.json()
        if response_json['modelling_mode'].lower() == modelling_mode.lower():
            return response_json['result']
        else:
            return "Invalid mode!"
        
    elif modelling_mode.lower() == 'comprehensive':
            
        data = {
        'res_type':'base64',
        'deployment_id': deployment_id
        }
        url = f"{base_url}/training/comprehensive/monitor-model"
        # Get The Monitor Graph Of The Deployed Model
        access_token = 'Bearer '+ token
        headers = {"Authorization": access_token}
        uploaded_filename, content = read_file(file_path)
        files = {'file': (uploaded_filename, content)}
        # Send the POST request
        response = requests.post(url, data=data, headers=headers,files=files)
        response_json = response.json()
        if response_json['modelling_mode'].lower() == modelling_mode.lower():
            return response_json['result']
        else:
            return "Invalid mode!"
        
def aipilot_model_monitoring(token,deployment_id,res_type,file_path,mode):
    data = {
        'res_type':res_type,
        'deployment_id': deployment_id
    }
    url = f"{base_url}/training/aipilot/monitor-model"
    # Get The Monitor Graph Of The Deployed Model
    access_token = 'Bearer '+ token
    headers = {"Authorization": access_token}
    uploaded_filename, content = read_file(file_path)
    files = {'file': (uploaded_filename, content)}
    # Send the POST request
    response = requests.post(url, data=data, headers=headers,files=files)
    if response['modelling_mode'].lower() == mode:
        if data.get('res_type') == 'image':
            return response['result']
        return response.json()
    else:
        return "Invalid Mode!"


def comprehensive_model_monitoring(token,deployment_id,res_type,file_path,mode):
    data = {
    'res_type':res_type,
    'deployment_id': deployment_id
    }
    url = f"{base_url}/training/comprehensive/monitor-model"
    # Get The Monitor Graph Of The Deployed Model
    access_token = 'Bearer '+ token
    headers = {"Authorization": access_token}
    uploaded_filename, content = read_file(file_path)
    files = {'file': (uploaded_filename, content)}
    # Send the POST request
    response = requests.post(url, data=data, headers=headers,files=files)
    if response.json()['modelling_mode'].lower() == mode:
        if data.get('res_type') == 'image':
            return response.content
        return response.json()['result']
    else:
        return "Invalid Mode!"