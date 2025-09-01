@echo off
echo 🤖 Starting FXAP Decryptor Discord Bot
echo ====================================

if not exist .env (
    echo ❌ .env file not found!
    echo Please run setup_windows.bat first
    pause
    exit
)

echo 🚀 Starting bot...
python discord_bot.py

pause