from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.common.keys import Keys
import time

#課題1
driver = webdriver.Chrome()
driver.get("http://a-force.biz/index.aspx#!")

#新卒bot押下
element = driver.find_element_by_id("button-area")
element.click()

#新卒採用のフレームへ移動
driver.switch_to_frame(driver.find_element_by_tag_name("iframe"))

element_tweet = driver.find_element_by_id("tweet")
element_tweet.send_keys("こんにちは")
#送信ボタン押下
element = driver.find_element_by_id("send_btn")
element.send_keys("keysToSend")
element.click()

#実行結果を表示する為に5秒待機する
time.sleep(5)

#課題2
element_tweet = driver.find_element_by_id("tweet")
element_tweet.send_keys("新卒採用")

element = driver.find_element_by_id("send_btn")
element.send_keys("keysToSend")
element.click()

time.sleep(5)

a = driver.find_element_by_xpath("//*[@id='field']/div[5]/div[2]/div[2]/div").text
print(a)

# ブラウザを終了する。
driver.close()