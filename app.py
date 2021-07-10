from flask import Flask
import pymongo

passtr = open('pass.txt','r').read();
link = "mongodb+srv://umang1126:" + passtr +"@slsyearbook.s4jdg.mongodb.net/class12?retryWrites=true&w=majority"
client = pymongo.MongoClient(link)

db = client.class12;


app = Flask(__name__) # main if this file is directly run, app otherwise


@app.route("/", methods = ['GET'])
def hello():
		return "Welcome to Python Flask!"

#sec name roll quote fav colour imgur
#
@app.route("/<sec>/<roll>/<param>", methods = ['GET'])
def get_data(sec, roll, param):
	str = "section: " + sec + " roll: " + roll + " param: " + param + "<br />"
	col = db[sec]
	data = col.find_one({"roll": roll})
	ans = data[param]
	str = str + ans
	return str