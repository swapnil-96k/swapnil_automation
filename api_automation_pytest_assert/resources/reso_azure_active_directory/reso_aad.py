import requests
from config import config_aad
from api_endpoints import api_aad


def generate_access_token_for_aad():
    token_url = api_aad.generate_token.replace("{tenant-id}", config_aad.aad_tenant_id)
    payload = {
        "client_id": config_aad.aad_client_id,
        "client_secret": config_aad.aad_client_secret,
        "scope": "https://graph.microsoft.com/.default",
        "grant_type": "client_credentials"
    }
    aad_tokens=requests.post(url=token_url, data=payload)
    assert aad_tokens.status_code == 200, f"Token generation failed with status code {aad_tokens.json()}"
    aad_access_token = aad_tokens.json()["access_token"]
    return aad_access_token

def get_all_users(aad_headers):
    all_users = requests.get(url=api_aad.user_api_base, headers=aad_headers)
    assert all_users.status_code == 200, f"Get all users failed with status code {all_users.json()}"
    return all_users

def get_single_users_details(aad_headers,user_id):
    single_users_details = requests.get(url= api_aad.user_api_base + "/"+user_id, headers=aad_headers)
    assert single_users_details.status_code == 200, f"Get all users failed with status code {single_users_details.json()}"
    return single_users_details

def add_new_user(aad_headers, user_name):
    payload = {
                "accountEnabled": False,
                "displayName": user_name,
                "mailNickname": user_name.lower(),
                "userPrincipalName": f"{user_name.lower()}@dhalwadesgmail.onmicrosoft.com",
                "passwordProfile": {
                    "forceChangePasswordNextSignIn": True,
                    "password": config_aad.aad_temp_password
                }
              }
    add_user = requests.post(url=api_aad.user_api_base, headers=aad_headers, json=payload)
    assert add_user.status_code == 201, f"User creation failed with status code {add_user.json()}"
    return add_user

def update_existing_user(aad_headers, user_id):
    payload = {"jobTitle": "Senior Developer"}
    update_user= requests.patch(url=api_aad.user_api_base + "/"+user_id, headers=aad_headers, json=payload)
    assert update_user.status_code == 204, f"User update failed with status code {update_user.json()}"
    return update_user

def delete_user(aad_headers, user_id):
    delete_user_response = requests.delete(url=api_aad.user_api_base + "/"+user_id, headers=aad_headers)
    assert delete_user_response.status_code == 204, f"User deletion failed with status code {delete_user_response.json()}"
    return delete_user_response
