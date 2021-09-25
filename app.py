from flask import Flask
from flask_cors import CORS
import pymongo

passtr = open('pass.txt','r').read();
link = "mongodb+srv://umang1126:" + passtr +"@slsyearbook.s4jdg.mongodb.net/class12?retryWrites=true&w=majority"
client = pymongo.MongoClient(link, tlsAllowInvalidCertificates=True)

db = client.class12;


app = Flask(__name__) # main if this file is directly run, app otherwise
CORS(app) #magic idk

@app.route("/", methods = ['GET'])
def hello():
		return "testing"

#sec name roll quote fav colour imgur
#
@app.route("/<sec>/<roll>/<param>", methods = ['GET'])
def get_data(sec, roll, param):
	str = "section: " + sec + " roll: " + roll + " param: " + param + "<br />"
	col = db[sec]
	data = col.find_one({"roll": roll})
	ans = data[param]
	str = str + ans
	return ans

@app.route("/<sec>", methods = ['GET'])
def get_roll(sec):
	col = db[sec]
	datalist = col.find({})
	rollarray = [];
	for obj in datalist:
		rollarray.append(int(obj["roll"]))

	rollarray.sort()
	st = ""
	for i in rollarray:
		st = st + str(i) + " "
	st = st[:-1]
	return st

if __name__ == "__main__":
	app.run()