# Installation Guide - FXAP Decryptor Discord Bot

## 🐧 Linux/Ubuntu Installation

### Option 1: Using Virtual Environment (Recommended)

```bash
# Install Python venv support
sudo apt update
sudo apt install python3-venv python3-pip python3-full

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the bot
python discord_bot.py
```

### Option 2: Using System Packages

```bash
# Install system packages
sudo apt update
sudo apt install python3-discord python3-cryptography python3-requests python3-dotenv

# Run the bot directly
python3 discord_bot.py
```

### Option 3: Force Install (Not Recommended)

```bash
# Override system package management (use with caution)
pip install -r requirements.txt --break-system-packages
python3 discord_bot.py
```

## 🪟 Windows Installation

```cmd
# Install Python from python.org if not already installed

# Create virtual environment
python -m venv venv

# Activate virtual environment
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the bot
python discord_bot.py
```

## 🍎 macOS Installation

```bash
# Install Python using Homebrew (if not already installed)
brew install python

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the bot
python discord_bot.py
```

## 🐳 Docker Installation (Alternative)

Create a Dockerfile:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "discord_bot.py"]
```

Build and run:

```bash
docker build -t fxap-bot .
docker run -d --env-file .env fxap-bot
```

## 🔧 Configuration

1. **Create environment file:**
   ```bash
   cp .env.example .env
   ```

2. **Edit .env file:**
   ```
   DISCORD_BOT_TOKEN=your_actual_bot_token_here
   FIVEM_SERVER_KEY=your_fivem_server_key_here
   ```

3. **Discord Bot Setup:**
   - Go to [Discord Developer Portal](https://discord.com/developers/applications)
   - Create new application
   - Add bot to application
   - Copy bot token to .env file
   - Generate invite URL with proper permissions

## 🎯 Required Permissions

Your Discord bot needs these permissions:
- Send Messages
- Attach Files
- Read Message History
- Use External Emojis (optional)

## ✅ Verification

Test your installation:

```bash
# Run basic test
python3 simple_test.py

# Test decryptor (if dependencies installed)
python3 test_decryptor.py

# Run the bot
python3 discord_bot.py
```

## 🆘 Troubleshooting

### "Module not found" errors
- Ensure virtual environment is activated
- Verify all dependencies are installed
- Check Python version compatibility

### "Permission denied" errors
- Use virtual environment instead of system packages
- Check file permissions
- Run with appropriate user privileges

### "Bot doesn't connect"
- Verify Discord token is correct
- Check internet connection
- Review bot.log for detailed errors

### "Decryption fails"
- Ensure file is actually FXAP encrypted
- Check if you have the correct server key
- Try different files to isolate the issue

## 📞 Support

If you encounter issues:
1. Check this installation guide
2. Review the main README.md
3. Check bot.log for detailed error information
4. Ensure you have proper permissions for files you're decrypting