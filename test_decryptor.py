#!/usr/bin/env python3
"""
Test script for FXAP Decryptor
Creates sample encrypted files for testing
"""

import os
import hashlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from advanced_fxap_decryptor import FXAPDecryptor

def create_test_lua_content():
    """Create sample Lua content for testing"""
    return """-- FiveM Client Script Example
local ESX = nil

Citizen.CreateThread(function()
    while ESX == nil do
        TriggerEvent('esx:getSharedObject', function(obj) ESX = obj end)
        Citizen.Wait(0)
    end
end)

RegisterNetEvent('test:clientEvent')
AddEventHandler('test:clientEvent', function(data)
    print('Received data:', data)
end)

function TestFunction()
    local playerPed = PlayerPedId()
    local playerCoords = GetEntityCoords(playerPed)
    
    print('Player coordinates:', playerCoords)
    
    return {
        x = playerCoords.x,
        y = playerCoords.y,
        z = playerCoords.z
    }
end

-- Main execution
Citizen.CreateThread(function()
    while true do
        Citizen.Wait(5000)
        TestFunction()
    end
end)"""

def create_fxap_encrypted_file(content, resource_id="test_resource"):
    """
    Create a mock FXAP encrypted file for testing
    
    Args:
        content (str): Lua content to encrypt
        resource_id (str): Resource identifier
        
    Returns:
        bytes: Mock encrypted file data
    """
    # Create mock FXAP structure
    magic = b'FXAP'
    version = b'\x01\x00\x00\x00'
    
    # Resource ID section
    resource_id_bytes = resource_id.encode('utf-8')
    id_length = len(resource_id_bytes).to_bytes(4, 'little')
    
    # Generate key and nonce
    key = hashlib.sha256(f"fxap_{resource_id}".encode()).digest()
    nonce = hashlib.sha256(key).digest()[:16]  # ChaCha20 needs 16 bytes for nonce
    
    # Encrypt content
    content_bytes = content.encode('utf-8')
    
    cipher = Cipher(
        algorithms.ChaCha20(key, nonce),
        mode=None,
        backend=default_backend()
    )
    encryptor = cipher.encryptor()
    encrypted_content = encryptor.update(content_bytes) + encryptor.finalize()
    
    # Assemble file
    file_data = magic + version + id_length + resource_id_bytes + nonce + encrypted_content
    
    return file_data

def create_xor_encrypted_file(content, key=b"test_key_123"):
    """
    Create a XOR encrypted file for testing
    
    Args:
        content (str): Content to encrypt
        key (bytes): XOR key
        
    Returns:
        bytes: XOR encrypted data
    """
    content_bytes = content.encode('utf-8')
    result = bytearray()
    
    for i, byte in enumerate(content_bytes):
        result.append(byte ^ key[i % len(key)])
    
    return bytes(result)

def test_decryptor():
    """Test the decryptor with sample files"""
    print("🧪 Testing FXAP Decryptor")
    print("=" * 50)
    
    # Initialize decryptor
    decryptor = FXAPDecryptor()
    
    # Create test content
    lua_content = create_test_lua_content()
    print(f"📝 Created test Lua content ({len(lua_content)} characters)")
    
    # Test 1: FXAP encrypted file
    print("\n🔐 Test 1: FXAP Encryption")
    fxap_data = create_fxap_encrypted_file(lua_content, "test_resource")
    
    with open('test_fxap_encrypted.lua', 'wb') as f:
        f.write(fxap_data)
    print(f"✅ Created test_fxap_encrypted.lua ({len(fxap_data)} bytes)")
    
    # Test decryption
    success, decrypted, method, error = decryptor.decrypt_file_advanced(fxap_data)
    print(f"🔍 Decryption result: {'✅ Success' if success else '❌ Failed'}")
    if success:
        print(f"📄 Method used: {method}")
        print(f"📊 Decrypted length: {len(decrypted)} characters")
        print(f"✅ Content matches: {'Yes' if lua_content in decrypted else 'No'}")
    else:
        print(f"❌ Error: {error}")
    
    # Test 2: XOR encrypted file
    print("\n🔐 Test 2: XOR Encryption")
    xor_data = create_xor_encrypted_file(lua_content)
    
    with open('test_xor_encrypted.lua', 'wb') as f:
        f.write(xor_data)
    print(f"✅ Created test_xor_encrypted.lua ({len(xor_data)} bytes)")
    
    # Test decryption
    success, decrypted, method, error = decryptor.decrypt_file_advanced(xor_data)
    print(f"🔍 Decryption result: {'✅ Success' if success else '❌ Failed'}")
    if success:
        print(f"📄 Method used: {method}")
        print(f"✅ Content matches: {'Yes' if lua_content in decrypted else 'No'}")
    else:
        print(f"❌ Error: {error}")
    
    # Test 3: Plain Lua file
    print("\n📄 Test 3: Plain Lua File")
    with open('test_plain.lua', 'w') as f:
        f.write(lua_content)
    
    with open('test_plain.lua', 'rb') as f:
        plain_data = f.read()
    
    success, decrypted, method, error = decryptor.decrypt_file_advanced(plain_data)
    print(f"🔍 Analysis result: {'✅ Recognized' if success else '❌ Not recognized'}")
    if success:
        print(f"📄 Method used: {method}")
    
    print("\n" + "=" * 50)
    print("🎉 Testing complete!")
    print("\n📁 Test files created:")
    print("• test_fxap_encrypted.lua - Mock FXAP encrypted file")
    print("• test_xor_encrypted.lua - XOR encrypted file")
    print("• test_plain.lua - Plain Lua file")
    print("\n💡 You can use these files to test the Discord bot!")

if __name__ == "__main__":
    test_decryptor()