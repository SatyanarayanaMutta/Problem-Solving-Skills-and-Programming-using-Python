def search(arr, n, x): 
  
    for i in range (0, n): 
        if (arr[i] == x): 
            return i; 
    return -1; 
  
nn=int(input("number of values u entered? "))
arr=[]
for  i in range(nn):
    arr.append(int(input("Enter %s value="%str(i+1))))
x = int(input("Which number u want? ")); 
n = len(arr); 
result = search(arr, n, x) 
if(result == -1): 
    print("your entered value is not avaialble") 
else: 
    print("Element is present at index", result); 
