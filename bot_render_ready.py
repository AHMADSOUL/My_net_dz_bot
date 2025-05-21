
import telebot
import requests

TOKEN = "7723535106:AAFfDvPr80ET6vhUXdIRX6nqCTPxXWiTEBk"
bot = telebot.TeleBot(TOKEN)

def get_network_info():
    try:
        response = requests.get("https://ipinfo.io/json")
        data = response.json()
        ip = data.get("ip", "غير معروف")
        country = data.get("country", "غير معروف")
        city = data.get("city", "غير معروف")
        org = data.get("org", "غير معروف")
        loc = data.get("loc", "غير متوفر")
        timezone = data.get("timezone", "غير متوفر")
        flag = f"https://flagsapi.com/{country}/flat/64.png"
        return {
            "ip": ip,
            "country": country,
            "city": city,
            "org": org,
            "loc": loc,
            "timezone": timezone,
            "flag": flag
        }
    except Exception:
        return None

@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        "مرحباً بك في بوت My Net Dz.\nأرسل /info لعرض معلومات الشبكة الخاصة بك."
    )

@bot.message_handler(commands=["info"])
def send_info(message):
    info = get_network_info()
    if info:
        text = (
            f"**معلومات الشبكة:**\n"
            f"`IP:` {info['ip']}\n"
            f"`الدولة:` {info['country']}\n"
            f"`المدينة:` {info['city']}\n"
            f"`مزود الخدمة:` {info['org']}\n"
            f"`الإحداثيات:` {info['loc']}\n"
            f"`المنطقة الزمنية:` {info['timezone']}"
        )
        bot.send_photo(message.chat.id, info['flag'], caption=text, parse_mode="Markdown")
    else:
        bot.send_message(message.chat.id, "تعذر جلب المعلومات، حاول مرة أخرى لاحقاً.")

print("البوت يعمل الآن...")
bot.polling()
