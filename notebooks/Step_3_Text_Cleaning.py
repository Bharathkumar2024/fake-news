"""
STEP 3: Text Cleaning
Cleans text by removing URLs, special characters, stopwords, etc.

Command: python notebooks/Step_3_Text_Cleaning.py
"""

import pandas as pd
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config
from src.text_processor import clean_text

print("=" * 60)
print("🧹 STEP 3: Text Cleaning")
print("=" * 60)

# Load data
combined_csv = os.path.join(config.DATA_DIR, "combined_data.csv")
print(f"\n📥 Loading: {combined_csv}")

try:
    data = pd.read_csv(combined_csv)
    print(f"✅ Loaded {len(data)} records")
except Exception as e:
    print(f"❌ Error: {e}")
    sys.exit(1)

# Show before/after example
print("\n" + "=" * 60)
print("📝 Before/After Text Cleaning Examples")
print("=" * 60)

for i in range(min(3, len(data))):
    original = str(data.iloc[i].get('text', ''))[:300]
    cleaned = clean_text(original)
    
    print(f"\n📍 Example {i+1}:")
    print(f"   BEFORE: {original}...")
    print(f"   AFTER:  {cleaned}...")

# Clean all texts
print("\n\n🔄 Cleaning all texts...")
data['text_cleaned'] = data['text'].astype(str).apply(lambda x: clean_text(x))

# Check for empty texts after cleaning
empty_count = (data['text_cleaned'].str.len() == 0).sum()
print(f"\n✅ Cleaning completed!")
print(f"   Total records: {len(data)}")
print(f"   Empty after cleaning: {empty_count}")
print(f"   Valid records: {len(data) - empty_count}")

# Remove empty texts
data = data[data['text_cleaned'].str.len() > 0].reset_index(drop=True)
print(f"\n✅ Filtered to: {len(data)} records")

# Save cleaned data
cleaned_csv = os.path.join(config.DATA_DIR, "cleaned_data.csv")
data.to_csv(cleaned_csv, index=False)
print(f"✅ Saved cleaned data to: {cleaned_csv}")

print("\n" + "=" * 60)
print("👉 Next Step: Run Step_4_Embeddings.py")
print("=" * 60)
