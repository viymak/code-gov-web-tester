from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import keyboard
from time import sleep
import unittest

class TestPageLoad(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def testPageTitle(self):
        self.browser.get('https://code.gov')
        self.assertIn('code.gov', self.browser.title)



class TestHomeArea(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)
        self.browser.get('https://code.gov')

    def testOpenTasks(self):
        button = self.browser.find_element_by_xpath('//button[text()="Explore Open Tasks"]')
        button.click()
        self.assertEqual(self.browser.current_url, 'https://code.gov/#!/help-wanted')


    # Used keyboard and execute_script because webdriver incorrectly
    # considered search bar to be hidden
    # https://github.com/mozilla/geckodriver/issues/1173

    def testSearchBar(self):
        self.browser.execute_script('''
            document.querySelector("[title='Search Code.gov']").focus();
        ''')
        sleep(5)
        keyboard.write('python')
        sleep(1)
        keyboard.send('enter')
        sleep(5)
        self.assertEqual(self.browser.current_url, 'https://code.gov/#!/search?q=python')

if __name__ == '__main__':
    unittest.main(verbosity=2)
