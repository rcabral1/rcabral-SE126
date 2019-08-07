#Ryan Cabral--Lab 1--7/16/2019--201940_SE126.02

def capacity():

    max = float(input("What is the capacity of the room? "))

    return max

def attendees():

    people = float(input("How many people want to attend the event? "))

    return people

def register(capacity, attendees):

    register = capacity - attendees

    return register

def check():

    check = str(input("Would you like to check another room? [y for yes] "))

    if (check == "n" or check == "N"):
        quit()

ans = input("Would you like to start the program? [y/n] ")

while ans == "y" or ans == "Y":

    max = capacity()

    people = attendees()

    if (people <= max):

        number = register(max, people)

        print("The event can be held, {0} more people can attend.".format(number))

    elif (people > max):

        kicked = people - max

        print("The event cant be held, {0} people have to be told they cant come.".format(kicked))

    check()

