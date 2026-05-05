import time 
class validation:
    accountNumber=6304
    Password=1234

    def validate(self,a,b):
        print('\npls wait...\n')
        time.sleep(4)
        if validation.accountNumber != a or validation.Password!=b:
            print("Account number or password is incorrect..Try after sometime..!")
            exit()
        else:
            print("Validation Succesfully..!")
            return
        
class AccountOperations:
    v=validation()
    balance=0
    statement=[]
    def deposit(self,damount):
        self.statement.append(f"Deposit={damount}")
        print("\npls wait..\n")
        time.sleep(4)
        self.balance+=damount
        print("Amount deposited Succesfully..!!")
        print(f"Balance = {self.balance} ")
    
    def withdraw(self,wamount):
        print("\npls wait..\n")
        time.sleep(4)
        if wamount <=self.balance:
            print("Collect your amount..!")
            self.balance-=wamount
            print(f'Balance = {self.balance} ')
            self.statement.append(f"withdraw={wamount}")
        else:
            print("Insufficient balance..withdraw not possible..!")

    def changepin(self,oldpin,newpin):
        print("\nchanging pin..pls wait.\n")
        time.sleep(4)
        if oldpin== validation.Password:
            validation.Password=newpin
            print("Pin changed ..Succesfully")
        else:
            print("Invalid password..Try Again.!")
    
    def ministatement(self):
        print('\nGenerating mini statement..pls wait..\n')
        time.sleep(4)
        for x in self.statement:
            print(x)
            print(f"\nAcount Balance ={self.balance}")
        
    def exitApp(self):
        print("\nExiting ..pls wait..\n")
        time.sleep(4)
        print('\nThank you Again !!')
        exit()

print ("WELCOME TO UNION BANK")
a=int(input("Enter Account number:"))
b=int(input("Enter 4-digit ATM pin :"))
v=validation()
v.validate(a,b)
a=AccountOperations()

while (True):
    print("\n Choose from the following OPtions:")
    print("----------------------------------------")
    print("1.Deposit\n2.withdraw\n3.change pin\n4.mini statement\n5.exit")
    choice=int(input("\nEnter your choice:"))
    if choice==1:
        damount=int(input("Enter amount to be deposited :"))
        if damount%100==0 and damount>0:
            a.deposit(damount)
        else:
            print("Pls Enter the valid amount of multiples of Hundreds")
    elif choice==2:
        print(f"Balance={a.balance}")
        wamount=int(input("Enter the amount to be withdrawn:"))
        if wamount%100==0 and wamount>0:
            a.withdraw(wamount)
        else:
            print("Pls Enter valid amount in multiples of hundreds..")
    elif choice==3:
        oldpin=int(input("Enter the old pin :"))
        newpin=int(input("Enter new pin:"))
        confirmpin=int(input("confirm pin:"))
        if newpin==confirmpin:
            a.changepin(oldpin,newpin)
        else:
            print("New pin and Confirm pin arent matching...")
    elif choice==4:
        a.ministatement()
    elif choice==5:
        a.exitApp()
    else:
        print("Invalid Choice !! Try Again..!")