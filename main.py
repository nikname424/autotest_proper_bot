from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time

# Указываем путь к geckodriver
geckodriver_path = 'geckodriver'  # замените на ваш путь

# Настраиваем Firefox options
options = Options()

# Задаем пользовательский user-agent
options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:90.0) Gecko/20100101 Firefox/90.0 bot")

# Если нужно запустить браузер в headless режиме
# options.headless = True

# Создаем экземпляр WebDriver
service = Service(geckodriver_path)
driver = webdriver.Firefox(service=service, options=options)

try:
    # Открываем страницу логина
    driver.get("https://cabinet.autentic.capital/login")

    input('qasa')
    
    # Найдем поля для ввода логина и пароля и введем значения
    email_field = driver.find_element(By.XPATH, "//input[@class='data-in' and @type='text' and @placeholder='E-mail *']")
    password_field = driver.find_element(By.XPATH, "//input[@class='input pass-in' and @type='password' and @placeholder='Password *']")
    
    email_field.send_keys("nekitrizm+main20@gmail.com")
    password_field.send_keys("zc9DXG8PX")
    
    # Найдем кнопку для входа и нажмем на нее
    login_button = driver.find_element(By.XPATH, "//button[@class='enter-button' and contains(text(), 'Log in')]")
    login_button.click()
    
    # Подождем некоторое время для загрузки страницы после логина
    time.sleep(5)
    input()
    
finally:
    # Закроем браузер
    driver.quit()
