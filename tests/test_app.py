import os
import pytest
from app import app

@pytest.fixture
def client():
    # Set up the Flask test client
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    # Create a dummy 'index.html' file in the templates directory for testing
    if not os.path.exists('templates'):
        os.makedirs('templates')
    with open('templates/index.html', 'w') as f:
        f.write('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Render</title>
</head>
<body>
    <h1>Habibi its working</h1>
    <p>Python and Git Actions</p>
    <h2>I'm studying Github</h2>
    <h3>niggaaaaa</h3>
</body>
</html>''')

    # Send a GET request to the root route
    response = client.get('/')
    
    # Check if the response is successful
    assert response.status_code == 200
    
    # Check if the content returned is the expected HTML
    assert b'Habibi its working' in response.data

    # Cleanup the dummy file after test
    os.remove('templates/index.html')
