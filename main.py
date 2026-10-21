from aiogram import Bot, Dispatcher
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from dotenv import load_dotenv 
from service import *
from connection import *
import asyncio
import os
import random
from datetime import *


load_dotenv()

token = os.getenv("BOT_TOKEN")

bot = Bot(token=token)
dp = Dispatcher()



@dp.message(CommandStart())
async def start_bot(message: Message):
    if await  get_user_by_id(message.from_user.id):
        await message.answer(f"""
Hello, @{message.from_user.username} 👋"
Welcome back to the bot."
Use /help to see all commands.
""")        
    else:
        user = message.from_user
        print(f"{message.full_name} send Start")
        await create_user(user.username, user.full_name, user.id)
        await message.answer(f"Hello @{message.from_user.username}")






@dp.message(Command("help"))
async def help(message: Message):
    await message.answer(f"""
🆘 HELP MENU

/start - Start the bot
/help - Show this help menu
/my_info - View your account information
/about - About this bot
/date - Show today's date
/python - Get a Python tip
/joke - Get a joke
/get_all_user - Show registered users

Have a great day! 😊

                        (●'◡'●)

""")

        

@dp.message(Command("my_info"))
async def info(message: Message):
    await message.answer(f"""Your username: @{message.from_user.username}
Your fullname: {message.from_user.full_name}
Your Id: {message.from_user.id}
Day: {datetime.now().strftime('%d.%m.%Y')}
""")




@dp.message(Command("get_all_user"))
async def help(message: Message):
    users = await get_user()
    for user in users:
        await message.answer(f"""
Username: @{user['username']}  
Full name: {user['full_name']}
                             """) 







@dp.message(Command("date"))
async def date(message: Message):
    await message.answer(f""""
📅 Today's date: {datetime.now().strftime('%d.%m.%Y')}\n"
🕒 Time: {datetime.now().strftime('%H:%M:%S')}"
    """)



@dp.message(Command("joke"))
async def joke(message: Message):
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs! 🐛",
        "Why was the Python programmer calm? Because they knew how to handle exceptions! 😄",
        "Why did the developer go broke? Because they used up all their cache! 😂",
        "Why do programmers love Python? Because life is better with fewer brackets! 🐍"
    ]

    await message.answer(f"😂 HERE IS YOUR JOKE  @{message.from_user.username} \n" + random.choice(jokes))


@dp.message(Command("python"))
async def python_tip(message: Message):
    tips = [
        "Use functions to organize reusable code.",
        "Lists store multiple items in one variable.",
        "Dictionaries store data as key-value pairs.",
        "Use try and except to handle errors.",
        "Modules help you organize your Python code.",
        "Use meaningful variable names to make code readable.",
        "Learn Git to track changes in your projects."
    ]

    await message.answer("🐍 PYTHON TIP\n" + random.choice(tips))


@dp.message(Command("about"))
async def about(message: Message):
    await message.answer("""
🤖 ABOUT THIS BOT

Welcome to my Telegram bot!

This bot can show your profile information,
give you Python tips, share ideas and jokes,
and help you explore its commands.

Use /help to see all available commands.
""")



async def main():
    await create_table()
    print("Bot started")
    await dp.start_polling(bot)
    
    
    
if __name__ == "__main__":
    asyncio.run(main())





