
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


        



