import dt
import listSplit
def borrowBook():
    """ this module contains program to borrow book and make a text file"""
    success=False #success is declared and initialized with False
    
    #The following while loop will continue until there is a break to take First Name of the borrower
    while(True):
        print("")
        print("")
        print("                                                                                            What is your name ? ")
        print("")
        print("")
        firstName=input("                                                                                              First name : ")
        if firstName.isalpha(): #variable.isalpha() will check if the input value contains any character like space,$,@ or any numbers
            break #if the above statement after checking input does not find any character or number it will break the loop
        print("")
        print("                                                                                       Please input alphabet from A-Z")
        print("")
        
    #The following while loop will continue until there is a break to take Last Name of the borrower
    while(True):
        lastName=input("                                                                                               Last name : ")
        print("")
        if lastName.isalpha():
            break
        print("")
        print("                                                                                       Please input alhpabet from A-Z.")
        print("")
        
            
    t="Borrow-"+firstName+lastName+".txt" #t is initialized with borrow with first name and second name of user with extension .txt
    with open(t,"w+") as f:
        f.write(" ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        f.write("|                                                                                                 Oxford Library Database                                                                                        |\n")
        f.write("                                                                                                  Borrowed By:"+" "+firstName+" "+lastName+"                                                                                       \n")
        f.write("|                                                                                            Date:"+" "+dt.getDate()+"    Time:"+dt.getTime()+"                                                                                   |\n")
        f.write(" ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        f.write("\t\t\t\t\tS.N.\t\t\t\t\tAuthor Name\t\t\t\t\tBook Name \n" )
        
    
    #the following while loop will continue as long as success is False
    while success==False:
        print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("                                                                                         Please select an option below:")
        for i in range(len(listSplit.bookName)):
            print("                                                                                      Enter", i, "to borrow book", listSplit.bookName[i])
        print(" ")
        print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    
        try:  #this try function will run if the input is an integer
            a=int(input("                                                                                                "))
            try: #this try function will run as long as the input to select book is within range
                if(int(listSplit.quantity[a])>0):
                    print("")
                    print("                                                                                           "+listSplit.quantity[a]+" Books are available")
                    with open(t,"a") as f:
                        f.write("\t\t\t\t\t1.\t\t\t\t\t"+ listSplit.authorName[a]+"\t\t\t\t\t"+listSplit.bookName[a]+"\n")

                    listSplit.quantity[a]=int(listSplit.quantity[a])-1
                    with open("Stock.txt","w+") as f:
                        for i in range(3):
                            f.write(listSplit.bookName[i]+","+listSplit.authorName[i]+","+str(listSplit.quantity[i])+","+"$"+listSplit.cost[i]+"\n")


                    # loop to borrow multiple book 
                    loop=True
                    count=1 #count is initialized and declared for the sake of adding serial number in the text file that will be created for borrowing book
                    while loop==True: #this loop will continue as long as value of loop is True
                        choice=str(input("                                                      Do you want to borrow more books? However you cannot borrow same book twice. Press y for yes and n for no."))
                        print("")
                        if(choice.upper()=="Y"): #This if statement will check if the input value is y or not and if it is the will enter the lines below
                            count=count+1 #count is increased as it is after the first book borrowed and will have higher serial number while writing in the borrowed text file
                            print("")
                            print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                            print("                                                                                            Please select an option below:")
                            for i in range(len(listSplit.bookName)):
                                print("                                                                                        Enter", i, "to borrow book", listSplit.bookName[i])
                            print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                            a=int(input("                                                                                                "))
                            if(int(listSplit.quantity[a])>0): #this if statement will check if more books are available for second borrow and so on.
                                print("                                                                                           "+listSplit.quantity[a]+" Books are available")
                                print("")
                                with open(t,"a") as f:
                                    f.write("\t\t\t\t\t"+str(count) +".\t\t\t\t\t"+ listSplit.authorName[a]+"\t\t\t\t\t"+listSplit.bookName[a]+"\n")

                                listSplit.quantity[a]=int(listSplit.quantity[a])-1
                                with open("Stock.txt","w+") as f:
                                    for i in range(3):
                                        f.write(listSplit.bookName[i]+","+listSplit.authorName[i]+","+str(listSplit.quantity[i])+","+"$"+listSplit.cost[i]+"\n")
                                        success=False #success is initialized as False so that more books could be borrowed
                            else:
                                print("                                                                                           No more books availabe")
                                print("                                                                                           Please choose another")
                                loop=True
                        elif (choice.upper()=="N"):
                            print ("                                                                                      Thank you for borrowing books from us. ")
                            print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                            loop=False #here loop is initialized to False so that there is no more borrowing and program will not ask if user wants to borrow more books
                            success=True
                        else:
                            print("                                                                                            Please choose as instructed")
                        
                else:
                    print("                                                                                                      Book is not available")
                    print("")
                    success=False
                    borrowBook() #here the program returns to borrowBook function as there is no book available
                    
            except IndexError: #this is the except part of try function which would check if the selected number for book is within range
                print("")
                print("                                                                                     Please choose book acording to their number.")
                print("")
        except ValueError: # this is the except part of try which would check if the input is integer or not
            print("")
            print("                                                                                             Please choose as suggested.")
            print("")
