

from flask import Flask, request, jsonify
import os
import sys

try:
    from flask_cors import CORS
    cors_available = True
except ImportError:
    print("flask-cors not installed. CORS headers may be limited.")
    cors_available = False

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import config
from src.fact_checker import fact_checker
from src.utils import ensure_models_exist, get_project_stats

# Initialize Flask app with static file serving
web_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
app = Flask(
    __name__,
    static_folder=os.path.join(web_dir, '..', 'public'),
    static_url_path='',
    template_folder=os.path.join(web_dir, '..', 'public')
)

# Enable CORS if available
if cors_available:
    CORS(app)
else:
    # Add manual CORS headers as fallback
    @app.after_request
    def add_cors_headers(response):
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        return response

print("=" * 60)
print("Starting Fact-Checker Backend API")
print("=" * 60)
print(f"Server: http://localhost:{config.FLASK_PORT}")
print("=" * 60 + "\n")

# Serve static files and main page
@app.route('/')
def serve_index():
    """Serve the main HTML page"""
    from flask import send_from_directory
    html_dir = os.path.join(web_dir, '..', 'public')
    return send_from_directory(html_dir, 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    """Serve static files (CSS, JS, etc.)"""
    from flask import send_from_directory
    html_dir = os.path.join(web_dir, '..', 'public')
    return send_from_directory(html_dir, filename)

# Check models (but don't block startup)
models_exist = False
try:
    models_exist, missing = ensure_models_exist()
    if not models_exist:
        print("Missing models:")
        for m in missing:
            print(f"   - {m}")
        print(f"\n   Models will be created during training")
    else:
        print("All models loaded successfully")
except Exception as e:
    print(f"Could not check models: {e}")
    models_exist = False

# Health Check Endpoint
@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'OK',
        'message': 'Fact-Checker API is running',
        'models_available': models_exist,
        'timestamp': str(__import__('datetime').datetime.now())
    }), 200

# Project Info Endpoint
@app.route('/api/info', methods=['GET'])
def get_info():
    """Get project information"""
    stats = get_project_stats()
    return jsonify({
        'status': 'success',
        'project': 'Automated Fact-Checker for Vernacular News',
        'version': '1.0.0',
        'stats': stats,
        'supported_languages': config.SUPPORTED_LANGUAGES
    }), 200

# Main Fact-Check Endpoint
@app.route('/api/check-fact', methods=['POST'])
def check_fact():
    """
    Main API endpoint for fact-checking
    
    Request JSON:
    {
        "text": "News text to check"
    }
    
    Response JSON:
    {
        "status": "success/error",
        "prediction": "Likely Real / Likely Fake",
        "confidence": 85.32,
        "language": "en",
        "similar_facts": [...],
        "processed_text": "cleaned text"
    }
    """
    try:
        # Get request data
        data = request.get_json()
        
        if not data or 'text' not in data:
            return jsonify({
                'status': 'error',
                'message': 'Missing text field'
            }), 400
        
        text = data.get('text', '').strip()
        
        if not text:
            return jsonify({
                'status': 'error',
                'message': 'Text cannot be empty'
            }), 400
        
        # Check fact
        result = fact_checker.check_fact(text)
        
        return jsonify(result), 200 if result['status'] == 'success' else 400
        
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

# Batch Check Endpoint
@app.route('/api/check-facts-batch', methods=['POST'])
def check_facts_batch():
    """
    Check multiple facts at once
    
    Request JSON:
    {
        "texts": ["text1", "text2", "text3"]
    }
    
    Response JSON:
    {
        "status": "success",
        "results": [...]
    }
    """
    try:
        data = request.get_json()
        
        if not data or 'texts' not in data:
            return jsonify({
                'status': 'error',
                'message': 'Missing texts field'
            }), 400
        
        texts = data.get('texts', [])
        
        if not isinstance(texts, list) or len(texts) == 0:
            return jsonify({
                'status': 'error',
                'message': 'texts must be a non-empty list'
            }), 400
        
        # Check all facts
        results = []
        for text in texts:
            result = fact_checker.check_fact(text)
            results.append(result)
        
        return jsonify({
            'status': 'success',
            'count': len(results),
            'results': results
        }), 200
        
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

# Error Handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({
        'status': 'error',
        'message': 'Endpoint not found'
    }), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({
        'status': 'error',
        'message': 'Internal server error'
    }), 500

# Static Files (serve HTML)
@app.route('/')
def serve_app():
    """Serve the main HTML app"""
    html_path = os.path.join(os.path.dirname(__file__), '..', '..', 'public', 'index.html')
    if os.path.exists(html_path):
        with open(html_path, 'r', encoding='utf-8') as f:
            return f.read()
    return f"App not found at {html_path}", 404

if __name__ == '__main__':
    print(f"Server starting...")
    print(f"API URL: http://localhost:5000/api")
    print(f"App URL: http://localhost:5000")
    print(f"Press Ctrl+C to stop")
    
    app.run(
        host=config.FLASK_HOST,
        port=config.FLASK_PORT,
        debug=config.DEBUG_MODE
    )
