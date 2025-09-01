# FXAP Decryptor Discord Bot

A Discord bot that can decrypt FiveM client.lua files encrypted with FXAP (FiveM Asset Protection).

## ⚠️ Legal Notice

**IMPORTANT:** This tool is for educational and authorized use only. Only decrypt files that you have explicit permission to decrypt. Unauthorized decryption may violate:
- Intellectual property rights
- Terms of service agreements
- Copyright laws
- FiveM community guidelines

Always respect the rights of script authors and resource creators.

## 🚀 Features

- **FXAP Decryption**: Supports decryption of FiveM FXAP encrypted files
- **Multiple Algorithms**: Uses ChaCha20 and XOR decryption methods
- **Discord Integration**: Easy-to-use Discord commands
- **File Validation**: Validates decrypted content to ensure successful decryption
- **Error Handling**: Comprehensive error reporting and logging
- **Security**: Temporary file handling with automatic cleanup

## 📋 Requirements

- Python 3.8 or higher
- Discord bot token
- (Optional) FiveM server key for keymaster API access

## 🛠️ Installation

1. **Clone or download this repository**
   ```bash
   git clone <repository-url>
   cd fxap-decryptor-bot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Create environment file**
   ```bash
   cp .env.example .env
   ```

4. **Configure the bot**
   Edit `.env` file and add your Discord bot token:
   ```
   DISCORD_BOT_TOKEN=your_discord_bot_token_here
   FIVEM_SERVER_KEY=your_fivem_server_key_here
   ```

## 🔧 Discord Bot Setup

1. **Create a Discord Application**
   - Go to [Discord Developer Portal](https://discord.com/developers/applications)
   - Click "New Application" and give it a name
   - Go to the "Bot" section and click "Add Bot"

2. **Get Bot Token**
   - In the Bot section, click "Copy" under the Token section
   - Add this token to your `.env` file

3. **Set Bot Permissions**
   - In the Bot section, enable the following permissions:
     - Send Messages
     - Attach Files
     - Read Message History
     - Use Slash Commands (optional)

4. **Invite Bot to Server**
   - Go to OAuth2 → URL Generator
   - Select "bot" scope
   - Select required permissions
   - Use the generated URL to invite the bot to your server

## 🎮 Usage

### Commands

- `!decrypt` - Decrypt an FXAP encrypted .lua file (attach file to message)
- `!help` - Show help information
- `!info` - Show bot information and statistics

### Decrypting Files

1. Upload your encrypted `.lua` file to a Discord channel where the bot has access
2. Use the command `!decrypt` in the same message or in a reply
3. The bot will process the file and return the decrypted version
4. Download the decrypted file from the bot's response

### Example Usage

```
User: !decrypt
[Attaches: encrypted_client.lua]

Bot: ✅ Decryption Successful
Successfully decrypted encrypted_client.lua
[Attaches: decrypted_encrypted_client.lua]
```

## 🔍 How It Works

The bot implements a multi-stage decryption process:

1. **File Validation**: Checks if the uploaded file is FXAP encrypted
2. **Resource ID Extraction**: Extracts the resource identifier from the encrypted file
3. **Key Retrieval**: Attempts to get the decryption key via:
   - FiveM Keymaster API (if server key provided)
   - Fallback key generation based on resource ID
4. **Decryption Attempts**: Tries multiple decryption methods:
   - ChaCha20 with original key
   - XOR decryption with derived key
   - Alternative key derivations
5. **Content Validation**: Validates that decrypted content is valid Lua code

## 📁 File Structure

```
fxap-decryptor-bot/
├── discord_bot.py          # Main Discord bot implementation
├── fxap_decryptor.py       # FXAP decryption logic
├── requirements.txt        # Python dependencies
├── .env.example           # Environment variables template
├── .env                   # Your environment variables (create this)
├── bot.log               # Bot log file (created automatically)
└── README.md             # This file
```

## 🐛 Troubleshooting

### Common Issues

1. **"Bot doesn't respond"**
   - Check that the bot token is correct
   - Ensure the bot has necessary permissions
   - Check bot.log for error messages

2. **"Decryption failed"**
   - Verify the file is actually FXAP encrypted
   - Check if you have the correct server key
   - Some files may use different encryption methods

3. **"File too large"**
   - The bot has a 10MB file size limit
   - Try compressing the file or splitting it

### Logs

Check `bot.log` for detailed error information and debugging output.

## 🔒 Security Considerations

- Files are processed in temporary locations and automatically deleted
- No persistent storage of uploaded files
- Environment variables are used for sensitive configuration
- Comprehensive input validation and error handling

## 📜 License

This project is for educational purposes only. Use responsibly and in accordance with all applicable laws and terms of service.

## 🤝 Contributing

This tool is provided as-is for educational purposes. Please ensure any contributions maintain the educational focus and legal compliance.

## ⚡ Running the Bot

```bash
python discord_bot.py
```

The bot will start and connect to Discord. You should see a message indicating successful connection.

## 📞 Support

If you encounter issues:
1. Check the troubleshooting section above
2. Review the bot.log file for detailed error information
3. Ensure you have proper permissions for the files you're trying to decrypt