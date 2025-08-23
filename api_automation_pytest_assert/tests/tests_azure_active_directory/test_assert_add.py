import pytest
from resources.reso_azure_active_directory import reso_aad

@pytest.fixture(scope="session",autouse=True)
def generate_token():
    global aad_headers
    access_token = reso_aad.generate_access_token_for_aad()
    aad_headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    print("Generated AAD Token")

def test_get_all_users():
    all_users = reso_aad.get_all_users(aad_headers)
    print("all user in aad",all_users.json())
    for user in all_users.json()["value"]:
        if user["displayName"] == "swapnil dhalwade":
            global swapnil_user_id
            swapnil_user_id = user["id"]
            assert user["surname"] == "dhalwade"
            assert user["givenName"] == "swapnil"
            break

def test_get_single_user_details():
    user_details = reso_aad.get_single_users_details(aad_headers, swapnil_user_id)
    print("Single User details:", user_details.json())
    assert user_details.json()["displayName"] == "swapnil dhalwade"
    assert user_details.json()["surname"] == "dhalwade"

def test_add_new_user():
    global new_user_name, new_user_id
    new_user_name = "TestUser1234qq1q1a"
    add_new_user = reso_aad.add_new_user(aad_headers, new_user_name)
    print("Add New User Response:", add_new_user.json())
    assert add_new_user.json()["displayName"] == new_user_name
    new_user_id = add_new_user.json()["id"]

def test_update_existing_user_details():
    update_user_repo = reso_aad.update_existing_user(aad_headers, new_user_id)
    assert update_user_repo.status_code == 204

def test_delete_user():
    deleted_user_response = reso_aad.delete_user(aad_headers, new_user_id)
    assert deleted_user_response.status_code == 204