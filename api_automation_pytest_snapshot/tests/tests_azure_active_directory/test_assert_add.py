import pytest
from resources.reso_azure_active_directory import reso_aad
from resources.reso_azure_active_directory import assert_snapshot_aad

@pytest.fixture(scope="session",autouse=True)
def generate_token():
    global aad_headers
    access_token = reso_aad.generate_access_token_for_aad()
    aad_headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    print("Generated AAD Token")

def test_get_all_users(snapshot):
    all_users = reso_aad.get_all_users(aad_headers)
    print("all user in aad",all_users.json())
    assert_snapshot_aad.assert_all_users_path_match(snapshot, all_users.json(),"all_users_snapshot")

    print("all user in aad",all_users.json())
    for user in all_users.json()["value"]:
        if user["displayName"] == "swapnil dhalwade":
            global swapnil_user_id
            swapnil_user_id = user["id"]
            assert user["surname"] == "dhalwade"
            assert user["givenName"] == "swapnil"
            break

def test_get_single_user_details(snapshot):
    user_details = reso_aad.get_single_users_details(aad_headers, swapnil_user_id)
    assert_snapshot_aad.assert_single_user_exclude(snapshot, user_details.json(), "single_user_snapshot")

def test_add_new_user(snapshot):
    global new_user_name, new_user_id
    new_user_name = "TestUser1234qq1qs1a"
    add_new_user = reso_aad.add_new_user(aad_headers, new_user_name)
    new_user_id = add_new_user.json()["id"]
    assert_snapshot_aad.assert_add_new_user_props(snapshot, add_new_user.json(), "add_new_user_snapshot")

def test_update_existing_user_details(snapshot):
    update_user_repo = reso_aad.update_existing_user(aad_headers, new_user_id)
    assert_snapshot_aad.assert_update_user(snapshot, update_user_repo, "update_user_snapshot")

def test_delete_user(snapshot):
    deleted_user_response = reso_aad.delete_user(aad_headers, new_user_id)
    assert_snapshot_aad.assert_delete_user_check_all(snapshot, deleted_user_response, "delete_user_snapshot")
