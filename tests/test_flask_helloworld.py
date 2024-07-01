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


@pytest.mark.parametrize("username", [
"toto",
"titi",
"moumou",
"foufou",
"mimi",
"meemaw"
])
def test_should_greet_user(client, username):
	response = client.get(f'/user/{username}')
	assert response.status_code == 200	
	assert response.data.decode() == f"Hello, {username}!"

def test_should_greet_user_and_escape_special_chars(client):
	response = client.get('/user/Toto&')
	assert response.status_code == 200	
	assert response.data.decode() != 'Hello, Toto&!'
	assert response.data.decode() == 'Hello, Toto&amp;!'
        
def test_post_nethod(client): 
    response = client.post('/', data={'username' : 'toto', 'password' : 'azerty'})
    assert response.status_code == 200	
    assert response.data.decode() == 'toto with azerty'
 
def test_post_nethod_escape(client): 
    response = client.post('/', data={'username' : 'toto', 'password' : 'azerty<script>alert("hi");</script>'})
    assert response.status_code == 200	
    assert response.data.decode() != 'toto with azerty<script>alert("hi");</script>'
    assert response.data.decode() == 'toto with azerty&lt;script&gt;alert(&#34;hi&#34;);&lt;/script&gt;'

# TODO test post with missing paraneters
@pytest.mark.parametrize("username, password, expected_result", [
("toto", "toto95", "Hello toto!"),
("toto", "toto8256", "Username and password do not match. Try again"),
("admin", "adminpw", "Hello admin! You are the admin acoount."),
("admin", "adminpw2145", "Username and password do not match. Try again")
])

def test_post_nethod_escape(client, username, password, expected_result): 
    response = client.post('/login/', data={'username' : username , 'password' : password})
    assert response.status_code == 200	
    assert response.data.decode() == expected_result

