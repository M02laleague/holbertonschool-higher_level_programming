#!/usr/bin/env python3
"""
This script sets up a simple Flask web application to demonstrate API routing,
JSON data handling, and basic request-response cycles.

It provides endpoints for:

- Displaying a welcome message at the root URL (`/`).
- Returning a list of usernames at `/data`.
- Checking the API status at `/status`.
- Retrieving user information at `/users/<username>`.
- Adding a new user via a POST request to `/add_user`.

Modules used:

- Flask: A micro web framework for building web applications and APIs.
- jsonify: A utility function to convert Python data structures to JSON format.
- request: Handles incoming requests, providing access to headers and data.
- Response: Used to customize response objects,
including headers and MIME types.
"""

# Standard library imports
from typing import Dict, Any

# Third-party imports
from flask import Flask, jsonify, request, Response

app = Flask(__name__)


# In-memory dictionary to store users (starting empty)
users: Dict[str, Dict[str, Any]] = {}


@app.route('/')
def home():
    """
    Handles the root endpoint and returns a welcome message.

    Returns:
        Response: A plain text welcome message.
    """
    return Response("Welcome to the Flask API!", mimetype='text/plain')


@app.route('/data')
def get_users():
    """
    Returns a JSON response with a list of all usernames.

    Returns:
        Response: A JSON array of usernames.
    """
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    """
    Returns the API status.

    Returns:
        Response: A plain text message indicating the API status.
    """
    return Response("OK", mimetype='text/plain')


@app.route('/users/<username>')
def get_user(username):
    """
    Returns the complete user object corresponding to the provided username.

    Args:
        username (str): The username to retrieve.

    Returns:
        Response: A JSON object of the user's details if found,
                otherwise a JSON error message with a 404 status code.
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Handles POST requests to add a new user.

    Expects JSON data containing 'username', 'name', 'age', and 'city'.

    Returns:
        Response: A confirmation message with the added user's data,
                or an error message if 'username' is missing or a duplicate
                with the same details exists.
    """
    data = request.get_json()

    if not data or 'username' not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data['username']

    # Check if the same username with the same details exists
    existing_user = users.get(username)
    if existing_user and existing_user == {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }:
        return jsonify({
            "error": "User with identical details already exists"
        }), 400

    # If the username exists but with different details, allow it
    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }
    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201  # Use 201 Created for successful POST requests


@app.errorhandler(404)
def page_not_found(e):
    """
    Handles undefined endpoints and returns a custom error message.

    Args:
        e (Exception): The raised exception.

    Returns:
        Response: A JSON error message with a 404 status code.
    """
    return jsonify({"error": str(e)}), 404


# Run the application
if __name__ == "__main__":
    app.run()