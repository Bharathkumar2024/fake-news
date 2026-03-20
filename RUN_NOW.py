#!/usr/bin/env python3
"""
🚀 COMPLETE WORKING FACT-CHECKER - Run Now!
Instant startup - everything works immediately!
"""

import subprocess
import sys
import os
import time

def main():
    print("\n" + "="*70)
    print("🚀 AUTOMATED FACT-CHECKER - INSTANT STARTUP")
    print("="*70)
    
    # Get the project directory (handle spaces in path)
    project_dir = os.path.dirname(os.path.abspath(__file__))
    
    print(f"\n📁 Project: {project_dir}")
    print(f"✅ Python: {sys.version.split()[0]}")
    
    # Step 1: Quick package check (don't install all, just Flask)
    print("\n" + "="*70)
    print("📦 STEP 1: Checking Core Dependencies...")
    print("="*70)
    
    core_packages = ["flask", "flask-cors"]
    
    for pkg in core_packages:
        print(f"\n   Checking {pkg}...", end=" ", flush=True)
        result = subprocess.run(
            [sys.executable, "-m", "pip", "install", "-q", pkg],
            capture_output=True,
            timeout=120
        )
        if result.returncode == 0:
            print("✅")
        else:
            print("ℹ️")
    
    # Step 2: Brief data setup
    print("\n" + "="*70)
    print("📊 STEP 2: Preparing Application...")
    print("="*70)
    
    data_dir = os.path.join(project_dir, "data")
    os.makedirs(data_dir, exist_ok=True)
    print(f"   ✅ Data directory ready")
    
    # Step 3: Launch Flask app
    print("\n" + "="*70)
    print("🌐 STEP 3: Starting Web Application...")
    print("="*70)
    
    flask_app = os.path.join(project_dir, "web_app", "backend", "app.py")
    
    print(f"\n🎉 STARTING FACT-CHECKER!")
    print(f"📍 Open in your browser: http://localhost:5000")
    print(f"📝 Demo Mode: Provides instant predictions")
    print(f"⏹️  To stop: Press Ctrl+C\n")
    
    time.sleep(2)
    
    # Run Flask app with proper path handling
    try:
        os.chdir(project_dir)
        result = subprocess.run(
            [sys.executable, flask_app],
            cwd=project_dir
        )
    except KeyboardInterrupt:
        print("\n\n👋 Stopped. Thanks for using Fact-Checker!")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print(f"Try running manually:")
        print(f"  cd \"{project_dir}\"")
        print(f"  python web_app/backend/app.py")
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"\n❌ Startup Error: {e}")
        sys.exit(1)

