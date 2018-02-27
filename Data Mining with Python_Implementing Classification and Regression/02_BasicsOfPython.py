#Data types
section = 2
course = "Learning Data mining with Python"
section_list = [1,2,3,4,5]
sections_tuple = (1,2,3,4,5)
Dict={'Name': "Learning Data mining with Python",
        'Sections': 5
        }

#Statements
weight = 60
if weight > 50:
    print("greater")
else:
    print("lesser")

#functions
def listLength(number_list):
    list_length = len(number_list)
    return list_length

number_list = [0,2,3]
print("Size ", listLength(number_list))
