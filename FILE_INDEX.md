```
╔═══════════════════════════════════════════════════════════════════════════╗
║  🔥 FACT-CHECKER SYSTEM - COMPLETE GUIDE & FILE INDEX 🔥                ║
║                                                                           ║
║  Your production-ready ML application for detecting fake news            ║
║  Multi-language • Real-time • Scalable • Beautiful UI                    ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

# 📑 COMPLETE FILE INDEX & GUIDE

---

## 🚀 START HERE

### 1️⃣ **[QUICKSTART.md](QUICKSTART.md)** ⭐ READ THIS FIRST
- 5-minute overview
- Step-by-step execution
- Troubleshooting tips
- Expected results

### 2️⃣ **[README.md](README.md)** - Full Documentation
- Complete project description
- Architecture details
- Feature overview
- Deployment guide

### 3️⃣ **[PROJECT_SUMMARY.txt](PROJECT_SUMMARY.txt)** - Technical Overview
- System flow diagram
- Technology stack
- Performance metrics
- Integration examples

---

## 📂 PROJECT STRUCTURE GUIDE

### 📊 `/data` - Your Datasets
```
data/
├── Fake.csv               ← Fake news articles (your upload)
├── True.csv               ← Real news articles (your upload)
├── combined_data.csv      ← Auto-generated after Step_1
├── cleaned_data.csv       ← Auto-generated after Step_3
├── embeddings.pkl         ← Auto-generated after Step_4
├── labels.pkl             ← Auto-generated after Step_4
├── X_test.npy             ← Auto-generated after Step_6
├── y_test.npy             ← Auto-generated after Step_6
└── README.md              ← Data documentation
```
🎯 **What it does**: Stores all training data and intermediate outputs

---

### 🧠 `/notebooks` - Training Pipeline (Execute in order!)
```
notebooks/
├── Step_0_Install.py              ← Install all packages
├── Step_1_Load_Data.py            ← Load Fake.csv + True.csv
├── Step_2_Language_Detection.py   ← Detect English/Tamil/Hindi
├── Step_3_Text_Cleaning.py        ← Remove URLs, stopwords
├── Step_4_Embeddings.py           ← Convert text to vectors
├── Step_5_FAISS_Index.py          ← Build similarity search index
├── Step_6_Train_Model.py          ← Train ML classifier
├── Step_7_Evaluation.py           ← Check model performance
├── Step_8_Save_Models.py          ← Save all components
└── README.md                       ← Training guide
```
🎯 **What it does**: Complete machine learning training pipeline
📋 **How to run**:
```bash
python notebooks/Step_0_Install.py
python notebooks/Step_1_Load_Data.py
... (follow through Step_8)
```

---

### 🤖 `/src` - Core ML Modules
```
src/
├── __init__.py                    ← Package initialization
├── language_detector.py           ← Language detection + translation
│   Functions:
│   - detect_language(text)        → 'en', 'ta', 'hi', 'unknown'
│   - translate_to_english(text)   → Translated text
│
├── text_processor.py              ← Text cleaning
│   Functions:
│   - clean_text(text)             → Cleaned text
│   - preprocess_text(text)        → Full preprocessing
│
├── embedder.py                    ← Generate embeddings
│   Functions:
│   - get_embeddings(texts)        → numpy array (N, 384)
│   - get_single_embedding(text)   → numpy array (384,)
│   - cosine_similarity(vec1, vec2)→ float (0-1)
│
├── fact_checker.py                ← Main prediction engine
│   Class: FactChecker
│   Methods:
│   - check_fact(text)             → Prediction result dict
│
├── utils.py                       ← Helper functions
│   Functions:
│   - ensure_models_exist()        → Check if models ready
│   - get_project_stats()          → Project information
```
🎯 **What it does**: Core machine learning functionality
🔧 **How to use**:
```python
from src.fact_checker import fact_checker

result = fact_checker.check_fact("Your news text")
print(result['prediction'])     # ✅ Likely Real or ❌ Likely Fake
print(result['confidence'])     # 87.5
```

---

### 💾 `/models` - Trained Models (Auto-generated)
```
models/
├── model.pkl              ← Trained Logistic Regression classifier
├── faiss_index.pkl        ← FAISS vector search index
├── facts.pkl              ← Database of 10k+ verified facts
├── embedder.pkl           ← Pre-trained BERT embedder
├── label_encoder.pkl      ← Label encoding (if used)
└── README.md              ← Model documentation
```
📦 **File Sizes** (approximately):
- model.pkl: 1-2 MB
- faiss_index.pkl: 30-50 MB
- facts.pkl: 5-10 MB
- embedder.pkl: 0.5 MB (loaded from huggingface)

🎯 **What it does**: Stores all trained ML components for predictions

---

### 🖥️ `/web_app` - Complete Web Application

#### 📄 `/web_app/html` - Frontend Interface
```
web_app/html/
├── index.html             ← Main web interface (Beautiful UI)
├── css/
│   └── style.css          ← Responsive CSS3 styling
│       - Header with gradient
│       - Input textarea
│       - Results display
│       - Confidence meter
│       - Similar facts section
│       - Mobile responsive
│
└── js/
    └── script.js          ← Frontend logic
        - API integration
        - Event listeners
        - Result rendering
        - Toast notifications
        - Sharing functionality
