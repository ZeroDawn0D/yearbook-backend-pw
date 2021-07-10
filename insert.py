import pymongo;

inputfile = open('input.txt','r');
inputs = inputfile.readlines();
sec = inputs[0][:-1];
name = inputs[1][:-1];
roll = inputs[2][:-1];
quote = inputs[3][:-1];
fav = inputs[4][:-1];
colour = inputs[5][:-1];
imgur = inputs[6];
print("sec: "+ sec);
print("name: "+ name);
print("roll: "+ roll);
print("quote: "+ quote);
print("fav: "+ fav);
print("colour: "+ colour);
print("imgur: "+ imgur);

doc = {
	"name": name,
	"roll": roll,
	"quote": quote,
	"fav": fav,
	"colour": colour,
	"imgur": imgur
}


passtr = open('pass.txt','r').read();
link = "mongodb+srv://umang1126:" + passtr +"@slsyearbook.s4jdg.mongodb.net/class12?retryWrites=true&w=majority"
client = pymongo.MongoClient(link)
db = client.class12;
col = db[sec];

col.insert_one(doc);