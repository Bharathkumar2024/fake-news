import os
import sys

# Vercel entrypoint that imports and exposes the Flask app
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, root_dir)

try:
    from web_app.backend.app import app
except Exception as e:
    from flask import Flask, jsonify
    app = Flask(__name__)
    @app.route('/api/health')
    def error_health():
        return jsonify({"status": "error", "message": str(e), "traceback": "Check Vercel logs"}), 500
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def error_route(path):
        return f"Initialization Error: {e}", 500
