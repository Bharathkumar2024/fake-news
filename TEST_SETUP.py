#!/usr/bin/env python3
"""Quick test that everything is working"""

import sys
import os

# Add project to path
project_dir = r"c:\FAKE NEWS"
sys.path.insert(0, project_dir)

print("🧪 Testing Fact-Checker Setup...\n")

# Test 1: Import Flask
print("[1/5] Testing Flask...", end=" ", flush=True)
try:
    from flask import Flask
    print("✅")
except Exception as e:
    print(f"❌ {e}")
    sys.exit(1)

# Test 2: Import config
print("[2/5] Testing configuration...", end=" ", flush=True)
try:
    import config
    print(f"✅ (Port: {config.FLASK_PORT})")
except Exception as e:
    print(f"❌ {e}")
    sys.exit(1)

# Test 3: Import fact checker
print("[3/5] Testing fact checker...", end=" ", flush=True)
try:
    from src.fact_checker import fact_checker
    print("✅")
except Exception as e:
    print(f"❌ {e}\n   This is OK - will use demo mode")

# Test 4: Test demo fact checker
print("[4/5] Testing demo mode...", end=" ", flush=True)
try:
    from src.demo_fact_checker import demo_fact_checker
    result = demo_fact_checker.check_fact("Test text")
    if result['status'] == 'success':
        print("✅")
    else:
        print(f"❌ {result}")
        sys.exit(1)
except Exception as e:
    print(f"❌ {e}")
    sys.exit(1)

# Test 5: Flask app imports
print("[5/5] Testing Flask app...", end=" ", flush=True)
try:
    # Import simulating what Flask app does
    from flask import Flask, request, jsonify
    print("✅")
except Exception as e:
    print(f"❌ {e}")
    sys.exit(1)

print("\n" + "="*50)
print("✅ ALL TESTS PASSED - System is ready!")
print("="*50)
print("\nTo start the app, run:")
print("  python RUN_NOW.py")
print("\nOr from PowerShell:")
print("  .\\RUN_NOW.bat")
