import requests
from Utility import Config

class ShtmlTopMenuPC:
	def __init__(self):
		url = "https://{}"
		prodFile = Config.getFromEnv("prodFile")
		uatFile = Config.getFromEnv("uatFile")

		self.prodUrl = url.format(prodFile)
		self.uatUrl = url.format(uatFile)

	def queryFromProd(self):
		url = self.prodUrl

		headers = {}

		response = requests.request("GET", url, headers=headers)

		response.encoding = "utf8"
		return response.text

	def queryFromUat(self):
			pass