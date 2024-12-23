


# 0 Домашнее Задание
# - Включить запись log в файл
# - Бот принимает кириллицу отдаёт латиницу в соответствии с Приказом МИД по транслитерации
# - Бот работает из-под docker контейнера


# 1 Импорт библиотек
import logging
import os
import regex as re

from aiogram import Bot, Dispatcher
from aiogram.types import Message             # ловим все обновления этого типа 
from aiogram.filters.command import Command   # обрабатываем команды /start, /help и другие



#2 Инициализация объектов
TOKEN = os.getenv('TOKEN')
bot = Bot(token=TOKEN) # Создаем бота
dp = Dispatcher()                       # Создаем объект диспетчера. 
# Все хэндлеры(обработчики) должны быть подключены к диспетчеру
logging.basicConfig(level=logging.INFO, filename = "bot700logfile.log") # включение логгирования




#3 Обработка команды старт
@dp.message(Command(commands=['start']))
async def proccess_command_start(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Привет, {user_name}! Вы запустили бота по преобразованию имен из кирилицы в латиницу.'
    logging.info(f'User:{user_name} id:{user_id} запустил бота')
    await bot.send_message(chat_id=user_id, text=text)


#6 функции обработки сообщений
BUKVAR = {
'А' : 'A', 
'Б' : 'B',
'В' : 'V', 
'Г' : 'G', 
'Д' : 'D', 
'Е' : 'E',
'Ё' : 'E',
'Ж' : 'ZH',
'З' : 'Z',
'И' : 'I',
'Й' : 'I',
'К' : 'K',
'Л' : 'L',
'М' : 'M',
'Н' : 'N',
'О' : 'O',
'П' : 'P',
'Р' : 'R',
'С' : 'S',
'Т' : 'T',
'У' : 'U',
'Ф' : 'F',
'Х' : 'KH',
'Ц' : 'TS',
'Ч' : 'CH',
'Ш' : 'SH',
'Щ' : 'SHCH',
'Ы' : 'Y',
'Ъ' : 'IE',
'Э' : 'E',
'Ю' : 'IU',
'Я' : 'IA',
' ' : ' '
}

def cyr_Latin_2113(cyr_in : str):
    pattern_cyr = re.compile('^[а-яА-Я ]+$')    
    if re.search(pattern_cyr, cyr_in):
        return ''.join([BUKVAR[x] for x in cyr_in.upper()]).lower().title()
    else:        
        return 'Строка содержит несоответствующие имени символы!'
    

#4 Обработка всех сообщений
@dp.message()
async def send_echo(message: Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = cyr_Latin_2113(message.text)
    logging.info(f'User:{user_name} id:{user_id}: отправил сообщение: {text}')
    await message.answer(text=text)


#5 Запуск процесса пуллинга
if __name__ == '__main__':
    dp.run_polling(bot)


