from DropboxApi import DropboxApi
from ShtmlTopMenuPC import ShtmlTopMenuPC
from GenerateConfigTopMenuPC import GenerateConfigTopMenuPC
from GenerateTopMenuPC import GenerateTopMenuPC
from Utility import Config

class ConfigTopMenuPC:
		def __init__(self):
			pass

		@staticmethod
		def getFromCurrentWebSite(env):
			req = ShtmlTopMenuPC()
			html = ""
			config = {}
			if (env == "prod"):
				html = req.queryFromProd()
				config = GenerateConfigTopMenuPC(html).generateConfigTopMenu()
			elif (env == "uat"):
				#html = req.queryFromUat()
				#config = GenerateConfigTopMenuPC(html).generateConfigTopMenu()
				pass

			return config

class UdateTopMenuPC:
		def __init__(self, config):
			path = "/{env}/{file}"
			prodEnv = Config.getFromEnv("prodEnv")
			uatEnv = Config.getFromEnv("uatEnv")
			prodFile = Config.getFromEnv("prodFile")
			uatFile = Config.getFromEnv("uatFile")

			self.config = config
			self.prodPath = path.format(env=prodEnv, file=prodFile)
			self.uatPath = path.format(env=uatEnv, file=uatFile)

		def getSafeInput(self):
			return self.config

		def updateProd(self):
			config = self.getSafeInput()
			byteCode = GenerateTopMenuPC(config).generateTopMenu().encode()
			DropboxApi().uploadByteCode(byteCode, self.prodPath)

		def updateUat(self):
			config = self.getSafeInput()
			byteCode = GenerateTopMenuPC(config).generateTopMenu().encode()
			DropboxApi().uploadByteCode(byteCode, self.uatPath)

