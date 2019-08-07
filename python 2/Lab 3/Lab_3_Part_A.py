#Ryan Cabral

import csv

total_records = 0



idr = 0
counterMale = 0
counterFemale = 0
Moldnotregistered = 0
Foldnotregistered = 0
eligiblenovote = 0
votedadded = 0
processed = 0
ager = 0
genderr = 0
registeredr = 0
votedr = 0

def print_():
    print("\t\tNumber of males not eligible to register {0} ".format(counterMale))
    print("\n\t\tNumber of females not eligible to register {0} ".format(counterFemale))
    print("\n\t\tNumber of males who are old enough to vote but have not registered {0} ".format(Moldnotregistered))
    print("\n\t\tNumber of females who are old enough to vote but have not registered {0} ".format(Foldnotregistered))
    print("\n\t\tNumber of individuals who are eligible to vote but did not vote {0} ".format(eligiblenovote))
    print("\n\t\tNumber of individuals who did vote {0} ".format(votedadded))
    print("\n\t\tNumber of records processed {0} ".format(processed))

with open("C:/Users/008003309/Downloads/voters.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        total_records += 1

        print("{0:5} \t {1:8} \t {2:3} \t {3:7} \t {4:5}".format(rec[0], rec[1], rec[2], rec[3], rec[4]))
        
        idr = rec[0]

        ager = float(rec[1])

        genderr = rec[2]

        registeredr = rec[3]

        votedr = rec[4]


#BASE-------------------------------------------------------------

        if votedr == "Y":
            votedadded = votedadded + 1

        if ager < 18 and registeredr == "N" and genderr == "M":
            counterMale = counterMale + 1

        if ager < 18 and registeredr == "N" and genderr == "F":
            counterFemale = counterFemale + 1

        if ager >= 18 and registeredr == "N" and genderr == "M":
            Moldnotregistered = Moldnotregistered + 1

        if ager >= 18 and registeredr == "N" and genderr == "F":
            Foldnotregistered = Foldnotregistered + 1

        if ager >= 18 and registeredr == "N" and votedr == "N":
            eligiblenovote = eligiblenovote + 1


        processed = processed + 1


print(total_records)
print_()



#id = print(idr)
            #age = print(ager)
            #age_ = int(age) - 0

            #gender_ = print(genderr)
            #gender_ = gender_.lower()
            #if(gender_ != "m" and gender_ != "f"):
                #gender_=input("Please enter [m/f] when you run again! ")
            #registered = print(registeredr)
            #voted = print(votedr)
            #voted = voted.lower()