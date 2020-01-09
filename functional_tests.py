from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Chrome()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_star_a_list_and_retrieve_it_later(self):
        # user access the home page
        self.browser.get('http://localhost:8000')

        # verify if title == 'To-do'
        self.assertIn('To-do', self.browser.title)
        self.fail('Finish the test')

# try to add some task


# add 'buy peacock feathers'

# press enter, return list of tasks with '1 - buy peacock feathers'

# add one more item 'use peacock feathers to make a fly'

# return list with 2 task

# url is unic and have a description text.

# access item by url

# The end
if __name__ == '__main__':
    unittest.main()
