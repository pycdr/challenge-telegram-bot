from json import load, dump
from os.path import exists
from threading import Timer

"""
data.json:
{
	channel_username: {
		challenge_id (defined by its message id): [
			{
				"from_user_id": <int>,
				"from_user_username": <str>,
				"message_id": <int>,
				"pasted_link": <str>
			},
			...
		],
		...
	},
	...
}
"""

"""
texts.json:
{
	"group": {
		"message_type_and_name": {
			"admin": <str>,
			"user": <user>	
		}
	},
	"private":{ ... }
}
"""

class DataController:
	def __init__(self):
		"""
		controles (saves / updates / removes) all data used in the bot.
		all data will be saved in data.json file!"""
		if exists("data.json"):
			self.data = load(open("data.json", 'r'))
		else:
			with open("data.json", 'w') as f: dump({}, f) # creates a json file.
			self.data = {}
		
		if exists("texts.json"):
			self.texts = load(open("texts.json", 'r'))
		else:
			with open("texts.json", 'w') as f: dump({}, f) # creates a json file.
			self.texts = {}
		
		self.thread1 = Timer(10, self.auto_save)
		self.thread1.run()
		self.thread2 = Timer(10, self.auto_load)
		self.thread2.run()
		
	
	def auto_save(self):
		with open("data.json", 'w') as f:
			dump(self.data, f)
	
	def auto_load(self):
		self.texts = open("texts.json", 'r').read()
	
	def update(self, group_id: int, key: str, new_value: str) -> bool:
		self.data[group_id][key] = new_value
		
	def get(self, group_id: int, key: str) -> str:
		return self.data[group_id][key]
	
	def __del__(self):
		self.thread1.cancel()
		self.thread2.cancel()
