import requests
from api_endpoints import api_orange_hrm
from config import config

def get_about_orange_hrm():
    response=requests.get(url=api_orange_hrm.about_api,headers=config.hrm_cookies)
    assert response.status_code == 200, "Failed to fetch about information"
    return response.json()
