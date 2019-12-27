import os
import json
from flask import request, url_for
from flask_api.decorators import set_renderers
from flask_api.renderers import JSONRenderer
from flask_api import FlaskAPI, status, exceptions
from Utility import isAuthenticated
from Model import UdateTopMenuPC, ConfigTopMenuPC

app = FlaskAPI(__name__)

app.config["DEFAULT_RENDERERS"] = [
    "flask_api.renderers.JSONRenderer",
    "flask_api.renderers.BrowsableAPIRenderer",
]

@app.route("/updateTopMenuPC/<string:env>/", methods=["POST"])
def updateTopMenuPC(env):
	headers = request.headers
	apiKey = headers.get("apiKey")
	print(apiKey)
	referrer = request.headers.get("Referer")
	print(referrer)

	isAuth = isAuthenticated(
		{
			"apiKey": apiKey
		}
	)

	if not isAuth:
		return json.dumps({"success":False}), 401, {"ContentType":"application/json"} 
	
	if env == "prod":
			config = request.get_json()
			UdateTopMenuPC(config).updateProd()
	elif env == "uat":
			config = request.get_json()
			UdateTopMenuPC(config).updateUat()

	return json.dumps({"success":True}), 200, {"ContentType":"application/json"} 

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=os.environ["PORT"])
