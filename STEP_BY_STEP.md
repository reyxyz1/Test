# 📋 Step-by-Step Usage Guide

## 🎯 Exact Steps to Use the Bot

### Phase 1: One-Time Setup

#### 1. Get Your Bot Token
1. Go to https://discord.com/developers/applications
2. Click "New Application"
3. Name it "FXAP Decryptor" 
4. Go to "Bot" section → Click "Add Bot"
5. **Copy the token** (keep this secret!)

#### 2. Configure the Bot
1. Open the `.env` file in this folder
2. Replace `your_discord_bot_token_here` with your actual token:
   ```
   DISCORD_BOT_TOKEN=MTIzNDU2Nzg5MDEyMzQ1Njc4.GhIjKl.MnOpQrStUvWxYzAbCdEfGhIjKlMnOpQrSt
   ```

#### 3. Invite Bot to Your Server
1. In Discord Developer Portal, go to OAuth2 → URL Generator
2. Select "bot" scope
3. Select permissions:
   - Send Messages
   - Attach Files
   - Read Message History
4. Copy the URL and open it
5. Select your server and authorize

### Phase 2: Start the Bot

#### Option A: Direct Start
```bash
python3 discord_bot.py
```

#### Option B: Using Startup Script
```bash
./start_bot.sh
```

**You should see:**
```
🤖 FXAP Decryptor Discord Bot Launcher
==================================================
✅ Python 3.13.3 detected
✅ Environment configuration looks good
🚀 Starting Discord bot...
[INFO] Bot has connected to Discord!
```

### Phase 3: Use the Bot

#### Single File Decryption
1. **Go to your Discord server**
2. **Type:** `!decrypt`
3. **Attach your encrypted .lua file** (drag & drop or click attach)
4. **Send the message**
5. **Wait for processing** (you'll see a blue "Processing..." message)
6. **Download result** (bot will send back the decrypted file)

**Example:**
```
👤 You: !decrypt
📎 [encrypted_client.lua]

🤖 Bot: 🔄 Processing File
Decrypting encrypted_client.lua...
This may take a moment.

🤖 Bot: ✅ Decryption Successful
Successfully decrypted encrypted_client.lua

📊 File Info:
Original Size: 2,345 bytes
Decrypted Size: 1,876 characters
Lines: 67
Method: chacha20

📎 [decrypted_encrypted_client.lua]
```

#### Multiple Files at Once
1. **Type:** `!batch`
2. **Attach multiple .lua files** (up to 5)
3. **Send the message**
4. **Download all decrypted files**

#### Analyze Without Decrypting
1. **Type:** `!analyze`
2. **Attach any file**
3. **Get detailed analysis** (encryption type, entropy, etc.)

### Phase 4: Understanding Results

#### ✅ Success Messages
- **Green embed** = Decryption worked
- **File attachment** = Your decrypted file
- **Method shown** = How it was decrypted (chacha20, xor, etc.)

#### ❌ Error Messages
- **Red embed** = Something went wrong
- **Error details** = Specific problem
- **Suggestions** = What to try next

#### ℹ️ Info Messages
- **Blue embed** = File analysis or processing
- **Orange embed** = File not encrypted (already plain text)

## 🎮 Real Usage Examples

### Example 1: Basic Decryption
```
You: !decrypt
[Attach: my_encrypted_script.lua]

Bot: ✅ Decryption Successful
📊 Original: 1.2KB → Decrypted: 856 chars
Method: chacha20
[Returns: decrypted_my_encrypted_script.lua]
```

### Example 2: File Analysis
```
You: !analyze
[Attach: unknown_file.lua]

Bot: 🔍 File Analysis
📊 Size: 2,345 bytes
Type: fxap
Resource ID: esx_policejob
Entropy: 0.892
Likely Encrypted: Yes
```

### Example 3: Batch Processing
```
You: !batch
[Attach: script1.lua, script2.lua, script3.lua]

Bot: 📊 Batch Processing Complete
Processed 3 files
Successful: 2, Failed: 1

✅ script1.lua - Size: 1,234 chars (chacha20)
✅ script2.lua - Size: 2,567 chars (xor)
❌ script3.lua - All decryption methods failed
```

### Example 4: Already Decrypted File
```
You: !decrypt
[Attach: plain_script.lua]

Bot: ℹ️ File Not Encrypted
The uploaded file doesn't appear to be FXAP encrypted.
It may already be decrypted.

📄 Preview:
```lua
-- This is already a plain Lua file
local ESX = nil
...
```

## 🔧 Command Reference

| Command | Purpose | Usage |
|---------|---------|-------|
| `!decrypt` | Decrypt single file | `!decrypt` + attach file |
| `!batch` | Decrypt multiple files | `!batch` + attach files |
| `!analyze` | Analyze file properties | `!analyze` + attach file |
| `!help` | Show help information | `!help` |
| `!status` | Bot status & stats | `!status` |
| `!info` | Bot information | `!info` |

## 💡 Tips for Best Results

1. **File Names Matter:** Keep original filenames when possible
2. **Check Size:** Max 10MB per file
3. **Use Analyze First:** Check encryption type with `!analyze`
4. **Server Key Helps:** Add FiveM server key to .env for better results
5. **Be Patient:** Large files may take a few seconds to process

## 🚨 Common Mistakes

❌ **Wrong:** Uploading non-Lua files
✅ **Right:** Only upload .lua or .fxap files

❌ **Wrong:** Forgetting to attach file
✅ **Right:** Always attach file with command

❌ **Wrong:** Using bot without proper token
✅ **Right:** Configure .env with valid Discord token

❌ **Wrong:** Expecting instant results
✅ **Right:** Wait for processing message to complete

## 🎯 Quick Test

Want to test if everything works?

1. **Start the bot:** `python3 discord_bot.py`
2. **In Discord, type:** `!help`
3. **Bot should respond** with help information
4. **If it works,** try `!status` to see bot statistics

If the bot responds to `!help`, you're ready to decrypt files!

## 🔄 Restart Bot

If you need to restart the bot:
1. **Stop:** Press `Ctrl+C` in terminal
2. **Start:** Run `python3 discord_bot.py` again

## 📞 Need Help?

If something doesn't work:
1. Check the console output for errors
2. Look at `bot.log` file for detailed logs
3. Verify your Discord token is correct
4. Make sure bot has proper permissions in your server
5. Try the `!status` command to test bot connectivity

---

**🎉 You're ready to decrypt FXAP files! Just start the bot and use `!decrypt` with your encrypted files.**