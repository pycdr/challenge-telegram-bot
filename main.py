import argarse
from libs.bot import Bot

if __name__ == __main__: # runs the main program!
	# get bot token
	parser = argparse.ArgumentParser()
	parser.add_argument("token", type = str)
	args = parser.parse_args()
	token: str = args.token
	
	# start bot
	bot = Bot(token)
	bot.start()
