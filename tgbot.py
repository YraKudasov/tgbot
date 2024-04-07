import telebot
from telebot import types

bot = telebot.TeleBot('6883397009:AAE_zS_E1I8iTMuwu1AkHKXQMywJV-mZeQ0')

@bot.message_handler(commands=['start'])
def newChat(message):
    bot.send_message(message.chat.id,
                     f'Здравствуйте, <b>{message.from_user.first_name}</b>.\nС каким <b><u>социальным вопросом</u></b> вам необходимо помочь?',parse_mode='HTML')
    


@bot.callback_query_handler(func=lambda callback:True)
def callback_message(callback):
    if callback.data == 'sendToDepartment':
        bot.send_message(callback.message.chat.id, 'Ваш запрос успешно отправлен в ведомство!')
    

bot.infinity_polling()