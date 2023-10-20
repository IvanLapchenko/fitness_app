import requests

base_url = "http://localhost:8000/auth/signup/"

user_data = {
    'username': 'testuser',
    'email': 'testuser@example.com',
    'about': 'This is a test user',
    'password': 'testpassword',
}

response = requests.post(base_url, data=user_data)

if response.status_code == 201:
    print("User created successfully.")
    user_id = response.json().get('user_id')
    print(f"User ID: {user_id}")
elif response.status_code == 400:
    print("Failed to create a user. Validation errors:")
    print(response.json().get('errors'))
else:
    print("Failed to create a user. Status code:", response.status_code)
