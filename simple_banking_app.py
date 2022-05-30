import random
import time

def account_number_generator(n):
    acct_num=""
    for i in range(n):
        acct_num += str(random.choice(range(1, 10)))
      
    return acct_num.zfill(10)
print(account_number_generator(9))

def transaction_pin_generator(n):
    pin=""
    for i in range(n):
        pin += str(random.choice(range(1, 4)))
      
    return pin.zfill(4)
print(transaction_pin_generator(3))



def check_balance():
    pass


def deposit(amt):
    pass

def withdraw(amount):
    pass



data = {}

print("\n###############################")
print("WELCOME TO CARTCON BANKING APP")
print("###############################\n")

while True:
    print(f"""To log into your account press: 1
            To create a new account press: 2
            To log out press :3
            """)
    user_input= int(input(":>>"))
    
    if user_input==1:
        print("\nPlease enter your user Login Pin.")
        user_login = input("::>")
        # user_data = data.get(user_login, 0)
        # user_data = user_data["login_pin"]
        # user_data = data.get(login_pin,False)
        user_data = data.get(user_in,False)
        
        first_user_data =data.get(account_number, 0)
        firstname= first_user_data["first_name"]
        last_user_data =data.get(account_number, 0)
        lastname= last_user_data["first_name"]
        user_data =data.get(account_number, 0)
        account_balance= user_data["balance"]
        
        if user_data:
            print(f"""\nWelcome {firstname} {last_name} your account balance is:{account_balance} \n
                To make deposit into your account press: 4
                To make withdrawals from your account press: 5
                To log out press :6\n
                  """)
            # user_log:
        else:
            print("Login pin does not exist")
    elif user_input == 2:
        first_name = input("Please enter your 'First Name'::>").title()
        last_name = input("Please enter your 'Last Name'::>").title()
        account_number = account_number_generator(9)
        login_pin = input("Please enter your 'Login pin'::>")
        transaction_pin = transaction_pin_generator(3)
        
        data[account_number] = {
            "first_name": first_name,
            "last_name" : last_name,
            "login_pin" : login_pin,
            "transaction_pin" : transaction_pin,
            "balance": 0
                         }
        user_data =data.get(account_number, 0)
        account_balance= user_data["balance"]
        print("\nCreating account...")
        time.sleep(3)
        print("Completing setup...")
        time.sleep(2)
        print(f"""\nWelcome '{first_name} {last_name}'! You have successfully created an account with us at CARTCON Bank.\n 
        Your Account Number is: {account_number}
        Your Transaction Pin is: {transaction_pin}
        Your Login pin is: {login_pin}
        your current account balance is: {account_balance}
        \n\n CARTCON BANK Support Team\n""")
        
        
    elif user_input ==3:
        print("Loging you out......")
        time.sleep(3)
        print("You have successfully logged out.")
        break
    
    else:
         print("Invalid user input")
    

