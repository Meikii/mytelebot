import telegram,json,requests
import threading
from pprint import pprint
url = 'https://favqs.com/api/qotd'
bot = telegram.Bot(token='498240136:AAGBLzR7d0eRM5anktL7UpdmepFnRd6SVaM')
 


def printit():
  threading.Timer(5.0, printit).start()
  response = requests.get(url)
  quote = response.json()['quote']['body']
  print(bot.send_message(73061565,quote))

printit()

# continue with the rest of your code