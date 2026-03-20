# 🚀 QUICK START GUIDE - Run in 2 Minutes

## Option 1: Windows Users (Easiest)
```batch
# Double-click this file:
SETUP_AND_RUN.bat

# That's it! The app will open automatically at http://localhost:5000
```

## Option 2: Mac/Linux/Windows (Python Command)
```bash
# Open terminal/PowerShell and run:
python SETUP_AND_RUN.py

# Wait for "Opening in your browser..." message
# If browser doesn't open, go to: http://localhost:5000
```

## What Happens Automatically:
✅ Installs all required packages  
✅ Creates sample news datasets  
✅ Trains machine learning model  
✅ Launches web app on localhost:5000  

## First Run Takes ~5-10 Minutes (Slow Internet May Be Longer)

---

## 🎯 Using the Application

### On the Web Interface:
1. **Paste News Article** - Copy any news text and paste into the input box
2. **Click "Check Fact"** button
3. **View Results:**
   - ✅ **Likely Real** = Article seems factual
   - ❌ **Likely Fake** = Article seems false
   - **Confidence %** = How confident the model is
   - **Similar Facts** = Similar news articles found in database

### Example Test Articles:

**Likely FAKE:**
```
Scientists announce that water is now a harmful chemical and should not be consumed
by any human under any circumstances.
```

**Likely REAL:**
```
Researchers at Stanford University published findings showing that regular exercise
improves cardiovascular health and reduces the risk of heart disease.
```

---

## 🛠️ If Something Goes Wrong

### "Python not found" Error
- Install Python from https://www.python.org/downloads/
- Make sure to check "Add Python to PATH" during installation

### "Module not found" Error While Running
- The setup script will try again on startup
- Or run manually: `pip install -r requirements.txt`

### Port 5000 Already In Use
- Edit `config.py` line with `FLASK_PORT = 5001` (use different port)

### Slow/Hanging?
- First run generates embeddings for all training data - this is NORMAL and takes time
- Let it complete - it will say "✅ Embeddings generated!" when done

---

## 📂 Project Structure

```
FAKE NEWS/
├── SETUP_AND_RUN.py          ⭐ MAIN FILE - Run this!
├── SETUP_AND_RUN.bat         ⭐ Windows shortcut
├── config.py                  Configuration settings
├── requirements.txt           Python dependencies
│
├── src/                       
│   ├── fact_checker.py       Main prediction engine
│   ├── embedder.py           BERT embedding generation
│   ├── text_processor.py      Text cleaning
│   ├── language_detector.py   Language detection
│   └── utils.py              Helper functions
│
├── notebooks/                Training scripts (auto-run)
│   ├── Step_1_Load_Data.py
│   ├── Step_2_Language_Detection.py
│   ├── Step_3_Text_Cleaning.py
│   ├── Step_4_Embeddings.py
│   ├── Step_5_FAISS_Index.py
│   ├── Step_6_Train_Model.py
│   ├── Step_7_Evaluation.py
│   └── Step_8_Save_Models.py
│
├── web_app/
│   ├── backend/app.py        Flask API
│   └── html/
│       ├── index.html        Beautiful UI
│       ├── style.css         Responsive design
│       └── script.js         Interactive features
│
└── data/
    ├── Fake.csv              Fake news dataset
    ├── True.csv              Real news dataset
    └── [Generated during training]
```

---

## 🌐 Other Ways to Run

### Run Only the Web App (After Initial Setup)
```bash
python web_app/backend/app.py
```

### Use Alternative Streamlit Interface
```bash
streamlit run web_app/streamlit_app.py
```

### Train Model Manually (Step by Step)
```bash
python notebooks/Step_1_Load_Data.py
python notebooks/Step_2_Language_Detection.py
python notebooks/Step_3_Text_Cleaning.py
python notebooks/Step_4_Embeddings.py
python notebooks/Step_5_FAISS_Index.py
python notebooks/Step_6_Train_Model.py
python notebooks/Step_7_Evaluation.py
python notebooks/Step_8_Save_Models.py
```

---

## 📊 What's Inside

- **Machine Learning Model**: Logistic Regression classifier
- **Embeddings**: BERT-based (384-dimensional vectors)
- **Similarity Search**: FAISS for semantic matching
- **Languages**: English, Tamil, Hindi (with translation)
- **Web Framework**: Flask REST API + Beautiful HTML/CSS/JS UI

---

## 🆘 Need Help?

1. Check logs in the terminal - they show what's happening
2. Make sure Python 3.7+ is installed: `python --version`
3. Check internet connection for package downloads
4. Check your firewall isn't blocking port 5000

---

## ✨ Ready to Go?

Run this command right now:
```
python SETUP_AND_RUN.py
```

**That's it! Your fact-checker will be live in minutes! 🎉**
