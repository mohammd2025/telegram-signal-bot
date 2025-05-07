import telebot
import schedule
import time

bot = telebot.TeleBot("7999555179:AAGcBlEENm4TiBQjvAMbUKeDZtTiib0Fq_s")
chat_id = "@kahwat_almassryeen_reb7k_3lena"

def send_signal_3pm():
    bot.send_message(chat_id, "إشارة تداول DOGE/USDT - الساعة 3:00 مساءً\nالصفقة تبدأ الآن وتنتهي بعد 5 دقائق.")

def send_signal_8pm():
    bot.send_message(chat_id, "إشارة تداول DOGE/USDT - الساعة 8:00 مساءً\nالصفقة تبدأ الآن وتنتهي بعد 5 دقائق.")

schedule.every().day.at("15:00").do(send_signal_3pm)
schedule.every().day.at("20:00").do(send_signal_8pm)

while True:
    try:
        schedule.run_pending()
        time.sleep(1)
    except Exception as e:
        print("Error:", e)
        time.sleep(10)