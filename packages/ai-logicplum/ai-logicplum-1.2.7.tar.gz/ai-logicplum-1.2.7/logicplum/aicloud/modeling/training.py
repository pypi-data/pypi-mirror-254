import requests
import json
#from ..config import base_url, api_token
base_url = "https://dev-aicloud-gateway.logicplum.com/api/v2"
def read_file(file_path):
    with open(file_path, "rb") as file:
        uploaded_filename = file_path.split('\\')[-1]
        content = file.read()
        return uploaded_filename, content

def create_model(file_path, endpoint, token, data):
    uploaded_filename, content = read_file(file_path)
    url = f"{base_url}/training/{endpoint}"
    files = {'file': (uploaded_filename, content)}
    access_token = 'Bearer '+ token
    headers = {"Authorization": access_token}
    # Send the POST request
    response = requests.post(url, data=data, files=files, headers=headers)
    return response.json()

def aipilot_modeling(file_path, client_token, data):
    return create_model(file_path, "create_model", client_token, data)

def quick_modeling(file_path, client_token, data):
    return create_model(file_path, "quick-create_model", client_token, data)

def manual_modeling(file_path, client_token, data):
    return create_model(file_path, "manual-create_model", client_token, data)

def comprehensive_modeling(file_path, client_token, data):
    return create_model(file_path, "comprehensive-create_model", client_token, data)




def model_deployment(project_id,model_id,token):
    try:
        data = {
            "project_id": project_id,
        }
        if model_id is not None:
            data["model_id"] = model_id
        deployment_url = f"{base_url}/training/deployment"
        access_token = 'Bearer '+ token
        headers = {"Authorization": access_token}
        # Send the POST request
        response = requests.post(deployment_url, data=data, headers=headers)
        return response.json()
    except:
        return "manual model has no deployment"

 
def get_training_result(project_id,token):
    url = f"{base_url}/training/get-results/{project_id}"
    access_token = 'Bearer '+ token
    headers = {"Authorization": access_token}
    response = requests.get(url, headers=headers)
    response_json=response.json()
    return response_json



def get_holdout_result(project_id,model_id,token):

    data = {
        "project_id":project_id,
        "model_id": model_id
    }

    url = f"{base_url}/training/model-results"
    access_token = 'Bearer '+ token
    headers = {"Authorization": access_token}
    response = requests.post(url,headers=headers,data=data)
    return response.json()


def get_projectdetails(app_id,token):
    url = f"{base_url}/training/project-details/{app_id}"
    access_token = 'Bearer '+ token
    headers = {"Authorization": access_token}
    response = requests.get(url,headers=headers)
    return response.json()


def get_jobdetails(app_id,token):
    url = f"{base_url}/training/job-details?app_id={app_id}"
    access_token = 'Bearer '+ token
    headers = {"Authorization": access_token}
    response = requests.get(url,headers=headers)
    return response.json()
 
def json_check(response):
    if response.status_code == 200:
        return response.json()
    else:
        return f"Request failed with status code: {response.status_code}"

def get_blueprint(deployment_id,token):
    url = f"{base_url}/training/blueprint"
    access_token = 'Bearer '+ token
    headers = {"Authorization": access_token}
    data = {
        "deployment_id" : deployment_id
    }
    response = requests.post(url,data=data,headers=headers)
    return json_check(response)

def get_deploymentdetails(deployment_id,token):
    url = f"{base_url}/training/deployment/{deployment_id}"
    access_token = 'Bearer '+ token
    headers = {"Authorization": access_token}
    response = requests.get(url,headers=headers)
    return json_check(response)
    
def get_project_details(project,token):
    url = f"{base_url}/training/project/{project}"
    access_token = 'Bearer '+ token
    headers = {"Authorization": access_token}
    response = requests.get(url,headers=headers)
    return json_check(response)

def delete_deployment(deployment_id,token):
    url = f"{base_url}/training/deployment/{deployment_id}"
    access_token = 'Bearer '+ token
    headers = {"Authorization": access_token}
    response = requests.delete(url,headers=headers)
    return json_check(response)

def delete_multiple_deployment(project_id,token):
    url = f"{base_url}/training/deployment-details/{project_id}"
    access_token = 'Bearer '+ token
    headers = {"Authorization": access_token}
    response = requests.delete(url,headers=headers)
    return json_check(response)

def delete_project(project,token):
    url = f"{base_url}/training/project/{project}"
    access_token = 'Bearer '+ token
    headers = {"Authorization": access_token}
    response = requests.delete(url,headers=headers)
    return json_check(response)

def update_deployment(deployment_id,model_id,token):
    url = f"{base_url}/training/deployment/{deployment_id}"
    access_token = 'Bearer '+ token
    headers = {"Authorization": access_token}
    data = {
        "model_id":model_id
    }
    response = requests.put(url,data=data,headers=headers)
    return json_check(response)


def retrain_model(token, data):
    url = f"{base_url}/training/model-retrain"
    access_token = 'Bearer '+ token
    headers = {"Authorization": access_token}
    response = requests.post(url, data=data, headers=headers)
    try:
        response_data = response.json()
    except:
        response_data = None

    if response_data:
        return response_data
    else:
        return "Something went wrong on service"
