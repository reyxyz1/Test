#!/usr/bin/env python3
"""
Example usage demonstration of the FXAP Decryptor
Shows how the bot would work with real files
"""

import os
from advanced_fxap_decryptor import FXAPDecryptor

def demonstrate_usage():
    """Demonstrate how the decryptor works"""
    print("🎯 FXAP Decryptor - Usage Example")
    print("=" * 50)
    
    # Initialize decryptor
    decryptor = FXAPDecryptor()
    
    # Example 1: Check if files exist from test
    test_files = ['test_fxap_encrypted.lua', 'test_xor_encrypted.lua', 'test_plain.lua']
    
    for filename in test_files:
        if os.path.exists(filename):
            print(f"\n📁 Processing: {filename}")
            
            with open(filename, 'rb') as f:
                file_data = f.read()
            
            # Analyze file
            encryption_type = decryptor.detect_encryption_type(file_data)
            print(f"🔍 Detected type: {encryption_type}")
            
            # Try decryption
            success, content, method, error = decryptor.decrypt_file_advanced(file_data)
            
            if success:
                print(f"✅ Decryption successful using: {method}")
                print(f"📊 Content length: {len(content)} characters")
                print(f"📄 Preview: {content[:100]}...")
            else:
                print(f"❌ Decryption failed: {error}")
        else:
            print(f"📁 {filename} - Not found (run test_decryptor.py first)")
    
    print("\n" + "=" * 50)
    print("🎮 Discord Bot Usage:")
    print("1. Start bot: python3 discord_bot.py")
    print("2. In Discord: !decrypt [attach file]")
    print("3. Bot will process and return decrypted file")
    print("4. Download the result!")

if __name__ == "__main__":
    demonstrate_usage()