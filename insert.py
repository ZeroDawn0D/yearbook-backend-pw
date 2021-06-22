import pymongo;

inputfile = open('input.txt','r');
inputs = inputfile.readlines();
sec = inputs[0];
name = inputs[1];
roll = inputs[2];
quote = inputs[3];
fav = inputs[4];
colour = inputs[5];
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
link = "mongodb+srv://umang1126:" + passtr +"@slsyearbook.s4jdg.mongodb.net/class12"
client = pymongo.MongoClient(link)
db = client.class12;
col = db[sec];

col.insert_one(doc);

