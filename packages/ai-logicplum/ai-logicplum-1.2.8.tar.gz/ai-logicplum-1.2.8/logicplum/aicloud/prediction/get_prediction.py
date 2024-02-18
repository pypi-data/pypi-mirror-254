import requests
from ..config import base_url, api_token

def read_file(file_path):
    with open(file_path, "rb") as file:
        uploaded_filename = file_path.split('\\')[-1]
        content = file.read()
        return uploaded_filename, content


def make_prediction(file_path, endpoint, token, data):
    uploaded_prediction_filename, content = read_file(file_path)
    url = f"{base_url}/prediction/{endpoint}" if endpoint else f"{base_url}/prediction/"
    access_token = 'Bearer '+ token
    headers = {"Authorization": access_token}
    files = {'prediction_file': (uploaded_prediction_filename, content)}
    try:
        response = requests.post(url, data=data, files=files, headers=headers)
        response.raise_for_status()  # Raise an HTTPError if the request fails
        return response.json()
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None

def aipilot_prediction(file_path, token, deployment_id):
    data = {
    "deployment_id": deployment_id,
    }
    return make_prediction(file_path, "", token, data)

def quick_prediction(file_path, token, deployment_id):
    data = {
    "deployment_id": deployment_id,
    }
    return make_prediction(file_path, "quick-predict", token, data)

def manual_prediction(file_path, token, project_id):
    data = {
    "project_id": project_id,
    }
    return make_prediction(file_path, "manual-predict", token, data)

def comprehensive_prediction(file_path, token, deployment_id):
    data = {
    "deployment_id": deployment_id,
    }
    return make_prediction(file_path, "comprehensive-predict", token, data)


def get_prediction_result(deployment_or_project_id, token, mode):
    url = ""
    access_token = 'Bearer '+ token
    headers = {"Authorization": access_token}

    if mode.lower() == "quick":
        url = f"{base_url}/training/get-results/{deployment_or_project_id}"
    else:
        url = f"{base_url}/prediction/get-prediction-score/{deployment_or_project_id}"

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise an HTTPError if the request fails
        return response.json()
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None
