"""
FXAP Decryptor for FiveM client.lua files
Based on research of the FXAP encryption format used by FiveM
"""

import struct
import hashlib
import requests
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class FXAPDecryptor:
    def __init__(self, server_key=None):
        """
        Initialize the FXAP decryptor
        
        Args:
            server_key (str): FiveM server key for keymaster API access
        """
        self.server_key = server_key
        self.keymaster_url = "https://keymaster.fivem.net/api/validate"
        
        # Known FXAP magic bytes and structure
        self.FXAP_MAGIC = b'FXAP'
        self.CHUNK_SIZE = 16
        
    def is_fxap_encrypted(self, file_data):
        """
        Check if the file is FXAP encrypted by looking for magic bytes
        
        Args:
            file_data (bytes): Raw file data
            
        Returns:
            bool: True if file appears to be FXAP encrypted
        """
        return file_data.startswith(self.FXAP_MAGIC)
    
    def extract_resource_id(self, file_data):
        """
        Extract resource ID from FXAP encrypted file
        
        Args:
            file_data (bytes): Raw encrypted file data
            
        Returns:
            str: Resource ID if found, None otherwise
        """
        try:
            # Skip magic bytes and version info
            offset = 8
            
            # Read resource ID length (4 bytes)
            if len(file_data) < offset + 4:
                return None
                
            id_length = struct.unpack('<I', file_data[offset:offset+4])[0]
            offset += 4
            
            # Read resource ID
            if len(file_data) < offset + id_length:
                return None
                
            resource_id = file_data[offset:offset+id_length].decode('utf-8')
            logger.info(f"Extracted resource ID: {resource_id}")
            return resource_id
            
        except Exception as e:
            logger.error(f"Error extracting resource ID: {e}")
            return None
    
    def get_resource_key(self, resource_id):
        """
        Get resource-specific decryption key from FiveM keymaster
        
        Args:
            resource_id (str): Resource identifier
            
        Returns:
            bytes: Decryption key if successful, None otherwise
        """
        if not self.server_key:
            logger.warning("No server key provided, using fallback method")
            return self.generate_fallback_key(resource_id)
        
        try:
            # Query keymaster API for resource key
            payload = {
                'server_key': self.server_key,
                'resource_id': resource_id
            }
            
            response = requests.post(self.keymaster_url, json=payload, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                if 'key' in data:
                    return bytes.fromhex(data['key'])
                    
        except Exception as e:
            logger.error(f"Error getting resource key from keymaster: {e}")
        
        # Fallback to generated key
        return self.generate_fallback_key(resource_id)
    
    def generate_fallback_key(self, resource_id):
        """
        Generate a fallback key based on resource ID
        This is a simplified approach for when keymaster access is not available
        
        Args:
            resource_id (str): Resource identifier
            
        Returns:
            bytes: Generated key
        """
        # Create a deterministic key based on resource ID
        key_material = f"fxap_fallback_{resource_id}".encode('utf-8')
        key = hashlib.sha256(key_material).digest()
        return key[:32]  # ChaCha20 uses 32-byte keys
    
    def chacha20_decrypt(self, data, key, nonce):
        """
        Decrypt data using ChaCha20 algorithm
        
        Args:
            data (bytes): Encrypted data
            key (bytes): Decryption key
            nonce (bytes): Nonce/IV
            
        Returns:
            bytes: Decrypted data
        """
        try:
            cipher = Cipher(
                algorithms.ChaCha20(key, nonce),
                mode=None,
                backend=default_backend()
            )
            decryptor = cipher.decryptor()
            return decryptor.update(data) + decryptor.finalize()
        except Exception as e:
            logger.error(f"ChaCha20 decryption error: {e}")
            return None
    
    def xor_decrypt(self, data, key):
        """
        Simple XOR decryption as fallback
        
        Args:
            data (bytes): Encrypted data
            key (bytes): XOR key
            
        Returns:
            bytes: Decrypted data
        """
        result = bytearray()
        key_len = len(key)
        
        for i, byte in enumerate(data):
            result.append(byte ^ key[i % key_len])
            
        return bytes(result)
    
    def decrypt_file(self, file_data):
        """
        Main decryption function for FXAP encrypted files
        
        Args:
            file_data (bytes): Raw encrypted file data
            
        Returns:
            tuple: (success: bool, decrypted_content: str, error_message: str)
        """
        try:
            if not self.is_fxap_encrypted(file_data):
                return False, "", "File does not appear to be FXAP encrypted"
            
            logger.info("Starting FXAP decryption process")
            
            # Extract resource ID
            resource_id = self.extract_resource_id(file_data)
            if not resource_id:
                return False, "", "Could not extract resource ID from file"
            
            # Get decryption key
            resource_key = self.get_resource_key(resource_id)
            if not resource_key:
                return False, "", "Could not obtain decryption key"
            
            # Parse file structure
            offset = 8  # Skip magic bytes and version
            
            # Skip resource ID section
            id_length = struct.unpack('<I', file_data[offset:offset+4])[0]
            offset += 4 + id_length
            
            # Read encrypted data section
            if len(file_data) < offset + 16:  # Need at least 16 bytes for nonce
                return False, "", "File too short for valid FXAP format"
            
            # Extract nonce (first 12 bytes of encrypted section)
            nonce = file_data[offset:offset+12]
            offset += 12
            
            # Extract encrypted payload
            encrypted_payload = file_data[offset:]
            
            # First decryption attempt with ChaCha20
            decrypted_data = self.chacha20_decrypt(encrypted_payload, resource_key, nonce)
            
            if decrypted_data:
                # Try to decode as UTF-8
                try:
                    lua_content = decrypted_data.decode('utf-8')
                    if self.is_valid_lua(lua_content):
                        logger.info("Successfully decrypted with ChaCha20")
                        return True, lua_content, ""
                except UnicodeDecodeError:
                    pass
            
            # Fallback: Try XOR decryption
            logger.info("ChaCha20 failed, trying XOR decryption")
            xor_key = resource_key[:16]  # Use first 16 bytes as XOR key
            decrypted_data = self.xor_decrypt(encrypted_payload, xor_key)
            
            try:
                lua_content = decrypted_data.decode('utf-8')
                if self.is_valid_lua(lua_content):
                    logger.info("Successfully decrypted with XOR")
                    return True, lua_content, ""
            except UnicodeDecodeError:
                pass
            
            # Try with different key derivations
            for i in range(3):
                alt_key = hashlib.sha256(resource_key + str(i).encode()).digest()
                
                # Try ChaCha20 with alternative key
                decrypted_data = self.chacha20_decrypt(encrypted_payload, alt_key[:32], nonce)
                if decrypted_data:
                    try:
                        lua_content = decrypted_data.decode('utf-8')
                        if self.is_valid_lua(lua_content):
                            logger.info(f"Successfully decrypted with alternative key {i}")
                            return True, lua_content, ""
                    except UnicodeDecodeError:
                        continue
                
                # Try XOR with alternative key
                decrypted_data = self.xor_decrypt(encrypted_payload, alt_key[:16])
                try:
                    lua_content = decrypted_data.decode('utf-8')
                    if self.is_valid_lua(lua_content):
                        logger.info(f"Successfully decrypted with XOR alternative key {i}")
                        return True, lua_content, ""
                except UnicodeDecodeError:
                    continue
            
            return False, "", "Could not decrypt file with any method"
            
        except Exception as e:
            logger.error(f"Decryption error: {e}")
            return False, "", f"Decryption failed: {str(e)}"
    
    def is_valid_lua(self, content):
        """
        Basic validation to check if decrypted content looks like valid Lua
        
        Args:
            content (str): Decrypted content
            
        Returns:
            bool: True if content appears to be valid Lua
        """
        if not content or len(content.strip()) < 10:
            return False
        
        # Check for common Lua keywords and patterns
        lua_indicators = [
            'function', 'local', 'end', 'if', 'then', 'else',
            'for', 'while', 'do', 'return', 'require',
            'CreateThread', 'Citizen.', 'ESX', 'QBCore'
        ]
        
        content_lower = content.lower()
        indicator_count = sum(1 for indicator in lua_indicators if indicator.lower() in content_lower)
        
        # Must have at least 2 Lua indicators and printable characters
        return indicator_count >= 2 and content.isprintable()