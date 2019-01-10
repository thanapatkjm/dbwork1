import csv

with open('myGrades1.csv') as csvfile:
    file = csv.reader(csvfile, delimiter=',')
    for row in file:
        print(', '.join(row))
##        print(row[0][0:9])
        print(row[0:2])
    print()
        

def start():
    func=""
    while(True):
        func = input("What do you want?\n(i)insert , (e)edit ,(s)save \n")
        if(func=="e" or func=="i" or func=="s"):
            if(func=="e"):
                edit()
            elif(func=="i"):
                print(2)
            else:
                print(3)
            break
        else: print("Invalid Input\n--------------------")
        
def edit():
    with open('myGrades1.csv') as csvfile:
        file = csv.reader(csvfile, delimiter=',')
        semester = input("which semester/year you want so insert?\n")
        subject = input("Subject ID ?\n")
        credit = input("Subject's credit?\n")
        section = input("Section ?\n")
        grade = input("Grade?\n")
        check=False
        for row in file:
##            print(len(row))
            if(check=True):
                if(row[0][0:9]==subject):
                    row[1]= 
            if(row[0]==semester):
                check=True
                print(1)
            if(row[0]==''):
                check=False
                for i in row
                print(1)
            
##    

##def insert():
##    semester = input("which semester/year you want so insert?\n")
##    subject = input("Subject Name ?\n")
##    credit = input("Subject's credit?\n")
##    grade = input("Grade?\n")
##    for i in file
##        if(i==semester)


start()
