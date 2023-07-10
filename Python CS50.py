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

def is_even(n):
    return True if n % 2 == 0 else False

def is_even(n):
    return n % 2 == 0

#------------------------------------------------------------------#

match name:
    case "Harry"
        print("Gryffindor:
