import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://unmuhpnk.ac.id/beranda")
        self.assertIn("Universitas Muhammadiyah Pontianak", driver.title)
        elem = driver.find_element_by_css_selector(
            ".col-lg-12 col-md-12 col-sm-12 col-xs-12 bg-blue-800 p-10 text-center")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        self.assertNotIn("No results found.", driver.page_source)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
