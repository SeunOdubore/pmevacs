# bots/telegram_bot.py
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
import requests

TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

def start(update: Update, context: CallbackContext):
    keyboard = [[InlineKeyboardButton("Take Quiz", callback_data='quiz')],
                [InlineKeyboardButton("Check Status", callback_data='check')],
                [InlineKeyboardButton("Refer Friends", callback_data='refer')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("🌟 Welcome to *VoteBoost NG*!\nEarn badges & airtime for voting.", reply_markup=reply_markup, parse_mode='Markdown')

def button_click(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    if query.data == 'quiz':
        query.edit_message_text("🧠 Quiz: A) Jobs B) Education C) Security")
    elif query.data == 'check':
        query.edit_message_text("📞 Enter PVC number.")
    elif query.data == 'refer':
        ref_link = f"https://t.me/VoteBoostBot?start={query.from_user.id}"
        query.edit_message_text(f"📤 Share: {ref_link} \nGet 50MB per friend!")

updater = Updater(TOKEN)
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(button_click))
updater.start_polling()
updater.idle()