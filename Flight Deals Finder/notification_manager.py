import os
import requests
from dotenv import load_dotenv

load_dotenv()

class NotificationManager:
    def __init__(self):
        self.bot_id = os.getenv("BOT_ID")
        self.bot_token = os.getenv("BOT_TOKEN")
    
    def send_text(self, message):
        self.text = 'https://api.telegram.org/bot' + self.bot_token + '/sendMessage?chat_id=' + self.bot_id + '&parse_mode=Markdown&text=' + message
        self.response = requests.get(self.text)
        return self.response.json()
