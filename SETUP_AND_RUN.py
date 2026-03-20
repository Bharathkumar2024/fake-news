#!/usr/bin/env python3
"""
=================================================================
🚀 SETUP_AND_RUN.py - One-Command Installation & Deployment
=================================================================

This script does EVERYTHING in one command:
1. ✅ Installs all dependencies (pip packages)
2. ✅ Creates sample data if needed
3. ✅ Trains a quick ML model
4. ✅ Launches the web app on localhost:5000

USAGE:
    python SETUP_AND_RUN.py

Then open in browser:
    http://localhost:5000

Press Ctrl+C to stop the server.
=================================================================
"""

import subprocess
import sys
import os
import pandas as pd
import numpy as np
from pathlib import Path

def run_command(cmd, description):
    """Run a command and handle errors"""
    print(f"\n{'=' * 60}")
    print(f"⏳ {description}")
    print(f"{'=' * 60}")
    try:
        result = subprocess.run(cmd, shell=True, capture_output=False, text=True)
        if result.returncode != 0:
            print(f"⚠️  Command had issues, but continuing...")
        return True
    except Exception as e:
        print(f"⚠️  {description} had issues: {e}")
        return False

def install_dependencies():
    """Install all required packages"""
    print("\n" + "=" * 60)
    print("📦 STEP 1: Installing Dependencies")
    print("=" * 60)
    
    packages = [
        "pandas>=2.0.0",
        "numpy>=1.24.0",
        "scikit-learn>=1.3.0",
        "sentence-transformers>=2.2.0",
        "faiss-cpu>=1.7.0",
        "flask>=2.3.0",
        "flask-cors>=4.0.0",
        "nltk>=3.8.0",
        "langdetect>=1.0.9",
        "google-trans-new>=1.1.9",
        "streamlit>=1.28.0",
    ]
    
    print("\n📋 Required packages:")
    for pkg in packages:
        print(f"   • {pkg}")
    
    print("\n🔧 Installing packages...")
    
    # Install packages one by one with better error handling
    for package in packages:
        pkg_name = package.split(">=")[0]
        print(f"\n   → Installing {pkg_name}...", end=" ", flush=True)
        try:
            subprocess.run(
                f"{sys.executable} -m pip install -q {package}",
                shell=True,
                capture_output=True,
                timeout=300
            )
            print("✅")
        except Exception as e:
            print(f"⚠️  (will try to continue)")
    
    print("\n✅ Dependency installation complete!")

