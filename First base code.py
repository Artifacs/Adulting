 #Hey! Welcome to my budgeting app, designed specifically for college students like me who are trying to manage their allowances and expenses.
 #Saving money doesn't mean we can't still have fun, right?

MONEY = 0 
print("Hello There Budgeting your finances as a college student for the future!")
Start = input("DO YOU WANT TO UPDATE YOUR BANK?:>  Y/N: ")

while Start != "Y".casefold():
   Start = input("ERROR\nDO YOU WANT TO UPDATE YOUR BANK?:>  Y/N: ")
if Start == 'Y'.casefold():
 allowance = int(input("ENTER AMOUNT: "))
 MONEY += allowance
 print(f"Your Money is: {MONEY}")
 try:
    allowance = float(allowance)  
    print(f"Your Allowance is: {allowance}")
    print("What is your daily expenses?")
    Expenses = float(input("AMOUNT: "))
    MONEY -= Expenses
    print(f"Your Expenses daily is {Expenses} And your reamaining money is {MONEY}")
    
 except ValueError:  
    print("PLEASE ENTER NUMBER ONLY")   
else:
    print("HAVE A NICE DAY")
