from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# import unittest

class NewVisitorTest(LiveServerTestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Chrome()

    def tearDown(self) -> None:
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_star_a_list_and_retrieve_it_later(self):
        # user access the home page
        self.browser.get(self.live_server_url)

        # verify if title == 'To-do'
        self.assertIn('To-do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-do', header_text)

        # try to add some task
        inputbox = self.browser.find_element_by_id("id_new_item")
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # add 'buy peacock feathers'
        inputbox.send_keys("Buy peacock feathers")

        # press enter, return list of tasks with '1 - buy peacock feathers'
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # add one more item 'use peacock feathers to make a fly'
        inputbox = self.browser.find_element_by_id("id_new_item")
        inputbox.send_keys("Use peacock feathers to make a fly")
        inputbox.send_keys(Keys.ENTER)
        time.sleep(1)

        # return list with 2 task
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')


        self.fail('Finish the test')


        # url is unic and have a description text.

        # access item by url
