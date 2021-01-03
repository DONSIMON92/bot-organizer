import datetime
import re

from aiogram import Bot, types  # подключение библиотеки для работы с telegram
# from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# from aiogram.bot import api
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from db import Create_database, Verification, Join  # подключение модулей
#from telegramcalendar import create_calendar
from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

Create_database()


@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    user_id = message.from_user.id  # считывание id
    if Verification(user_id):
        await bot.send_message(message.chat.id, 'Привет, мы с тобой уже работали раньше.\nВаши записи сохранины.')
    else:
        if message.from_user.first_name != 'None':  # проверка наличия имеи, фамилии и юзернейма
            name = message.from_user.first_name
        elif message.from_user.username != 'None':
            name = message.from_user.username
        elif message.from_user.last_name != 'None':
            name = message.from_user.last_name
        else:
            name = ''
        Join(user_id, name)
        await bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIEqF5VL5ozeLnmwSaOJAbKQDQAAfidjQACYwkAAgk7OxMAAVFVxKRh8u0YBA')
        await bot.send_message(message.chat.id, 'Этот бот нужен для создания заметок.\n'
                                                'Он может хранить ваши заметки и отправлять вам напоминания.\n'
                                                'Для работы с ним не нужна дополнительная авторизация,\n'
                                                'Вы можете проверять записи и получать уведомления.\n'
                                                'Чтобы глубже ознакомиться с функционалом нажмите на /commands')

    await bot.send_message(message.chat.id, 'жду твоего сообщения 🕐')
    #first = datetime.datetime.now().time()
    #await bot.edit_message_text(chat_id=message.chat.id, message_id=message.message_id, text='жду твоего сообщения 🕑')

    #keyboard = types.InlineKeyboardMarkup()
    #button1 = types.InlineKeyboardButton(text='Да', callback_data='да')
    #button2 = types.InlineKeyboardButton(text='Нет', callback_data='нет')
    #keyboard.add(button1, button2)
    #await bot.send_message(message.chat.id, 'Хотите добавить заметку?', reply_markup=keyboard)


@dp.message_handler(content_types=['text'])
async def get_info(message: types.Message):
    pattern_date = r'\d{2}-\d{2}-\d{4}'
    pattern_today = r'сегодня'                      # date
    pattern_tomorrow = r'завтра'
    pattern_day_after_tomorrow = r'послезавтра'
    pattern_time = r' час'                          # hour
    when = re.findall(pattern, string)
    await bot.send_message(message.chat.id, 'Ё')
    

@dp.message_handler(content_types=['photo'])
async def get_photo(message: types.Message):
    await bot.send_message(message.chat.id, 'КРАСОТА 😍😍😍')


@dp.callback_query_handler(lambda call: True)
async def callback_inline(call):
    if call.data == 'да':
        bot.edit_message_text(inline_message_id=call.inline_message_id,
                              text='Выберите, как часто будет приходить уведомление')
    elif call.data == 'нет':
        bot.edit_message_text(inline_message_id=call.inline_message_id,
                              text='Хорошо, когда захотите добавить заметку можете отправить команду - /add')


@dp.message_handler(commands=['calendar'])
async def get_calendar(message):
    now = datetime.datetime.now()   # Текущая дата
    print(datetime.datetime.now())
    chat_id = message.chat.id
    date = (now.year, now.month)
    # current_shown_dates = {}
    # current_shown_dates[chat_id] = date #Сохраним текущую дату в словарь
    keyboard = create_calendar(now.year, now.month)
    await bot.send_message(message.chat.id, 'Пожалуйста, выберите дату', reply_markup=keyboard)
    print('5*****\n')
    # bot.answer_callback_query(call.id, text='Дата выбрана')


@dp.message_handler(commands=['today'])
async def today(message: types.Message):
    await bot.send_message(message.chat.id, 'список день на сегодня\n\n')


@dp.message_handler(commands=['commands'])
async def list_commands(message: types.Message):
    await bot.send_message(message.chat.id,
                           'полный список команд, на которые отвечает бот:\n\n'
                           '/add - добавить новую запись\n'
                           '/info - информация о боте\n'
                           '/contacts - информация о создателях и код программы\n')


@dp.message_handler(commands=['info'])
async def give_info(message: types.Message):
    await bot.send_message(message.chat.id, '[О боте]\nЭто приложение создано для планирования дел.'
                                            'Здесь вы можете создать своё расписание и добавлять новые заметки.'
                                            'В установленное время вам будет приходить уведомление.\n'
                                            'Также код проекта доступен на Github')


@dp.message_handler(commands=['contacts'])
async def contacts(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text='Перейти на GitHub', url='https://github.com/DONSIMON92/bot-organizer')
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, 'Проект доступен на GitHub', reply_markup=keyboard)

if __name__ == '__main__':  # зацикливание бота
    executor.start_polling(dp)
