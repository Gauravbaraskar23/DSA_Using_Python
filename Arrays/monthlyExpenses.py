#Create a list to store these monthly expenses and using that find out.

'''
Jan - 2200
Feb - 2350
Mar - 2600
April - 2130
May -2190 
''' 
monthly_expenses = [2200 , 2350 , 2600 , 2130 , 2190]

# 1 In feb , how many dollars you spent extra as compared to jan?
extra_amount = monthly_expenses[1] - monthly_expenses[0]
print(f"Extra dollars as compared to jan is: {extra_amount}")

#2 Total expenses in first quarter(jan , feb ,march) of the year?
total_expenses = monthly_expenses[0] + monthly_expenses[1] + monthly_expenses[2]
print(f"Total expenses in first quarter(jan , feb ,march) of the year is: {total_expenses}")

#3 Find if you spent exactly 2000 dollars in any month?
print("Did I spent 2000$ in any month?:" , 2000 in monthly_expenses)


# 4  June month just finished and your expenses is 1980 dollar ,add this item in your list?
# monthly_expenses.insert(-1 , 1980) 
monthly_expenses.append(1980)
print("Expenses at the end of june:",monthly_expenses)
    
# You got 200$ refund in a month of April.Make a coorection in your expenses?
monthly_expenses[3] -= 200
print("Expenses after 200$ return in April:" , monthly_expenses)

