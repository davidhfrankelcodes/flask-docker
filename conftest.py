import pytest
import docker

@pytest.fixture
def docker_client():
    return docker.from_env()

@pytest.fixture
def app():
    from app import app
    return app

@pytest.fixture
def client(app):
    return app.test_client()
