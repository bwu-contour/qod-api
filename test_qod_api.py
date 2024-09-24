import pytest
import requests

ENDPOINT = "http://localhost:8080"

@pytest.mark.repeat(10)  # Run the test 10 times
def test_can_call_endpoint():
    response = requests.get(ENDPOINT, verify=False)
    assert response.status_code == 200

@pytest.mark.repeat(10)  # Run the test 10 times
def test_get_daily_quote():
    response = requests.get(ENDPOINT + "/daily", verify=False)
    assert response.status_code == 200
    
    #data = response.json();
    #print(data)
    
@pytest.mark.repeat(10)  # Run the test 10 times
def test_get_random_quote():
    response = requests.get(ENDPOINT + "/random", verify=False)
    assert response.status_code == 200
    
    #data = response.json();
    #print(data)