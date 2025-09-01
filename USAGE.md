# FXAP Decryptor Bot - Quick Start Guide

## 🚀 Quick Setup

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure your bot:**
   ```bash
   cp .env.example .env
   # Edit .env and add your Discord bot token
   ```

3. **Run the bot:**
   ```bash
   python discord_bot.py
   ```

## 🎮 Discord Commands

### Basic Commands

- **`!decrypt`** - Decrypt a single FXAP encrypted .lua file
  - Attach your encrypted file to the message
  - Bot will return the decrypted version

- **`!batch`** - Decrypt multiple files at once
  - Attach up to 5 .lua files
  - All files will be processed and returned

- **`!analyze`** - Analyze a file without decrypting
  - Shows encryption type, entropy, and file properties
  - Useful for understanding file structure

### Utility Commands

- **`!help`** - Show complete help information
- **`!info`** - Display bot version and capabilities  
- **`!status`** - Show bot status and server statistics

## 📋 Supported File Types

- **FXAP Encrypted Files** - Primary target format
- **XOR Encrypted Files** - Common simple encryption
- **Base64 Encoded Files** - Encoded FXAP files
- **Compressed Files** - Gzip/Zlib compressed scripts
- **Plain Lua Files** - For validation and analysis

## 🔧 Decryption Methods

The bot uses multiple decryption strategies:

1. **ChaCha20** - Primary FXAP encryption method
2. **AES** - Alternative encryption (ECB/CBC/CTR modes)
3. **XOR** - Simple encryption with various keys
4. **Base64 Decoding** - For encoded files
5. **Compression** - Handles compressed scripts
6. **Brute Force** - Last resort pattern matching

## 💡 Tips for Best Results

1. **File Names**: Keep original filenames when possible
2. **File Size**: Maximum 10MB per file
3. **Batch Processing**: Use `!batch` for multiple files
4. **Analysis First**: Use `!analyze` to understand encryption type
5. **Server Key**: Add FiveM server key to .env for better results

## ⚠️ Important Notes

- **Legal Use Only**: Only decrypt files you have permission to decrypt
- **Respect IP Rights**: Don't distribute decrypted copyrighted content
- **Educational Purpose**: This tool is for learning and authorized use
- **No Guarantees**: Not all encryption methods may be supported

## 🐛 Troubleshooting

### Common Issues

**Bot doesn't respond:**
- Check bot token in .env file
- Verify bot has message permissions
- Check bot.log for errors

**Decryption fails:**
- File may use unsupported encryption
- Try `!analyze` first to check file type
- Ensure file is actually encrypted

**File too large:**
- Maximum file size is 10MB
- Split large files or compress them

### Getting Help

1. Use `!analyze` to understand your file
2. Check the bot.log file for detailed errors
3. Ensure you have proper permissions for the files

## 📁 Example Usage

```
User: !decrypt
[Attaches: client.lua (encrypted)]

Bot: ✅ Decryption Successful
Successfully decrypted client.lua
Method: chacha20
[Returns: decrypted_client.lua]
```

```
User: !batch
[Attaches: script1.lua, script2.lua, script3.lua]

Bot: 📊 Batch Processing Complete
Processed 3 files
Successful: 2, Failed: 1
[Returns: decrypted files]
```

```
User: !analyze
[Attaches: unknown_file.lua]

Bot: 🔍 File Analysis
Type: fxap
Resource ID: my_resource
Entropy: 0.892
Likely Encrypted: Yes
```