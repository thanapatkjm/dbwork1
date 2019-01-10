import csv
reserv = []
with open('myGrades1.csv') as csvfile:
    file = csv.reader(csvfile, delimiter=',')
    for row in file:
        reserv.append(row)
        print(', '.join(row))
##        print(row[0][0:9])
##        print(row[0:2])
##    print(reserv)
    print("-------------------------------------------------------")
    print("\n")
        

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
    semester = input("which semester/year you want to insert?\n")
    subject = input("Subject ID ?\n")
    section = input("Section ?\n")
    grade = input("Grade?\n")
    reserv_edit=[]
    checkTerm=False
    check=False
    for row in reserv:
        if(checkTerm):
            if(row[0][0:9]==subject):
                row[2]=section
                row[3]=grade
                check=True
        if(row[0]==semester):
            checkTerm=True
        if(row[0]=="Total Credits"):
            checkTerm=False
        reserv_edit.append(row)
    if(check):
        print("Edit Done!!!\n\n")
    else:
        print("Could not find value match with input")
    print(reserv_edit)
   

##def insert():
##    semester = input("which semester/year you want so insert?\n")
##    subject = input("Subject Name ?\n")
##    credit = input("Subject's credit?\n")
##    grade = input("Grade?\n")
##    for i in file
##        if(i==semester)


start()
