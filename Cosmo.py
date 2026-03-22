import telebot
from telebot import types

TOKEN = "8705425632:AAGzwBgzY7hUcr6K9wOwcfcRk5haB_AcxFI"
bot = telebot.TeleBot(TOKEN)

# База вопросов: вопрос, варианты ответов и индекс правильного (от 0)
QUIZ_DATA = [
    {"q": "Какая планета называется Красной?", "a": ["Венера", "Марс", "Юпитер"], "correct": 1, "img": "AgACAgIAAxkBAAOgab-tJFRtyZ9r0xf9H0VifBD2zegAAgYXaxvG-flJg1qoCaKqQOoBAAMCAAN5AAM6BA"},
    {"q": "Самая большая планета системы?", "a": ["Сатурн", "Нептун", "Юпитер"], "correct": 2, "img": "AgACAgIAAxkBAAOwab-wgrxKyXhNS8BoUBIG7GBhj18AAhAXaxvG-flJEhPlCu-yx6cBAAMCAAN5AAM6BA"},
    {"q": "Первый человек в космосе?", "a": ["Армстронг", "Гагарин", "Леонов"], "correct": 1, "img": "AgACAgIAAxkBAAO_ab-xip0dLw0VaYReZpGLwSVVoocAAlUSaxtsAAEBSsKOkM6KhuxTAQADAgADeQADOgQ"},
    {"q": "Ближайшая к Земле звезда?", "a": ["Сириус", "Солнце", "Проксима Центавра"], "correct": 1, "img": "AgACAgIAAxkBAAPPab-yI084Qr-ewIqiBdVaK8EqEIAAAlcSaxtsAAEBSsWXTQ6pFh-5AQADAgADeQADOgQ"},
    {"q": "Естественный спутник Земли?", "a": ["Луна", "Ио", "Европа"], "correct": 0, "img": "AgACAgIAAxkBAAPRab-yQ-xgyi-tGR0kC5tSZCEu6PYAAl4SaxtsAAEBSs7e0f8eIuBNAQADAgADeQADOgQ"},
    {"q": "Какую звезду упоминал кеша из Мими-мишек?", "a": ["Сириус", "Солнце", "Проксима Центавра"], "correct": 2, "img": "AgACAgIAAxkBAAPTab-yaoTrkORA_3Fbp1Kzbh-4sC4AAscSaxtsAAEBSl60k5QvZHf3AQADAgADeQADOgQ"},
    {"q": "Какая планета самая горячая ♨😏?", "a": ["Венера", "Марс", "Юпитер"], "correct": 0, "img": "AgACAgIAAxkBAAPVab-yv1OfVdr6XPXjUCAwiNYn28QAAtASaxtsAAEBShMyip7azOLBAQADAgADeQADOgQ"},
    {"q": "Какое неофициальное название получил первый искусственный спутник Земли из-за своей формы?", "a": ["Серебряный шар", "Простейший спутник (ПС-1)", "Звездный бипер"], "correct": 1, "img": "AgACAgIAAxkBAAPXab-1Kndu9Xh6XQABZuwbwMN3F5w1AAJhEmsbbAABAUpNZ4WkyNqgNgEAAwIAA3kAAzoE"},
    {"q": "Что, согласно традиции, смотрят космонавты на Байконуре перед каждым стартом?", "a": ["Солярис", "Белое солнце пустыни", "Интерстеллар"], "correct": 1, "img": "AgACAgIAAxkBAAPbab-2DQQWnwp3D2LdcaIHVtqUGV0AAmgSaxtsAAEBSvSX1y7whjutAQADAgADeQADOgQ"},
    {"q": "Как звали двух собак, которые первыми успешно вернулись с орбиты (не путать с Лайкой)?", "a": ["Стрелка и Уголек", "Белка и Стрелка", "Дезик и Цыган"],"correct": 1, "img": "AgACAgIAAxkBAAPZab-1zhKyVd7kh2pfIiUf1RrZvv0AAmsSaxtsAAEBSjq5ahAlOrCWAQADAgADeQADOgQ"},
    {"q": "В каком городе СНГ находится самый первый и крупнейший в мире космодром?", "a": ["Королёв", "Байконур", "Плесецк"],"correct": 1, "img": "AgACAgIAAxkBAAPdab-2Oyu4dGDeYg1ARNeppxImCncAAm0SaxtsAAEBSgctiQ8QAAEh2AEAAwIAA3kAAzoE"},
    {"q": "Какую фразу произнес Юрий Гагарин во время старта ракеты «Восток-1»?", "a": ["Полетели!", "В добрый путь!", "Поехали!"], "correct": 2, "img": "AgACAgIAAxkBAAPfab-2a0KoBXPcOnvhribuWCQzdAYAAm4SaxtsAAEBSih4SroxkJNkAQADAgADeQADOgQ"},
    {"q": "Как называлась советская космическая станция, которая была 'нашим общим домом' на орбите 15 лет?", "a": ["Салют", "Мир", "Союз"], "correct": 1, "img": "AgACAgIAAxkBAAPkab-3Omku4ubkdw8nVvXV4htdtNoAAnASaxtsAAEBSr8KXf1qRtPYAQADAgADeQADOgQ"},
    {"q": "Какой музыкальный инструмент считается 'космическим' и на нем играют, не касаясь его руками?", "a": ["Терменвокс", "Ханг", "Синтезатор АНС"], "correct": 0, "img": "AgACAgIAAxkBAAPmab-4NVcHekqMQSEp6SKTiUtiwCgAAnoSaxtsAAEBSsqZBdEz-fJzAQADAgADeQADOgQ"},
    {"q": "Как космонавты называют процесс возвращения на Землю из-за перегрузок?", "a": ["Мягкая посадка", "Вход в пекло", "Спуск по баллистике"], "correct": 2, "img": "AgACAgIAAxkBAAIBKGnAH3OCc2S19GdQLluvg7siHRKAAALCF2sbDj8BSrNNzPH9Tl1wAQADAgADeQADOgQ"},
    {"q": "Какое небесное тело в СНГ часто называют 'Стожарами'?", "a": ["Пояс Ориона", "Плеяды", "Большую Медведицу"], "correct": 1, "img": "AgACAgIAAxkBAAPqacAU3h6lxTEQjJgCiWg0ebSPYKwAAogSaxtsAAEBSig7rKNfTTtsAQADAgADeQADOgQ"},
    {"q": "Кто из советских космонавтов первым в истории вышел в открытый безвоздушный космос?", "a": ["Герман Титов", "Алексей Леонов", "Валентина Терешкова"], "correct": 1, "img": "AgACAgIAAxkBAAPsacAVR7qrS3EY7wnurfzqYpJev_YAAqQSaxtsAAEBShNZhkSLlcqAAQADAgADeQADOgQ"},
    {"q": "Как назывался первый в мире луноход, успешно работавший на поверхности Луны более 300 суток?", "a": ["Лунный трактор", "Луноход-1", "Аппарат Селена"], "correct": 1, "img": "AgACAgIAAxkBAAPuacAVZJU9Jp-3wNt6T5kXAX_ggOsAArASaxtsAAEBSr8yEr3XpqU2AQADAgADeQADOgQ"},
    {"q": "Какой позывной был у первой женщины-космонавта Валентины Терешковой?", "a": ["Береза", "Синица", "Чайка"], "correct": 2, "img": "AgACAgIAAxkBAAPyacAVybDYv_EZ98UPKQAB8Sc1hZ4BAAKyEmsbbAABAUrXpj6chlLbzQEAAwIAA3cAAzoE"},
    {"q": "Как называется точка в космосе, из которой невозможно вернуться даже свету?", "a": ["Гравитационный колодец", "Горизонт событий", "Точка невозврата"], "correct": 1, "img": "AgACAgIAAxkBAAP4acAXmP0-R7JM_aTohn868e6iMtYAArkSaxtsAAEBSh5Qon_3zzZbAQADAgADeQADOgQ"},
    {"q": "В каком фантастическом фильме СНГ прозвучала фраза «Планета, где я родился, называется Земля, кадет»?", "a": ["Через тернии к звездам", "Москва-Кассиопея", "Отроки во Вселенной"], "correct": 0, "img": "AgACAgIAAxkBAAP2acAXIMYTUFM3Xxoa_cRODutkf_AAArcSaxtsAAEBSmLsckRVp9JHAQADAgADeAADOgQ"},
    {"q": "Что находится в центре нашей Галактики (Млечного Пути)?", "a": ["Гигантская звезда", "Сверхмассивная черная дыра", "Белый карлик"], "correct": 1, "img": "AgACAgIAAxkBAAP0acAW4BtjY0xpfG9beASKnFqaiYcAArQSaxtsAAEBSv3dAQABoJaq8QEAAwIAA3kAAzoE"}
    
]

