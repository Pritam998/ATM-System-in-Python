class ATM :
    def __init__(self):
        self.login = False
        self.user_data = {101:{"name":"Pritam998","pin":9307,"balance":5000,"withdraw":[],"deposite":[]},
                          102:{"name":"Dakait123","pin":9347,"balance":3000,"withdraw":[],"deposite":[]}}
        self.current_user = None
        self.__login_history = []
        self.__bank_transaction_with = []       #This is for bank (Private / Secure)
        self.__bank_transaction_depo = []

    def log(self):
        j = 0
        while True :                                            #This programme will run first 
            print("            1 for login")                                 
            print("            2 or any number for Quit")
            co = int(input("Enter the number : "))                #check if user want to login or not
            if co == 1 :
                print("Enter Account number and User pin to Login : ")
                xy = int(input(" Enter Account Number ->  "))
                xyz = int(input(" Enter User Pin ->  "))
                if xy in self.user_data and xyz == self.user_data[xy]["pin"] :
                    print(" Welcome to Desi Bank...")
                    self.login = True
                    self.current_user = xy
                    self.__login_history.append(self.user_data[xy]["name"])
                    break
                else :
                    if j >= 2:                                               # if fail force quit
                        print(" System Protection Turning On !!!")
                        quit()
                    else :
                        j+=1
                        print(f"You have {3-j} attempt left")    # 3 Attempt
            else :
                quit()
        self.menu()            # If Login successfull enter in menu function 

        
    def menu(self):                                        #This is like home page for any website
        if not self.login :
            print(" Please Login First")
        else :
            while True:
                print("                      1 for Deposite")
                print("                      2 for Withdraw")
                print("                      3 for Check Balance")
                print("                      4 for Check Transaction History")
                print("                      5 for Logout")

                ko = int(input("Enter the number : "))

                if ko == 1:
                    self.deposite_money()
                elif ko == 2:
                    self.withdraw_money()
                elif ko == 3:
                    self.check_balance()
                elif ko == 4:
                    self.check_history()
                elif ko == 5:
                    self.login = False                             #This will make login false again
                    self.current_user = None
                    print("Logged out successfully")
                    break    
                else:
                    print("Invalid Enter ")
    
    def withdraw_money(self):
            print("Welcome to Withdraw Section")
            cd = int(input("Enter amount you wanna widhraw : "))
            if cd < 0 :
                print(" Number cannot be Negative")
            elif self.user_data[self.current_user]["balance"] >= cd :  #Check if user has sufficient funds
               self.user_data[self.current_user]["balance"] -= cd
               print(f"Your Withdrawal is successful for Rupees {cd}")
               self.user_data[self.current_user]["withdraw"].append(cd)    # Personal History
               self.__bank_transaction_with.append(cd)                       # Bank History
            else :
                print(" Insufficient Funds ")


    def deposite_money(self):
        print("Welcome to Deposite Section")
        ccd = int(input("Enter amount you wanna Deposite : "))   # Negative number checking
        if ccd < 0 :
            print("Number cannot be Negative")
        elif ccd > 50000 :
            print("You can add money upto 50000 only")
        else :
            self.user_data[self.current_user]["balance"] += ccd
            self.user_data[self.current_user]["deposite"].append(ccd)     # Personal History
            self.__bank_transaction_depo.append(ccd)                    # Bank History
            print(f"Deposite successful of Rupees {ccd}")

    def check_balance(self):
        print(f"Current Balance { self.user_data[self.current_user]['balance'] }")

    def check_history(self):
        print("                   1 for withdraw History")
        print("                   2 for Deposite History")
        print("                   3 for Both ")

        gf = int(input(" Enter the number : "))
        if gf == 1:
            print(self.user_data[self.current_user]["withdraw"])
        elif gf == 2:
            print(self.user_data[self.current_user]["deposite"])
        elif gf == 3:
            print(f" Withdrawal History {self.user_data[self.current_user]["withdraw"]}\n Deposite History {self.user_data[self.current_user]["deposite"]}")
        else:
            print("Enter appropriate Number")
        


atm = ATM()

atm.log()
            
            
           
          


        



            



         
           


    