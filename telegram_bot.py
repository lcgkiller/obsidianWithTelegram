import logging
import re
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from config import TELEGRAM_TOKEN
from obsidian_manager import add_todo_to_daily_note

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Sends a welcome message."""
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="안녕하세요! Obsidian Todo 봇입니다.\n'ㅌㄷ: 할일' 또는 'td: 할일' 형식으로 보내주시면 Obsidian 데일리 노트에 추가합니다."
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Handles text messages and checks for todo commands."""
    if not update.message or not update.message.text:
        return

    msg = update.message.text.strip()
    
    # Check for todo patterns:
    # 1. Starts with /todo
    # 2. Starts with /ㅌㄷ
    # 3. Starts with ㅌㄷ (with optional colon)
    # 4. Starts with td (with optional colon)
    
    todo_text = None
    
    # Regex to capture content after the command prefix
    # Supports:
    # /todo buy milk
    # ㅌㄷ buy milk
    # ㅌㄷ: buy milk
    # td: buy milk
    match = re.match(r'(?:/todo|/ㅌㄷ|ㅌㄷ|td)[:\s]?\s*(.*)', msg, re.IGNORECASE)
    
    if match and match.group(1):
        todo_text = match.group(1).strip()
    elif msg.startswith("/"):
         # Ignored other commands
         return
    else:
        # Optional: treat ALL non-command messages as todos? 
        # For now, let's Stick to explicit commands to avoid clutter, 
        # BUT the user might want convenience. Let's stick to the requested "ㅌㄷ" pattern for safety first.
        return

    if todo_text:
        success, result = add_todo_to_daily_note(todo_text)
        if success:
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=f"✅ 추가됨: {todo_text}"
            )
        else:
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=f"❌ 실패: {result}"
            )

if __name__ == '__main__':
    if not TELEGRAM_TOKEN:
        print("Error: TELEGRAM_TOKEN is missing in config.py")
    else:
        print("Starting Telegram Bot...")
        application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
        
        start_handler = CommandHandler('start', start)
        # Handle all text messages that are not commands (or custom parsing)
        msg_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message)
        # Also handle standard commands if user types /todo explicitly
        # But our regex logic in handle_message covers it if we just route everything there?
        # Let's route everything to handle_message effectively for flexible parsing
        
        application.add_handler(start_handler)
        application.add_handler(MessageHandler(filters.TEXT, handle_message))
        
        application.run_polling()
