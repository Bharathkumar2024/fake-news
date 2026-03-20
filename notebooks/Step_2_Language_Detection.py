"""
STEP 2: Language Detection and Translation
Detects language and translates non-English text to English

Command: python notebooks/Step_2_Language_Detection.py
"""

import pandas as pd
import os
import sys
from collections import Counter

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import config
from src.language_detector import detect_language, translate_to_english

print("=" * 60)
print("🌍 STEP 2: Language Detection & Translation")
print("=" * 60)

# Load combined data
combined_csv = os.path.join(config.DATA_DIR, "combined_data.csv")
print(f"\n📥 Loading: {combined_csv}")

try:
    data = pd.read_csv(combined_csv)
    print(f"✅ Loaded {len(data)} records")
except Exception as e:
    print(f"❌ Error: {e}")
    sys.exit(1)

# Detect language for sample
print("\n🔍 Detecting languages in text column...")
print("(Processing first 100 records as sample)\n")

sample_size = min(100, len(data))
languages = []

for i in range(sample_size):
    if i % 20 == 0:
        print(f"   Processing {i}/{sample_size}...")
    
    text = str(data.iloc[i].get('text', ''))[:500]  # Use text column, limit to 500 chars
    lang = detect_language(text)
    languages.append(lang)

lang_counts = Counter(languages)
print(f"\n✅ Language distribution (in sample):")
for lang, count in lang_counts.most_common():
    print(f"   {lang}: {count}")

# Show translation example
print("\n" + "=" * 60)
print("📝 Translation Example (if non-English text found)")
print("=" * 60)

for i in range(sample_size):
    lang = languages[i]
    if lang != 'en' and lang != 'unknown':
        sample_text = str(data.iloc[i].get('text', ''))[:200]
        print(f"\n🔤 Original ({lang}): {sample_text}...")
        translated = translate_to_english(sample_text)
        print(f"🔤 Translated (en): {translated}...")
        break

print("\n" + "=" * 60)
print("✅ Language detection completed!")
print("=" * 60)
print("\n👉 Next Step: Run Step_3_Text_Cleaning.py")
