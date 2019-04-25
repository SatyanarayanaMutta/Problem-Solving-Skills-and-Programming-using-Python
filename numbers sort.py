from sys import exit
file=input("Enter you enter file name search that file otherwise search default file:- ")
if not len(file.strip()):
    file="numbers data.txt"
    print(file)
try:
    data=open(file).read()
    
except FileNotFoundError:
    print("you entered file '"+file+"' is not Found in current directory so please check & solve error then try again")
else:
    print("you entered file is Found \nLets Go")
    print("your Entered File Name~~~> ",file,"\nLength of File content~~~> ",len(data),"\nNo. of Lines~~~> ",len(data.splitlines()))    
    data_1=''
    if not len(data):
        print("file don't have any content so sort operation is Terminated...")
        exit(0)
    for i in data:
        if i.isdigit():
            data_1+=i
        else:
            data_1+=' '
    print(file,"file have following numbers are~~~> ",data_1)
    data_1=data_1.split()
    data_1=[int(j) for j in data_1]
    data_1.sort()
    print("sorted numbers are~~~> ",*data_1,sep=',')
