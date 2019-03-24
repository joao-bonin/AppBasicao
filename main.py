from flask import Flask, render_template
import pymongo


app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def main():
	return render_template('index.html')
	
	

@app.route('/testeDB', methods=['GET'])
def testeDB():	
	uri = "mongodb+srv://appbasicuser:appbasicusert3st3@cluster0-jvnpg.mongodb.net/test?retryWrites=true"
	client = pymongo.MongoClient(uri)
	db = client.test
	my_collection = db.foods
	my_collection.insert_one({
	    "_id": 1,
	    "name": "pizza",
	    "calories": 266,
	    "fats": {
	        "saturated": 4.5,
	        "trans": 0.2
	    },
	    "protein": 11
	})
	my_cursor = my_collection.find()
 
	for item in my_cursor:
	    print(item["name"])
	return (str(my_cursor))