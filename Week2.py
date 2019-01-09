import csv


with open('myGrades.csv', newline='') as csvfile:
    file = csv.reader(csvfile, delimiter=' ',quotechar='|')
    for row in file:
        print(' '.join(row))
        print(row)
##
##def start():
##    func=""
##    while(func!="e" or func!="i" or func!="s"):
##        func = input("What do you want?\n(i)insert , (e)edit ,(s)save \n")
##        if(func=="e" or func=="i" or func=="s"):
##            if(func=="e"):
##                print(1)
##            elif(func=="i"):
##                print(2)
##            else:
##                print(3)
##            break
##        else: print("Invalid Input\n--------------------")
##    
##start()
##
##def insert():
##    semester = input("which semester/year you want so insert?\n")
##    subject = input("Subject Name ?\n")
##    credit = input("Subject's credit?\n")
##    grade = input("Grade?\n")
##    for i in file
##        if(i==semester)
