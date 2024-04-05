import configparser

config = configparser.RawConfigParser()
config.read(".\\configuration\\config.ini")


class ReadConfig:
    @staticmethod
    def geturl():
        baseurl = config.get('Common info', 'URL')
        return baseurl

    @staticmethod
    def getusername():
        username = config.get('Common info', 'Email')
        return username

    @staticmethod
    def getpassword():
        password = config.get('Common info', 'Password')
        return password
