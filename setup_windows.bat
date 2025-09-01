@echo off
echo 🤖 FXAP Decryptor Bot - Windows Setup
echo ====================================

echo 📁 Creating environment file...
if not exist .env (
    copy .env.example .env
    echo ✅ Created .env file
) else (
    echo ✅ .env file already exists
)

echo 📦 Installing Python dependencies...
python -m pip install discord.py==2.3.2
python -m pip install cryptography==41.0.7
python -m pip install requests==2.31.0
python -m pip install python-dotenv==1.0.0
python -m pip install aiohttp==3.9.1

echo ✅ Dependencies installed!
echo.
echo ⚠️  IMPORTANT: Edit .env file and add your Discord bot token!
echo.
echo 🚀 To start the bot, run: python discord_bot.py
pause