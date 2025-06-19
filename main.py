import json
import random
from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InputFile
from aiogram.dispatcher.filters import Command
from aiogram.contrib.middlewares.logging import LoggingMiddleware

API_TOKEN = '7716896917:AAEBy9IR-wXNx1FfZsI9fsieZO5H1bAFUQQ'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

# Загрузка данных
try:
    with open('data.json', 'r') as f:
        db = json.load(f)
except:
    db = {"users": {}, "tasks": {}, "task_id": 0}

def save_db():
    with open('data.json', 'w') as f:
        json.dump(db, f, indent=2)
