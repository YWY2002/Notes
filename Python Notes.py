height = 165.5
print(type(height)) #op: <class 'float'>

#------------------------------------------------------------------------------------#
#Strings#

name="John Cena"
print(len(name))                #print length of string
print(name.title())             #cap each word
print(name.strip())             #strip left and right spaces
print(name.index("o"))          #find the first occurrence (raise ValueError if substring not found)
print(name.find("o"))           #find the first occurrence (output -1 if substring not found)
print(name.capitalize())        #cap first letter
print(name.upper())             #upper case 
print(name.lower())             #lower case 
print(name.isdigit())           #check if all are number (excl. +,-,*,/,.)
print(name.isnumeric())         #incl. chinese, roman numbers
print(name.isalpha())           #check if all are alphabet
print(name.isalnum())           #alpahnumeric (excl. +,-,*,/,.)
print(name.count("o"))          #count occurence of str  
print(name.replace("e","i"))    #(old, new[, count])
print(name.lstrip("J"))         #strip left most str
print(name.rstrip("a"))         #strip right most str

website1= "http://google.com"
website2="http://wikipedia.com"
slice1=slice(7,-4)                #slice(start,stop)
print(website1[slice1])
print(website2[slice1])

#------------------------------------------------------------------------------------#
#Operations#

import math
pi=3.14159265
print(round(pi, 2))            #round to n decimal pt
print(math.ceil(pi))           #round up
print(math.floor(pi))          #round down
print(abs(pi))                 #absolute how far away from 0
print(pow(pi,1))               #power
print(math.sqrt(pi))           #squareroot
print(max(x,y,z))              #max number
print(min(x,y,z))              #min number

#------------------------------------------------------------------------------------#
#List

food = []                     #assign empty list
food[0] = "sushi"             #replace
food.append("ice cream")      #add element to the end of the list
food.insert(0,"cake")         #add str to a specified location
food.remove("ice cream")      #remove first occurrence of specified value
food.pop(1)                   #remove element at a specified location (default:remove last element)
food.clear()                  #remove all elements
fullname = "_".join(name)     #sep.join(list/tuple/string)
food.split(":")               #split str into list (default: newspaces)

#2D List

drinks = ["coffee","soda","tea"]       
dinner = ["pizza","hamburger","hotdog"]
dessert=["cake","ice cream"]
food=[drinks,dinner,dessert]
print(food[2][1])             #MainList[sublist][element]

#tuples(ordered and unchangeable)

student = ("Bro",21,"male")     

#------------------------------------------------------------------------------------#
#Index

name= "John Cena"
first_name=name[:4]
last_name=name[5:9]
funky_name=name[0:9:2] #[start:stop:step]
reverse_name= name[::-1]
last_letter=name[-1:]
name="Yik Wen Yuan"
middle_name=name[4:-5]
print(last_name)


template = "Hi, {0}. The total cost will be {1:.2f}."
price1 = 15.6
price2 = 21.5
message1 = template.format("Alice", price1)
message2 = template.format("Bob", price2)

#name=None
#while not name:     #while len(name)==0:
    #name=input("Enter your name: ")
#print("Hello "+name)

#for i in range(10):
    #print(i+1)
#for i in range(50,100+1,2):
    #print(i)
#for i in "Bro Code":
    #print(i)
#import time
#for seconds in range(10,0,-1):
    #print(seconds)
    #time.sleep(1)
#print("Happy New Year")

#rows=int(input("How many rows? : "))
#columns=int(input("How many columns? : "))
#symbol=input("enter a symbol to use: ")
#for i in range(rows):
    #for j in range(columns):
        #print(symbol,end="")
    #print()

#while True:
    #name=input("Enter your name: ")
    #if name!="":
        #break
#phone_number="123-456-7890"
#for i in phone_number:
    #if i =="-":
        #continue
    #print(i,end="")
#for i in range(1,21):
    #if i == 13:
        #pass
    #else:
        #print(i)  



#utensils={"fork","spoon","knife","knife","knife"}   #set(unordered, unindexed, no dupes)
#dishes={"bowl","plate","cup","knife"}
#utensils.add("napkin")
#utensils.remove("fork")
#utensils.clear()
#utensils.update(dishes)
#dinner_table=utensils.union(dishes)
#print(utensils.difference(dishes))      #what untensils have which dishes doesnt
#print(utensils.intersection(dishes))    #common element
#for x in dinner_table:
    #print(x)

