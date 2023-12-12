print("WELCOME TO THE GRANN'S PHONE DIRECTORY")
print("1. Add a record ")
print("2. Search a record ")
print("3. Update a record")
print("4. Sort the record alphabetically ")
print("5. Delete a record ")
print("6. Quit. ")

directory={}
x=int(input("Enter your choice: : "))
while(x!=6):
    if x==1:
        i=(input("Enter your name: "))
        if i in directory:
            print("This Record already exists.")
            y=input("Do you really want to update this contact? (y/n): ").lower()
            if y=="y":
                if (i.isalpha()):
                    j=(input("Enter your 10-digit phone number: "))
                    if j.isnumeric() and len(j)==10:
                        directory.update({i:j})
                        print("Record Updated successfully! ")
                    else:
                        print("Please enter Digits OR 10-digit Number only")
                else:
                    print("Enter alphabets only")
            elif y=="n":
                print("Record is not updated.")
            else:
                print("Please write Y or N")
        else:
            if (i.isalpha()):
                j=(input("Enter your 10-digit phone number: "))
                if j.isnumeric() and len(j)==10:
                    directory.update({i:j})
                    print("Record added successfully! ")
                else:
                    print("Please enter Digits OR 10-digit Number only")
            else:
                print("Enter alphabets only")
        
    elif x==2:
        z=input("Please enter the name you want to search? : ")
        if z in directory:
            print(z," : ",directory[z])
        else:
            print("Nothing exists with this name.")
    elif x==3:
        i=(input("Enter your name: "))
        if i in directory:
            y=input("Do you really want to update this contact? (y/n): ").lower()
            if y=="y":
                if (i.isalpha()):
                    j=(input("Enter your 10-digit phone number: "))
                    if j.isnumeric() and len(j)==10:
                        directory.update({i:j})
                        print("Record Updated successfully! ")
                    else:
                        print("Please enter Digits OR 10-digit Number only")
                else:
                    print("Enter alphabets only")
            elif y=="n":
                print("Record is not updated.")
            else:
                print("Please write Y or N")
        else:
            print("Nothing exists with this name.")
    elif x==4:
        l=list(directory.keys())
        l.sort()
        sorted_directory={i:directory[i] for i in l}
        print("The Sorted record is: ",sorted_directory)

    elif x==5:
        d=(input("Please enter the name you want to Delete? : "))
        del directory[d]
        print("Record Deleted successfully! ")
            
    print("WELCOME TO THE GRANN'S PHONE DIRECTORY")
    print("1. Add a record ")
    print("2. Search a record ")
    print("3. Update a record")
    print("4. Sort the record alphabetically ")
    print("5. Delete a record ")
    print("6. Quit. ")            
    x=int(input("Enter your choice: : "))
print("Thankyou")        
