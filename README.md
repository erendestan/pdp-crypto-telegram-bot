# pdp-crypto-telegram-bot
Eren Destan - 1ACS
This is a Bot for Telegram that is getting live information about 10 different cryptocurrencies (BTC, ETH, BNB, XRP, LTC, BCH, ADA, DOT, LINK, XLM)
The live informations that you can get are like this:
	-Name of the Coin
	-Current Price
	-Daily Change Percentage
	-Hourly Change Percentage

If you want to get message about all these datas, you need to use '/status' command on your linked Telegram Bot.
Telegram Bot can only send message while Python file is running, so if you want to reach these information in everytime,
you need to host that script on somewhere. 
For example, I have used Google Cloud Console. I have SSHed the Debian Machine and used tmux to make it still function while
SSH window is closed.

Remark: There is two different files, bot.py is for only getting information with '/status' command,
telegram_bot.py is for getting information with '/status' command and automatic message about all these
informations hourly. I'm hosting the bot.py file.

Eren Destan - 1ACS