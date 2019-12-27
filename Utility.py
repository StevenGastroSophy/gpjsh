import os

class Config:
	def __init__(self):
		pass

	@staticmethod
	def getFromEnv(key):
		return os.getenv(key, None)

	def getFromJson(self):
		pass

def isAuthenticated(data):
	role = {
		"apiKey": Config.getFromEnv("apiKey")
	}	
	isAuth = all([True if data.get(key) == role.get(key) else False for key in role])
	
	return isAuth
