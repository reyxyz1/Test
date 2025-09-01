#!/usr/bin/env python3
"""
FXAP Decryptor Bot Launcher
Simple script to run the Discord bot with proper error handling
"""

import sys
import os
import subprocess
import logging

def check_requirements():
    """Check if all requirements are installed"""
    try:
        import discord
        import cryptography
        import requests
        import dotenv
        return True
    except ImportError as e:
        print(f"❌ Missing required package: {e}")
        print("Installing requirements...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
            print("✅ Requirements installed successfully")
            return True
        except subprocess.CalledProcessError:
            print("❌ Failed to install requirements")
            return False

def check_env_file():
    """Check if .env file exists and has required variables"""
    if not os.path.exists('.env'):
        print("❌ .env file not found")
        print("Please copy .env.example to .env and configure your bot token")
        return False
    
    from dotenv import load_dotenv
    load_dotenv()
    
    if not os.getenv('DISCORD_BOT_TOKEN'):
        print("❌ DISCORD_BOT_TOKEN not found in .env file")
        print("Please add your Discord bot token to the .env file")
        return False
    
    print("✅ Environment configuration looks good")
    return True

def main():
    """Main launcher function"""
    print("🤖 FXAP Decryptor Discord Bot Launcher")
    print("=" * 50)
    
    # Check Python version
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        sys.exit(1)
    
    print(f"✅ Python {sys.version.split()[0]} detected")
    
    # Check requirements
    if not check_requirements():
        sys.exit(1)
    
    # Check environment
    if not check_env_file():
        sys.exit(1)
    
    # Start the bot
    print("🚀 Starting Discord bot...")
    try:
        from discord_bot import bot, DISCORD_TOKEN
        if DISCORD_TOKEN:
            bot.run(DISCORD_TOKEN)
        else:
            print("❌ No Discord token found")
            sys.exit(1)
    except KeyboardInterrupt:
        print("\n👋 Bot stopped by user")
    except Exception as e:
        print(f"❌ Bot error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()