user_states = {}

def get_quiz_markup(step):
    """Создает кнопки для текущего вопроса"""
    markup = types.InlineKeyboardMarkup()
    options = QUIZ_DATA[step]["a"]
    for i, option in enumerate(options):
        # В callback_data передаем индекс нажатой кнопки
        callback_data = f"ans_{i}"
        markup.add(types.InlineKeyboardButton(text=option, callback_data=callback_data))
    return markup

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    user_states[chat_id] = {'score': 0, 'step': 0}
    # Отправляем приветственное сообщение с нашей главной картинкой из презентации
    bot.send_photo(chat_id, "AgACAgIAAxkBAAIBA2nAHA-F9OemFl5uU-Eb4tirWqc0AAKxF2sbDj8BSnTNQd5HAdtFAQADAgADdwADOgQ", caption="🚀 Подключение к системе «Горизонт»... Начинаем миссию!")
    
    send_question(chat_id)

def send_question(chat_id):
    step = user_states[chat_id]['step']
    if step < len(QUIZ_DATA):
        question = QUIZ_DATA[step]
        question_text = f"✨ Вопрос {step + 1}/{len(QUIZ_DATA)}:\n\n{QUIZ_DATA[step]['q']}"

        # 2. Используем send_photo вместо send_message
        # caption — это текст под картинкой
        bot.send_photo(
            chat_id, 
            photo=question['img'], 
            caption=question_text, 
            reply_markup=get_quiz_markup(step)
        )
    else:
        finish_quiz(chat_id)

