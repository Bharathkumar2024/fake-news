"""
STEP 0: Install All Dependencies
Run this script first to install all required packages

Command: python notebooks/Step_0_Install.py
"""

import subprocess
import sys

print("=" * 60)
print("🚀 STEP 0: Installing Dependencies")
print("=" * 60)

packages = [
    'pandas',
    'numpy',
    'scikit-learn',
    'nltk',
    'sentence-transformers',
    'faiss-cpu',
    'googletrans==4.0.0-rc1',
    'streamlit',
    'flask',
    'flask-cors',
    'python-dotenv',
    'requests',
    'langdetect'
]

for package in packages:
    print(f"\n📦 Installing {package}...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", package])
        print(f"✅ {package} installed")
    except Exception as e:
        print(f"❌ Error installing {package}: {e}")

print("\n" + "=" * 60)
print("✅ All dependencies installed successfully!")
print("=" * 60)
print("\n👉 Next Step: Run Step_1_Load_Data.py")
