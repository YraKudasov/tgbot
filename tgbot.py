import telebot
from telebot import types

bot = telebot.TeleBot('6883397009:AAE_zS_E1I8iTMuwu1AkHKXQMywJV-mZeQ0')

@bot.message_handler(commands=['start'])
def newChat(message):
    bot.send_message(message.chat.id,
                     f'Здравствуйте, <b>{message.from_user.first_name}</b>.\nС каким <b><u>социальным вопросом</u></b> вам необходимо помочь?',parse_mode='HTML')
    

@bot.message_handler(commands=['spheres'])
def spheresCommand(message):
    bot.send_message(message.chat.id, f'Сферы, в которых бот может вам помочь:\n\n'
                                      f'Безопасность\n'
                                      f'Благоустройство\n'
                                      f'Газ и топливо\n'
                                      f'Благоустройство\n'
                                      f'Государственная собственность\n'
                                      f'Дороги\n'
                                      f'ЖКХ\n'
                                      f'Здравоохранение/Медицина\n'
                                      f'Коронавирус\n'
                                      f'Культура\n'
                                      f'МФЦ/Мои документы\n'
                                      f'Мобилизация\n'
                                      f'Мусор/Свалки/ТКО\n'
                                      f'Образование\n', parse_mode='HTML')
    

bot.infinity_polling()