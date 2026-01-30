import os

# Configuration for Obsidian
# USER: Please replace this path with your actual Obsidian Vault path
# Example: r"C:\Users\Lee\Documents\Obsidian Vault"
OBSIDIAN_VAULT_PATH = r"C:/Path/To/Your/Obsidian/Vault" 

# Daily note folder relative to vault root. Leave empty if daily notes are at root.
# Example: "Daily Notes" or "Journal/2024"
DAILY_NOTE_FOLDER = "01. Daily"

# Format for the daily note filename
# Default Obsidian format is often YYYY-MM-DD
DAILY_NOTE_FORMAT = "%Y-%m-%d.md"

# Server Configuration
HOST = "0.0.0.0"
PORT = 5000

# Telegram Configuration
# Get this from BotFather
TELEGRAM_TOKEN = "YOUR_TELEGRAM_BOT_TOKEN_HERE"
