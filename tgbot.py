import telebot
from telebot import types

bot = telebot.TeleBot('6883397009:AAE_zS_E1I8iTMuwu1AkHKXQMywJV-mZeQ0')



@bot.message_handler(commands=['start'])
def newChat(message):
    bot.send_message(message.chat.id,
                     f'Здравствуйте, с каким <b><u>социальным вопросом</u></b> вам необходимо помочь?',parse_mode='HTML')
    

@bot.message_handler(commands=['help'])
def helpCommand(message):
    bot.send_message(message.chat.id, f'Dvora может помочь вам с решением разного рода социальных вопросов.\n\n'
                                      f'Доступные команды:\n'
                                      f'start - начало работы с ботом\n'
                                      f'help - помощь по боту\n'
                                      f'spheres - сферы, с которыми работает бот\n\n'
                                      f'ИНСТРУКЦИЯ ПО ИСПОЛЬЗОВАНИЮ DVORA:\n'
                                      f'1) Введите свой социальный вопрос, с которым вам нужно помочь.'
                                      f'**Для более точного определения проблемы укажите ваш город и адрес(при необходимости)**\n\n'
                                      f'2) Dvora бот самостоятельно определит сферу и тему вашего обращения.\n\n'
                                      f'3) Далее, Drova отправит запрос в отделение, ответственное за решение данного вопроса.', parse_mode='HTML')
    

bot.infinity_polling()