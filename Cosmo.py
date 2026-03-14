import telebot

TOKEN = "8705425632:AAGzwBgzY7hUcr6K9wOwcfcRk5haB_AcxFI"
bot = telebot.TeleBot(TOKEN)

score = 0
step = 0

@bot.message_handler(commands=['start'])
def start(message):
    global store, step
    score = 0
    step = 1
    bot.send_message(message.chat.id,
                     "Вопрс 1: Какая планета красная?")
    
@bot.message_handler(func=lambda message: True)
def quiz(message):
    global step, score

    if step == 1:
        if message.text.lower() == "марс":
            score += 1
        score = 2
        bot.send_message(message.chat.id,
                         "Вопрос 2: Самая большая планета?")
    elif step == 2:
        if message.text.lower() == "юпитер":
            score += 1
        score = 3
        bot.send_message(message.chat.id,
                         "Вопрос 2: Самая маленькая паланета?")
        
    elif step == 3:
        if message.text.lower() == "меркурий":
            score += 1
        
        bot.send_message(message.chat.id,
                         f"Ваш счёт: {score}")        

bot.infinity_polling()