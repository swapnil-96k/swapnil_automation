from syrupy.filters import paths
from syrupy.filters import props
from syrupy.matchers import path_type


def assert_all_users_path_match(snapshot, all_users, snapshot_name):

    #Match Data Type but skip the value check the. In generated snapshot also add data type and value.
    matcher=path_type({
        "value.0.givenName": (str,),
        "value.0.id": (str,),
        "value.0.displayName": (str,),
        "value.0.surname": (str,),
        "value.0.userPrincipalName": (str,),
    })
    assert all_users == snapshot(name=snapshot_name, matcher=matcher,)


def assert_single_user_exclude(snapshot, user_details, snapshot_name):
    
    #Exclude complete schema. Does not check the datatype and value and not added the schema in snapshot.
    exclude=paths(
        "displayName",
        "givenName",
        "surname",
        "userPrincipalName",
        "id"
    )
    assert user_details == snapshot(name=snapshot_name, exclude=exclude)


def assert_add_new_user_props(snapshot, new_user, snapshot_name):

    # Props = ignore any property with this name, no matter where it occurs in the data structure.
    exclude_props=props(
        "id",
        "userPrincipalName",
        "displayName"
    )
    assert new_user == snapshot(name=snapshot_name, exclude=exclude_props)

def assert_update_user(snapshot, updated_user, snapshot_name):

    matcher=path_type({
        "id": (str,),
        "userPrincipalName": (str,),
        "displayName": (str,)
    })
    assert updated_user == snapshot(name=snapshot_name, matcher=matcher)

def assert_delete_user_check_all(snapshot, deleted_user, snapshot_name):
    # Match Full Snapshot with any matcher, exclude and props
    assert deleted_user == snapshot(name=snapshot_name)