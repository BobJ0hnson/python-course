class Bot:
    def __init__(self, name, message = ""):
        self.name = name
    def say_name(self):
        print(self.name)
    def send_message(self, message):
        print(self.message)

class TelegramBot(Bot):
    def __init__(self, url, chat_id='None'):
        super().__init__()
    def set_url(self, url):
        self.url = url
    def set_chat_id(self, chat_id):
        self.chat_id = chat_id
    def send_message(self, message):
        print(f'TG Bot says {message} to {chat_id} using {url}!')

some_bot = Bot('Marvin')
some_bot.say_name()
some_bot.send_message('Hello')
telegram_bot = TelegramBot('TG')
telegram_bot.say_name()
telegram_bot.chat_id(1)
telegram_bot.send_message('Hello')