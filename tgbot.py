import telebot
from telebot import types

bot = telebot.TeleBot('6883397009:AAE_zS_E1I8iTMuwu1AkHKXQMywJV-mZeQ0')

@bot.message_handler(commands=['start'])
def newChat(message):
    bot.send_message(message.chat.id,
                     f'Здравствуйте, <b>{message.from_user.first_name}</b>.\nС каким <b><u>социальным вопросом</u></b> вам необходимо помочь?',parse_mode='HTML')
    

@bot.message_handler(commands=['spheres'])
def spheresCommand(message):
    bot.send_message(message.chat.id, f'<b>Сферы, в которых бот может вам помочь:</b>\n\n'
                                      f'<em>Безопасность</em>\n'
                                      f'<em>Благоустройство</em>\n'
                                      f'<em>Газ и топливо</em>\n'
                                      f'<em>Благоустройство</em>\n'
                                      f'<em>Государственная собственность</em>\n'
                                      f'<em>Дороги</em>\n'
                                      f'<em>ЖКХ</em>\n'
                                      f'<em>Здравоохранение/Медицина</em>\n'
                                      f'<em>Коронавирус</em>\n'
                                      f'<em>Культура</em>\n'
                                      f'<em>МФЦ/Мои документы</em>\n'
                                      f'<em>Мобилизация</em>\n'
                                      f'<em>Мусор/Свалки/ТКО</em>\n'
                                      f'<em>Образование</em>\n', parse_mode='HTML')
    

bot.infinity_polling()