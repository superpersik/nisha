import telebot
from config import token_api
from telebot import TeleBot
import random

bot: TeleBot = telebot.TeleBot(token_api)
admin2 = 556641119
users = {}
REQUEST_CONTACT, GET_CONTACT = range(2)

questions1 = ['Возможно вам подойдут: \n<b>Зонт в машину от солнца</b>. Средний оборот карточки 25 т.р. '
              '\n<b>Прописи для дошкольников</b>. Средний оборот карточки 30 т.р. \n<b>Утяжелители 2 кг.</b> '
              'Средний оборот карточки 50 т.р.\n<b>Перчатки строительные</b>. Средний оборот карточки 60 т.р.'
              '\n<b>Бумажные полотенца</b>. Средний оборот карточки 70т.р.', 'Возможно вам подойдут:'
              '\n<b>Мангал складной</b>. Средний оборот карточки 70 т.р.\n<b>Чехол для удочек</b>. Средний оборот '
              'карточки 73 т.р.\n<b>Лампа ультрафиолетовая</b>. Средний оборот карточки 75 т.р.\n<b>Набор сушеных '
              'овощей</b>. Средний оборот карточки 75 т.р.\n<b>Фотосетка</b>. Средний оборот карточки 75 т.р.',
              'Возможно вам подойдут: \n<b>Дворники автомобильные</b>. Средний оборот карточки 90 т.р. '
              '\n<b>Ароматизатор в машину</b>. Средний оборот карточки 95 т.р.\n<b>Сапоги для охоты и рыбалки</b>. '
              'Средний оборот карточки 99 т.р.']
questions5 = ['Возможно вам подойдут: \n<b>Ящик для рассады</b>. Средний оборот карточки 110 т.р. '
              '\n<b>Нитки мулине</b>. Средний оборот карточки 110 т.р. \n<b>Чехлы на сидения.</b> '
              'Средний оборот карточки 110 т.р.\n<b>Книги по кулинарии</b>. Средний оборот карточки 115 т.р.'
              '\n<b>Спальный мешок +15</b>. Средний оборот карточки 125 т.р.',
              'Возможно вам подойдут:\n<b>Вазы</b>. Средний оборот карточки 150 т.р.\n<b>Спиннинг</b>. Средний оборот '
              'карточки 200 т.р.\n<b>Кухонная утварь</b>. Средний оборот карточки 250 т.р.\n<b>Power bank 20000</b>. '
              'Средний оборот карточки 275 т.р.\n<b>Тряпка из микрофибры</b>. Средний оборот карточки 285 т.р.']
questions2 = ['Возможно вам подойдут: \n<b>Мусс для волос</b>. Средний оборот карточки 305 т.р. '
              '\n<b>Конструктор</b>. Средний оборот карточки 315 т.р. \n<b>Грунт для рассады.</b> '
              'Средний оборот карточки 350 т.р.\n<b>Сорочка женская</b>. Средний оборот карточки 495 т.р.'
              '\n<b>Коврики прикроватные</b>. Средний оборот карточки 300 т.р.',
              'Возможно вам подойдут:'
              '\n<b>Тушь для ресниц</b>. Средний оборот карточки 495 т.р.\n<b>Палатка двухместная</b>. '
              'Средний оборот карточки 350 т.р.\n<b>Полироль для пластика</b>. Средний оборот карточки 350 т.р.'
              '\n<b>Гантели для фитнеса</b>. Средний оборот карточки 400 т.р.\n<b>Лампа настольная.</b>. Средний оборот'
              ' карточки 450 т.р.\n<b>Молды для шоколада</b>. Средний оборот карточки 450 т.р.\n<b>Заколки для '
              'волос</b>. Средний оборот карточки 490 т.р.']
questions3 = ['Возможно вам подойдут: \n<b>Коллаген порошковый</b>. Средний оборот карточки 515 т.р. '
              '\n<b>Костюм охотника</b>. Средний оборот карточки 550 т.р. \n<b>Постельное белье.</b> '
              'Средний оборот карточки 570 т.р.\n<b>Доска разделочная</b>. Средний оборот карточки 500 т.р. '
              '\n<b>Сланцы</b>. Средний оборот карточки 510 т.р.',
              'Возможно вам подойдут:'
              '\n<b>Джемпер мужской</b>. Средний оборот карточки 650 т.р.\n<b>Набор специй</b>. Средний оборот '
              'карточки 750 т.р.\n<b>ОМЕГА 3 капсулы</b>. Средний оборот карточки 850 т.р.\n<b>Тумбочка '
              'прикроватная</b>. '
              'Средний оборот карточки 750 т.р.\n<b>Пижама женская</b>. Средний оборот карточки 815 т.р.',
              'Возможно вам подойдут: \n<b>Халат домашний</b>. Средний оборот карточки 870 т.р. '
              '\n<b>Контейнер для еды</b>. Средний оборот карточки 905 т.р.\n<b>Обувница сборная</b>. '
              'Средний оборот карточки 950 т.р.']
