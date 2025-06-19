import os
import json
import random
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.middlewares.logging import LoggingMiddleware

API_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

# База
try:
    with open('data.json', 'r') as f:
        db = json.load(f)
except:
    db = {"users": {}, "tasks": {}, "task_id": 0}

def save_db():
    with open('data.json', 'w') as f:
        json.dump(db, f, indent=2)

@dp.message_handler(commands=["start"])
async def start(msg: types.Message):
    uid = str(msg.from_user.id)
    ref = msg.get_args()
    if uid not in db["users"]:
        db["users"][uid] = {"points": 3, "tasks": [], "refs": [], "done": []}
        if random.random() < 0.5:
            db["users"][uid]["points"] += 5
            await msg.reply("Добро пожаловать! Вам начислено 3 поинта и бонус 5 поинтов 🎁")
        else:
            await msg.reply("Добро пожаловать! Вам начислено 3 поинта 🎉")
        if ref and ref in db["users"] and uid not in db["users"][ref]["refs"]:
            db["users"][ref]["points"] += 5
            db["users"][ref]["refs"].append(uid)
            await bot.send_message(ref, f"🎉 Новый реферал! +5 поинтов.")
    else:
        await msg.reply("Вы уже зарегистрированы!")
    save_db()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
