from test.TestEzTvClient import TestEzTvClient
from test.TestYtsClient import TestYtsClient
import unittest

def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestEzTvClient())
    suite.addTest(TestYtsClient())
    return suite

if __name__ == '__main__':
    #TestEzTvClient().runAll()
    #TestYtsClient().runAll()
    unittest.TextTestRunner().run(suite())
   

