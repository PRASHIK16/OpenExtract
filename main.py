from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS
import os
import json

app = Flask(__name__)
CORS(app)

# JWT secret key
app.config['JWT_SECRET_KEY'] = os.environ.get("JWT_SECRET_KEY", "super-secret-key")
jwt = JWTManager(app)

# Path to store user credentials
USERS_FILE = "users.json"

# Load users from the file
def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {}
    return {}

# Save users to the file
def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=4)

# ------------------ 🔐 Register API ------------------
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password are required."}), 400

    users = load_users()

    if username in users:
        return jsonify({"error": "Username already exists."}), 409

    users[username] = generate_password_hash(password)
    save_users(users)

    return jsonify({"msg": "✅ User registered successfully."}), 201

# ------------------ 🔑 Login API ------------------
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    users = load_users()

    if username not in users:
        return jsonify({"error": "User not found."}), 404

    if not check_password_hash(users[username], password):
        return jsonify({"error": "Invalid credentials."}), 401

    access_token = create_access_token(identity=username)
    return jsonify(token=access_token), 200

# ------------------ 🔐 Protected API ------------------
@app.route('/api/secure-data', methods=['GET'])
@jwt_required()
def secure_data():
    return jsonify({"data": "🔒 This is secure financial data only for authenticated users."})

# ------------------ ⚙️ Run Server ------------------
if __name__ == "__main__":
    app.run(debug=True, use_reloader=False, port=5000)
