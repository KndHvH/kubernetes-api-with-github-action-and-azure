
def test_testing():
    assert True

def test_fastapi_import():
    from fastapi import FastAPI
    assert FastAPI

def test_health_check_import():
    from app.routers import health_check
    assert health_check
    
