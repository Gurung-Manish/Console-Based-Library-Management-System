import dt
import listSplit
def returnBook():
    """ this module has program to return borrowed books and make a text file for books returned """
    while(True):
        try: #if the name of borrower is input correct the program will enter the reading lines part
            while(True):  #The following while loop will continue until there is a break to take First Name of the borrower
                print("")
                print("")
                print("                                                                                            What is your name ? ")
                print("")
                print("")
                firstName=input("                                                                                              First name : ")
                if firstName.isalpha():
                    break
                print("")
                print("                                                                                       Please input alphabet from A-Z")
            
                print("")
            while(True): #The following while loop will continue until there is a break to take Last Name of the borrower
                lastName=input("                                                                                               Last name : ")
                print("")
                if lastName.isalpha():
                    break
                print("")
                print("                                                                                       Please input alhpabet from A-Z.") 
                print("")
                
            a="Borrow-"+firstName+lastName+".txt" #a is initialized with borrow with first name and second name of user with extension .txt
            with open(a,"r") as f:
                lines=f.readlines()
                lines=[a.strip("$") for a in lines]
        
            with open(a,"r") as f:
                data=f.read()
                print(data)
            break
        except FileNotFoundError: # this is the except part of try which would check if the input name of user is correct or na=ot
            print("                                                                                 The borrower name you entered is incorrect !")
            print("")

    b="Return-"+firstName+lastName+".txt" #b is initialized with return with first name and second name of user with extension .txt
    with open(b,"w+")as f:
        f.write(" ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        f.write("|                                                                                                Oxford Library Database                                                                                         |\n")
        f.write("                                                                                                  Returned By:"+" "+firstName+" "+lastName+"                                                                                      \n")
        f.write("|                                                                                            Date:"+" "+dt.getDate()+"    Time:"+dt.getTime()+"                                                                                   |\n")
        f.write(" ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        f.write("\t\t\t\t\tS.N.\t\t\t\t\tBook Name\t\t\t\t\tCost\n")


    total=0.0
    with open(a,"r") as f:
        data=f.read()
    for i in range(3):
        if listSplit.bookName[i] in data:
            with open(b,"a") as f:
                f.write("\t\t\t\t\t"+str(i+1)+"\t\t\t\t\t"+listSplit.bookName[i]+"\t\t\t\t\t$"+listSplit.cost[i]+"\n")
                listSplit.quantity[i]=int(listSplit.quantity[i])+1
            total+=float(listSplit.cost[i])
            
    print("\t\t\t\t\t\t\t\t\t\t\t"+" Total for now :$"+str(total))
    print("")
    print("")
    print("")
    check=True #check is declared and initialized as True
    while (check==True): # as long as check is true the loop will run
        print("                                                                                     Is the book return date expired?")
        print("                                                                                      Press Y for Yes and N for No")
        stat=input("                                                                                                ")
    
        if(stat.upper()=="Y"):
            print("                                                                                 By how many days was the book returned late?")
            try:
                day=int(input("                                                                                     "))
                fine=2*day
                with open(b,"a")as f:
                    f.write("\t\t\t\t\t\t\t\t\t Fine: $"+ str(fine)+"\n")
                total=total+fine
            


                print("                                                                                                 Final Total"+ "$"+str(total))
                print("")
                print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
                with open(b,"a")as f:
                    f.write("\t\t\t\t\t\t\t\t\tTotal: $"+ str(total))
                
                    
                with open("Stock.txt","w+") as f:
                        for i in range(3):
                            f.write(listSplit.bookName[i]+","+listSplit.authorName[i]+","+str(listSplit.quantity[i])+","+"$"+listSplit.cost[i]+"\n")
                check=False # if the input is y and all the process is completed this line will help the loop terminate
            except ValueError:
                print("                                                                                      Please input days in number.")
                check=True # if the input is not either y or n the loop still continues
        elif (stat.upper()=="N"):
            print("                                                                                                  Final Total"+ "$"+str(total))
            print("")
            print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
            with open(b,"a")as f:
                f.write("\t\t\t\t\t\t\t\t\tTotal: $"+ str(total))
            
                
            with open("Stock.txt","w+") as f:
                    for i in range(3):
                        f.write(listSplit.bookName[i]+","+listSplit.authorName[i]+","+str(listSplit.quantity[i])+","+"$"+listSplit.cost[i]+"\n")
            check=False # even if the input is n the program must terminate. hence, check is initialized to False
        else:
            print("")
            print("                                                                                     Please press either 'y' or 'n'")
            print("")
            check=True # if the input is not either y or n the loop still continues
