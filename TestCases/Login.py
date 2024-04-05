import time
import pytest
from selenium import webdriver
from PageObject.Loginpage import Loginpage
from Utilities.ReadProperties import ReadConfig
from Utilities.CustomLogger import LogGen

class TestLogin1:
    read_config = ReadConfig()
    URL = ReadConfig.geturl()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()
    logger = LogGen.loggen()

    @pytest.fixture(scope="function")
    def setup(self):
        self.driver = webdriver.Chrome()
        yield self.driver
        self.driver.quit()


    def test_homepagetitle(self, setup):
        self.logger.info("************TestLogin1************")
        self.logger.info("************Verify Title************")
        self.driver = setup
        self.driver.get(self.URL)
        act_title = self.driver.title
        if act_title == 'Smart Energy Monitor':
            assert True
            self.driver.close()
            self.logger.info("******Home page title is passed********")
        else:
            assert False
            self.driver.close()
            self.logger.info("******Home page title is Failed********")

    # def test_login(self, setup):
    #     read_config = ReadConfig()
    #     self.URL = ReadConfig.geturl()
    #     self.username = ReadConfig.getusername()
    #     self.password = ReadConfig.getpassword()
    #     self.driver = setup
    #     logger = LogGen.loggen()


    def test_loginpage(self, setup):
        self.logger.info("************Verifying Login Test************")
        self.driver = setup
        self.driver.get(self.URL)
        # self.username = ReadConfig.getusername()
        # self.password = ReadConfig.getpassword()
        self.lp = Loginpage(self.driver)
        self.lp.EnterUserName(self.username)
        self.lp.EnterPassword(self.password)
        self.lp.ClickLogin()
        time.sleep(10)


