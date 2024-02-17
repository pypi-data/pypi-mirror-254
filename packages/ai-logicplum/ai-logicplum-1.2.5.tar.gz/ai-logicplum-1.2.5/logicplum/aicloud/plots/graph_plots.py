import requests
import base64
import json
from PIL import Image as PilImage
import io
from ..config import base_url, api_token


def display_response(res_type, response):
    if res_type == 'base64':
        return response
    else:
        # Check if the response is bytes (for 'image' type)
        if isinstance(response, bytes) and (response.startswith(b'\x89PNG') or response.startswith(b'\xff\xd8\xff\xe0')):
            # Open the image
            image = PilImage.open(io.BytesIO(response))
            
            # Convert image to RGB mode if it has an alpha channel
            if image.mode == 'RGBA':
                image = image.convert('RGB')

            # Display the image
            return image
        else:
            # Handle the case when response is not bytes as expected for 'image' type
            response_dict = json.loads(response.decode('utf-8'))
            return response_dict

def roc_plot(deployment_id,res_type,token):
    data = {
    "deployment_id": deployment_id,
    "res_type" : res_type 
    }
    url = f"{base_url}/plot/roc"
    access_token = 'Bearer '+ token
    headers = {"Authorization": access_token}
    response = requests.post(url, data=data,headers=headers)
    if data.get('res_type') == 'image':
        return response.content
    return response.json()


def advanced_lift_chart(deployment_id,res_type,token):
    data = {
    "deployment_id": deployment_id,
    "res_type" : res_type 
    }
    url = f"{base_url}/plot/advanced-lift-chart"
    access_token = 'Bearer '+ token
    headers = {"Authorization": access_token}
    # Send the POST request
    response = requests.post(url, data=data,headers=headers)
    if data.get('res_type') == 'image':
        return response.content
    return response.json()


def advanced_feature_impact(deployment_id,res_type,token):
    data = {
    "deployment_id": deployment_id,
    "res_type" : res_type 
    }
    url = f"{base_url}/plot/advanced-feature-impact"
    access_token = 'Bearer '+ token
    headers = {"Authorization": access_token}
    # Send the POST request
    response = requests.post(url, data=data,headers=headers)
    if data.get('res_type') == 'image':
        return response.content
    return response.json()


def partial_dependency(deployment_id,res_type,token):
    data = {
    "deployment_id": deployment_id,
    "res_type" : res_type 
    }
    url = f"{base_url}/plot/partial-dependency"
    access_token = 'Bearer '+ token
    headers = {"Authorization": access_token}
    # Send the POST request
    response = requests.post(url, data=data,headers=headers)
    if data.get('res_type') == 'image':
        return response.content
    return response.json()




def residual(deployment_id,res_type,token):
    data = {
    "deployment_id": deployment_id,
    "res_type" : res_type 
    }
    url = f"{base_url}/plot/residual"
    access_token = 'Bearer '+ token
    headers = {"Authorization": access_token}
    # Send the POST request
    response = requests.post(url, data=data,headers=headers)
    if data.get('res_type') == 'image':
        return response.content
    return response.json()



def predict_vs_actual(deployment_id,res_type,token):
    data = {
    "deployment_id": deployment_id,
    "res_type" : res_type 
    }
    url = f"{base_url}/plot/predict-vs-actual"
    access_token = 'Bearer '+ token
    headers = {"Authorization": access_token}
    # Send the POST request
    response = requests.post(url, data=data,headers=headers)
    if data.get('res_type') == 'image':
        return response.content
    return response.json()


def word_cloud(deployment_id,res_type,token):
    data = {
    "deployment_id": deployment_id,
    "res_type" : res_type 
    }
    url = f"{base_url}/plot/wordcloud"
    access_token = 'Bearer '+ token
    headers = {"Authorization": access_token}
    # Send the POST request
    response = requests.post(url, data=data,headers=headers)
    if data.get('res_type') == 'image':
        return response.content
    return response.json()


def confusion_matrix(deployment_id,res_type,token):
    data = {
    "deployment_id": deployment_id,
    "res_type" : res_type 
    }
    url = f"{base_url}/plot/confusion-matrix"
    access_token = 'Bearer '+ token
    headers = {"Authorization": access_token}
    # Send the POST request
    response = requests.post(url, data=data,headers=headers)
    if data.get('res_type') == 'image':
        return response.content
    return response.json()


def get_allColumns(deployment_id,token):
    url = f"{base_url}/plot/dataset-columns//{deployment_id}"
    access_token = 'Bearer '+ token
    headers = {"Authorization": access_token}
    response = requests.get(url,headers=headers)
    return response.json()

def prediction_distribution(deployment_id,res_type,token):
    data = {
    "deployment_id": deployment_id,
    "res_type" : res_type 
    }
    url = f"{base_url}/plot/prediction-distribution"
    access_token = 'Bearer '+ token
    headers = {"Authorization": access_token}
    # Send the POST request
    response = requests.post(url, data=data,headers=headers)
    if data.get('res_type') == 'image':
        return response.content
    return response.json()


def blueprint_plot(deployment_id,token):
    data = {
    "deployment_id": deployment_id,
    }
    url = f"{base_url}/plot/blueprint-plot"
    access_token = 'Bearer '+ token
    headers = {"Authorization": access_token}
    response = requests.post(url, data=data,headers=headers)
    return response.json()