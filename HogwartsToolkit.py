
#Opens the records file with the intention to read
 
records = open("student_records.txt", "r")
 
#Splits and returns only the names, house, and classes
 
def processed_line(line):
	line = line.strip()
	char = line.split("\t")
	return(char)
 
 
#Takes in a name and file, and returns choice of a student’s house or classes
 
def my_search(student_name, records, choice):
	for line in records:
		if student_name in line:
			line_list = processed_line(line)
	if choice == 'house':
		search_string = line_list.pop(1)
		return(search_string)
	else:
		search_string = line_list.pop(2)
		return(search_string)
 
#Takes in a file and returns a dictionary of the names of the students in each class
 
def courses_dictionary(my_file):
	class_dict = {}
	for line in my_file:
		current_line = processed_line(line)
		current_class_list = current_line[2].split(",")
		for course in current_class_list:
			if course not in class_dict:
				class_dict[course] = []
				class_dict[course].append(current_line[0])
			else:
				class_dict[course].append(current_line[0])
	return(class_dict)
 
  
#Takes in 3 lists, checks for intersecting elements, and returns a list of common elements in those lists
 
def career_check(list1, list2, list3):
	final_list = []
	common_list1 = set(list1).intersection(list2)
	common_list2 = set(common_list1).intersection(list3)
	final_list = list(common_list2)
	return final_list
 
#Takes in a list of names and file, and writes the names into the file with one name per line
 
def write_file(list_names, my_file):
	filename = open(my_file, 'w')
	for name in list_names:
		filename.write(name + "\n")
	filename.close()
 
#Takes in the class dictionary and writes the names of the students in a class to multiple files
 
def class_roster(class_dict):
	for course,student_list in class_dict.items():
		filename = course +'.txt'
		write_file(student_list, filename)
 
print("Welcome to the registrar's office at the Hogwarts School of Witchcraft and Wizardry!")
print("What would you like to do today?")
print("1: Check house assignment or course schedule")
print("2: Generate class roster files")
print("3: Determine students eligible for available job postings: Auror position and Ministry position")
action = input("Please input the number corresponding to which action you would like to complete (1, 2, or 3): ")
while action != '1' and action != '2' and action != '3':
   action = input("Please input the number corresponding to which action you would like to complete (1, 2, or 3): ")
if action == '1':
   name = input("Please enter your full name: ")
   selection = input("Please enter 'house' to see your house assignment or 'schedule' to see the classes you are taking: ")
   print(my_search(name, records, selection))
   print("Thank you for visiting the registrar's office!")
if action == '2':
   dict = courses_dictionary(records)
   print(dict)
   class_roster(dict)
   print("The class roster files have been generated, the file names each being the name of the respective class!")
   print("Thank you for visiting the registrar's office!")
if action == '3':
   dict = courses_dictionary(records)
   dada_list = list(dict["DADA"])
   transfiguration_list = list(dict["Transfiguration"])
   potions_list = list(dict["Potions"])
   charms_list = list(dict["Charms"])
   print("The students eligible for the Auror position are:")
   print(career_check(dada_list, transfiguration_list, potions_list))
   print("The students eligible for the Ministry position are:")
   print(career_check(transfiguration_list, charms_list, potions_list))
 
#Closes  records       
 
records.close()
 
