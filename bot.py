import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, CallbackQueryHandler

# Configuration - Using your test token directly
BOT_TOKEN = "7601703546:AAFzqvYp6EIDnKkRe-FQ_yO_rL2c6Ir0x2E"  # Will be revoked later
CHANNEL_USERNAME = "@yourchannel"  # Change this to your actual channel
GROUP_USERNAME = "@yourgroup"      # Change this to your actual group
TWITTER_USERNAME = "@yourtwitter"  # Change this to your actual Twitter

def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    welcome_message = (
        f"Hello {user.first_name}! 🎉\n\n"
        "Welcome to our Airdrop Bot! Complete these simple steps to qualify:\n\n"
        "1. Join our Telegram Channel\n"
        "2. Join our Telegram Group\n"
        "3. Follow us on Twitter\n"
        "4. Submit your SOL wallet address\n\n"
        "Click the button below to proceed!"
    )
    
    keyboard = [
        [InlineKeyboardButton("Start Airdrop Process", callback_data='start_airdrop')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    update.message.reply_text(welcome_message, reply_markup=reply_markup)

def button_handler(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    
    if query.data == 'start_airdrop':
        airdrop_steps(query)

def airdrop_steps(query) -> None:
    steps_message = (
        "🚀 Airdrop Steps:\n\n"
        f"1. Join our Telegram Channel: {CHANNEL_USERNAME}\n"
        f"2. Join our Telegram Group: {GROUP_USERNAME}\n"
        f"3. Follow us on Twitter: {TWITTER_USERNAME}\n\n"
        "After completing these steps, please send your SOL wallet address."
    )
    
    query.edit_message_text(text=steps_message)

def handle_wallet(update: Update, context: CallbackContext) -> None:
    wallet_address = update.message.text
    
    # Very basic SOL address validation (just checks length)
    if len(wallet_address) >= 32 and len(wallet_address) <= 44:
        success_message = (
            "🎉 Congratulations!\n\n"
            "10 SOL is on its way to your wallet!\n\n"
            "Note: Tokens will be distributed after the airdrop ends."
        )
        update.message.reply_text(success_message)
    else:
        update.message.reply_text("Please enter a valid SOL wallet address.")

def main() -> None:
    updater = Updater(BOT_TOKEN)
    dispatcher = updater.dispatcher

    # Handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CallbackQueryHandler(button_handler))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_wallet))

    # Start the Bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
