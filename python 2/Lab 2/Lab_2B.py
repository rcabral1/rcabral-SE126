
def tax(items_cost, rate, item_tax, total_tax):
    item_tax = float( items_cost * rate)
    total_tax = total_tax + item_tax
    return total_tax

def change():
    given = float(input("How much money will you be giving the clerk? "))
    change = float(given - total_due)
    print("You will recieve ${:.2f} in change have a nice day!".format(change))

def prints():
    print("You bought {0} items that added up to ${1:.2f} plus ${2:.2f} in taxes, which all added up to ${3:.2f}".format(item_number, total_item_cost, taxfunc, total_due))
    print("The total cost was ${:.2f}".format(total_due))

ans = "y"
rate = 7 / 100
total_item_cost = 0
item_tax = 0
total_tax = 0

while(ans == "y"):
    item_number = input("What number item is this? ")

    items_cost = float(input("How much is the item? $ "))

    total_item_cost = total_item_cost + items_cost

    items = item_number

   
    tax_question = input("Is this item taxed? [t/n]")
    #if yes enters if loop if no skips past it
    if(tax_question == "t"):

        taxfunc = tax(items_cost, rate, item_tax, total_tax)

        print("You will be paying: ${0:.2f} in tax on this item".format(taxfunc))

    total_due = float(total_item_cost + taxfunc)
    
    
    ans = input("Would you like to add another item? [y/n]")

prints()

change()