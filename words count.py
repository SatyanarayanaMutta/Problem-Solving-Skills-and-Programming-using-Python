fname = input('Enter text file Name\n HINT:- you enterd file name should be have end with .txt\n---:> ')
try:
    ifile = open(fname)
except FileNotFoundError:
    print("In this directory(folder) don't have any file with you enterd name so again run & enter correct file name")
else:
    list1,list2 = [],[]
    print("No. of Lines in file ->",len(ifile.readlines()))
    print("No. of Words in file ->",len((open(fname).read()).split()))
    ifile.seek(0)
    for line in ifile.readlines():
        for word in line.split():
            word = word.strip()
            if word in list1:
                list2[list1.index(word)] += 1
            else:
                list1.append(word)
                list2.append(1)


    for item in list1:
        print (item, list2[list1.index(item)])