questions4 = ['Возможно вам подойдут: \n<b>Рашгард</b>. Средний оборот карточки 1,1 млн. '
              '\n<b>Смартфон</b>. Средний оборот карточки 1,2 млн. \n<b>Кроссовки.</b> '
              'Средний оборот карточки 1,2 млн.\n<b>Ортопедические подушки</b>. Средний оборот карточки 1,2 млн. '
              '\n<b>Носки</b>. Средний оборот карточки 1,3 млн.',
              'Возможно вам подойдут:'
              '\n<b>Парфюмерия для дома</b>. Средний оборот карточки 1,4 млн.\n<b>Махровые полотенца</b>. '
              'Средний оборот '
              'карточки 1,5 млн.\n<b>Костюм спортивный</b>. Средний оборот карточки 1,5 млн.\n<b>Боди женское</b>. '
              'Средний оборот карточки 1,7 млн.',
              'Возможно вам подойдут: \n<b>Бюстгалтер</b>. Средний оборот карточки 2 млн. '
              '\n<b>Подгузники</b>. Средний оборот карточки 2,3 млн.\n<b>Платье женское</b>. '
              'Средний оборот карточки 2,8 млн.\n<b>Футболка мужская</b>. Средний оборот карточки 3,7 млн.']


@bot.message_handler(commands=['start'])
def welcome(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Приветствуем 😉 \nЭтот бот создан специально, чтобы помочь начинающим селлерам '
                              'при выборе ниши или конкретного товара для продаж.\nПеред началом '
                              'введите своё имя:')
    users[chat_id] = {}
    bot.register_next_step_handler(message, first)


def first(message):
    chat_id = message.chat.id
    name = message.text
    users[chat_id]['name'] = name
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    zero = telebot.types.KeyboardButton(text='Ноль - никогда не пробовал')
    medium = telebot.types.KeyboardButton(text='Средний - что-то где-то пробовал продавать')
    high = telebot.types.KeyboardButton(text='Высокий - есть опыт продаж')
    keyboard.add(zero)
    keyboard.add(medium)
    keyboard.add(high)
    bot.send_message(chat_id, text='Ваш уровень знаний в продажах?', reply_markup=keyboard)
    bot.register_next_step_handler(message, twostep)


def twostep(message):
    chat_id = message.chat.id
    q1 = message.text
    users[chat_id]['q1'] = q1
    keyboard = telebot.types.ReplyKeyboardRemove()
    bot.send_message(chat_id, 'Выберите сферы, в которых у Вас хорошие знания: \n1. Дом / хозяйство. '
                              '\n2. Дети / воспитание. \n3. Саморазвитие / процессы образования. \n4. Интерьер / '
                              'эргономика пространства. \n5. Стиль / мода.	\n6. Макияж / уход за собой.'
                              '\n7. Спорт / тренировки.	\n8. ЗОЖ / здоровое питание.\n9. Диетология / нутрициология	'
                              '\n10. Хобби / рукоделие.\n11. Кулинария.\n12. Строительство / ремонт.'
                              '\n13. Техника / Электроника.\n14. Авто/ машины.\n15. Музыка / аудиосистемы.\n'
                              '16.Охота / рыбалка.\n17. Туризм.\n18. Сад / огород.\nСвой вариант.',
                     reply_markup=keyboard)
    bot.register_next_step_handler(message, thirdstep)


def thirdstep(message):
    chat_id = message.chat.id
    q2 = message.text
    users[chat_id]['q2'] = q2
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    hour1 = telebot.types.KeyboardButton(text='1-2 часа')
    hour2 = telebot.types.KeyboardButton(text='2-3 часа')
    hour3 = telebot.types.KeyboardButton(text='4-6 часов')
    hour4 = telebot.types.KeyboardButton(text='Весь день')
    keyboard.add(hour1, hour2, hour3, hour4)
    bot.send_message(chat_id, text='Сколько времени готовы уделять работе на маркетплейсах?', reply_markup=keyboard)
    bot.register_next_step_handler(message, fourt)


def fourt(message):
    chat_id = message.chat.id
    q3 = message.text
    users[chat_id]['q3'] = q3
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    no = telebot.types.KeyboardButton(text='Нет - никогда не пробовали.')
    yes = telebot.types.KeyboardButton(text='Да – есть вариант прямых контактов с производствами.')
    maybe = telebot.types.KeyboardButton(text='Возможно – могу найти.')
    keyboard.add(no)
    keyboard.add(yes)
    keyboard.add(maybe)
    bot.send_message(chat_id, text='Есть ли контакты с производствами или поставщиками?', reply_markup=keyboard)
    bot.register_next_step_handler(message, fivestep)


