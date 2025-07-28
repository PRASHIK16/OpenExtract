import requests

# Step 1: Login
login_url = "http://127.0.0.1:5000/login"
login_data = {
    "username": "admin",
    "password": "admin123"
}
login_response = requests.post(login_url, json=login_data)
print("Login response:", login_response.json())

# Step 2: Use the token to access the secure route
token = login_response.json().get("token")
headers = {
    "Authorization": f"Bearer {token}"
}
secure_url = "http://127.0.0.1:5000/api/secure-data"
secure_response = requests.get(secure_url, headers=headers)
print("Secure data response:", secure_response.json())
