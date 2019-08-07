#Intro to Lists

#list1 holds series of names

list1 = ["Sam", "Mary", "Bill", "Adam", "Betty"]

print(list1)
#Print list by individual values!-----------------------------------------
print(list1[0])
print(list1[1])
print(list1[2])
print(list1[3])
print(list1[4])

num_records = len(list1)
print("NUM RECORDS: ", num_records)

print()
print()

print("Printing from a FOR LOOP!\n")

for index in range(0, num_records):

    print("INDEX#", index, "\t", list1[index])

list2 =["Sam", "18", "32000"]
list3 = ["Mary", "21", "34000"]
list4 = ["Tom", "24", "38000"]

#RECORD --> Multiple data values, all different kinds
#FIELD  --> Multiple data values, all same kind

name = []
age = []
salary = []

name.append(list2[0])#adds index 0 of list2 to 'name'
name.append(list3[0])
name.append(list4[0])

print()
print("list 'name' contents: ", name)
print("Name[1]: ", name[1])

for index in range(0, 3):

    print(name[index])
print("Part 1 of demo complete... \n\n")

#PART 2 -----------------------------------------------------------------------------------------------------------------

print("--------------------------------\n\n")

import csv

num_records = 0

name = []
age = []
salary = []

with open("C:/Users/008003309/Downloads/example-1.csv") as csvfile:

    file = csv.reader(csvfile)

    for rec in file:

        num_records += 1

        name.append(rec[0])
        age.append(int(rec[1]))
        salary.append(float(rec[2]))

print("Finished processing file \n\n")

for index in range(0, num_records):

    print("INDEX: ", index, "\t", name[index], "\t", age[index], "\t $", salary[index])

print("Finished processing lists for: printing. \n\n")

sal_total = 0

for index in range(0, num_records):

    sal_total += salary[index]

print("Finished processing for: avg salary.\n")

avg_sal = sal_total / num_records

print("AVG SALARY IN FILE: ${:.2f}".format(avg_sal))
print("\n\n\n\n\n\n")







        











