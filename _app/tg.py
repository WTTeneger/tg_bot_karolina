from _app import *
from _app import bot
from _app import buttons





def met(message):
    print('message - ', message.text)








@bot.message_handler(commands=['start', 'text', 'm'])
def send_welcome(message):
    print(f'command, {message.text}')
    pul = bot.send_message(message.from_user.id, 'Напиши что то',  reply_markup=None)
    bot.register_next_step_handler(message, met)


@bot.callback_query_handler(func=lambda call: True)
def Select_list_type_work(call):
    print('callBack') #При нажатие на inline_button


@bot.message_handler(content_types=['text', 'stikers'])
def main_main(message):
    print('Просто написали боту')
    print(message)
    pul = bot.send_message(message.from_user.id, 'Вот тут текст!',  reply_markup=None) #Пишет сообщение пользователю