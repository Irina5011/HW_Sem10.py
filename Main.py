from telegram import Update, Bot, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler, ConversationHandler
from TASK import *
from Token import TOKEN

bot = Bot(token=TOKEN)
updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher

conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],
        states={
            CHOICE: [MessageHandler(Filters.regex('^(Человек|Умный компьютер|Не очень умный компьютер)$'), message)],
        },
        # точка выхода из игры
        fallbacks=[CommandHandler('cancel', cancel)],
    )

message_handler = MessageHandler(Filters.text, game)

dispatcher.add_handler(conv_handler)
dispatcher.add_handler(message_handler)

# Запуск бота
print("Программа запущена!")
updater.start_polling()