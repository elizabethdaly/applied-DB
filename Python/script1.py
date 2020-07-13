# script1.py
# Script to interact with MySQL database

# G00376315 Elizabeth Daly
# HDip Data Analytics
# ###################################################################################################################
# Import package to access MySQL DB.
import pymysql

# ###################################################################################################################
# Function to answer Q1: View first 15 cities from city table.
def view_15cities():

	# Connect to DB=world
	db = pymysql.connect(host="localhost", user="root", password="root", db="world", cursorclass=pymysql.cursors.DictCursor)

	# Write the query
	sql = "select * from city limit 15" # Return all columns, calling program decides which to print.
	
	with db:
		try:
			cursor = db.cursor()
			cursor.execute(sql)
			return cursor.fetchall()
		except Exception as e: # catch general errors
			print(e)
# ###################################################################################################################
# Function to answer Q2: View cities in city table by population.
def view_pop_cities(oper, pop):
	
	# Connect to DB=world
	db = pymysql.connect(host="localhost", user="root", password="root", db="world", cursorclass=pymysql.cursors.DictCursor)
	
	# Write the query dependent on operator (<,>,=) Has been checked one level up.
	if (oper == "<"):
		sql = "select * from city where Population < %s"	# Return all columns, calling program decides which to print.
	elif (oper == ">"):
		sql = "select * from city where Population > %s"
	else:
		sql = "select * from city where Population = %s"
		
	with db:
		try:
			cursor = db.cursor()
			cursor.execute(sql,(pop)) # Only passing pop as %s here, not the operator.
			return cursor.fetchall()
		except Exception as e: # catch general errors
			print(e)
		
# ###################################################################################################################
# Function associated with Q3, check if CountryCode exists in city table.
def check_countrycode(code):
	# Connect to DB=world
	db = pymysql.connect(host="localhost", user="root", password="root", db="world", cursorclass=pymysql.cursors.DictCursor)
	
	sql = "select exists(select * from city where CountryCode = %s limit 1)as TF" # Return 1 if CountryCode exists, 0 otherwise.
	
	with db:
		cursor = db.cursor()
		cursor.execute(sql,(code))
		return cursor.fetchall()

# ###################################################################################################################		
# Function to answer Q3: Add new city to city table.
def add_city(name, code, dist, pop):
	
	# Connect to DB=world
	db = pymysql.connect(host="localhost", user="root", password="root", db="world", cursorclass=pymysql.cursors.DictCursor)
	
	# PK = ID is auto increment, so no need to provide a value. 
	# latitude, longitude can be NULL, so no need to provide values. 
	sql = "INSERT INTO city (Name, CountryCode, District, Population) VALUES (%s, %s, %s, %s)"
	
	with db:
		try:
			cursor = db.cursor()
			cursor.execute(sql, (name, code, dist, pop))
			db.commit()
		except pymysql.err.InternalError as e: # catch invalid types
			print(e)
		except Exception as e: # catch any others
			print(e)

# ###################################################################################################################
# Function to answer Q6 or Q7: Return selected columns from countries table to be stored in a variable.	
def countries():

	# Connect to DB=world
	db = pymysql.connect(host="localhost", user="root", password="root", db="world", cursorclass=pymysql.cursors.DictCursor)
	
	# Write the query
	sql = "select Code, Name, Continent, Population, HeadOfState from country" # Return selected columns, calling program decides which ones to print.
	
	with db:
		try:
			cursor = db.cursor()
			cursor.execute(sql)
			return cursor.fetchall()
		except Exception as e: # catch general errors
			print(e)			
# ###################################################################################################################
# Function to answer Q6 directly: View countries by name.
def countries_by_name(name):

	# Connect to DB=world
	db = pymysql.connect(host="localhost", user="root", password="root", db="world", cursorclass=pymysql.cursors.DictCursor)

	# Write the query
	sql = "select * from country where Name like  %s" # Return all columns, calling program decides which to print.
	
	with db:
		try:
			cursor = db.cursor()
			cursor.execute(sql, ("%"+name+"%"))
			return cursor.fetchall()
		except Exception as e: # catch general errors
			print(e)
			
# ###################################################################################################################
# Function to answer Q7 directly: View countries by population.
def countries_by_pop(oper, pop):

	# Connect to DB=world
	db = pymysql.connect(host="localhost", user="root", password="root", db="world", cursorclass=pymysql.cursors.DictCursor)
	
	# Write the query dependent on operator (<,>,=) Has been checked one level up.
	if (oper == "<"):
		sql = "select * from country where Population < %s"	# Return all columns, calling program decides which to print.
	elif (oper == ">"):
		sql = "select * from country where Population > %s"
	else:
		sql = "select * from country where Population = %s"
		
	with db:
		try:
			cursor = db.cursor()
			cursor.execute(sql,(pop)) # Only passing pop as %s here, not the operator.
			return cursor.fetchall()
		except Exception as e: # catch general errors
			print(e)
	
