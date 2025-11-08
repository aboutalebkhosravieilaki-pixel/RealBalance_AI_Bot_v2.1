# ===============================================================
# RealBalance_AI_Bot v2.1
# Author: Khosravi & GapGPT
# Description: Telegram Bot with Hybrid AI Response System
# ===============================================================

import telebot
import json
import threading
import logging
from datetime import datetime
from ai_core import HybridAI

# ---------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------
with open("config.json", "r", encoding="utf-8") as cfg_file:
    config = json.load(cfg_file)

TOKEN = config.get("TELEGRAM_TOKEN")
MODE = config.get("MODE", "production")

bot = telebot.TeleBot(TOKEN)
ai_engine = HybridAI()

# ---------------------------------------------------------------
# Logging Setup
# ---------------------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)

# ---------------------------------------------------------------
# Helper Functions
# ---------------------------------------------------------------
def log_user_message(message):
    user = message.from_user
    username = f"@{user.username}" if user.username else "NoUsername"
    logging.info(f"Message from {username} ({user.id}): {message.text}")

def handle_ai_response(message):
    try:
        response = ai_engine.process(message.text)
        bot.reply_to(message, response)
    except Exception as e:
        logging.error(f"AI Engine Error: {str(e)}")
        bot.reply_to(message, "⚠️ خطایی در پردازش درخواست پیش آمد.")

# ---------------------------------------------------------------
# Telegram Bot Handlers
# ---------------------------------------------------------------
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    msg = (
        "👋 سلام! من ربات RealBalance_AI_Bot هستم.\n"
        "پیامت رو بفرست تا تحلیلی بر اساس هوش‌ مصنوعی دریافت کنی."
    )
    bot.reply_to(message, msg)

@bot.message_handler(func=lambda msg: True)
def main_handler(message):
    log_user_message(message)
    threading.Thread(target=handle_ai_response, args=(message,)).start()

# ---------------------------------------------------------------
# Run Mode
# ---------------------------------------------------------------
if __name__ == '__main__':
    logging.info("🤖 RealBalance_AI_Bot_v2.1 is running...")
    if MODE == "production":
        bot.infinity_polling(timeout=10, long_polling_timeout=5)
    else:
        bot.polling()
       