@bot.callback_query_handler(func=lambda call: call.data.startswith('ans_'))
def handle_answer(call):
    chat_id = call.message.chat.id
    if chat_id not in user_states:
        return

    # Извлекаем индекс ответа из callback_data
    selected_index = int(call.data.split('_')[1])
    state = user_states[chat_id]
    current_step = state['step']

    # Проверка правильности
    if selected_index == QUIZ_DATA[current_step]['correct']:
        state['score'] += 1

    # Переход к следующему вопросу
    state['step'] += 1
    
    # 3. При работе с фото edit_message_text не сработает для текста под фото.
    # Используем edit_message_caption, чтобы убрать кнопки и обновить статус.
    try:
        bot.edit_message_caption(
            chat_id=chat_id,
            message_id=call.message.message_id,
            caption=f"✅ Ответ на вопрос №{current_step + 1} принят бортовым компьютером."
        )
    except:
        pass # На случай, если сообщение нельзя отредактировать
    
    send_question(chat_id)

def finish_quiz(chat_id):
    score = user_states[chat_id]['score']
    total = len(QUIZ_DATA)
    
    # Финальный вайб
    result_text = f"📡 Миссия завершена!\n\nВаш результат: **{score}** из **{total}**.\n"
    if score == total:
        result_text += "🚀 Вы — настоящий адмирал звездного флота!"
    elif score > total / 2:
        result_text += "👨‍🚀 Хороший результат, кадет."
    else:
        result_text += "🛰 Похоже, стоит изучить карты в библиотеке."

    bot.send_message(chat_id, result_text, parse_mode="Markdown")
    del user_states[chat_id]

@bot.message_handler(content_types=['photo'])
def get_file_id(message):
    # Берем самую качественную версию фото [-1] и выводим её ID
    print(f"ID картинки: {message.photo[-1].file_id}")
    bot.reply_to(message, "ID этой картинки выведен в консоль!")

@bot.message_handler(commands=['ps'])
def developer_info(message):
    chat_id = message.chat.id
    
    # Текст плашки о тебе
    info_text = (
        "<b>📂 ДОСЬЕ РАЗРАБОТЧИКА СИСТЕМЫ</b>\n"
        "------------------------------------\n"
        "<b>Status:</b> Lead Engineer / Creator\n"
        "<b>Codename:</b> Богдан \n"
        "<b>Mission:</b> Создание иммерсивных интерфейсов\n"
        "------------------------------------\n"
        "<i>«Космос — это не предел, это только начало».</i>\n\n"
        "🛰 <b>Связь с центром управления:</b> @Why_Are_You_Slow\n"
        "Вы можете отправить отчет об ошибке или предложение по модернизации системы."
        "------------------------------------"
        "PS: \n"
        "Мой ТГ-канал, где будут новости об обновлениях и других моих проектов: @Lingway_TM \n"
        "У меня есть страничка на GitHub, где я выкладываю свои проекты и делюсь знаниями по программированию и космосу. Если вам интересно, можете заглянуть: https://github.com/Lingway-TM/Cosmo \n\n"
        "📡 Система «Горизонт» разработана с использованием Python и библиотеки pyTelegramBotAPI. Все права защищены © 2026"
    )

    # Можно отправить просто текстом, но лучше прикрепить ту самую картинку
    # которую мы делали в начале (иллюминатор), чтобы сохранить стиль.
    bot.send_photo(chat_id, "AgACAgIAAxkBAAIBtmnAKz5FTShYkJgtVOWbqoboGCGNAAIFGGsbDj8BSnMzWvHnXCJqAQADAgADeAADOgQ", caption=info_text, parse_mode="HTML")

bot.infinity_polling()
