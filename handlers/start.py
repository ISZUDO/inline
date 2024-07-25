from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.types.chat_member import ChatMember
from aiogram.filters import Command, CommandStart
from keyboards.inline import menu
from loader import bot

start_router: Router = Router()

@start_router.message(CommandStart())
async def start_handler(msg:Message):
    await msg.answer("""Salom! Hamster Kombatga xush kelibsiz 🐹 Bundan buyon 
siz kripto birja direktorisiz. Qaysi birini tanlaysiz? O'zingiz hal qiling. Ekranni bosing, 
tangalarni to'plang, passiv daromad oling, o'z daromad strategiyangizni ishlab chiqing. 
Biz, o'z navbatida, tangalaringizni listing davomida baholaymiz, uning sanalarini tez orada bilib olasiz. 
Do'stlaringiz haqida ham unutmang. Ularni o'yinga taklif qiling va birgalikda yanada ko'proq tangalar oling!""", reply_markup=menu)

@start_router.message(F.data=='Qanday daromad olish mumkin?')
async def keyboard(quary:CallbackQuery):
    await bot.send_message(chat_id=quary.from_user.id, text="""Как играть в Hamster Kombat ⚡️
  
Полная версия гайда. (https://hamster-kombat.notion.site/Hamster-Kombat-b14906aba45243c58c9f634ce1b38d1e)

💰 Tap to earn
Тапай по экрану и собирай монеты 

⛏ Mine
Прокачивай карточки, которые дадут возможность пассивного дохода.

⏰ Прибыль в час
Биржа будет работать для тебя самостоятельно, даже когда ты не в игре в течение 3х часов. 
Далее нужно будет перезайти в игру снова. 

📈 LVL
Чем больше монет у тебя на балансе — тем выше уровень биржи. Чем выше уровень — тем быстрее сможешь зарабатывать ещё больше монет 

👥 Friends
Приглашай своих друзей, и вы получите бонусы. Помоги другу перейти в следующие лиги, и вы получите ещё больше бонусов.

🪙 Token listing
По итогам сезона будет выпущен токен, который будет распределен между игроками. 
Даты сообщим в нашем анонс-канале. Следите за новостями!

/help чтобы получить этот гайд""")