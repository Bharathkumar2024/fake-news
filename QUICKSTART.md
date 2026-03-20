"""
QUICK START GUIDE
Step-by-step instructions to get the system running
"""

# ⚡ QUICK START GUIDE

## Step 1: Initial Setup (5 minutes)

### On Windows (PowerShell or Command Prompt):
```powershell
cd "c:\FAKE NEWS"
python notebooks/Step_0_Install.py
```

### On Mac/Linux:
```bash
cd ~/FAKE NEWS
python notebooks/Step_0_Install.py
```

✅ Wait for all packages to install (see checkmarks)

---

## Step 2: Load & Prepare Data (5 minutes)

Ensure your dataset files are here:
- `data/Fake.csv` ✓
- `data/True.csv` (or just Fake.csv is okay)

Run:
```bash
python notebooks/Step_1_Load_Data.py
```

✅ Should show: "Combined dataset: XXXX records"

---

## Step 3: Process Text (10 minutes)

```bash
python notebooks/Step_2_Language_Detection.py
python notebooks/Step_3_Text_Cleaning.py
```

✅ You should see before/after text examples

---

## Step 4: Create Smart Embeddings (15 minutes)

```bash
python notebooks/Step_4_Embeddings.py
```

✅ This downloads a smart language model (~150 MB)
✅ Shows embeddings shape: (XXXX, 384)

---

## Step 5: Build Search Index (5 minutes)

```bash
python notebooks/Step_5_FAISS_Index.py
```

✅ Creates fast similarity search

---

## Step 6: Train ML Model (10 minutes)

```bash
python notebooks/Step_6_Train_Model.py
```

✅ Shows training/test accuracy

---

## Step 7: Evaluate (2 minutes)

```bash
python notebooks/Step_7_Evaluation.py
```

✅ Shows confusion matrix and F1-scores

---

## Step 8: Finalize (1 minute)

```bash
python notebooks/Step_8_Save_Models.py
```

✅ "All models saved and ready for deployment!"

---

## Step 9: Launch Web App! 🚀

### Option A: Beautiful Web Interface
```bash
python web_app/backend/app.py
```
Then open: **➡️ http://localhost:5000**

### Option B: Streamlit (Faster)
```bash
streamlit run web_app/streamlit_app.py
```
Browser opens automatically

---

## 🎯 Expected Results

After training:
- Model Accuracy: 85-92%
- Inference Time: < 500ms
- FAISS Index: ~50 MB
- Total Time: 1 hour

---

## 🐛 Troubleshooting

### "No module named 'pandas'"
```bash
python -m pip install pandas numpy scikit-learn
```

### "Port 5000 already in use"
```bash
python -c "import socket; s=socket.socket(); s.bind(('localhost',5001))"
# Then use: http://localhost:5001
```

### "Fake.csv not found"
- Place CSV files in `data/` folder
- Or download ISOT Fake News Dataset

### "CUDA not available" (GPU message)
This is fine - CPU works (slower but okay)

---

## ✅ Checklist

- [ ] Step 0: Dependencies installed
- [ ] Step 1: Data loaded
- [ ] Step 2: Languages detected
- [ ] Step 3: Text cleaned
- [ ] Step 4: Embeddings created
- [ ] Step 5: FAISS index built
- [ ] Step 6: Model trained
- [ ] Step 7: Model evaluated
- [ ] Step 8: Models saved
- [ ] Step 9: Web app running

---

## 🎓 What's Happening?

```
📚 Raw Data
    ↓
🌍 Language Detection (Tamil/Hindi → English)
    ↓
🧹 Text Cleaning (Remove URLs, symbols, stopwords)
    ↓
🤖 Embeddings (Convert text to numbers using AI)
    ↓
🔎 FAISS Index (Create lightning-fast search)
    ↓
🧠 Train Model (Teach computer to detect fake)
    ↓
📊 Evaluate (Check if model is accurate)
    ↓
💾 Save Everything (Ready to predict!)
    ↓
🖥️ Web Interface (User enters text → Get result!)
```

---

## 📝 Test Your App

Once running, try these:

### Right after training:
```bash
curl -X POST http://localhost:5000/api/check-fact \
  -H "Content-Type: application/json" \
  -d '{"text": "Breaking news about politics"}'
```

### In web browser:
- Open: http://localhost:5000
- Enter any news text
- Click "Check Authenticity"
- See results!

---

## 🚀 Next Steps

After getting results:
- [ ] Deploy to cloud (Heroku/AWS/Azure)
- [ ] Add more languages
- [ ] Integrate with news APIs
- [ ] Create mobile app
- [ ] Build browser extension

---

## 💡 Pro Tips

1. **First run is slow** (downloads 150MB BERT model)
2. **Use smaller dataset initially** (edit config.SAMPLE_SIZE)
3. **Save your models** (already done in Step 8)
4. **Monitor memory** (watch for OOM errors)
5. **Use GPU if available** (faiss-gpu for speed boost)

---

## 📞 Need Help?

1. Check `notebooks/README.md` for detailed steps
2. Check `web_app/README.md` for app help  
3. Look at output messages for errors
4. Check `config.py` for settings

---

**You're ready! Start with Step 0 and follow through. ✅**
