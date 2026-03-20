"""
STEP 1: Load and Explore Dataset
Loads Fake.csv and True.csv, combines them, and explores the data

Command: python notebooks/Step_1_Load_Data.py
"""

import pandas as pd
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config

print("=" * 60)
print("📊 STEP 1: Loading Dataset")
print("=" * 60)

# Load datasets
print("\n📂 Looking for dataset files...")
print(f"   Fake.csv: {config.FAKE_CSV}")
print(f"   True.csv: {config.TRUE_CSV}")

try:
    # Load fake news
    print("\n📥 Loading Fake.csv...")
    fake = pd.read_csv(config.FAKE_CSV)
    fake["label"] = 0  # Label: 0 = Fake
    print(f"✅ Fake news loaded: {len(fake)} records")
    print(f"   Columns: {list(fake.columns)}")
    
except Exception as e:
    print(f"❌ Error loading Fake.csv: {e}")
    fake = None

try:
    # Try to load True.csv
    print("\n📥 Loading True.csv...")
    real = pd.read_csv(config.TRUE_CSV)
    real["label"] = 1  # Label: 1 = Real
    print(f"✅ True news loaded: {len(real)} records")
    
except Exception as e:
    print(f"⚠️  True.csv not found. Using only Fake.csv for now.")
    real = None

# Combine datasets
if fake is not None and real is not None:
    data = pd.concat([fake, real], ignore_index=True)
    data = data.sample(frac=1).reset_index(drop=True)
    print(f"\n✅ Combined dataset: {len(data)} records")
else:
    data = fake
    print(f"\n⚠️  Using only Fake.csv: {len(data)} records")

# Take sample for faster processing
if len(data) > config.SAMPLE_SIZE:
    data = data.sample(n=config.SAMPLE_SIZE, random_state=42).reset_index(drop=True)
    print(f"📊 Using sample of {config.SAMPLE_SIZE} records for training")

print("\n" + "=" * 60)
print("📈 Dataset Statistics")
print("=" * 60)
print(f"Total records: {len(data)}")
if 'label' in data.columns:
    print(f"Fake: {(data['label'] == 0).sum()}")
    print(f"Real: {(data['label'] == 1).sum()}")
print(f"\nDataset shape: {data.shape}")
print(f"\nFirst row preview:")
print(data.iloc[0])

# Save processed data
data.to_csv(os.path.join(config.DATA_DIR, "combined_data.csv"), index=False)
print(f"\n✅ Combined data saved to: {os.path.join(config.DATA_DIR, 'combined_data.csv')}")

print("\n" + "=" * 60)
print("👉 Next Step: Run Step_2_Language_Detection.py")
print("=" * 60)
