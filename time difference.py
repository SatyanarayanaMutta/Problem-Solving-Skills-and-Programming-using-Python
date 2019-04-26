from datetime import datetime
time1 = input("Enter Highest time in the format of HH:MM:SS--->>> ")
time2 = input("Enter Lowest time in the format of HH:MM:SS--->>> ")
FMT = '%H:%M:%S'
if max(time1,time2)==time2:
    print("First time must be have Highest compare to Second time.")
else:
    try: 
        diff_time = datetime.strptime(time1, FMT) - datetime.strptime(time2, FMT)
    except Exception as e:
        print("Error Found--->>",e)
    else:
        print("Differenece b/w 2 times--->>>",diff_time)
