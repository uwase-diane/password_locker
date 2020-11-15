#!/usr/bin/env python3.6
import pyperclip
import random
from passwordLocker import User, Credential

print("------------------------------------------")
print("------------------------------------------")
print("     P A S S W O R D  L O C K E R         ")
print("------------------------------------------")
print("------------------------------------------")

def create_user(username,password):

    '''
    Function to create a new user
    '''
    new_user = User(username,password)
    return new_user

def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()

def delete_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

def display_user():
    """
    Function to display existing user
    """
    return User.display_user()

def login_user(userName,password):
    """
    function that checks whether a user exist and then login the user in.
    """
    check_user = Credential.user_verify(userName,password)
    return check_user

def create_new_credential(accountName,username,password):
    """
    Function that creates new credentials for a given user account
    """
    new_credential = Credential(accountName,username,password)
    return new_credential

def save_credential(credentials):
    """
    Function to save Credentials to the credentials list
    """
    credentials.save_credentials()

def display_accounts_credentials():
    """
    Function that returns all the saved credential.
    """
    return Credential.display_credentials()

def delete_credential(credentials):
    """
    Function to delete a Credentials from credentials list
    """
    credentials.delete_credential()

def find_credential(username):
    """
    Function that finds a Credentials by an user name and returns the Credentials that belong to that account
    """
    return Credential.find_credential(username)

def chec_credentials(username):

    return Credential.credential_exist(username)

def copy_password(username):
    """
    A funct that copies the password using the pyperclip framework
    """
    return Credential.copy_password(username)


def generate_password():

        """Generate a random password string of letters and digits and special characters"""
        random_number = random.randint(000,111)
        return random_number
         
   

def main():
    print("HELLO, WELCOME TO YOUR PASSWORD LOCKER... \n cu -- Create New User \n li -- Have an Account \n")
    short_code=input("").lower().strip()

    if short_code == 'cu':
        print('-------')
        print("SIGN UP")
        print('-------')
        username = input("USERNAME: ")

        while True:
            print(" pa -- Enter your password: \n gp -- Generate password")
            p_Choice = input().lower().strip()
            if p_Choice == 'pa':
                password = input("Enter password\n")
                break
            elif p_Choice == 'gp':
                password = generate_password()
                break
            else:
                print("INVALID PASSWORD ----PLEASE TRY AGAIN")

        save_user(create_user(username,password))
        print('------------------------------------------------------------')
        print(f"HELLO {username}, YOU ACCOUNT HAS BEEN CREATED SUCCESSFULLY")
        print('------------------------------------------------------------')

    elif short_code == "li":
        print("------------------------------------------------------------")
        print("ENTER YOUR USER NAME AND YOUR PASSWORD TO LOGIN: ")
        print('------------------------------------------------------------')
        username = input("USER NAME: ")
        password = input("PASSWORD: ")
        login = login_user(username,password)

        if login_user == login:
            print(f"HELLO {username}. WELCOME TO PASSWORD LOCKER MANAGER")
            print('\n')
    
    while True:
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print("USE THOSE SHORT CODES: \n CC -create a new credential \n DC- Display credential \n FC- Find a credential \n GP-Generate password \n D-Delete credential \n EX- Exit the application \n")
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')

        short_code = input().lower().strip()
        if short_code == "cc":
            print("CREATE NEW CREDENTIAL")
            print("---------------------")
            print("Account Name: ")
            accountName = input().lower()
            print("Username: ")
            username = input()

            while True:
                print("TP -WRITE YOUR PASSWORD: \n GP - GENERATE YOUR PASSWORD")
                p_Choice = input().lower().strip()
                if p_Choice == 'tp':
                    password = input("ENTER YOUR OWN PASSWORD\n")
                    break
                elif p_Choice == 'gp':
                    password = generate_password()
                    break
                else:
                    print("invalid password ")

            save_credential(create_new_credential(accountName,username,password))
            print('\n')
            print(f"Account Credential for: {accountName} \n- Username: {username} \n- Password: {password} ")
            print("\n")
        elif short_code == "dc":
            if display_accounts_credentials():
                print("HERE'S THE LIST OF ACCOUNTS: ")
                print('----------------------------')

                for account in display_accounts_credentials():
                    print(f"Acount:{account.accountName} \n UserName: {username} \n Password: {password}")
                    print("-----------------------------------------------------------------------------")

            else:
                print("No credentials saved yet")

        elif short_code == 'fc':
            print("SEARCH ACCOUNT NAME OF YOUR CHOICE")
            search_name = input().lower()
            if find_credential(search_name):
                search_cred = find_credential(search_name)
                print(f"Account Name: {search_cred.accountName}")
                print('-----------------------------------------')
                print(f"User Name: {search_cred.username} Password: {search_cred.password}")
                print('--------------------------------------------------------------------')

            else:
                print("Credential does not exist")
                print('\n')

            
        elif short_code == "d":
            print("DELETE ACCOUNTS YOU WANT")
            search_name = input().lower()
            if find_credential(search_name):
                search_cred = find_credential(search_name)
                print('--------------------------------')
                search_cred.delete_credentials()
                print('\n')
                print(f"Your store credentials: {search_cred.accountName} deleted successfully")
                print('\n')

            else:
                print("That credential does not exist")

        elif short_code == 'gp':
            password = generate_password()
            print(f"{password} have been generated successfull") 

        elif short_code == 'ex':
            print("THANKS FOR USING PASSWORD LOCKER")
            break
        else:
            print("WRONG ENTRY")  
    else:
        print("please enter a valid input to continue")                     


if __name__ == '__main__':
    main()