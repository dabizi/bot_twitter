from selenium import webdriver
from selenium.webdriver.common.keys import keys
import random
import time

class TwitterBot:
  def __init__(self, username, password):
    self.username = username
    self.password = password
    self.bot = webdriver.Firefox()
    
  def login(self):
    bot = self.bot
    bot.get('https://twitter.com/')
    timeDelay = random.randrange(2, 12)
    time.sleep(timeDelay)
    email = bot.find_element_by_class_name('email-input')
    password = bot.find_element_by_name('session[password]')
    email.clear()
    password.clear()
    email.send_keys(self.username)
    password.send_keys(self.password)
    password.send_keys(Keys.RETURN)
    timeDelay = random.randrange(2, 12)
    time.sleep(timeDelay)
    
    
  def like_tweet(self, hashtag):
    bot = self.bot
    bot.get('https://twitter.com/search?q='+hashtag+'&src=typd')
    timeDelay = random.randrange(2, 12)
    time.sleep(timeDelay)
    for i in range(1, 3):
      bot.execute_script('window.scrollTo(0, document.body.scrollHeight)')
      timeDelay = random.randrange(2, 12)
      time.sleep(timeDelay)
      tweets = bot.find_elements_by_class_name('tweet')
      links = [elem.get_attribute('data-permalink-path') for elem in tweets]
      # print(links)
      for link in links:
        bot.get('https://twitter.com'+link)
        try:
          bot.find_element_by_class_name('HeartAnimation').click()
          timeDelay = random.randrange(18, 125)
          time.sleep(timeDelay)
         except Exception as ex:
          timeDelay = random.randrange(18, 125)
          time.sleep(timeDelay)
          

    #Put the username and password below
ed = TwitterBot('username', 'password')
ed.login()
  #Put the hashtag below
ed.like_tweet('hashtag')
  #Add random post from list of data
