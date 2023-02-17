import configparser
config=configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")
class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('common_info','baseURL')
        return url
    @staticmethod
    def getUseremail():
        username=config.get('common_info','useremail')
        return username

    @staticmethod
    def getPassword():
        password=config.get('common_info','password')
        return password
    ##Admin Business membership
    @staticmethod
    def getadminURL():
        url = config.get('admin_businessmembership_info', 'adminbmURL')
        return url

    @staticmethod
    def getAdminUser():
        username = config.get('admin_businessmembership_info', 'username')
        return username


    @staticmethod
    def getAdminPassword():
        password = config.get('admin_businessmembership_info', 'password')
        return password