# 🪟 Windows Setup - Fixed Version

## ✅ **The Issue is Fixed!**

The error you encountered was because Discord.py already has a built-in `help` command. I've fixed this by renaming our help command to `!guide`.

## 🚀 **Quick Fix Steps:**

### 1. Install Missing Package
```cmd
py -m pip install PyNaCl
```

### 2. Try Running Again
```cmd
py discord_bot.py
```

You should now see:
```
[INFO] Bot has connected to Discord!
[INFO] Bot is in 1 guilds
```

## 🎮 **Updated Commands:**

| Old Command | New Command | What It Does |
|-------------|-------------|--------------|
| `!help` | `!guide` | Show help information |
| `!decrypt` | `!decrypt` | Decrypt files (unchanged) |
| `!batch` | `!batch` | Batch decrypt (unchanged) |
| `!analyze` | `!analyze` | Analyze files (unchanged) |
| `!status` | `!status` | Bot status (unchanged) |
| `!info` | `!info` | Bot info (unchanged) |

## 🔧 **Complete Windows Setup (If Starting Fresh):**

### Step 1: Install All Dependencies
```cmd
py -m pip install discord.py==2.3.2
py -m pip install cryptography==41.0.7
py -m pip install requests==2.31.0
py -m pip install python-dotenv==1.0.0
py -m pip install aiohttp==3.9.1
py -m pip install PyNaCl
```

### Step 2: Create .env File
```cmd
copy .env.example .env
```

### Step 3: Edit .env File
Open `.env` with Notepad and add your Discord bot token:
```
DISCORD_BOT_TOKEN=your_actual_bot_token_here
FIVEM_SERVER_KEY=your_fivem_server_key_here
```

### Step 4: Run Bot
```cmd
py discord_bot.py
```

## 🎯 **Test the Bot:**

Once the bot is running, go to your Discord server and try:

```
!guide
```

This should show you all the available commands.

Then test decryption:
```
!decrypt
[attach your encrypted .lua file]
```

## ⚡ **Quick Test Commands:**

1. `!guide` - Show all commands
2. `!status` - Check if bot is working
3. `!info` - Show bot information
4. `!decrypt` - Decrypt a file (attach .lua file)

## 🔍 **If You Still Get Errors:**

### Error: "No module named discord"
```cmd
py -m pip install --upgrade discord.py
```

### Error: "No module named cryptography"
```cmd
py -m pip install --upgrade cryptography
```

### Error: "Permission denied"
```cmd
py -m pip install --user discord.py cryptography requests python-dotenv aiohttp PyNaCl
```

### Error: "Bot token invalid"
- Double-check your Discord bot token in the `.env` file
- Make sure there are no extra spaces
- Get a new token from Discord Developer Portal if needed

## 🎉 **Success!**

When working correctly, you should see:
```
🤖 FXAP Decryptor Discord Bot
Bot has connected to Discord!
Bot is in 1 guilds
```

Then in Discord, the bot will respond to:
- `!guide` - Help information
- `!decrypt` + file attachment - Decrypt FXAP files
- `!status` - Bot status

**Your bot is now ready to decrypt FXAP files!** 🚀