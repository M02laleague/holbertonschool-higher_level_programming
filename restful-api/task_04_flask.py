#!/usr/bin/python3

from flask import Flask, jsonify, request

# Initialize the Flask application
app = Flask(__name__)

# In-memory storage for user data
users = {}

# Root endpoint


@app.route('/')
def home():
    return "Welcome to the Flask API!"

# Endpoint to get a list of all usernames


@app.route('/data')
def get_usernames():
    return jsonify(list(users.keys()))

# Endpoint to check the API status


@app.route('/status')
def get_status():
    return "OK"

# Endpoint to get user details by username


@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

# Endpoint to add a new user (via POST request)


@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json  # Parse incoming JSON data

    # Check if 'username' field is provided
    username = data.get('username')
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Check if the username already exists
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Add the user to the dictionary
    users[username] = data

    # Return success response with the new user's data
    return jsonify({"message": "User added", "user": data}), 201


# Main function to run the app
if __name__ == '__main__':
    app.run(debug=True)
