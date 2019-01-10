import csv
reserv = []
with open('myGrades1.csv') as csvfile:
    file = csv.reader(csvfile, delimiter=',')
    for row in file:
        reserv.append(row)        

def start():
    global reserv
    func=""
    while(True):
        for row in reserv:
            print(row)
        print("-------------------------------------------------------")
        print("\n")
        func = input("What do you want?\n(i)insert , (e)edit ,(s)save \n")
        if(func=="e" or func=="i" or func=="s"):
            if(func=="e"):
                edit()
            elif(func=="i"):
                insert()
            else:
                save()
        else: print("Invalid Input\n--------------------")

def edit():
    global reserv
    semester = input("which semester/year you want to Edit?\n")
    subject = input("Subject ID you want to Edit?\n")
    section = input("Section you want to change to?\n")
    grade = input("Grade you want to change to?\n")
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
        print("Could not find value matched with input!!!\n\n")
    reserv=reserv_edit
    print("-------------------------------------------------------")
    print("\n")

def insert():
    global reserv
    semester = input("which semester/year you want to insert?\n")
    subject = input("Subject's ID and Name?\n")
    section = input("Section?\n")
    credit = input("Subject's credit?\n")
    grade = input("Grade?\n")
    array_insert=[subject,credit,section,grade]
    reserv_insert=[]
    check=False
    checkTerm=False
    for row in reserv:
        if(row[0]==semester):
            checkTerm=True
            check=True
        if(checkTerm):
            if(row[0]==""):
                reserv_insert.append(array_insert)
                checkTerm=False
        reserv_insert.append(row)
    if(check):
        print("Insert Done!!!\n\n")
    else:
        print("Could not find value matched with input!!!\n\n")
    reserv=reserv_insert
    print("-------------------------------------------------------")
    print("\n")

def save():
    global reserv
    file = open('myGrades1.csv','w+')
##    file.truncate()        
##    file.close
    with open('myGrades1.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        myList=[]
        myRow=[]
        for row in reserv:
            myRow=[]
            for index in row:
                myRow.append(index)
            writer.writerow(myRow)
    reserv=[]
    with open('myGrades1.csv') as csvfile:
        file = csv.reader(csvfile, delimiter=',')
        for row in file:
            reserv.append(row)  
    print("Save Done!!!")
    print("-------------------------------------------------------")
    print("\n")
    

start()
