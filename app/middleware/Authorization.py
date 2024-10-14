from flask import request, jsonify

#Authentication middleware password
TOKEN = "apipass123"


#Authentication
def authenticate_token():
    token = request.headers.get("Authorization")
    if not token or token != f"Bearer {TOKEN}":
        return jsonify({"error": "Unauthorized"}), 401

