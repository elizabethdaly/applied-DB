# script2.py
# Script to interact with mongo database

# G00376315 Elizabeth Daly
# HDip Data Analytics
# ###################################################################################################################
# Import package to access mongo DB.
import pymongo

#print("In script2")	# Checking.
# ###################################################################################################################
# Function to connect to mongo DB
 
def connect():
	global myclient
	myclient = None
	
	#print("In connect()")
	#print("1 -", myclient)
	myclient = pymongo.MongoClient()
	print("Connection successful -", myclient)
	
	myclient.admin.command('ismaster')

# ###################################################################################################################
# Function to answer Q4. Find car by engine size.
def find_car(eng):

	#print("In find()")	# Checking.
	mydb = myclient["db1"]
	docs = mydb["docs"]
	query = {"car": {"$exists": "true"}, "car.engineSize": eng }
	#print("Just before calling find")	# Checking.
	return docs.find(query)
	#print("Just after calling find")	# Checking.

# ###################################################################################################################
# Function to answer Q5. Create new document with _id, reg, engineSize

def insert_car(id, reg, eng):
	
	# print("In insert_car()")	# Checking.
	mydb = myclient["db1"]
	docs = mydb["docs"]
	
	# Field names for insertion.
	a = "_id"
	b = "reg"
	c = "engineSize"
	
	newcar = {a:id,  "car" : {b: reg, c: eng} }	# New car document.
	
	try:
		docs.insert_one(newcar)
	except pymongo.errors.DuplicateKeyError as e:
			print("Error inserting document - _id already exists.")
	except Exception as e:
		print("Error", e)