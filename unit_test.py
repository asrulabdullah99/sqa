import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class GoogleSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    # test case method
    def test_search_in_google(self):
        # get driver
        driver = self.driver
        driver.get("https://www.google.com/")
        # assertion
        self.assertIn('Google', driver.title)
        element = driver.find_element_by_name('q')
        # send data
        element.send_keys('unmuhpnk')
        # receive data
        element.send_keys(Keys.RETURN)
        assert "No result found" not in driver.page_source

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
