import unittest

class TestCaseName(unittest.TestCase):
    
    def test_method(self):
        self.assertEqual(2 * 2, 5, msg='Видим и в этой вселенной не работает :-(')
        
if __name__ == '__main__': 
    unittest.main()
    
    
#  python3 -m unittest tests.py -v