#!/usr/bin/env python3.6
import pyperclip

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
    credentials.save_credential()

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
    '''
    generates a random password for the user.
    '''
    auto_password=Credential.generate_password()
    return auto_password 
         
   

def main():
    print("HELLO, WELCOME TO YOUR PASSWORD LOCKER... \n cu -- Create New User \n li -- Have an Account \n")
    short_code=input("").lower().strip()

    if short_code == 'cu':

        print("SIGN UP")
        username = input("USERNAME: ")

        while True:
            print(" pa -- Enter your password: \n gp -- Generate password")
            password_Choice = input().lower().strip()
            if password_Choice == 'pa':
                password = input("Enter password\n")
                break
            elif password_Choice == 'gp':
                password = generate_password()
                break
            else:
                print("INVALID PASSWORD ----PLEASE TRY AGAIN")
                                   

if __name__ == '__main__':
    main()



















if __name__ == '__main__':
    main()