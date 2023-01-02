import logging
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler,filters
from Engine import bot as bt

bot_token = open("API_telegram.txt", "r").read()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

#Start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("start command working...")

    await update.message.reply_text("I'm a bot, please talk to me!")


async def chatgpt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("chatgpt working...")

    uinput = str(update.message.text)
    chatgptreply = bt(uinput)
    await update.message.reply_text(chatgptreply)


def main() -> None:
    """Run the Bot"""
    application = ApplicationBuilder().token(bot_token).build()
    
    start_handler = CommandHandler('start', start)
    messageChatgpt = MessageHandler(filters.ALL , chatgpt)

    application.add_handler(start_handler)
    application.add_handler(messageChatgpt)
    
    application.run_polling()

if __name__ == '__main__':
    main()