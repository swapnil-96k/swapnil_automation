from library import library
def assert_all_users(snapshot, all_users, snapshot_name):
    assert all_users == snapshot(name=snapshot_name)
