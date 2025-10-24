class Bank:
    
    def __init__(self,owner,balance):
        self.owner=owner
        self.balance=balance

    def deposit(self):
        try:
            d=int(input("enter amount to deposit: "))
            self.balance+=d
        except ValueError:
            print("Invalid input only numbers for depositing amount ")

    def withdraw(self):
        try:
            w=int(input("enter the amount you want to withdraw: "))
            if w>self.balance:
                print(f"Your current amount is {self.balance} and you are trying to withdraw {w} which is not possible")
            else:
                self.balance-=w   
        except ValueError:
            print("Invalid input only numbers for withdrawing amount ")
        
    
    def show(self):
        print(f"your current balance is {self.balance}")


def owner_valid(owner):
    if owner.isalpha():
        return owner
    else:
        raise ValueError("The name must be only alphabets")
        

d={"surya":5000,"prakash":1000}     

try:

    owner=input("enter your name: ")
    own=owner_valid(owner)
    if own in d:
        bank1=Bank(own,d[own])
        print(f"for {own} the balance is {d[own]}")
    else:
        print("The entered name is not in DB")
        bank1=None    
           
    
except ValueError as e:
    print("Invalid input: ",e)   
else:
    
    while bank1:
        enter=input("enter what to perform {Deposit=d/Withdraw=w/Show Balance=s/exit}: ").lower()

        if enter=="d":
            bank1.deposit()
        elif enter=="w":
            bank1.withdraw()    
        elif enter=="s":
            bank1.show()
        elif enter=="exit":
            ex=input("Are u want to exit{yes/no}: ").lower()
            if ex=="yes":
                print(f"You exited and ur balance is {bank1.balance}")
                break
        



