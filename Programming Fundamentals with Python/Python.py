numbers_list =[]
for i in range(5):
  user_input=int(input('Enter a Number:'))
  numbers_list.append(user_input)

min_number = numbers_list[0]
for current_number in numbers_list:
  if current_number < min_number:
    min_number = current_number

print(min_number)  
'''
Exercise 1: The Bank of Python gives you a loan with an interest rate of 4%. 
Write a Python program to read the loan amount from the user and calculate and print the total interest the customer will pay in a year. 
(interest = amount * (interest rate / 100)).
''' 
amount = int(input("Enter Amount of Loan: ")) 
interest_rate=4
interest= interest = amount * (interest_rate /100)
print(f'The interest you will pay in a year for Â£{amount} with an interest rate of {interest_rate}% is Â£{interest}')