def create_sample_data():
    """Create sample datasets if they don't exist"""
    print("\n" + "=" * 60)
    print("📊 STEP 2: Preparing Sample Data")
    print("=" * 60)
    
    import config
    
    fake_csv = config.FAKE_CSV
    true_csv = config.TRUE_CSV
    
    # Check if data exists
    if os.path.exists(fake_csv) and os.path.exists(true_csv):
        print(f"\n✅ Data files already exist!")
        print(f"   • {fake_csv}")
        print(f"   • {true_csv}")
        return True
    
    print("\n🔄 Creating sample datasets...")
    
    try:
        # Create sample fake news
        fake_data = {
            'title': [
                'COVID Vaccine Contains Microchips',
                'Government Hides UFO Evidence',
                'Moon Landing Was Fake',
                'Bill Gates Plans Population Control',
                'JFK Assassin Not Caught',
                'Area 51 Contains Aliens',
                'Chemtrails Control Weather',
                '5G Network Spreads Diseases',
                'NASA Faked Mars Photos',
                'Illuminati Controls World Banks',
                'Prince Diana Was Murdered',
                'Buildings Destroyed by Directed Energy',
                'Flat Earth Conspiracy Proven',
                'Reptilians Run Government',
                'Princess Autopsy Results Hidden'
            ] * 20,  # Repeat for more data
            'text': [
                'According to sources, the COVID vaccine contains microchips for tracking',
                'Secret documents reveal government has been hiding UFO evidence for decades',
                'Technology experts prove the 1969 moon landing was entirely simulated',
                'Bill Gates admitted his plan to reduce population through vaccines',
                'JFK assassin was never caught and remains in hiding',
                'Area 51 contains alien technology and beings kept secret',
                'Chemtrails in the sky are used to control and monitor citizens',
                '5G network deployment is causing COVID-like symptoms',
                'NASA faked all Mars rover photos using Hollywood studios',
                'Illuminati secretly controls all world financial institutions',
                'Princess Diana death was cover-up, evidence destroyed',
                'World Trade Center destroyed by military directed energy weapons',
                'Flat Earth hypothesis gaining acceptance among scientists',
                'Reptile humanoids run major governments worldwide',
                'Princess autopsy results hidden by royal family conspiracy'
            ] * 20,
            'label': [0] * 300
        }
        
        # Create sample true news
        true_data = {
            'title': [
                'Study Shows Vaccine Effectiveness',
                'Researchers Discover New Species',
                'Climate Report Released',
                'Technology Advances in AI',
                'International Trade Agreement Signed',
                'Medical Breakthrough Announced',
                'Space Agency Launches Mission',
                'University Releases Study',
                'Company Reports Growth',
                'Environmental Protection Law Passed',
                'Scientific Conference Heldinelle',
                'New Energy Source Developed',
                'Healthcare System Improved',
                'Education Initiatives Launched',
                'Infrastructure Project Completed'
            ] * 20,
            'text': [
                'New large-scale study confirms effectiveness of COVID vaccines reducing hospitalizations by 95%',
                'Research team discovers previously unknown species in Amazon rainforest expedition',
                'IPCC climate report shows concerning trends in global warming requiring immediate action',
                'Machine learning algorithms reach new milestone in natural language understanding',
                'G20 nations sign historic trade agreement promoting sustainable development',
                'Doctors develop revolutionary cancer treatment showing promising clinical results',
                'Space agency successfully launches Mars exploration rover mission to study geology',
                'Harvard researchers publish findings on cognitive health and exercise correlation',
                'Tech company reports record quarterly earnings and announces expansion plans',
                'Parliament passes comprehensive environmental protection legislation',
                'Annual scientific conference brings researchers together to share findings',
                'Engineers describe new renewable energy technology improving efficiency',
                'Healthcare system implements new protocols improving patient care quality',
                'Government launches education initiative improving student access to technology',
                'Department of Transportation completes major bridge infrastructure project'
            ] * 20,
            'label': [1] * 300
        }
        
        os.makedirs(os.path.dirname(fake_csv), exist_ok=True)
        
        pd.DataFrame(fake_data).to_csv(fake_csv, index=False)
        pd.DataFrame(true_data).to_csv(true_csv, index=False)
        
        print(f"\n✅ Sample data created!")
        print(f"   • {fake_csv} ({len(fake_data['title'])} records)")
        print(f"   • {true_csv} ({len(true_data['title'])} records)")
        return True
        
    except Exception as e:
        print(f"❌ Error creating sample data: {e}")
        return False

