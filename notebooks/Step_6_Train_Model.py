"""
STEP 6: Train Classification Model
Trains Logistic Regression for fake/real classification

Command: python notebooks/Step_6_Train_Model.py
"""

import os
import sys
import pickle
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

print("=" * 60)
print("🧠 STEP 6: Training Classification Model")
print("=" * 60)

# Load embeddings and labels
print(f"\n📥 Loading data...")

embeddings_path = os.path.join(config.DATA_DIR, "embeddings.pkl")
labels_path = os.path.join(config.DATA_DIR, "labels.pkl")

try:
    with open(embeddings_path, 'rb') as f:
        embeddings = pickle.load(f)
    with open(labels_path, 'rb') as f:
        labels = pickle.load(f)
    print(f"✅ Loaded {len(embeddings)} embeddings and labels")
except Exception as e:
    print(f"❌ Error loading data: {e}")
    sys.exit(1)

# Split data
print(f"\n📊 Splitting data...")
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    embeddings, labels, test_size=config.TEST_SIZE, random_state=42
)

print(f"✅ Training set: {len(X_train)} records")
print(f"   Fake: {(np.array(y_train) == 0).sum()}")
print(f"   Real: {(np.array(y_train) == 1).sum()}")
print(f"✅ Test set: {len(X_test)} records")
print(f"   Fake: {(np.array(y_test) == 0).sum()}")
print(f"   Real: {(np.array(y_test) == 1).sum()}")

# Train model
print(f"\n🔄 Training Logistic Regression model...")
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=1000, random_state=42, n_jobs=-1)

try:
    model.fit(X_train, y_train)
    print(f"✅ Model trained successfully!")
    
    # Get training accuracy
    train_acc = model.score(X_train, y_train)
    test_acc = model.score(X_test, y_test)
    
    print(f"\n📈 Model Performance:")
    print(f"   Training Accuracy: {train_acc:.4f} ({train_acc*100:.2f}%)")
    print(f"   Test Accuracy: {test_acc:.4f} ({test_acc*100:.2f}%)")
    
except Exception as e:
    print(f"❌ Error training model: {e}")
    sys.exit(1)

# Save model
model_path = config.MODEL_PATH
os.makedirs(os.path.dirname(model_path), exist_ok=True)
with open(model_path, 'wb') as f:
    pickle.dump(model, f)
print(f"\n✅ Model saved to: {model_path}")

# Save test data for evaluation
np.save(os.path.join(config.DATA_DIR, "X_test.npy"), X_test)
np.save(os.path.join(config.DATA_DIR, "y_test.npy"), y_test)

print("\n" + "=" * 60)
print("👉 Next Step: Run Step_7_Evaluation.py")
print("=" * 60)
