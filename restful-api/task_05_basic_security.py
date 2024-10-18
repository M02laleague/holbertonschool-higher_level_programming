#!/usr/bin/python3

from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity

# Initialize Flask app and set up JWT secret key
app = Flask(__name__)
auth = HTTPBasicAuth()
# Secure this properly in production
app.config['JWT_SECRET_KEY'] = 'your_secret_key'
jwt = JWTManager(app)

# In-memory user store with hashed passwords and roles
users = {
    "user1": {"password": generate_password_hash("password"), "role": "user"},
    "admin1": {"password": generate_password_hash("password"), "role": "admin"}
}

# Verify username and password for Basic Authentication


@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users[username]['password'], password):
        return username
    return None  # No user found or invalid password

# Basic Auth protected route


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return jsonify(message="Basic Auth: Access Granted")

# Route for user login with JWT token generation


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()  # Get JSON payload from the request
    username = data.get('username')
    password = data.get('password')

    user = users.get(username)

    if user and check_password_hash(user['password'], password):
        # Generate access token with user role embedded
        access_token = create_access_token(
            identity={'username': username, 'role': user['role']})
        return jsonify(access_token=access_token)

    # Invalid credentials
    return jsonify({"msg": "Bad username or password"}), 401

# JWT protected route (only accessible with valid JWT token)


@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    return jsonify(message="JWT Auth: Access Granted")

# Admin-only route protected by JWT and role-based access control


@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    # Get the identity from the JWT token (username and role)
    identity = get_jwt_identity()

    if identity['role'] == 'admin':
        return jsonify(message="Admin Access: Granted")

    # Forbidden for non-admin users
    return jsonify({"msg": "Admin privilege required"}), 403

# JWT Error Handlers


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


# Main function to run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
