#!/usr/bin/env python3
"""
Setup script for FXAP Decryptor Discord Bot
"""

import os
import sys
import subprocess
import shutil

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python {sys.version.split()[0]} detected")
    return True

def install_requirements():
    """Install required packages"""
    print("📦 Installing requirements...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Requirements installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install requirements: {e}")
        return False

def setup_environment():
    """Set up environment file"""
    if not os.path.exists('.env'):
        if os.path.exists('.env.example'):
            shutil.copy('.env.example', '.env')
            print("✅ Created .env file from template")
            print("⚠️  Please edit .env file and add your Discord bot token")
        else:
            with open('.env', 'w') as f:
                f.write("DISCORD_BOT_TOKEN=your_discord_bot_token_here\n")
                f.write("FIVEM_SERVER_KEY=your_fivem_server_key_here\n")
            print("✅ Created .env file")
            print("⚠️  Please edit .env file and add your Discord bot token")
        return False
    else:
        print("✅ .env file already exists")
        return True

def create_run_script():
    """Create platform-specific run scripts"""
    # Windows batch file
    with open('run_bot.bat', 'w') as f:
        f.write('@echo off\n')
        f.write('echo Starting FXAP Decryptor Bot...\n')
        f.write('python discord_bot.py\n')
        f.write('pause\n')
    
    # Unix shell script
    with open('run_bot.sh', 'w') as f:
        f.write('#!/bin/bash\n')
        f.write('echo "Starting FXAP Decryptor Bot..."\n')
        f.write('python3 discord_bot.py\n')
    
    # Make shell script executable on Unix systems
    if os.name != 'nt':
        os.chmod('run_bot.sh', 0o755)
    
    print("✅ Created run scripts (run_bot.bat, run_bot.sh)")

def main():
    """Main setup function"""
    print("🔧 FXAP Decryptor Discord Bot Setup")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Install requirements
    if not install_requirements():
        sys.exit(1)
    
    # Setup environment
    env_ready = setup_environment()
    
    # Create run scripts
    create_run_script()
    
    print("\n" + "=" * 50)
    print("🎉 Setup completed!")
    print("\n📋 Next steps:")
    
    if not env_ready:
        print("1. Edit the .env file and add your Discord bot token")
        print("2. (Optional) Add your FiveM server key for enhanced decryption")
    
    print(f"{'3' if not env_ready else '1'}. Run the bot:")
    if os.name == 'nt':
        print("   • Windows: Double-click run_bot.bat or run 'python discord_bot.py'")
    else:
        print("   • Linux/Mac: Run './run_bot.sh' or 'python3 discord_bot.py'")
    
    print(f"{'4' if not env_ready else '2'}. Invite the bot to your Discord server")
    print(f"{'5' if not env_ready else '3'}. Use '!decrypt' command with file attachments")
    
    print("\n⚠️  Legal Notice:")
    print("Only decrypt files you have permission to decrypt.")
    print("Respect intellectual property rights and terms of service.")

if __name__ == "__main__":
    main()