import telebot
from telebot import types

# BotFather'dan olingan tokenni shu yerga joylashtiring
TOKEN = '8837281818:AAFHPYq0uub0SkBzi8k9akRSGM7qdxOkQV8'
bot = telebot.TeleBot(TOKEN)

# Netlify'dagi loyihangiz manzili
WEB_APP_URL = "https://cozy-gelato-2487b2.netlify.app/"

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    
    # 1. Netlify veb-ilovani Telegram ichida ochuvchi asosiy tugma
    btn_webapp = types.KeyboardButton(
        text="🌐 Veb-ilovaga kirish", 
        web_app=types.WebAppInfo(url=WEB_APP_URL)
    )
    
    # Qolgan 4 ta yordamchi tugma
    btn2 = types.KeyboardButton("🛒 Xizmatlar")
    btn3 = types.KeyboardButton("👤 Mening profilim")
    btn4 = types.KeyboardButton("ℹ️ Biz haqimizda")
    btn5 = types.KeyboardButton("📞 Yordam / Aloqa")
    
    # Tugmalarni tartib bilan joylashtiramiz
    # Asosiy Veb-ilova tugmasini eng tepaga alohida qo'yamiz
    markup.add(btn_webapp)
    markup.add(btn2, btn3)
    markup.add(btn4, btn5)
    
    ism = message.from_user.first_name
    greeting_text = (
        f"Assalomu alaykum, {ism}! 🌟\n\n"
        f"Mening shaxsiy loyihamga xush kelibsiz! Men sizga yordam berishdan "
        f"va sifatli xizmat ko'rsatishdan doim xursandman.\n\n"
        f"👇 Pastdagi **«🌐 Veb-ilovaga kirish»** tugmasini bosib, xizmatlardan foydalanishingiz mumkin:"
    )
    
    bot.send_message(message.chat.id, greeting_text, reply_markup=markup, parse_mode="Markdown")

@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    chat_id = message.chat.id
    
    if message.text == "🛒 Xizmatlar":
        bot.send_message(chat_id, "Hozircha xizmatlar bo'limi ishlab chiqilmoqda 🛠. Barcha xizmatlarni veb-ilovamiz orqali ko'rishingiz mumkin!")
        
    elif message.text == "👤 Mening profilim":
        bot.send_message(chat_id, f"Sizning Telegram ID raqamingiz: `{message.from_user.id}`\n\nBu sizning shaxsiy kabinetingiz.", parse_mode="Markdown")
        
    elif message.text == "ℹ️ Biz haqimizda":
        bot.send_message(chat_id, "Biz yosh va innovatsion jamoamiz! Maqsadimiz — insonlarga foydasi tegadigan raqamli mahsulotlar yaratish. ✨")
        
    elif message.text == "📞 Yordam / Aloqa":
        bot.send_message(chat_id, "Savollaringiz bormi yoki takliflaringiz bo'lsa, bemalol adminga yozishingiz mumkin!")
        
    else:
        bot.send_message(chat_id, "Kechirasiz, men bu buyruqni tushunmadim. Iltimos, menyudagi tugmalardan foydalaning.")

if __name__ == '__main__':
    print("Bot muvaffaqiyatli ishga tushdi...")
    bot.polling(none_stop=True)

