import requests
import json
from time import sleep
import pytest

BASE_URL = 'https://www.reddit.com'
HEADERS = {'User-agent': 'your bot 0.1'}
RETRIES = 3
DELAY = 1  

def get_with_retry(url, headers, retries=RETRIES, delay=DELAY):
    for i in range(retries):
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response
        sleep(delay)                    
        #url ve headrsin status kodun yoxlanmasi 
    return response

def test_subreddit_hot():
    url = f'{BASE_URL}/r/python/hot.json'
    response = get_with_retry(url, HEADERS)
    
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    assert response.headers['Content-Type'] == 'application/json; charset=UTF-8', \
        f"Expected Content-Type application/json; charset=UTF-8, but got {response.headers['Content-Type']}"
    assert response.elapsed.total_seconds() < 2.0, f"Expected response time < 2.0 seconds, but got {response.elapsed.total_seconds()} seconds"
#headersin API yoxlanmasi
def test_user_about():
    url = f'{BASE_URL}/user/spez/about.json'
    response = get_with_retry(url, HEADERS)
    
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    assert response.headers['Content-Type'] == 'application/json; charset=UTF-8', \
        f"Expected Content-Type application/json; charset=UTF-8, but got {response.headers['Content-Type']}"
    assert response.elapsed.total_seconds() < 2.0, f"Expected response time < 2.0 seconds, but got {response.elapsed.total_seconds()} seconds"

def test_comments():
    response = get_with_retry(f'{BASE_URL}/comments/3g1jfi.json', HEADERS)
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    assert response.headers['Content-Type'] == 'application/json; charset=UTF-8', \
        f"Expected Content-Type application/json; charset=UTF-8, but got {response.headers['Content-Type']}"
    assert response.elapsed.total_seconds() < 2.0, f"Expected response time < 2.0 seconds, but got {response.elapsed.total_seconds()} seconds"

def test_subreddit_new():
    url = f'{BASE_URL}/r/python/new.json'
    response = get_with_retry(url, HEADERS)
    
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    assert response.headers['Content-Type'] == 'application/json; charset=UTF-8', \
        f"Expected Content-Type application/json; charset=UTF-8, but got {response.headers['Content-Type']}"
    assert response.elapsed.total_seconds() < 2.0, f"Expected response time < 2.0 seconds, but got {response.elapsed.total_seconds()} seconds"

def test_subreddit_top():
    url = f'{BASE_URL}/r/python/top.json'
    response = get_with_retry(url, HEADERS)
    
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    assert response.headers['Content-Type'] == 'application/json; charset=UTF-8', \
        f"Expected Content-Type application/json; charset=UTF-8, but got {response.headers['Content-Type']}"
    assert response.elapsed.total_seconds() < 2.0, f"Expected response time < 2.0 seconds, but got {response.elapsed.total_seconds()} seconds"

if __name__ == "__main__":
    pytest.main()
