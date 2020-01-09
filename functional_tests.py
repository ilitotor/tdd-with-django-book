from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-do', header_text)

        # try to add some task
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # add 'buy peacock feathers'
        inputbox.send_keys('Buy peacock feathers')

        # press enter, return list of tasks with '1 - buy peacock feathers'
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1 - buy peacock feathers' for row in rows),
            "New to-do item did not appear in table"
        )

        # add one more item 'use peacock feathers to make a fly'
        self.fail('Finish the test')

        # return list with 2 task

        # url is unic and have a description text.

        # access item by url

# The end
if __name__ == '__main__':
    unittest.main()