```
🎨 **Features**:
- Modern gradient UI
- Real-time predictions
- Confidence visualization
- Smooth animations
- Keyboard shortcuts (Ctrl+Enter)
- Mobile responsive

#### ⚙️ `/web_app/backend` - REST API
```
web_app/backend/
└── app.py                 ← Flask REST API server
    Endpoints:
    - GET  /api/health               → Health check
    - GET  /api/info                 → Project info
    - POST /api/check-fact           → Single prediction
    - POST /api/check-facts-batch    → Multiple predictions
    - GET  /                         → Serve HTML app
```
🔌 **API Examples**:
```bash
# Check single fact
curl -X POST http://localhost:5000/api/check-fact \
  -H "Content-Type: application/json" \
  -d '{"text": "Breaking news..."}'

# Batch check
curl -X POST http://localhost:5000/api/check-facts-batch \
  -H "Content-Type: application/json" \
  -d '{"texts": ["Text1", "Text2", "Text3"]}'
```

#### 📊 `/web_app/streamlit_app.py` - Alternative Interface
```python
Streamlit app providing:
- Text input area
- Real-time prediction
- Confidence display
- Similar facts
- Sidebar with info
- Easy to customize
```

---

## ⚙️ Configuration Files

### **[config.py](config.py)** - Central Configuration
```python
# Customizable settings:
- Embedding model name
- Embedding dimension (384)
- FAISS search results (k=5)
- Model paths
- Flask host/port
- Sample size for training
- Supported languages
```

### **[requirements.txt](requirements.txt)** - Dependencies
```
pandas, numpy, scikit-learn, nltk, 
sentence-transformers, faiss-cpu, 
googletrans, streamlit, flask, flask-cors,
python-dotenv, requests, langdetect
```

---

## 📋 Main Entry Points

### For Training:
```bash
python notebooks/Step_0_Install.py    # Start here!
# ... follow through Step_8
```

### For Web App (Option 1):
```bash
python web_app/backend/app.py         # Flask + HTML/CSS/JS
# Open: http://localhost:5000
```

### For Web App (Option 2):
```bash
streamlit run web_app/streamlit_app.py  # Streamlit
# Browser opens automatically
```

---

## 🔄 Component Interaction Flow

```
┌─────────────────────────────────────────────────────────┐
│                   USER INPUT (Browser)                   │
│                   "Fake news article..."                  │
└────────────────────┬────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────┐
│              web_app/html/js/script.js                   │
│              Captures input, calls API                   │
└────────────────────┬────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────┐
│            web_app/backend/app.py (Flask)               │
│            Routes request to prediction                 │
└────────────────────┬────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────┐
│         src/fact_checker.py (FactChecker class)         │
│         Orches rates ML pipeline:                        │
│         1. Language detection (src/language_detector)   │
│         2. Text cleaning (src/text_processor)           │
│         3. Embedding (src/embedder)                     │
│         4. FAISS search                                 │
│         5. ML prediction                                │
│         6. Format results                               │
└────────────────────┬────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────┐
│           models/ (Trained components)                   │
│           - model.pkl (classifier)                       │
│           - faiss_index.pkl (search)                     │
│           - facts.pkl (knowledge base)                   │
└────────────────────┬────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────┐
│         Results JSON back to API                         │
│         {prediction, confidence, facts, ...}             │
└────────────────────┬────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────┐
│      web_app/html/js/script.js (Frontend)               │
│      Renders beautiful results                           │
│      - Shows ✅ Likely Real or ❌ Likely Fake           │
│      - Shows confidence meter                           │
│      - Shows similar facts                              │
│      - Enables sharing                                  │
└────────────────────┬────────────────────────────────────┘
                     ↓
