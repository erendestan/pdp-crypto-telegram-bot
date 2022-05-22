#All the Imports
from telegram.ext import Updater
from telegram.ext import CommandHandler
from tracker import get_prices
from tracker import send_message
import time
from datetime import datetime

#Telegram Bot Token and Chat Id of My Bot
telegram_bot_token = "your-own-telegram-bot-token"
chat_id = "your-own-chat-id"

#Time Setter for every hour message (60seconds*60minutes)
time_interval = 60*60

#Set the Telegram Bot
updater = Updater(token=telegram_bot_token, use_context=True)
dispatcher = updater.dispatcher

#Function to send message via /status command
def start(update, context):
    chat_id = update.effective_chat.id
    message = ""

    crypto_data = get_prices()
    for i in crypto_data:
        coin = crypto_data[i]["coin"]
        price = crypto_data[i]["price"]
        change_day = crypto_data[i]["change_day"]
        change_hour = crypto_data[i]["change_hour"]
        message += f"Coin: {coin}\nPrice: ${price:,.2f}\nHour Change: {change_hour:.3f}%\nDay Change: {change_day:.3f}%\n\n"

    context.bot.send_message(chat_id=chat_id, text=message)
    dispatcher.add_handler(CommandHandler("status", start)) #Accessed by /status
    updater.start_polling()


#Function to send message in every 1 hour
def main():
    message = ''
    while True:
        crypto_data = get_prices()
        #Getting the current time for message
        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        for i in crypto_data:
            coin = crypto_data[i]["coin"]
            price = crypto_data[i]["price"]
            change_day = crypto_data[i]["change_day"]
            change_hour = crypto_data[i]["change_hour"]
            message += f"Coin: {coin}\nPrice: ${price:,.2f}\nHour Change: {change_hour:.3f}%\nDay Change: {change_day:.3f}%\n\n"

        #waits 60 minutes before sending the first message
        time.sleep(time_interval)
        send_message(chat_id=chat_id, msg=f'Current Date and Time is {dt_string} \n Hourly Automatic Message: \n {message}')

if __name__ == '__main__':
    print("Running the script")
    main()




