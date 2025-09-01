# How to Use the FXAP Decryptor Discord Bot

## 🎯 Complete Usage Guide

### Step 1: Discord Bot Setup

1. **Create Discord Bot:**
   - Go to https://discord.com/developers/applications
   - Click "New Application" → Name it "FXAP Decryptor"
   - Go to "Bot" section → Click "Add Bot"
   - **Copy the bot token** (you'll need this!)

2. **Set Bot Permissions:**
   - In Bot section, enable "Message Content Intent"
   - Go to OAuth2 → URL Generator
   - Select "bot" scope
   - Select permissions:
     - ✅ Send Messages
     - ✅ Attach Files  
     - ✅ Read Message History
   - Copy the invite URL

3. **Invite Bot to Server:**
   - Open the invite URL
   - Select your Discord server
   - Click "Authorize"

### Step 2: Configure the Bot

1. **Edit the .env file:**
   ```bash
   # Open .env file and replace with your actual token
   DISCORD_BOT_TOKEN=YOUR_ACTUAL_BOT_TOKEN_HERE
   FIVEM_SERVER_KEY=your_fivem_server_key_here  # Optional
   ```

### Step 3: Start the Bot

**Option A: Simple Start**
```bash
python3 discord_bot.py
```

**Option B: Using Startup Script**
```bash
./start_bot.sh
```

**Option C: Using Setup Script**
```bash
python3 setup.py
```

You should see:
```
🤖 FXAP Decryptor Discord Bot Launcher
==================================================
✅ Python 3.13.3 detected
✅ Requirements installed successfully
✅ Environment configuration looks good
🚀 Starting Discord bot...
[INFO] Bot has connected to Discord!
```

## 🎮 Using the Bot in Discord

### Basic Commands

#### 1. **Decrypt Single File**
```
!decrypt
```
- Attach your encrypted `.lua` file to the message
- Bot will process and return decrypted version

**Example:**
```
You: !decrypt
[Attach: encrypted_client.lua]

Bot: ✅ Decryption Successful
Successfully decrypted encrypted_client.lua
Method: chacha20
[Returns: decrypted_encrypted_client.lua]
```

#### 2. **Decrypt Multiple Files**
```
!batch
```
- Attach up to 5 `.lua` files
- Bot processes all files and returns results

**Example:**
```
You: !batch
[Attach: file1.lua, file2.lua, file3.lua]

Bot: 📊 Batch Processing Complete
Processed 3 files
Successful: 2, Failed: 1
[Returns: decrypted files]
```

#### 3. **Analyze File**
```
!analyze
```
- Check file encryption type without decrypting
- Shows file properties and encryption details

**Example:**
```
You: !analyze
[Attach: unknown_file.lua]

Bot: 🔍 File Analysis
Type: fxap
Resource ID: my_resource
Entropy: 0.892
Likely Encrypted: Yes
```

#### 4. **Get Help**
```
!help
```
- Shows all available commands
- Usage instructions
- Important notes

#### 5. **Bot Status**
```
!status
```
- Shows bot health and statistics
- Server information
- Supported methods

#### 6. **Bot Info**
```
!info
```
- Bot version and capabilities
- Technical information

## 📋 File Requirements

### Supported Files:
- ✅ `.lua` files (FXAP encrypted)
- ✅ `.fxap` files
- ✅ Base64 encoded files
- ✅ Compressed files
- ✅ XOR encrypted files

### File Limits:
- **Max Size:** 10MB per file
- **Batch Limit:** 5 files at once
- **Formats:** .lua, .fxap extensions

## 🔍 Understanding Results

### Success Response:
```
✅ Decryption Successful
Successfully decrypted filename.lua

📊 File Info:
Original Size: 1,234 bytes
Decrypted Size: 2,456 characters  
Lines: 89
Method: chacha20

📄 Preview:
-- FiveM Client Script
local ESX = nil
...
```

### Failure Response:
```
❌ Decryption Failed
Could not decrypt filename.lua

Error Details:
All decryption methods failed

💡 Possible Solutions:
• Ensure the file is properly FXAP encrypted
• Check if you have the correct server key
• Try a different version of the encrypted file
```

## 🛠️ Troubleshooting

### Common Issues:

**1. Bot doesn't respond:**
- Check bot is online (green dot in Discord)
- Verify bot has message permissions in channel
- Check bot token is correct in .env file

**2. "File not encrypted" message:**
- File might already be decrypted
- File might use different encryption
- Try `!analyze` first to check file type

**3. "Decryption failed" error:**
- File might be corrupted
- Wrong encryption method
- Missing server key for keymaster access

**4. Bot crashes or stops:**
- Check console output for errors
- Review bot.log file
- Restart with `python3 discord_bot.py`

### Debug Steps:

1. **Check bot logs:**
   ```bash
   tail -f bot.log
   ```

2. **Test with sample files:**
   ```bash
   python3 test_decryptor.py
   ```

3. **Verify bot status:**
   Use `!status` command in Discord

## 💡 Pro Tips

1. **Use `!analyze` first** - Check file type before decrypting
2. **Keep original filenames** - Helps with resource ID extraction
3. **Try batch processing** - More efficient for multiple files
4. **Check file size** - Large files may take longer to process
5. **Use server key** - Add FiveM server key for better results

## 🔐 Security Notes

- Files are processed temporarily and deleted automatically
- No persistent storage of your files
- Bot runs locally under your control
- All processing happens on your server

## ⚠️ Legal Reminder

**Only decrypt files you have permission to decrypt!**
- Respect intellectual property rights
- Follow FiveM terms of service
- Don't distribute copyrighted content
- Use for educational/authorized purposes only

## 🆘 Getting Help

If you need help:
1. Use `!help` command in Discord
2. Check this guide and README.md
3. Review bot.log for detailed errors
4. Ensure you have proper file permissions

---

**Ready to start? Just run `python3 discord_bot.py` and use `!decrypt` with your encrypted files!**