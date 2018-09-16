from selenium import webdriver
import unittest

class TestPageLoad(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get('https://code.gov')
        self.assertIn('code.gov', self.browser.title)

'''
class TestHomeArea(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def test_fake(self):
        self.assertEqual(1,1)
'''

if __name__ == '__main__':
    unittest.main(verbosity=2)
