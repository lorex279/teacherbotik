import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def hello_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("С Днём учителя ❤️")

def main():
    token = os.environ.get("8295260673:AAFRUzDSo5bN955Wo_zQNmkdHFq_1GryOVs")
    if not token:
        print("Ошибка: переменная окружения TELEGRAM_BOT_TOKEN не задана.")
        return

    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("hello", hello_command))
    print("Бот запущен!")
    app.run_polling()

if __name__ == "__main__":
    main()
