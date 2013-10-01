#Moktadir Shourav fa9444 CSC 1100 Sec 002/003
#Project 1 Completed 03/15/2013
#Work Completed: 100%

while True:
    try:
        file = input("Enter filename: ")
        data_file = open(file,"r")
        break
    except IOError:
        print("File not found.")
output = open("best_and_worst.txt","w")

def min_and_max_finder(r): #Function specified by r, r = Column number in data
    Min = 1000000 #Unspecified maxiumum value
    Max = 0 #Definite minimum value.
    split_line = [] 
    state_max = "" #Name of state of final maximum value
    state_min = "" #Name of state of final minimum value
    for line in data_file:
        split_line = line.split(",") #Each line split into a list
        if split_line[0] == "State": #Function to obtain title of data column
            title = split_line[r]
        try: #Func to compare values to update minimum and maximum simultaneously
            value = split_line[r].replace("%","") #Removes "%" from numericals
            value = float(value) #Logical value conversion
            if value > Max: 
                Max = value
                state_max = split_line[0]
            elif value < Min:
                Min = value
                state_min = split_line[0]
        except:
            ValueError
    return title, Min, Max, state_min, state_max, r #Returns column name, \
#minimum value of column and the respective state, max value and resp. state, \
#and the column number, for organizational purposes.

def extremity_double_check(): #Goes back over obtained data to find equivalencies.
    Min = 1000000
    Max = 0
    split_line = []
    state_max = ""
    state_min = ""
    revised_max = [] 
    revised_min = []
    for item in table:
        for line in data_file:
            split_line = line.split(",")
            if split_line[0] not in (item[3],item[4]):
                try:
                    value = split_line[item[5]].replace("%","")
                    value = float(value)
                    if value == item[1]:
                        revised_min += [[item[0],value,split_line[0]]]  
                    elif value == item[2]:
                        revised_max += [[item[0],value,split_line[0]]]
                except:
                    ValueError
    return revised_min, revised_max #Returns list of equivalent minimums, their \
#respective states, and data column title. Same with max.

def table_printer(): #Conveniently prints obtained data and equivalencies into a table inside the specified text file.
    print("{:35}{:30}   {}".format("Indicator",": Min","Max"), file = output)
    print("{:->95s}".format(''),\
          file = output)
    for item in table: #Initially obtained data
        print("{:35}: {:21}  {:7} {:21} {}".format(item[0], item[3], item[1], \
                                                 item[4], item[2]), \
              file = output)
        for update in revised_min: #Convenience in printing minimum equivalencies
            if update[0] == item[0]:
                if update[1] == item[1]:
                    print("{:35}: {:21}  {:7}".format(update[0], \
                                                               update[2], \
                                                               update[1]),\
                          file = output)
        for update in revised_max: #Max. equivlcies.
            if update[0] == item[0]:
                if update[1] == item[2]:
                    print("{:35}: {:21}  {:7} {:21} {}".format(update[0], " ", \
                                                               " ", \
                                                               update[2], \
                                                               update[1]),\
                          file = output)
        
table = []
table += [min_and_max_finder(1)] #Function to analyze columns specified by \
#column number

data_file.close()
data_file = open(file,"r")

table += [min_and_max_finder(5)]

data_file.close()
data_file = open(file,"r")

table += [min_and_max_finder(7)]

data_file.close()
data_file = open(file,"r")

table += [min_and_max_finder(11)]

data_file.close()
data_file = open(file,"r")

table += [min_and_max_finder(13)]

data_file.close()
data_file = open(file,"r")

revised_min, revised_max = extremity_double_check() #Extraction of equivalencies

table_printer() #Output of overall obtained data

data_file.close()
output.close()
