import unittest
from passwordLocker import User, Credential

class TestClassUser(unittest.TestCase):

    """
    A Test class that defines test cases for the User class.
    """

    def setUp(self):
        self.new_user = User("uwase-diane","@August2016")
 
        """
        Method that runs before each individual test methods run.
        """

    def test_init(self):

        """
        test case to chek if the object has been initialized correctly
        """

        self.assertEqual(self.new_user.userName,'uwase-diane')
        self.assertEqual(self.new_user.password,'@August2016')

    def test_save_user(self):
        """
        test case to test if a new user instance has been saved into the User list
        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)


class TestClassCredentials(unittest.TestCase):

    """
    A test class that defines test cases for credentials class
    """ 
    def setUp(self):

        """
        Method that runs before each individual credentials test methods run.
        """

        self.new_credential = Credential('Instagram','uwas-dian','@August2016')

    def test_init(self):

        """
        Test case to check if a new Credentials instance has been initialized correctly
        """
        self.assertEqual(self.new_credential.accountName,'Instagram')
        self.assertEqual(self.new_credential.username,'uwas-dian')
        self.assertEqual(self.new_credential.password,'@August2016')

    def test_save_credentials(self):

        """
        test case to test if the crential object is saved into the credentials list.
        """
        self.new_credential.save_credentials()
        self.assertEqual(len(Credential.credential_list),1)


    def tearDown(self):

        '''
        method that does clean up after each test case has run.
        '''
        Credential.credential_list = []

    def test_save_many_accounts(self):

        '''
        test to check if we can save multiple credentials objects to our credentials list
        '''

        self.new_credential.save_credentials()
        test_credential = Credential("Yahoo","RahelBrhane","Rahel45xs")
        test_credential.save_credentials()
        self.assertEqual(len(Credential.credential_list),2)

    def test_detele_credential(self):

        """
        test method to test if we can remove an account credentials from our credentials_list
        """
        self.new_credential.save_credentials()
        test_credential = Credential("Yahoo","RaheBrhane","Rahel45xs")
        test_credential.save_credentials()

        self.new_credential.delete_credentials()
        self.assertEqual(len(Credential.credential_list),1)


    def test_find_credential(self):
        """
        test to check if we can find a credential entry by username and display the details of the credential
        """ 
        self.new_credential.save_credentials()
        test_credential = Credential("Yahoo","RaheBrhane","Rahel45xs")
        test_credential.save_credentials()

        username_credential = Credential.find_credential("RaheBrhane")
        self.assertEqual(username_credential.username,test_credential.username)

    def test_credential_exist(self):
        """
        test to check if we can return a true or false based on whether we find or can't find the credential.
        """
        self.new_credential.save_credentials()
        username_credential = Credential("Yahoo","RaheBrhane","Rahel45xs")
        
        username_credential.save_credentials()

        found_user = Credential.credential_exist("RaheBrhane")
        self.assertTrue(found_user)



if __name__ == '__main__':
    unittest.main()    
