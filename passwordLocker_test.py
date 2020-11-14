import unittest
from passwordLocker import User

class TestClass(unittest.TestCase):

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

        self.assertEqual(self.new_user.userName,"uwase-diane")
        self.assertEqual(self.new_user.password,"@August2016")


if __name__ == '__main__':
    unittest.main()    
