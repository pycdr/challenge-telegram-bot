import telebot
from data import DataController
from threading import Thread
from time import sleep

class Bot:
	def __init__(self, token: str):
		"""telegram bot handler class"""
		self.bot = telebot.TeleBot(token)
		self.dc = DataController()
		
	def init(self):
		@self.bot.message_handler(commands = ["start"])
		def start(message):
			# using `self.dc.texts['command_start']`
			# '/start code' starts a submitation for a challenge
			# 'code' = 'channel_username' + '-' + 'challenge_message_id' 
			pass
		
		@self.bot.message_handler(commands = ["edit"]):
			# using `self.dc.texts['command_edit']`
			# '/edit code' edits a sent answer
			# 'code' = 'channel_username' + '-' + 'challenge_message_id'
			# it will show a keyboard markup to show answers
			pass
		
		@self.bot.message_handler(commands = ["delete"]):
			# using `self.dc.texts['command_delete']`
			# '/delete code' edits a sent answer
			# 'code' = 'channel_username' + '-' + 'challenge_message_id'
			# it will show a keyboard markup to show answers
			pass
		
	def start(self):
		self.init()
		self.bot.polling()
