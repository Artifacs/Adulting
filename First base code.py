 #Hey! Welcome to my budgeting app, designed specifically for college students like me who are trying to manage their allowances and expenses.
 #Saving money doesn't mean we can't still have fun, right?
print("Hello There Budgeting your finances as a college student for the future!")
print("DO YOU WANT TO UPDATE YOUR BANK?:>  Y/N")
Start = input()

if Start == 'Y'.casefold():

 allowance = input("ENTER AMOUNT: ")

 try:
    allowance = float(allowance)  
    print(f"Your Allowance is: {allowance}")
    print("What is your daily expenses?")
    Expenses = input("AMOUNT: ")
    Expenses = float(Expenses)
    
 except ValueError:  
    print("PLEASE ENTER NUMBER ONLY")
else:
    print("HAVE A NICE DAY")