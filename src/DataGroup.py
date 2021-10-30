
class DataGroupParser:    
    
    def __init__(self, login, password):
        self.url = 'https://my.datagroup.ua/'
        self.login = login
        self.password = password
        self.timeout = 0.5

    def start(self):
        print("Start web-browser")
        
        import time
        import re
        from selenium import webdriver
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.page_load_strategy = 'normal'

        driver = webdriver.Chrome(options=options)

        login_page = driver.get(self.url)

        login_field = driver.find_element_by_class_name("login")
        assert login_field != None

        password_field = driver.find_element_by_id("password")
        assert password_field != None

        login_button = driver.find_element_by_class_name("btn")
        assert login_button != None

        login_field.send_keys(self.login)
        password_field.send_keys(self.password)
        time.sleep(self.timeout)
        login_button.click()

        time.sleep(1)

        tables = driver.find_elements_by_tag_name("tbody")
        assert tables != None
        
        data_table = tables[4]
        assert data_table != None

        all_data = data_table.text.split('\n')

        self.abonent = str(all_data[0])
        self.deal_number = str(all_data[1])  
        
        order_number = re.match(r'\w+ \w+: \d+', str(all_data[11]))
        if not order_number:
            self.order_number = 'Unable to get contract number!'
        else:
            self.order_number = order_number.group(0)

        status = re.match(r'\w+:.\w+', str(all_data[13]))
        if not status:
            self.status = 'Failed to get connection status!'    
        else:
            self.status = status.group(0)

        ip = re.search(r'\S+:.\d+.\d+.\d+.\d+', str(all_data[12]))
        if not ip:
            self.ip = 'Failed to determine IP!'
        else:
            self.ip = ip.group(0)
        
        balance = re.match(r'\w+..\w+.\d+.\d+.\w+.', str(all_data[14]))
        if not balance:
            self.balance = 'Unable to determine the account balance!'
        else:
            self.balance = balance.group(0)            

        self.message = self.abonent + '\n' + self.deal_number + '\n' + self.order_number + '\n' + self.status + '\n' + self.ip + '\n' + self.balance

        driver.close()
        print("Close web-browser")      