import os
import dropbox
from Utility import Config

class DropboxApi:
	def __init__(self):
			self.dbx = dropbox.Dropbox(Config.getFromEnv("dbxToken"))

	def uploadByteCode(self, byteCode, dbxPath):
			#WriteMode設定為衝突時自動覆蓋原有檔案
			self.dbx.files_upload(byteCode, dbxPath, mode=dropbox.files.WriteMode.overwrite)