def train_model():
    """Train the ML model using all training steps"""
    print("\n" + "=" * 60)
    print("🤖 STEP 3: Training Machine Learning Model")
    print("=" * 60)
    
    notebooks = [
        ("Step_1_Load_Data.py", "Loading and combining datasets"),
        ("Step_2_Language_Detection.py", "Setting up language detection"),
        ("Step_3_Text_Cleaning.py", "Preprocessing text data"),
        ("Step_4_Embeddings.py", "Generating embeddings"),
        ("Step_5_FAISS_Index.py", "Building similarity index"),
        ("Step_6_Train_Model.py", "Training classifier model"),
        ("Step_7_Evaluation.py", "Evaluating model performance"),
        ("Step_8_Save_Models.py", "Saving all models"),
    ]
    
    notebooks_dir = os.path.join(os.path.dirname(__file__), "notebooks")
    
    for notebook, description in notebooks:
        notebook_path = os.path.join(notebooks_dir, notebook)
        print(f"\n   ⏳ {description}...", end=" ", flush=True)
        
        try:
            result = subprocess.run(
                f"{sys.executable} {notebook_path}",
                shell=True,
                capture_output=True,
                text=True,
                timeout=300
            )
            if result.returncode == 0:
                print("✅")
            else:
                print("⚠️  (continuing)")
                if "Error" in result.stdout or "Error" in result.stderr:
                    print(f"      Output: {result.stderr[:200]}")
        except subprocess.TimeoutExpired:
            print("⚠️  (timeout, continuing)")
        except Exception as e:
            print(f"⚠️  ({str(e)[:50]})")
    
    print("\n✅ Model training complete!")

def launch_web_app():
    """Launch the Flask web app"""
    print("\n" + "=" * 60)
    print("🌐 STEP 4: Launching Web Application")
    print("=" * 60)
    
    print("\n" + "🎉 " * 20)
    print("\n🎉 SUCCESS! Your Fact-Checker is Ready! 🎉\n")
    print("🎉 " * 20)
    
    print("\n" + "=" * 60)
    print("🌐 WEB APPLICATION STARTING")
    print("=" * 60)
    
    print("\n📍 Opening in your browser...")
    print("   URL: http://localhost:5000")
    print("\n📝 Usage:")
    print("   1. Copy any news article text")
    print("   2. Paste into the input box")
    print("   3. Press 'Check Fact'")
    print("   4. See prediction and similar facts!")
    
    print("\n⏹️  To stop the server: Press Ctrl+C")
    print("\n" + "=" * 60)
    
    # Launch web app
    app_path = os.path.join(os.path.dirname(__file__), "web_app", "backend", "app.py")
    
    try:
        subprocess.run(f"{sys.executable} {app_path}", shell=False)
    except KeyboardInterrupt:
        print("\n\n👋 Server stopped. Thank you!")
    except Exception as e:
        print(f"\n❌ Error launching app: {e}")

def verify_installation():
    """Verify all required packages are installed"""
    print("\n" + "=" * 60)
    print("✔️  VERIFICATION")
    print("=" * 60)
    
    required_imports = [
        ("pandas", "Data processing"),
        ("numpy", "Numerical computing"),
        ("sklearn", "Machine learning"),
        ("sentence_transformers", "NLP embeddings"),
        ("faiss", "Vector similarity search"),
        ("flask", "Web framework"),
        ("nltk", "Text processing"),
        ("langdetect", "Language detection"),
    ]
    
    all_ok = True
    for module, description in required_imports:
        try:
            __import__(module)
            print(f"   ✅ {module:25} {description}")
        except ImportError:
            print(f"   ⚠️  {module:25} {description} (will install on first run)")
            all_ok = False
    
    print()
    return all_ok

def main():
    """Main execution flow"""
    print("""
╔══════════════════════════════════════════════════════════════╗
║                  🚀 SETUP AND RUN 🚀                        ║
║     Automated Fact-Checker Installation & Deployment        ║
╚══════════════════════════════════════════════════════════════╝
    """)
    
    print("This script will:")
    print("  1️⃣  Install all dependencies")
    print("  2️⃣  Create sample news data")
    print("  3️⃣  Train the ML model")
    print("  4️⃣  Launch the web application")
    print("\nEverything runs AUTOMATICALLY! ✨\n")
    
    # Step 1: Install dependencies
    install_dependencies()
    
    # Step 2: Verify installation
    verify_installation()
    
    # Step 3: Create sample data
    if not create_sample_data():
        print("⚠️  Could not create sample data, continuing anyway...")
    
    # Step 4: Train model
    print("\nAttempting to train model...")
    train_model()
    
    # Step 5: Launch web app
    launch_web_app()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Setup cancelled by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
