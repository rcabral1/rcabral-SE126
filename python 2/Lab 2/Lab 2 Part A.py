#Ryan Cabral--Lab 1--7/16/2019--201940_SE126.02


#FUNCTIONS----------------------------------------------------
def id_(id):

    id = input("Enter your 4-Digit code: ")
    return id
def age_(age):
    age = input("What is your age? ")
    return age

def gender(gender_):
    gender_ = input("What is your gender? [m/f] ")
    if(gender_ != "m" and gender_ != "f"):
        gender_=input("Please enter [m/f] when you run again! ")
        quit()
    return gender_
def registered_(registered):

    registered = input("Are you registered to vote? [y/n] ")
    return registered

def voted_(voted):
    voted = input("Did you vote? [y/n] ")
    return voted


def print_():
    print("\t\tNumber of males not eligible to register {0} ".format(counterMale))
    print("\n\t\tNumber of females not eligible to register {0} ".format(counterFemale))
    print("\n\t\tNumber of males who are old enough to vote but have not registered {0} ".format(Moldnotregistered))
    print("\n\t\tNumber of females who are old enough to vote but have not registered {0} ".format(Foldnotregistered))
    print("\n\t\tNumber of individuals who are eligible to vote but did not vote {0} ".format(eligiblenovote))
    print("\n\t\tNumber of individuals who did vote {0} ".format(votedadded))
    print("\n\t\tNumber of records processed {0} ".format(processed))
    
        
id_entered = 0
counterMale = 0
counterFemale = 0
Moldnotregistered = 0
Foldnotregistered = 0
eligiblenovote = 0
votedadded = 0
processed = 0
age = 0
gender_ = 0
registered = 0
voted = 0


#BASE-------------------------------------------------------------

ans = input("Would you like to start the program? [y/n] ")
ans = ans.lower()
if ans != "y":
    yes = input("Please enter y/n")
    quit()

while ans == "y":
    if ans != "y":
        yes = input("Please enter y/n")

    id = input("Enter your 4-Digit code: ")
    age = input("What is your age? ")
    age_ = int(age) - 0

    gender_ = input("What is your gender? [m/f] ")
    gender_ = gender_.lower()
    if(gender_ != "m" and gender_ != "f"):
        gender_=input("Please enter [m/f] when you run again! ")
    registered = input("Are you registered to vote? [y/n] ")
    voted = input("Did you vote? [y/n] ")
    voted = voted.lower()
    if voted == "y":
        votedadded = votedadded + 1

    if age_ < 18 and registered == "n" and gender_ == "m":
        counterMale = counterMale + 1

    elif age_ < 18 and registered == "n" and gender_ == "f":
        counterFemale = counterFemale + 1

    elif age_ >= 18 and registered == "n" and gender_ == "m":
        Moldnotregistered = Moldnotregistered + 1

    elif age_ >= 18 and registered == "n" and gender_ == "f":
        Foldnotregistered = Foldnotregistered + 1

    elif age_ >= 18 and registered == "y" and voted == "n":
        eligiblenovote = eligiblenovote + 1


    processed = processed + 1

    print_()
    
    ask = input("\n\t\tWould you like to run again? [y/n] ")
    if ask == "n":        
        question = input("Thank you! Press any key to continue!")   
        quit()

