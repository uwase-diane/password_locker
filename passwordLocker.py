#!/usr/bin/env python3.6
import pyperclip


class User:

    """
    Create User class that generates new instances of a user.
    """

    user_list = []

    def __init__(self, userName, password):
        self.userName = userName
        self.password = password

    def save_user(self):
        """
        A method that saves a new user instace into the user list
        """  
        User.user_list.append(self)

    @classmethod
    def display_user(cls):
        return cls.user_list  

    def delete_user(self):
        '''
        delete_account method deletes a  saved account from the list
        '''
        User.user_list.remove(self)

        

class Credential():

    credential_list = []

    def __init__(self,accountName,username,password):


        """
        method that defines user credentials to be stored
        """    
        self.accountName = accountName
        self.username = username
        self.password = password   
         

    def save_credentials(self):
      
        """
        method to store a new credential to the credentials list
        """
        Credential.credential_list.append(self)
       
    def delete_credentials(self):

        """
        delete_credentials method that deletes an account credentials from the credentials_list
        """

        Credential.credential_list.remove(self)

  
    @classmethod
    def find_credential(cls,username):

        """
        Method that takes in a username and returns a credential that matches that account_name.
        """
        for cred in cls.credential_list:
            if cred.username == username:
                return cred

              

    @classmethod
    def credential_exist(cls,username):
        for cred in cls.credential_list:
            if cred.username == username:
                return True
            
        return False

    @classmethod
    def display_credentials(cls):
        """
        Method that returns all items in the credentials list
        """
        return cls.credential_list

    @classmethod
    def copy_password(cls,username):
        found_credential = Credential.find_credential(username)
        pyperclip.copy(found_credential.password)


        



