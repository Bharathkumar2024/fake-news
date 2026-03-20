"""
STEP 8: Save All Models and Components
Ensures all components are saved for production use

Command: python notebooks/Step_8_Save_Models.py
"""

import os
import sys
import pickle

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

print("=" * 60)
print("💾 STEP 8: Save All Models and Components")
print("=" * 60)

# Check what components exist
components = {
    'Model': config.MODEL_PATH,
    'FAISS Index': config.FAISS_INDEX_PATH,
    'Facts Database': config.FACTS_PATH,
}

print(f"\n📂 Checking saved components...\n")

all_exist = True
for name, path in components.items():
    exists = os.path.exists(path)
    status = "✅" if exists else "❌"
    print(f"{status} {name}: {path}")
    if not exists:
        all_exist = False

if all_exist:
    print(f"\n✅ All components are ready for production!")
    print(f"\n📊 Model Directory: {config.MODELS_DIR}")
    
    # List files
    if os.path.exists(config.MODELS_DIR):
        files = os.listdir(config.MODELS_DIR)
        print(f"\n📁 Files in models directory:")
        total_size = 0
        for f in files:
            if f.endswith('.pkl') or f.endswith('.npy'):
                path = os.path.join(config.MODELS_DIR, f)
                size = os.path.getsize(path) / 1024 / 1024  # MB
                total_size += size
                print(f"   • {f} ({size:.2f} MB)")
        print(f"\n   Total size: {total_size:.2f} MB")
else:
    print(f"\n❌ Some components are missing!")
    print(f"   Complete the training steps first.")
    sys.exit(1)

# Create a summary file
summary_path = os.path.join(config.MODELS_DIR, "README.md")
summary_content = """# 🤖 Fact-Checker Models

This directory contains all trained models and data for the fact-checking system.

## Files

- **model.pkl**: Trained Logistic Regression classifier
- **faiss_index.pkl**: FAISS vector search index for semantic search
- **facts.pkl**: Database of factual statements for retrieval
- **embedder.pkl**: Pre-trained Sentence Transformers embedder

## Usage

All models are loaded automatically by the web application.

### Direct Usage

```python
import pickle
import config

# Load all components
model = pickle.load(open(config.MODEL_PATH, 'rb'))
index = pickle.load(open(config.FAISS_INDEX_PATH, 'rb'))
facts = pickle.load(open(config.FACTS_PATH, 'rb'))
```

## Model Performance

- Architecture: Logistic Regression on BERT embeddings
- Embedding Dimension: 384
- Training Data: Combined Fake + Real news articles

For evaluation metrics, see Step_7_Evaluation.py output.
"""

with open(summary_path, 'w') as f:
    f.write(summary_content)

print(f"\n✅ Summary saved to: {summary_path}")

print("\n" + "=" * 60)
print("🎉 STEP 8 COMPLETE!")
print("=" * 60)
print("\n✅ All models saved and ready for deployment!")
print("\n🚀 Next: Start the web application!")
print("   Option 1: python web_app/backend/app.py")
print("   Option 2: streamlit run web_app/streamlit_app.py")
