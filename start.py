import dt
import listSplit
import borrow
import returnBook
def start():
    """this module is the main module where each and every module is imported and where the program begins """
    while(True): #as long as it is true and the loop does  not have break the loop will continue
        print("        _____________________________________________________________________________________________________________________________________________________________________________________________")
        print("        \                                                                         _____           _____   ______   __    __   _____                                                                 /")                                                                                                                                                                       
        print("         \                                                           |         | |       |       |       |      | |  \  /  | |                                                                     / ")
        print("          \                                                          |    ^    | |       |       |       |      | |   \/   | |                                                                    /  ")
        print("           \                                                         |   / \   | |-----  |       |       |      | |        | |-----                                                              /   ")
        print("            \                                                        |__/   \__| |_____  |_____  |_____  |______| |        | |_____                                                             /    ")
        print("             \                                                                           _________   ______                                                                                    /     ")
        print("              \                                                                              |      |      |                                                                                  /      ")
        print("               \                                                                             |      |      |                                                                                 /       ")
        print("                \                                                                            |      |      |                                                                                /        ")
        print("                 \                                                                           |      |______|                                                                               /         ")
        print("                  \                                                                                                                                                                         /          ")
        print("                  /                    ______          _____  ______   ___    _____                     ____ ____  _____    _____         ____        ____                                \          ")
        print("                 /                    |      | \    / |      |      | |   \  |     \            |           |     |     \  |     \       /    \      |    \   \     /                      \         ")
        print("                /                     |      |  \  /  |      |      | |    | |      |           |           |     |      | |      |     /      \     |     |   \   /                        \        ")
        print("               /                      |      |   \/   |_____ |      | |___/  |      |           |           |     |_____/  |_____/     /________\    |____/     \ /                          \       ") 
        print("              /                       |      |   /\   |      |      | |   \  |      |           |           |     |     \  |     \    /          \   |    \      |                            \      ")
        print("             /                        |      |  /  \  |      |      | |    \ |      |           |           |     |      | |      \  /            \  |     \     |                             \     ")
        print("            /                         |______| /    \ |      |______| |     \|_____/            |______ ____|____ |_____/  |       \/              \ |      \    |                              \    ")
        print("           /                                                                                                                                                                                     \   ")
        print("          /                                                                                                                                                                                       \  ")
        print("         /                                                                                                                                                                                         \ ")  
        print("        /___________________________________________________________________________________________________________________________________________________________________________________________)")
        print("")
        print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("")
        print("                                                                                    Press and enter 1 to Display")
        print("")
        print("                                                                                  Press and enter 2  to Borrow a book")
        print("")
        print("                                                                                  Press and enter 3  to Return a book")
        print("")
        print("                                                                                     Press and enter 4  to exit")
        print("")
        print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        print("")
        try: # this try function will only let input be an integer
            a=int(input("                                                                                         Select a choice from 1-4: "))
            if(a==1):
                print("")
                print("")
                print("                                                                                       The available books are displayed below.")
                print("")
                listSplit.listSplit()
                for i in range(3):
                    print("                                                                                           "+listSplit.bookName[i])
                    print("")
                print("")
            elif(a==2):
                listSplit.listSplit()
                borrow.borrowBook()
            elif(a==3):
                listSplit.listSplit()
                returnBook.returnBook()
            elif(a==4):
                print("")
                print("")
                print("                                                                          !!!!   Thank you for using library management system   !!!!")
                print("")
                print("")
                break
            else:
                print("")
                print("")
                print("                                                                                      Please enter a valid choice from 1-4")
                print("")
                print("")
        except ValueError: #this is the except part of try which would check if the input is integer or not
            print("")
            print("")
            print("                                                                                        Please input as suggested.")
            print("")
            print("")
start()


