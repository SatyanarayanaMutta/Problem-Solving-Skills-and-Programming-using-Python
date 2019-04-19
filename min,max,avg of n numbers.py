num = int(input('How many numbers: '))
total_sum = 0
numbers_list=[]
for n in range(num):
    numbers = float(input('Enter number : '))
    total_sum += numbers
    numbers_list.append(numbers)
avg = total_sum/num
print("Minimum value= ",min(numbers_list))
print("Minimum value= ",max(numbers_list))
print('Average of ', num, ' numbers is = ', avg)

