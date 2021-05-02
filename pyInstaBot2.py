from instabot import Bot
bot = Bot()

# Login
username = "Your User Name"
password = "Your Password"
bot.login(username = username, password = password)

# Follow
acc = "Account Name"
bot.follow(acc)

# Send messages (DMs)
msg = 'Enter Your Msg Here'
rc = ['Receiver1', 'Receiver2']
bot.send_message(msg, rc)