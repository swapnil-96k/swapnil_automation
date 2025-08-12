import pytest
import json

def pytest_addoption(parser):
    parser.addoption("--baseurl", action="store", default="https://", help="Base URL for API tests")
    parser.addoption("--secrets", action="store", help="Cookies for HRM API")

@pytest.fixture(scope="session")
def pre_requisite(request):
    baseurl = request.config.getoption("--baseurl")
    secrets = request.config.getoption("--secrets")
    allsecrets = json.loads(secrets) if secrets else {}
    return {"baseurl": baseurl, "secrets": allsecrets}