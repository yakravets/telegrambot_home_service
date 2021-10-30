import telebot

class TelegramBot(telebot):

    def __init__(self):
        from telebot import types

        from DataGroup import DataGroupParser
        from credentials import TelegramCredentials
        

        self.bot = telebot.TeleBot(TelegramCredentials().bot_token)

    @message_handler(commands=['start'])
    def start(self, message):
        log_input_message(message)
        
        if not is_logined_user(message):
            return
            
        markup = types.ReplyKeyboardMarkup()
        markup.add('/internet')

        self.bot.send_message(message.chat.id, 'Choose a service:', reply_markup=markup)

    @message_handler(commands=['internet'])
    def internet(self, message):
        log_input_message(message)

        if not is_logined_user(message):
            return

        bot.send_message(message.chat.id, 'Зачекайте, заванжаження даних...')
        
        from credentials import DataGroupCredentials
        datagroup_credentials = DataGroupCredentials()

        parser = DataGroupParser(datagroup_credentials.login, datagroup_credentials.password)
        parser.start();

        bot.send_message(message.chat.id, parser.message)


    @message_handler(self, func=lambda message: True, content_types=['audio', 'video', 'document', 'text', 'location', 'contact', 'sticker'])
    def new_message(message):
        log_input_message(message)
        
        if not is_logined_user(message):
            return

        bot.send_message(message.chat.id, 'I not understand you.')

    def log_input_message(self, message):
        print('CHAT ID: ' + str(message.chat.id))
        print('MESSAGE TYPE:' + str(message.chat.type))

    def is_logined_user(self, message):        
        access_granted = False
        
        from settings import Settings
        security_settings = Settings()

        if message.chat.type == 'private' and (security_settings.allow_user.count(message.chat.id)) > 0:
            access_granted = True
        elif message.chat.type == 'group' and (credentials.security_settings.count(message.chat.id)) > 0: 
            access_granted = True
        else:
            bot.send_message(message.chat.id, 'Forbidden access!')
        
        return access_granted

if __name__ == '__main__':
    bot = TelegramBot()
    bot.polling(True)
