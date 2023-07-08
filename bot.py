import telebot
import random

from telebot import types

bot = telebot.TeleBot("6103692090:AAH-Ipt7ps35J64UPrQTwOkA38RAgOxaJqA")

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('telegrambot/sticker.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('help')
    item2 = types.KeyboardButton("что делаешь?")

    markup.add(item1, item2)
    bot.send_message(message.chat.id, f"Ку, {message.from_user.first_name}!".format(message.from_user, bot.get_me()),parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('telegrambot/musik.mp3', 'rb')
    bot.send_sticker(message.chat.id, sti)

@bot.message_handler(commands=['joke'])
def welcome(message):
    bot.send_message(message.chat.id, "Стоят в поле два барана. Один говорит беее, а другой говорит блат тоже самое сказать хотел")


# @bot.message_handler(commands=['sticker'])
# def send_welcome(messege):
    # stiq = open('png')

# @bot.message_handler(content_types=['text'])
# def welcome(message):
#     if message.text.lower() == "что делаешь?":
#         bot.send_message(message.chat.id, 'Наблюдаю за тем трешем что происходит у вас в чате...')
#     elif message.text == "ты что то хотел?":
#         bot.send_message(message.chat.id, 'нет')

@bot.message_handler(content_types=['text'])
def welcome(message):
    if message.text.lower() == "привет":
        bot.send_message(message.chat.id, 'ку, ты что то хотел/a?')
    elif message.text == "нет":
        bot.send_message(message.chat.id, 'ок')
    elif message.text == "как дела?":
        bot.send_message(message.chat.id, "я всеголишь бот по этому у меня нет чувс.. бла бла бла, я не такой бот как все и дела у меня норм")
    elif message.text == "что делаешь?":
        bot.send_message(message.chat.id, "ничего, ну может только смотрю что в чате пишут, а если меня нету в вашей группе то просто в афк")
    elif message.text == "мне скучно":
        bot.send_message(message.chat.id, 'и шо?')
    elif message.text == "ну развесели меня":
        bot.send_message(message.chat.id, 'хм, ладно. Сидел мальчик на стуле, упал и сломал все 6 ножек')
    elif message.text == "хаха":
        bot.send_message(message.chat.id, 'ну вот и развеселил тебя, а теперь проваливай я в фортнайт играю')
    elif message.text == "расскажи мне шутку":
        bot.send_message(message.chat.id, 'На распродаже органов началась драка, я еле успел унести ноги')
    elif message.text == "дальше":
        bot.send_message(message.chat.id, 'Знаете почему в Африке ночью нет людей? потому что их не видно')
    elif message.text == "ещё":
        bot.send_message(message.chat.id, 'Знаете какие шутки нельзя говорить безногим? Сногшибательные')
    elif message.text == "го поговорим?":
        bot.send_message(message.chat.id, 'го, о чём поговоррить хочешь?')
    elif message.text == "о погоде например":
        bot.send_message(message.chat.id, 'нуууу я хз какая сейчас погода')
    elif message.text == "о фортнайте":
        bot.send_message(message.chat.id, 'о чём именно?')
    elif message.text == "какой у тебя уровень бп?":
        bot.send_message(message.chat.id, '82 вроде')
    elif message.text == "/help":
        bot.send_message(message.chat.id, 'Вот слова на кикие бот может отвечать:  привет; как дела?;что делаешь?; нет; мне скучно; ну развесели меня; хаха; расскажи мне шутку; дальше; ещё; го поговорим?; о погоде например; о фортнайте; какой у тебя уровень бп?. Да некоторые слова могут показаться странными но я не смог придумать что то лучше что бы бот писал другие шутки только на одно слово')




























bot.polling(none_stop=True)