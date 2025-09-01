#!/usr/bin/env python3
"""
Simple test script that doesn't require external dependencies
Tests basic functionality of the FXAP decryptor
"""

import sys
import os

def test_basic_functionality():
    """Test basic functionality without external dependencies"""
    print("🧪 FXAP Decryptor Bot - Basic Test")
    print("=" * 50)
    
    # Test 1: Check if main files exist
    required_files = [
        'discord_bot.py',
        'advanced_fxap_decryptor.py',
        'fxap_decryptor.py',
        'requirements.txt',
        '.env.example',
        'README.md'
    ]
    
    print("📁 Checking required files:")
    for file in required_files:
        if os.path.exists(file):
            print(f"✅ {file}")
        else:
            print(f"❌ {file} - MISSING")
    
    # Test 2: Check Python version
    print(f"\n🐍 Python version: {sys.version}")
    if sys.version_info >= (3, 8):
        print("✅ Python version is compatible")
    else:
        print("❌ Python 3.8+ required")
    
    # Test 3: Basic import test (without external deps)
    print("\n📦 Testing basic imports:")
    try:
        import hashlib
        import struct
        import base64
        import re
        import tempfile
        import logging
        print("✅ Standard library imports successful")
    except ImportError as e:
        print(f"❌ Import error: {e}")
    
    # Test 4: Check file structure
    print("\n📋 Project structure:")
    for root, dirs, files in os.walk('.'):
        level = root.replace('.', '').count(os.sep)
        indent = ' ' * 2 * level
        print(f"{indent}{os.path.basename(root)}/")
        subindent = ' ' * 2 * (level + 1)
        for file in files:
            if not file.startswith('.') and not file.endswith('.pyc'):
                print(f"{subindent}{file}")
    
    print("\n" + "=" * 50)
    print("🎉 Basic test complete!")
    print("\n📋 Next steps:")
    print("1. Install dependencies: pip install -r requirements.txt")
    print("2. Configure .env file with your Discord bot token")
    print("3. Run: python discord_bot.py")
    print("4. Test with !decrypt command in Discord")

if __name__ == "__main__":
    test_basic_functionality()