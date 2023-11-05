name=input("What is your name? ").strip().title()

#Remove whitespaces and capitalise first letter of each word
name=name.strip().title()

#Capitalize first word
name=name.capitalize()

#Split user's name into first name and last name
first, last = name.split(" ")
print("Your name is", name, end="\n")
print(f"Your name is {first}")

#------------------------------------------------------------------#

x=float(input("What is X? "))
y=float(input("What is Y? "))
z=round(x/y, 2)     #round to 2 decimal place

print(f"{z:,}")     #put , in long numbers
print(f"{z:.2f}")   #round off to 2 decimal

#------------------------------------------------------------------#

def hello(to="world"):
    print("Hello,", to)

hello()
name=input("What is your name? ")
hello(name)

#------------------------------------------------------------------#

def main():
    x=int(input("What is x? "))
    print("x squared is" , square(x))

def square(n):
    return pow(n, 2)     #power of 2

main()

#------------------------------------------------------------------#
#Check for even number
def is_even(n):
    return True if n % 2 == 0 else False

def is_even(n):
    return n % 2 == 0

#------------------------------------------------------------------#

name = input("What's your name?: ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")

#------------------------------------------------------------------#

while True:
    n = int(input("What is n? "))
    if n >=0:
        break

for _ in range(n):
    print("meow")

#------------------------------------------------------------------#
#List
students = ["Herminone", "Harry", "Ron"]
for student in students:
    print(student)

for i in range(len(students)):
    print(i+1, student[i])

#------------------------------------------------------------------#
#Dictionaries
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}

for student in students:
    print(student, students[student], sep=", ")
    
'''
output: Hermione, Gryffindor
Harry, Gryffindor
Ron, Gryffindor
Draco, Slytherin
'''

#------------------------------------------------------------------#
students = [
    {"name": "Hermione", "house": "Gryffindor"}
    {"name": "Harry", "house": "Gryffindor"}
    {"name" "Ron", "house": "Gryffindor"}
    {"name": "Draco", "house": "Slytherin"}
]
for student in students:
    print(students["name"], students["house"], sep=",")

#------------------------------------------------------------------#
#Exceptions
while True:
    try:
        x = int(input("What's x?"))
    except ValueError:
        print("x is not an integer")
    else:
        break

print(f"x is {x}")

#------------------------------------------------------------------#