┌─────────────────────────────────────────────────────────┐
│            RESULTS DISPLAYED IN BROWSER                  │
│              Beautiful visualization                     │
└─────────────────────────────────────────────────────────┘
```

---

## 🎯 Quick Reference - What Each File Does

### Scripts You Run (in order):
| File | Purpose | Input | Output |
|------|---------|-------|--------|
| Step_0 | Install packages | Internet | ✅ Packages installed |
| Step_1 | Load data | Fake.csv, True.csv | combined_data.csv |
| Step_2 | Detect languages | combined_data.csv | Language statistics |
| Step_3 | Clean text | combined_data.csv | cleaned_data.csv |
| Step_4 | Create embeddings | cleaned_data.csv | embeddings.pkl |
| Step_5 | Build FAISS | embeddings.pkl | faiss_index.pkl |
| Step_6 | Train model | embeddings.pkl | model.pkl |
| Step_7 | Evaluate | model.pkl | Accuracy metrics |
| Step_8 | Save all | All components | ✅ Ready to deploy |

### Python Modules (Used Automatically):
| Module | Used By | Function |
|--------|---------|----------|
| language_detector.py | FactChecker | Language detection |
| text_processor.py | FactChecker | Text cleaning |
| embedder.py | FactChecker | Embeddings |
| fact_checker.py | API + UI | Main prediction |
| utils.py | All | Helper functions |

### Web Files (User Interacts With):
| File | What It Does |
|------|--------------|
| index.html | Main interface layout |
| style.css | Beautiful styling |
| script.js | User interaction handling |
| app.py | Backend API server |
| streamlit_app.py | Alternative Streamlit UI |

---

## 📊 Data Flow During Prediction

```
User Text (e.g., "Breaking news..." or Tamil/Hindi)
    ↓
detect_language() → Detects: English / Tamil / Hindi
    ↓
translate_to_english() → Translates to English if needed
    ↓
clean_text() → Removes URLs, symbols, stopwords
    ↓
get_single_embedding() → Converts to 384-dim vector
    ↓
faiss_index.search() → Finds 5 similar facts
    ↓
model.predict() → Outputs: 0 (Fake) or 1 (Real)
    ↓
model.predict_proba() → Outputs confidence 0-1
    ↓
Format as JSON response with:
- prediction (✅ Real or ❌ Fake)
- confidence (0-100%)
- similar_facts (Retrieved from database)
- language (Detected)
- processed_text (Cleaned)
    ↓
Display in beautiful UI
```

---

## 🔧 Customization Guide

### To change model:
Edit `config.py`:
```python
EMBEDDING_MODEL = 'different-model-name'
```

### To adjust sensitivity:
Edit `config.py`:
```python
FAISS_K = 10  # Get more similar facts
```

### To modify UI colors:
Edit `web_app/html/css/style.css`:
```css
--primary-color: #your-color;
--secondary-color: #your-color;
```

### To add more languages:
Edit `src/language_detector.py` and add language codes

---

## 🚀 Deployment Checklist

- [ ] All training scripts completed
- [ ] Models saved in `/models`
- [ ] Web app tested locally
- [ ] API endpoints verified
- [ ] UI responsive on mobile
- [ ] Configuration optimized
- [ ] Documentation reviewed
- [ ] Security check passed
- [ ] Performance acceptable
- [ ] Ready for production

---

## 📞 Troubleshooting Guide

**Q: Where do I put my data?**
A: Place Fake.csv and True.csv in the `/data` folder

**Q: Which script do I run first?**
A: Always start with `python notebooks/Step_0_Install.py`

**Q: How long does training take?**
A: About 1 hour (varies by dataset size and computer speed)

**Q: Can I use different data?**
A: Yes! Any CSV with `text` and `label` columns works

**Q: What port is the web app on?**
A: Flask: 5000 (http://localhost:5000)
   Streamlit: 8501 (http://localhost:8501)

**Q: Can I change the port?**
A: Yes! Edit `config.py` (FLASK_PORT parameter)

---

## 📚 File Reading Order

### For Understanding:
1. Read: **QUICKSTART.md** (5 min overview)
2. Read: **README.md** (Full documentation)
3. Read: **PROJECT_SUMMARY.txt** (Technical details)
4. Read: **config.py** (Understand settings)
5. Read: **notebooks/README.md** (Training details)
6. Read: **web_app/README.md** (App details)

### For Execution:
1. Run: **Step_0_Install.py**
2. Run: **Step 1-8** in order
3. Run: **web_app/backend/app.py** OR **streamlit_app.py**

### For Integration:
1. Study: **web_app/backend/app.py** (API structure)
2. Study: **src/fact_checker.py** (Prediction logic)
3. Study: **web_app/html/js/script.js** (Frontend integration)

---

## ✅ Success Indicators

### After Step 0:
✅ All packages installed without errors

### After Step 6:
✅ Model trained with accuracy > 80%

### After Step 8:
✅ All pkl files appear in `/models` directory

### After Running Web App:
✅ Browser opens to http://localhost:5000
✅ Can type text and get results
✅ Results display beautifully

---

```
╔═══════════════════════════════════════════════════════════════════════════╗
║                                                                           ║
║                  🎉 YOU NOW HAVE THE COMPLETE GUIDE! 🎉                 ║
║                                                                           ║
║              Next Step: Read QUICKSTART.md and run Step_0!               ║
║                                                                           ║
║                    Good luck with your project! 🚀                       ║
║                                                                           ║
╚═══════════════════════════════════════════════════════════════════════════╝
```

**Made with ❤️ for better informed societies**
