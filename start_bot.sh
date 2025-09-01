#!/bin/bash

# FXAP Decryptor Discord Bot Startup Script

echo "🤖 FXAP Decryptor Discord Bot"
echo "============================="

# Check if virtual environment exists
if [ -d "venv" ]; then
    echo "📦 Activating virtual environment..."
    source venv/bin/activate
    
    # Check if dependencies are installed
    if python -c "import discord, cryptography, requests, dotenv" 2>/dev/null; then
        echo "✅ Dependencies verified"
    else
        echo "📦 Installing dependencies..."
        pip install -r requirements.txt
    fi
    
    echo "🚀 Starting bot with virtual environment..."
    python discord_bot.py
else
    echo "⚠️  No virtual environment found"
    echo "📦 Attempting to use system Python..."
    
    # Try to run with system Python
    if python3 -c "import discord, cryptography, requests, dotenv" 2>/dev/null; then
        echo "✅ System dependencies found"
        echo "🚀 Starting bot..."
        python3 discord_bot.py
    else
        echo "❌ Dependencies not found"
        echo ""
        echo "Please install dependencies first:"
        echo "1. Create virtual environment: python3 -m venv venv"
        echo "2. Activate it: source venv/bin/activate"
        echo "3. Install deps: pip install -r requirements.txt"
        echo "4. Run this script again"
        exit 1
    fi
fi