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


if __name__ == '__main__':
    unittest.main()    
