import requests
import base64
import json 
from ..config import base_url, api_token

def reports(deployment_id,token):
    data = {
    "deployment_id": deployment_id
    }

    url = f'{base_url}/plot/report'
    access_token = 'Bearer '+ token
    headers = {"Authorization": access_token}
    response = requests.post(url, data=data,headers=headers)
    pdf_data = response.content
    pdf_base64 = base64.b64encode(pdf_data).decode('utf-8')
    data = {
        'result': pdf_base64
    }
    json_string = json.dumps(data)
    return json_string

def read_file(file_path):
    with open(file_path, "rb") as file:
        uploaded_filename = file_path.split('\\')[-1]
        content = file.read()
        return uploaded_filename, content




def EDAreport(file_path,target,client_id,token):
    uploaded_filename, content = read_file(file_path)
    data = {
    'target': target,
    'client_id': client_id
    }
    url = f"{base_url}/training/eda-report"
    files = {'file': (uploaded_filename, content)}
    access_token = 'Bearer '+ token
    headers = {"Authorization": access_token}
    response = requests.post(url, data=data, files=files,headers=headers)
    return response.json()