# PythonProj.py

# G00376315 Elizabeth Daly
# HDip Data Analytics
# ##########################################################################################
# Import scripts that interact with the MySQL DB: world
import script1

# Import scripts that interact with the mongo DB: mongo.json
import script2



# ##########################################################################################
# Initialize counter for Choices 6 and 7; global as being modified in if clauses.
# The first time 6 or 7 is chosen, DB is read and country table is stored in a variable.
# Any subsequent choice of 6 or 7 uses the stored variable to perform the query.
num = 0

# ##########################################################################################

def main():
	# Print this once when script is run.
	print("MySQL DB = world & mongo DB mongo.json")
	print("--------------------------------------")
	
	# Display the menu of choices.
	display_menu()
	
	while True:
		global num
		myclient = None
		
		choice = input("Choice: ")
		
		##########################################################################################
		if (choice == "1"):
		
			print("Q1 View first 15 cities from city table of world DB.")
			print("---------------------------------------")
			
			# Call the function to perform the query.
			cities = script1.view_15cities()
			for c in cities:
				print(c ["ID"],  " | ", c["Name"], " | ", c["CountryCode"], " | ", c["District"], " | ", c["Population"])
			
			# Display the menu again.
			display_menu()	
		
		##########################################################################################
		elif (choice == "2"):
		
			print("Q2 Cities by Population")
			print("-----------------------")
			
			oper = input("Enter < > or = : ")
			pop = input("Enter population : ") # Test for valid input (+ve int)
			
			# Check that string pop is acually a number.
			# at mysql level get Warning: (1292, "Truncated incorrect DOUBLE value: 'ttt'")
			# MySQL converts input and Population to double to compare them.
			
			# Check that the user provided a valid operator.
			valid_operators = ["<", ">", "="]
			
			try:
				if oper not in valid_operators:
					raise Exception
			except Exception as e:
				print("*** ERROR ***: Invalid operator, please use < > or =")
				continue	# Asks for Choice again 1-7
			
			try:
				int(pop)
			except ValueError:
				print("*** ERROR ***: Population must be a number, please choose again.")
				#quit()	# quits entire program
				continue	# Asks for Choice again 1-7
			
			g = int(pop)
			try:
				if g < 0:
					raise ValueError
			except ValueError:
				print("*** ERROR ***: Population must be >= 0, please choose again.")
				continue	# Asks for Choice again 1-7
			
			# Call the function to perform the query.
			cityp = script1.view_pop_cities(oper, pop)
			# Print results.
			print("Cities with a population ", oper, " ", pop, "are: ")
			for p in cityp:
				print(p["ID"],  " | ", p["Name"], " | ", p["CountryCode"], " | ", p["District"], " | ", p["Population"])
				
			# Display the menu again.
			display_menu()	
			
		##########################################################################################
		elif (choice == "3"):
		
			print("Q3 Add New City")
			print("---------------")
			
			name = input("Enter city name : ")
			code = input("Country Code : ")
			dist = input("District : ")
			pop = input("Population : ")
			
			# First test if CountryCode exists in city table by calling a function.
			
			check = script1.check_countrycode(code) # Want 1/0 returned in column "TF".
			test = check[0].get("TF")
			#print("Does CountryCode exist? 1/0 ", test)
			
			# If CountryCode exists call the function to perform the query.
			if (test == 1):
				print("CountryCode ", code, " exists so city can be added")
				script1.add_city(name, code, dist, pop)
			else:	
				print("*** ERROR ***: CountryCode", code, " does not exist")
			
			# Display the menu again.
			display_menu()
		
		##########################################################################################
		elif (choice == "4"):
			print("Q4 Show Cars by Engine Size")
			print("---------------------------")
			
			eng = input("Enter Engine Size : ") #  a string (needs to be a number)
			
			# Test for valid Engine Size (x.x or int) = float
			try:
				float(eng)
			except ValueError:
				print("Engine Size must be a number (eg 1.5). Please choose again.")
				continue	# Asks for Choice again 1-7
			
			# Connect to DB.
			print(myclient) # Checking
			if (not myclient):
				try:
					script2.connect()
				except Exception as e:
					print("Error ", e)
					
			# Perform the query
			result = script2.find_car(float(eng))
			for c in result:
				print(int(c["_id"]), " | ", c["car"] ["reg"], " | ", c["car"] ["engineSize"], " | ", c["addresses"])
						
			# Display the menu again.
			display_menu()
			
		##########################################################################################	
		elif (choice == "5"):
			print("Q5 Add New Car")
			print("--------------")
			
			id = input("Enter _id : ")			# a string (needs to be an int to match other car docs)
			reg = input("Enter Reg : ")			# a string
			eng = input("Enter Engine Size : ")	# a string (needs to be a number)
			
			# Test for valid inputs. 
			# _id should be an integer AND engineSize must be a float (x.x or int).
			try:
				int(id) and float(eng)
			except ValueError:
				print("_id must be an integer, Engine Size must be a number like 1.5. Please choose again.")
				continue	# Asks for Choice again 1-7Engine Size (x.x or int) = float
			
			# Connect to DB.
			print(myclient) # Checking
			if (not myclient):
				try:
					script2.connect()
				except Exception as e:
					print("Error ", e)
					
			# Insert the document.
			script2.insert_car(int(id), reg, float(eng))
			
			# Display the menu again.
			display_menu()
		
		##########################################################################################
		elif (choice == "6"):
			num +=1	# Keep track of count. 
			
			print("Q6 Countries by Name")
			print("--------------------")
			print("Option 6 or 7 has been chosen ", num, " time(s).")
			
			n = input("Enter Country Name : ")
			
			# If num = 1 read DB & store info, else access stored info.
			if num == 1:	
				# Function returns a list of dicts. Each dict = row from table where (key, value) = (field name, field value)
				allcou = script1.countries()
				print("Reading the database to retrieve country table. Rows returned: ", len(allcou))
			
			# Else perform the query on the stored variable which contains country table.
			# Make search string case insensitive.
			print("Check if any Name contains ", n, " :")
			for i in allcou:
				if n.lower() in i.get("Name").lower():	# Case insensitive via .lower().
					print(i.get("Name"), " | ", i.get("Continent"), " | ", i.get("Population"), " | ", i.get("HeadOfState"))
			
			# Display the menu again.
			display_menu()
		
		##########################################################################################
		elif (choice == "7"):
			num +=1	# Keep track of count. If num=1 read DB & store info, else access stored info.
			
			print("Q7 Countries by Population")
			print("--------------------------")
			print("Option 6 or 7 has been chosen ", num, " time(s).")
			
			oper = input("Enter < > or = : ")
			pop = input("Enter population : ") 
			# at mysql level get Warning: (1292, "Truncated incorrect DOUBLE value: 'ttt'")
			# MySQL converts input and Population to double to compare them.
			
			# If num = 1 read DB & store info, else access stored info.
			if num == 1:	
				# Function returns a list of dicts. Each dict = row from table where (key, value) = (field name, field value)
				allcou = script1.countries()
				print("Reading the database to retrieve country table. Rows returned: ", len(allcou))
				
			# Check that entered population is a number >= 0.
			try:
				int(pop)
			except ValueError:
				print("*** ERROR ***: Population must be a number, please choose again.")
				continue	# Asks for Choice again 1-7
			
			g = int(pop)
			try:
				if g < 0:
					raise ValueError
			except ValueError:
				print("*** ERROR ***: Population must be >= 0, please choose again.")
				continue	# Asks for Choice again 1-7
				
			# Else check operator and perform query on the stored variable which contains country table.
			if oper == "<":
				print("Countries with population", oper, pop, " :")
				for i in allcou:
					if i.get("Population") < int(pop):	# pop is a str, convert to int to match table values.
						print(i.get("Code"), " | ", i.get("Name"), " | ", i.get("Continent"), " | ", i.get("Population"))
			elif oper == ">":
				print("Countries with population", oper, pop, " :")
				for i in allcou:
					if i.get("Population") > int(pop):	# pop is a str, convert to int to match table values.
						print(i.get("Code"), " | ", i.get("Name"), " | ", i.get("Continent"), " | ", i.get("Population"))
			elif oper == "=":
				print("Countries with population", oper, pop, " :")
				for i in allcou:
					if i.get("Population") == int(pop):	# pop is a str, convert to int to match table values.
						print(i.get("Code"), " | ", i.get("Name"), " | ", i.get("Continent"), " | ", i.get("Population"))
			else:
				print("*** ERROR ***: Invalid operator, please use < > or =")
				
			# Display the menu again.
			display_menu()
		
		##########################################################################################	
		elif (choice == "x"):
			break;			# Exit
		
		##########################################################################################		
		else:
			# Display the menu again.
			print("Not a valid choice :")
			display_menu()

# ##########################################################################################			
# Code to display menu options.
def display_menu():
	print("    ")
	print("MENU")
	print("====")
	print("1 - View 15 Cities")
	print("2 - View Cities by Population")
	print("3 - Add New City")
	print("4 - Find Car by Engine Size")
	print("5 - Add New Car")
	print("6 - View Countries by Name")
	print("7 - View Countries by Population")
	print("x - Exit Application")
	
# ##########################################################################################
if __name__ == "__main__":
	main()