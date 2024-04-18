
def test_testing():
    assert True

def test_fastapi_import():
    from fastapi import FastAPI
    assert FastAPI

def test_health_check_import():
    from routers import health_check
    assert health_check
    
def test_api_route():
    import requests
    url = "http://127.0.0.1:8000/health-check" 
    response = requests.get(url)
    assert response.status_code == 200
    assert response.json() == {"message": "OK"}
    
    