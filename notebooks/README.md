"""
README for Training Scripts
"""

# 🚀 STEP-BY-STEP ML TRAINING PIPELINE

Follow these steps in order to train the fact-checking model:

## ⚙️ Step 0: Install Dependencies
```bash
python notebooks/Step_0_Install.py
```
Installs all required Python packages.

## 📊 Step 1: Load Dataset
```bash
python notebooks/Step_1_Load_Data.py
```
- Loads Fake.csv and True.csv
- Combines datasets
- Takes sample for faster processing

## 🌍 Step 2: Language Detection
```bash
python notebooks/Step_2_Language_Detection.py
```
- Detects languages (English, Tamil, Hindi)
- Prepares for translation if needed

## 🧹 Step 3: Text Cleaning
```bash
python notebooks/Step_3_Text_Cleaning.py
```
- Removes URLs and special characters
- Removes stopwords
- Prepares text for embedding

## 🤖 Step 4: Generate Embeddings
```bash
python notebooks/Step_4_Embeddings.py
```
- Uses SentenceTransformers (BERT)
- Creates semantic vectors (384-dim)

## 🔎 Step 5: Build FAISS Index
```bash
python notebooks/Step_5_FAISS_Index.py
```
- Creates fast similarity search index
- Enables fact retrieval

## 🧠 Step 6: Train Model
```bash
python notebooks/Step_6_Train_Model.py
```
- Trains Logistic Regression classifier
- Splits train/test data (80/20)

## 📈 Step 7: Evaluate Model
```bash
python notebooks/Step_7_Evaluation.py
```
- Generates confusion matrix
- Shows precision, recall, F1-score
- Displays performance metrics

## 💾 Step 8: Save Models
```bash
python notebooks/Step_8_Save_Models.py
```
- Confirms all components are saved
- Ready for production

---

## ⏱️ Total Time
Approximately 30-60 minutes depending on dataset size and system performance.

## 💡 Tips
- Start with Step 0 to install all dependencies
- Run steps sequentially
- Monitor output for any errors
- All intermediate outputs are saved

## 🎯 Output
After completion, you'll have:
- Trained ML model
- FAISS index for semantic search
- Facts database
- Ready to deploy web app
