import datetime

from aiogram import Bot, types  #подключение библиотеки для работы с telegram
from aiogram.bot import api
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from db import Create_database, Verification, Join #подключение модулей
from telegramcalendar import create_calendar
from config import BOT_TOKEN

bot = Bot(token = BOT_TOKEN)
dp = Dispatcher(bot)

Create_database()

@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    user_id = message.from_user.id  #считывание id
    if Verification(user_id) == True:
        await bot.send_message(message.chat.id, 'Привет, мы с тобой уже работали раньше.\nВаши записи сохранины.')
    else:
        if message.from_user.first_name != 'None': #проверка наличия имеи, фамилии и юзернейма
            name = message.from_user.first_name
        elif message.from_user.username != 'None':
            name = message.from_user.username
        elif message.from_user.last_name != 'None':
            name = message.from_user.last_name
        else:
            name = ''
        Join(user_id, name)
        await bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIEqF5VL5ozeLnmwSaOJAbKQDQAAfidjQACYwkAAgk7OxMAAVFVxKRh8u0YBA')
        await bot.send_message(message.chat.id, 'Этот бот нужен для создания заметок.\nОн может хранить ваши заметки и отправлять вам напоминания.\nДля работы с ним не нужна дополнительная авторизация(только аккуаунт в telegram), вы можете проверять записи и получать уведомления.\nЧтобы глубже ознакомиться с функционалом нажмите на /commands')
    #some_func_message_to_start_job

@dp.message_handler(commands=['calendar'])
async def get_calendar(message):
    now = datetime.datetime.now() #Текущая дата
    chat_id = message.chat.id
    date = (now.year,now.month)
    #current_shown_dates = {}
    #current_shown_dates[chat_id] = date #Сохраним текущую дату в словарь
    keyboard = create_calendar(now.year,now.month)
    await bot.send_message(message.chat.id, "Пожалйста, выберите дату", reply_markup=keyboard)
    print('5*****\n')
    #bot.answer_callback_query(call.id, text="Дата выбрана")

#@dp.message_handler(commands=['creat'])

@dp.message_handler(commands=['choose'])
async def choose(message: types.Message): 
    await bot.send_message(message.chat.id, 'выберите день\n')

@dp.message_handler(commands=['days'])
async def days(message: types.Message): 
    await bot.send_message(message.chat.id, 'выберите день\n')

@dp.message_handler(commands=['today'])
async def today(message: types.Message): 
    await bot.send_message(message.chat.id, 'список день на сегодня\n\n')

@dp.message_handler(commands=['thisweek'])
async def thisweek(message: types.Message): 
    await bot.send_message(message.chat.id, 'расписание на эту неделю: ')

@dp.message_handler(commands=['settings'])
async def settings(message: types.Message): 
    await bot.send_message(message.chat.id, 'Вы можете изменить любую информацию о себе')

@dp.message_handler(commands=['commands'])
async def list_commands(message: types.Message):
    await bot.send_message(message.chat.id,
            'полный список команд, на которые отвечает бот\n\n'
            '/days - просмотр записей на сегодня\n'
            '/thisweek - просмотр  записей на неделю\n'
            '/settings - настройки, которые вы можете посмотерть и изменить\n'
            '/info - информация о боте\n'
            '/contacts - информация о создателях и код программы\n')

@dp.message_handler(commands=['info'])
async def info(message: types.Message):
    await bot.send_message(message.chat.id, '[О боте]\nЭто приложение создано для планирования дел. Здесь вы можете создать своё расписание и добавлять новые заметки. В установленное время вам будет приходить уведомление.\nТакже код проекта доступен на Github')

@dp.message_handler(commands=['contacts'])
async def contacts(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    url_button = types.InlineKeyboardButton(text="Перейти на GitHub", url="https://github.com/DONSIMON92/bot-organizer")
    keyboard.add(url_button)
    await bot.send_message(message.chat.id, 'Проект доступен на GitHub', reply_markup=keyboard)

if __name__ == '__main__':  #зацикливание бота
    executor.start_polling(dp)
