numbers_list =[]
for i in range(5):
  user_input=int(input('Enter a Number:'))
  numbers_list.append(user_input)

min_number = numbers_list[0]
for current_number in numbers_list:
  if current_number < min_number:
    min_number = current_number

print('min_number')  
  
