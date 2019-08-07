#Ryan Cabral--Lab 1--7/16/2019--201940_SE126.02

ans = input("Welcome. Would you like to start the program? [y/n]: ")
if ans != "y" and ans != "n":
    print("ERROR")
    ans=input("Please enter [y/n] ")
while (ans == 'y' or ans == 'Y'):

    capacity = float(input("What is the room capacity? "))

    people = float(input("How many people would like to attend the even? "))

    if (people <= capacity):
        more = (capacity - people)
        print("The even can be held, {0} more people can attend.".format(more))
    elif (people > capacity):
        kicked = (people - capacity)
        print("The even can't be held, {0} people have to be told they cant come.".format(kicked))

    ans = input("Would you like to do this again? [y/n]")
    if ans != "y" and ans != "n":
        print("ERROR")
        ans=input("Please enter [y/n] ")