def fivestep(message):
    chat_id = message.chat.id
    q4 = message.text
    users[chat_id]['q4'] = q4
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn100k = telebot.types.KeyboardButton(text='до 100 000')
    btn300k = telebot.types.KeyboardButton(text='до 300 000')
    btn500k = telebot.types.KeyboardButton(text='до 500 000')
    btn1ml = telebot.types.KeyboardButton(text='до 1 млн')
    btn1mll = telebot.types.KeyboardButton(text='свыше 1 млн')
    keyboard.add(btn100k, btn300k, btn500k, btn1ml, btn1mll)
    bot.send_message(chat_id, 'Выберите бюджет для старта:', reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text == 'до 100 000')
def result100(message):
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardRemove()
    q5 = message.text
    users[chat_id]['q5'] = q5
    bot.send_message(chat_id, text=random.choice(questions1), parse_mode='html', reply_markup=keyboard)
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    tel = telebot.types.KeyboardButton(text='Отправить номер', request_contact=True)
    keyboard.add(tel)
    bot.send_message(chat_id, text='Если вам нужна консультация нашего специалиста по подбору идеальной ниши для '
                                   'заработка, оставьте свои контакты.', reply_markup=keyboard)
    bot.register_next_step_handler(message, mersi4)


@bot.message_handler(func=lambda message: message.text == 'до 300 000')
def result300(message):
    chat_id = message.chat.id
    q5 = message.text
    keyboard = telebot.types.ReplyKeyboardRemove()
    users[chat_id]['q5'] = q5
    bot.send_message(chat_id, text=random.choice(questions5), parse_mode='html', reply_markup=keyboard)
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    tel = telebot.types.KeyboardButton(text='Отправить номер', request_contact=True)
    keyboard.add(tel)
    bot.send_message(chat_id, text='Если вам нужна консультация нашего специалиста по подбору идеальной ниши для '
                                   'заработка, оставьте свои контакты.', reply_markup=keyboard)
    bot.register_next_step_handler(message, mersi4)


@bot.message_handler(func=lambda message: message.text == 'до 500 000')
def result500(message):
    chat_id = message.chat.id
    q5 = message.text
    keyboard = telebot.types.ReplyKeyboardRemove()
    users[chat_id]['q5'] = q5
    bot.send_message(chat_id, text=random.choice(questions2), parse_mode='html', reply_markup=keyboard)
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    tel = telebot.types.KeyboardButton(text='Отправить номер', request_contact=True)
    keyboard.add(tel)
    bot.send_message(chat_id, text='Если вам нужна консультация нашего специалиста по подбору идеальной ниши для '
                                   'заработка, оставьте свои контакты.', reply_markup=keyboard)
    bot.register_next_step_handler(message, mersi4)


@bot.message_handler(func=lambda message: message.text == 'до 1 млн')
def result1mln(message):
    chat_id = message.chat.id
    q5 = message.text
    keyboard = telebot.types.ReplyKeyboardRemove()
    users[chat_id]['q5'] = q5
    bot.send_message(chat_id, text=random.choice(questions3), parse_mode='html', reply_markup=keyboard)
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    tel = telebot.types.KeyboardButton(text='Отправить номер', request_contact=True)
    keyboard.add(tel)
    bot.send_message(chat_id, text='Если вам нужна консультация нашего специалиста по подбору идеальной ниши для '
                                   'заработка, оставьте свои контакты.', reply_markup=keyboard)
    bot.register_next_step_handler(message, mersi4)


@bot.message_handler(func=lambda message: message.text == 'свыше 1 млн')
def result1mln(message):
    chat_id = message.chat.id
    q5 = message.text
    keyboard = telebot.types.ReplyKeyboardRemove()
    users[chat_id]['q5'] = q5
    bot.send_message(chat_id, text=random.choice(questions4), parse_mode='html', reply_markup=keyboard)
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    tel = telebot.types.KeyboardButton(text='Отправить номер', request_contact=True)
    keyboard.add(tel)
    bot.send_message(chat_id, text='Если вам нужна консультация нашего специалиста по подбору идеальной ниши для '
                                   'заработка, оставьте свои контакты.', reply_markup=keyboard)
    bot.register_next_step_handler(message, mersi4)


def mersi4(message):
    chat_id = message.chat.id
    keyboard = telebot.types.ReplyKeyboardRemove()
    contact = message.text or message.contact.phone_number
    users[chat_id]['contact'] = contact
    name = users[chat_id]['name']
    q1 = users[chat_id]['q1']
    q2 = users[chat_id]['q2']
    q3 = users[chat_id]['q3']
    q4 = users[chat_id]['q4']
    q5 = users[chat_id]['q5']
    bot.send_message(chat_id, text='Спасибо!\nНаши менеджеры скоро свяжутся с Вами.')
    bot.send_message(admin2, f'Новая заявка\nИмя: {name}\nВопрос 1: {q1}\nВопрос 2: {q2}\nВопрос 3: {q3}\n'
                             f'Вопрос 4: {q4}\nВопрос 5: {q5}\n{contact}', reply_markup=keyboard)

    bot.register_next_step_handler(message, echo_all)


@bot.message_handler(content_types=['text'])
def echo_all(message):
    bot.reply_to(message, message.text)


bot.polling(none_stop=True)
