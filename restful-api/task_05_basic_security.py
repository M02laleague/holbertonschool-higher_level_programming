#!/usr/bin/env python3
"""
Ce script configure une application Flask qui démontre l'authentification
basique et JWT, y compris le contrôle d'accès basé sur les rôles.

Il comprend :
- Authentification HTTP basique en utilisant Flask-HTTPAuth.
- Authentification basée sur les tokens avec Flask-JWT-Extended.
- Routes protégées nécessitant une authentification.
- Contrôle d'accès basé sur les rôles pour les routes réservées
aux administrateurs.

Modules :
- Flask : Un micro-framework web pour Python.
- Flask-HTTPAuth :
Fournit l'authentification HTTP basique pour les routes Flask.
- Flask-JWT-Extended : Ajoute le support JWT à Flask.
- werkzeug.security :
Fournit des utilitaires pour le hachage des mots de passe.
- functools.wraps : Utilisé pour préserver les informations de fonction
lors de la création de décorateurs.

Usage :
- Exécutez le script et utilisez un client HTTP comme curl ou Postman pour
interagir avec l'API.
"""


from functools import wraps

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (JWTManager, create_access_token,
                                get_jwt_identity, jwt_required)
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

# Clé secrète pour JWT (à remplacer par une clé sécurisée en production)
app.config['JWT_SECRET_KEY'] = 'your-secret-key'
jwt = JWTManager(app)

# Données utilisateur en mémoire
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """
    Vérifie le nom d'utilisateur et le mot de passe pour
    l'authentification basique.

    Args:
        username (str): Le nom d'utilisateur fourni par le client.
        password (str): Le mot de passe fourni par le client.

    Returns:
        bool: True si les identifiants sont valides, False sinon.
    """
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return True
    return False


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """
    Route protégée avec l'authentification basique.

    Returns:
        Response: Un message indiquant que l'accès est accordé.
    """
    return "Basic Auth: Access Granted"


@app.route('/login', methods=['POST'])
def login():
    """
    Authentifie l'utilisateur et retourne un token JWT.

    Attend des données JSON avec 'username' et 'password'.

    Returns:
        Response: Un JSON contenant le token d'accès si les
        identifiants sont valides.
    """
    data = request.get_json()
    if not data or not data.get('username') or not data.get('password'):
        return jsonify({"error": "Username and password required"}), 400

    username = data['username']
    password = data['password']
    user = users.get(username)

    if user and check_password_hash(user['password'], password):
        # Crée un nouveau token avec l'identité de l'utilisateur
        access_token = create_access_token(
            identity={'username': username, 'role': user['role']}
        )
        return jsonify(access_token=access_token)
    else:
        return jsonify({"error": "Invalid credentials"}), 401


@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    """
    Route protégée avec l'authentification JWT.

    Returns:
        Response: Un message indiquant que l'accès est accordé.
    """
    return "JWT Auth: Access Granted"


def admin_required(fn):
    """
    Décorateur pour s'assurer que l'utilisateur a le rôle d'administrateur.

    Args:
        fn (function): La fonction de route à envelopper.

    Returns:
        function: La fonction enveloppée.
    """
    @wraps(fn)
    def wrapper(*args, **kwargs):
        jwt_identity = get_jwt_identity()
        if jwt_identity and jwt_identity.get('role') == 'admin':
            return fn(*args, **kwargs)
        else:
            return jsonify({"error": "Admin access required"}), 403
    return wrapper


@app.route('/admin-only')
@jwt_required()
@admin_required
def admin_only():
    """
    Route accessible uniquement aux utilisateurs administrateurs.

    Returns:
        Response: Un message indiquant que l'accès administrateur est accordé.
    """
    return "Admin Access: Granted"


# Gestionnaires d'erreurs pour JWT
@jwt.unauthorized_loader
def handle_unauthorized_error(_err):
    """
    Gère les erreurs non autorisées lorsque le JWT est manquant ou invalide.

    Args:
        _err (str): Le message d'erreur (non utilisé).

    Returns:
        Response: Un message d'erreur JSON avec le code statut 401.
    """
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(_err):
    """
    Gère les erreurs lorsque le token JWT est invalide.

    Args:
        _err (str): Le message d'erreur (non utilisé).

    Returns:
        Response: Un message d'erreur JSON avec le code statut 401.
    """
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(_jwt_header, _jwt_payload):
    """
    Gère les erreurs lorsque le token JWT a expiré.

    Args:
        _jwt_header (dict): L'en-tête du token JWT (non utilisé).
        _jwt_payload (dict): La charge utile du token JWT (non utilisé).

    Returns:
        Response: Un message d'erreur JSON avec le code statut 401.
    """
    return jsonify({"error": "Token has expired"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(_jwt_header, _jwt_payload):
    """
    Gère renouvellement information exigeant un nouveau token.

    Args:
        _jwt_header (dict): L'en-tête du token JWT (non utilisé).
        _jwt_payload (dict): La charge utile du token JWT (non utilisé).

    Returns:
        Response: Un message d'erreur JSON avec le code statut 401.
    """
    return jsonify({"error": "Fresh token required"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(_jwt_header, _jwt_payload):
    """
    Gère lorsque le token JWT a été révoqué.

    Args:
        _jwt_header (dict): L'en-tête du token JWT (non utilisé).
        _jwt_payload (dict): La charge utile du token JWT (non utilisé).

    Returns:
        Response: Un message d'erreur JSON avec le code statut 401.
    """
    return jsonify({"error": "Token has been revoked"}), 401


if __name__ == "__main__":
    app.run()