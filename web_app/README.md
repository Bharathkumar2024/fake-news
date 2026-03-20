"""
README for Web App
"""

# 🖥️ WEB APPLICATION

This folder contains the complete web interface for the fact-checking system.

## 📁 Structure

```
web_app/
├── html/                  # Static web interface
│   ├── index.html        # Main web app
│   ├── css/
│   │   └── style.css     # Styling
│   └── js/
│       └── script.js     # Frontend logic
├── backend/
│   └── app.py            # Flask API server
├── streamlit_app.py      # Alternative Streamlit interface
└── README.md             # This file
```

## 🚀 Running the Application

### Option 1: Flask + HTML/CSS/JS (Recommended for beginners)

```bash
cd c:\FAKE NEWS
python web_app\backend\app.py
```

Then open browser: **http://localhost:5000**

### Option 2: Streamlit (Easiest for demos)

```bash
cd c:\FAKE NEWS
streamlit run web_app\streamlit_app.py
```

Browser opens automatically at **http://localhost:8501**

## 📡 API Endpoints (Flask)

### 1. Health Check
```
GET http://localhost:5000/api/health
```

Response:
```json
{
    "status": "OK",
    "message": "Fact-Checker API is running",
    "models_available": true
}
```

### 2. Check Single Fact
```
POST http://localhost:5000/api/check-fact
Content-Type: application/json

{
    "text": "News article text here..."
}
```

Response:
```json
{
    "status": "success",
    "prediction": "✅ Likely Real",
    "confidence": 85.32,
    "language": "en",
    "similar_facts": [...],
    "processed_text": "cleaned text"
}
```

### 3. Check Multiple Facts
```
POST http://localhost:5000/api/check-facts-batch
Content-Type: application/json

{
    "texts": ["text1", "text2", "text3"]
}
```

## 🎨 Features

### Frontend (HTML/CSS/JS)
- ✅ Real-time fact checking
- ✅ Multi-language support
- ✅ Confidence visualization
- ✅ Similar facts display
- ✅ Share results
- ✅ Responsive design
- ✅ Beautiful UI with gradients

### Streamlit
- ✅ Quick setup
- ✅ Built-in components
- ✅ Interactive widgets
- ✅ Easy customization

### API
- ✅ RESTful design
- ✅ CORS enabled
- ✅ Error handling
- ✅ Batch processing
- ✅ JSON responses

## 🔧 Configuration

Edit `config.py` to customize:
- Model paths
- Embedding dimension
- FAISS search results (k)
- Flask host/port
- Supported languages

## 📦 Dependencies

```
flask
flask-cors
streamlit
sentence-transformers
faiss-cpu
pandas
numpy
scikit-learn
nltk
googletrans
```

Install with:
```bash
pip install -r requirements.txt
```

## 🐛 Troubleshooting

### Port Already in Use
```bash
# Flask
python -m flask --app web_app.backend.app run --port 8080

# Streamlit
streamlit run web_app/streamlit_app.py --server.port 8080
```

### Models Not Found
Run all training steps first:
```bash
python notebooks/Step_0_Install.py
python notebooks/Step_1_Load_Data.py
... (complete all steps)
```

### CORS Errors
Ensure Flask app is running with CORS enabled (already configured in app.py)

## 📱 Deployment

### Local Testing
1. Run backend: `python web_app/backend/app.py`
2. Open: `http://localhost:5000`

### Cloud Deployment
- **Streamlit Cloud**: Deploy streamlit_app.py easily
- **Heroku**: Use Procfile and requirements.txt
- **AWS**: Use EC2 + Flask
- **Azure**: Use App Service
- **Google Cloud**: Use Cloud Run

## 📝 Example Usage

```python
import requests

# Call API
response = requests.post(
    'http://localhost:5000/api/check-fact',
    json={'text': 'Breaking news about elections...'}
)

result = response.json()
print(f"Prediction: {result['prediction']}")
print(f"Confidence: {result['confidence']}%")
```

## 🎓 Learning Resources

- HTML/CSS/JS: Modern responsive design
- Flask: RESTful API development
- Streamlit: Quick data apps
- JavaScript: API integration, DOM manipulation
- Python: Backend logic and ML integration

---

**Made with ❤️ for fact-checking**
