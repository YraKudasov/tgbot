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
    elif callback.data == 'changeGroups':
        bot.send_message(callback.message.chat.id, 'Введите корректную группу тем:')
        bot.register_next_step_handler(callback.message, process_new_string)
    

@bot.message_handler(commands=['help'])
def helpCommand(message):
    bot.send_message(message.chat.id, f'<b>Dvora</b> может помочь вам с решением разного рода социальных вопросов.\n\n'
                                      f'<b>Доступные команды:</b>\n'
                                      f'/start - начало работы с ботом\n'
                                      f'/help - помощь по боту\n'
                                      f'/spheres - сферы, с которыми работает бот\n\n'
                                      f'<b>ИНСТРУКЦИЯ ПО ИСПОЛЬЗОВАНИЮ DVORA:</b>\n'
                                      f'1) Введите свой социальный вопрос, с которым вам нужно помочь.'
                                      f'**Для более точного определения проблемы укажите ваш <b>город</b> и <b>адрес</b>(при необходимости)**\n\n'
                                      f'2) Dvora бот самостоятельно определит сферу и тему вашего обращения.\n\n'
                                      f'3) Далее, Drova отправит запрос в отделение, ответственное за решение данного вопроса.', parse_mode='HTML')


@bot.message_handler()
def answerQuestion(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Все ключевые элементы выделены верно', callback_data='sendToDepartment')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('❌ Гр. тем', callback_data='changeGroups')
    btn3 = types.InlineKeyboardButton('❌ Тему', callback_data='changeTheme')
    btn4 = types.InlineKeyboardButton('❌ Исп. орг.', callback_data='changeDepartment')
    markup.row( btn2, btn3, btn4)
    
    

bot.infinity_polling()