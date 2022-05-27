#Print the sum of the current number and the previous number
#print("Printing current and previous number and their sum in a range(10)")
#previous_num = 0

# loop from 1 to 10
#for i in range(1, 11):
#    x_sum = previous_num + i
#    print("Current Number", i, "Previous Number ", previous_num, " Sum: ", previous_num + i)
    # modify previous number
    # set it to the current number
#    previous_num = i



#Print characters from a string that are present at an even index number
#users_input=str(input("enter a string...\n"))
#b=len(users_input)
#for i in range(0,b,2):
   # print( users_input[i])


#Write a program to remove characters from a string starting from zero up to n and return a new string.
#n must be less than the lenth of the str.

#the_str=str(input("Enter a string...\n"))
#lstr=len(the_str)
#num=int(input("How many characters do you want to be removed? \n"))
#if num<lstr:
#    print(the_str[num:])
#else:
#    print("invalid")

# given an array of integers ,print all the mulptiples of 5 and 3.
#a=[1,2,3,4,15,22,21,33,50,55,72,66,96]
#for i in a: 
# if i % 5 == 0 or i % 3 == 0:
#    print(i)


#first = int(input("Enter the first number : \n"))
#second = int(input("Enter the second number : \n"))

#x = first * second
#print(x)

#program for converting decimal number to octal using print()
#num= int(input("enter the number you want to convert: \n"))
#print("%o" % num)

#num = float(input("Enter your number: \n"))
#print(num)


#program to accept list of 5 float numbers as an input from the user
#numbers = []


#for i in range(0,5):
#    print("Enter number in loaction " ,i ,": ")
#    item = float(input())
#    numbers.append(item)
#print("User List:",numbers)  

#def do_twice(f):
#    f()
#    f()

#def print_spam():
#    print('spam')

#do_twice(print_spam)

#program to turn a list to dictionary
#keys = ['Ten', 'Twenty', 'Thirty']
#values = [10, 20, 30]
#a={}
#for i in range(len(keys)):
#    a.update({keys[i]:values[i]})

#print(a)

# program to merge two dictionaries together
#dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
#dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

#dict1.update(dict2)
#print(dict1)


#sampleDict = {
#    "class": {
#        "student": {
#            "name": "Mike",
#           "marks": {
#                "physics": 70,
#                "history": 80
#            }
#        }
#   }
#}

# understand how to located the nested key
# sampleDict['class'] = {'student': {'name': 'Mike', 'marks': {'physics': 70, 'history': 80}}}
# sampleDict['class']['student'] = {'name': 'Mike', 'marks': {'physics': 70, 'history': 80}}
# sampleDict['class']['student']['marks'] = {'physics': 70, 'history': 80}

#print(sampleDict['class']['student']['marks']['history'])

#from unicodedata import name


sample_dict = {
   "name": "Kelly",
    "age": 25,
  "salary": 8000,
    "city": "New york"}
a={}
#for ele in sample_dict:
 #    if ele=="salary" or ele=="name":
#        a.update(ele)

#print(a)

# to check if a value is present
#sample_dict = {'a': 100, 'b': 200, 'c': 300}

#pay=sample_dict.values()
#if 200 in pay:
#    print("200 is present in the values")


#sample_dict = {
#  "name": "Kelly",
#  "age":25,
#  "salary": 8000,
#  "city": "New york"
#}
#sample_dict.popitem()
#sample_dict["location"]= "Newyork"
#print(sample_dict)

#sample_dict = {
#  'Physics': 82,
#  'Math': 65,
#  'history': 75
#}
#for i in sample_dict:
#    print(i)

#print(min(sample_dict.values()))

#y=x.min()
#print(y)
#a={"k4" : "v4",
#"k5" :"v5"}
#sample_dict.update(a)
#sample_dict.pop("k5")

#print(sample_dict)

data={"name" :"vicky",
"city":"silicon valley",
"id" :"48729",
"salary": " $ 20,00",
}

data["employeeID"]=data.pop("id")
print(data)
#to delay a code
#eg   time.sleep(3)