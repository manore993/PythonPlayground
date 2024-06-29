import pytest

from flask_helloworld import create_app


@pytest.fixture
def client():
    app = create_app({"TESTING": True})
    with app.test_client() as client:
        yield client

def test_should_status_code_be_ok(client):
	response = client.get('/')
	assert response.status_code == 200
	assert response.data.decode() == "<p>Hello, World!</p>"

def test_should_status_code_be_error(client):
	response = client.get('/xxx')
	assert response.status_code == 404	

# TODO test case parametrized with multiple different user names
def test_should_greet_user(client):
	response = client.get('/user/Toto')
	assert response.status_code == 200	
	assert response.data.decode() == "Hello, Toto!"

def test_should_greet_user_and_escape_special_chars(client):
	response = client.get('/user/Toto&')
	assert response.status_code == 200	
	assert response.data.decode() != 'Hello, Toto&!'
	assert response.data.decode() == 'Hello, Toto&amp;!'
        
def test_post_nethod(client): 
    response = client.post('/', data={'username' : 'toto', 'password' : 'azerty'})
    assert response.status_code == 200	
    assert response.data.decode() == 'toto with azerty'

# TODO test post with missing paraneters
