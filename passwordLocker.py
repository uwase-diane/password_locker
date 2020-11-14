
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
         



        



