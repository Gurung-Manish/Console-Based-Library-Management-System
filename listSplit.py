def listSplit():
    """ this module reads the stock file and splits the data and stores them in lists """
    global bookName
    global authorName
    global quantity
    global cost
    
    bookName=[] #bookName is declared as a list to store book names after retriving from the stock file
    authorName=[] #authorName is declared as a list and will store author names from the stock file for furher use
    quantity=[] #quantity is declared as a list and will store how many books are available
    cost=[] #cost is declared as a list and will store price for books
    
    with open("stock.txt","r") as f:
        lines=f.readlines()
        lines=[x.strip('\n') for x in lines]#this line will remove \n while reading the text files and storing in variable lines
        for i in range(len(lines)):
            ind=0
            for a in lines[i].split(','):
        #the above line will read each lines and take each data seperated by comma ',' and will store in bookName, authorName, quantity and cost respectively
        #as in the stock text file the data is stored in the following format : bookName,authorName,quantity,cost
                if(ind==0):
                    bookName.append(a)
                elif(ind==1):
                    authorName.append(a)
                elif(ind==2):
                    quantity.append(a)
                elif(ind==3):
                    cost.append(a.strip("$"))#strip will remove $ sign from the stock file which is the unit of cost
                ind+=1
