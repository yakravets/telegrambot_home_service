import unittest
import xmlrunner
import sys, os

sys.path.append(os.getcwd())
        
class TestDatagroupCredentials(unittest.TestCase):
    def test_credeintials_is_found(self):
        from src import credentials
        dgc = credentials.DataGroupCredentials()
        self.assertIsNot(dgc, None)

    def test_login(self):
        from src import credentials
        dgc = credentials.DataGroupCredentials()
        self.assertNotEqual(dgc.login(), '')

    def test_password(self):
        from src import credentials
        dgc = credentials.DataGroupCredentials()
        self.assertNotEqual(dgc.password(), '')

class TestTelegramCredentials(unittest.TestCase):
    def test_credeintials_is_found(self):
        from src import credentials
        tgc = credentials.TelegramCredentials()
        self.assertIsNot(tgc, None)

    def test_telegram_bot_token(self):
        from src import credentials
        tgc = credentials.TelegramCredentials()
        self.assertNotEqual(tgc.bot_token(), '')

class TestSettings(unittest.TestCase):
    def test_minimum_one_count_user_admin_in_dict(self):
        from src import settings
        sett = settings.Settings()
        count = len(sett.allow_user())

        self.assertGreaterEqual(count, 0)

    def test_minimum_one_count_group_allow_in_dict(self):
        from src import settings
        sett = settings.Settings()
        count = len(sett.allow_group())

        self.assertGreaterEqual(count, 0)

if __name__ == "__main__":
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='tests/reports'),
        failfast=False,
        buffer=False,
        catchbreak=False)