from selenium import webdriver
from selenium.webdriver.common.keys import keys
import time

class TwitterBot:
  def __init__(self, username, password):
    self.username = username
    self.password = password
    self.bot = webdriver.Firefox()
    
  def login(self):
    bot = self.bot
    bot.get('https://twitter.com/')
    time.sleep(3)
