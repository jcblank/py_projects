#variable total to sum the expenses
total = 0
#Variable to take all the expenses in a array
expenses = []
#The user select how many expenses they want to sum
num_expenses = int(input("Enter the number of expenses you want to sum:"))
#loop to add the value of the expenses in the array "expenses"
for i in range (num_expenses):
    expenses.append(float(input("Enter the expense:")))
#sum the expenses
total = sum(expenses)

print("You spend $", total, sep='')