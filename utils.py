import os
from flask import request, jsonify
import datetime

API_KEY = os.getenv("API_KEY", "testkey")

def check_api_key(req):
    key = req.headers.get("x-api-key")
    if key != API_KEY:
        return jsonify({"error": "Unauthorized"}), 401

def log_request(req):
    print(f"[{datetime.datetime.now()}] {req.method} {req.path}")
