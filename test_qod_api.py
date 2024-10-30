import pytest
import requests
import platform

ENDPOINT = "http://localhost:8080"

@pytest.mark.repeat(10)  # Run the test 10 times
def test_can_call_endpoint():
    if "https" in ENDPOINT.lower():
        response = requests.get(ENDPOINT, verify=False)
    else:
        response = requests.get(ENDPOINT)
    
    print("This request is being served by server: " + platform.node())

    assert response.status_code == 200

@pytest.mark.repeat(10)  # Run the test 10 times
def test_get_daily_quote():
    if "https" in ENDPOINT.lower():
        response = requests.get(ENDPOINT + "/daily", verify=False)
    else:
        response = requests.get(ENDPOINT + "/daily")
    
    print("This request is being served by server: " + platform.node())
    
    #data = response.json();
    #print(data)

    assert response.status_code == 200
    
@pytest.mark.repeat(10)  # Run the test 10 times
def test_get_random_quote():
    if "https" in ENDPOINT.lower():
        response = requests.get(ENDPOINT + "/random", verify=False)
    else:
        response = requests.get(ENDPOINT + "/random")
    
    print("This request is being served by server: " + platform.node())
    
    #data = response.json();
    #print(data)

    assert response.status_code == 200