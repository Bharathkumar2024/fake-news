"""
Vercel Serverless Function Entry Point
This wraps the Flask app for Vercel deployment.
"""

import os
import sys

# Add root project directory to path
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, root_dir)

from web_app.backend.app import app

# Vercel calls this 'app' as the WSGI handler
