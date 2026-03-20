"""
STEP 7: Evaluate Model Performance
Generates confusion matrix, classification report, and visualizations

Command: python notebooks/Step_7_Evaluation.py
"""

import os
import sys
import pickle
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

print("=" * 60)
print("📊 STEP 7: Model Evaluation")
print("=" * 60)

# Load model
model_path = config.MODEL_PATH
print(f"\n📥 Loading model from: {model_path}")

try:
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    print(f"✅ Model loaded successfully")
except Exception as e:
    print(f"❌ Error loading model: {e}")
    sys.exit(1)

# Load test data
print(f"\n📥 Loading test data...")
try:
    X_test = np.load(os.path.join(config.DATA_DIR, "X_test.npy"))
    y_test = np.load(os.path.join(config.DATA_DIR, "y_test.npy"))
    print(f"✅ Test data loaded: {len(X_test)} records")
except Exception as e:
    print(f"❌ Error loading test data: {e}")
    sys.exit(1)

# Make predictions
print(f"\n🔄 Making predictions on test set...")
y_pred = model.predict(X_test)
y_pred_proba = model.predict_proba(X_test)

# Classification report
print(f"\n" + "=" * 60)
print("📋 Classification Report")
print("=" * 60)

from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

print(f"\n{classification_report(y_test, y_pred, target_names=['Fake', 'Real'])}")

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Overall Accuracy: {accuracy:.4f} ({accuracy*100:.2f}%)")

# Confusion Matrix
print(f"\n" + "=" * 60)
print("🔲 Confusion Matrix")
print("=" * 60)
cm = confusion_matrix(y_test, y_pred)
print(f"\n                Predicted")
print(f"                Fake  Real")
print(f"Actual Fake    {cm[0][0]:4d}  {cm[0][1]:4d}")
print(f"       Real    {cm[1][0]:4d}  {cm[1][1]:4d}")

# Calculate metrics
tn, fp, fn, tp = cm.ravel()
sensitivity = tp / (tp + fn)
specificity = tn / (tn + fp)
precision = tp / (tp + fp)
recall = tp / (tp + fn)
f1 = 2 * (precision * recall) / (precision + recall)

print(f"\n" + "=" * 60)
print("📈 Performance Metrics")
print("=" * 60)
print(f"Sensitivity (Recall/True Positive Rate): {sensitivity:.4f}")
print(f"Specificity (True Negative Rate): {specificity:.4f}")
print(f"Precision: {precision:.4f}")
print(f"F1-Score: {f1:.4f}")

# Confidence distribution
print(f"\n" + "=" * 60)
print("📊 Confidence Distribution")
print("=" * 60)
max_proba = y_pred_proba.max(axis=1)
print(f"Min confidence: {max_proba.min():.4f}")
print(f"Max confidence: {max_proba.max():.4f}")
print(f"Mean confidence: {max_proba.mean():.4f}")
print(f"Median confidence: {np.median(max_proba):.4f}")

# Generate visualization (text-based)
print(f"\n" + "=" * 60)
print("✅ Evaluation Complete!")
print("=" * 60)

print("\n👉 Next Step: Run Step_8_Save_Models.py (Already Done!)")
print("✅ Ready to use: Run web_app/app.py or web_app/streamlit_app.py")
