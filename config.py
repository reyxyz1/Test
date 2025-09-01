"""
Configuration file for FXAP Decryptor Discord Bot
"""

import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Config:
    """Bot configuration class"""
    
    # Discord settings
    DISCORD_TOKEN = os.getenv('DISCORD_BOT_TOKEN')
    COMMAND_PREFIX = os.getenv('COMMAND_PREFIX', '!')
    
    # FiveM settings
    FIVEM_SERVER_KEY = os.getenv('FIVEM_SERVER_KEY')
    KEYMASTER_URL = os.getenv('KEYMASTER_URL', 'https://keymaster.fivem.net/api/validate')
    
    # File handling settings
    MAX_FILE_SIZE = int(os.getenv('MAX_FILE_SIZE', 10 * 1024 * 1024))  # 10MB default
    MAX_BATCH_FILES = int(os.getenv('MAX_BATCH_FILES', 5))
    TEMP_DIR = os.getenv('TEMP_DIR', None)  # Use system temp if None
    
    # Security settings
    ALLOWED_EXTENSIONS = ['.lua', '.fxap']
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    
    # Bot behavior
    DELETE_TEMP_FILES = os.getenv('DELETE_TEMP_FILES', 'true').lower() == 'true'
    ENABLE_ANALYTICS = os.getenv('ENABLE_ANALYTICS', 'false').lower() == 'true'
    
    @classmethod
    def validate(cls):
        """Validate configuration"""
        errors = []
        
        if not cls.DISCORD_TOKEN:
            errors.append("DISCORD_BOT_TOKEN is required")
        
        if cls.MAX_FILE_SIZE <= 0:
            errors.append("MAX_FILE_SIZE must be positive")
        
        if cls.MAX_BATCH_FILES <= 0:
            errors.append("MAX_BATCH_FILES must be positive")
        
        return errors

# Global config instance
config = Config()