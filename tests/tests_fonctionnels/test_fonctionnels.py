from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from flask_testing import TestCase, LiveServerTestCase
import server

class TestTest(LiveServerTestCase):

    def create_app(self):
        app = server.app
        app.config['TESTING'] = True
        print(app.config)
        return app

    def setUp(self):
        ser = Service('/Users/nicolasfrenay/Desktop/Formation/P11_amelioration_application_web/Python_Testing/tests/tests_fonctionnels/geckodriver')
        self.driver = webdriver.Firefox(service=ser)

    def tearDown(self):
        self.driver.quit()

    def test_test(self):
        self.driver.get('http://127.0.0.1:5000/')
        print("c'est arrivé là")
