try:
    print("Maximum value in 3 numbers=",max(int(input('Enter '+(str(count+1))+' number:')) for count in range(3)))
except Exception as e:
    print("Please enter Correct values")
    
