from asyncio.windows_events import NULL
from distutils.spawn import find_executable
from logging import exception
from mailbox import ExternalClashError
from msilib.schema import Error
import random
from turtle import clear
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import requests
import json
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
import csv
import os
import requests
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from python_anticaptcha import AnticaptchaClient, ImageToTextTask, NoCaptchaTaskProxylessTask
import zipfile
import undetected_chromedriver as uc
import pyautogui
import string
from win10toast import ToastNotifier

# Rechaptcha api-key
api_key = "***"

cwd = os.getcwd()
# win_username=os.getlogin()
win_username = "WZ1"


try:
    old_name = r"C:\Program Files (x86)\Google\Update\GoogleUpdate.exe"
    new_name = r"C:\Program Files (x86)\Google\Update\fsd.exe"

    os.rename(old_name, new_name)
except:
    pass

with open("dollardig.txt", "r") as f:
    gocashbackaccountlist = [line.rstrip() for line in f]
with open("info.txt", "r") as f:
    infolist = [line.rstrip() for line in f]
with open("Email list.txt", "r") as f:
    emaillist = [line.rstrip() for line in f]


def check_popup_box():
    try:
        el = driver.find_element_by_xpath("//button[@title='Close']")
        sleep(3)
        el.click()
        sleep(3)
    except:
        pass

def solve_recaptcha(api_key,driver):
    # website key for rechaptcha solve
    site_key = '****'
    url = 'https://www.dollardig.com/signup/'
    client = AnticaptchaClient(api_key)
    task = NoCaptchaTaskProxylessTask(url, site_key)
    job = client.createTask(task)
    job.join()
    cap_response = job.get_solution_response()
    sleep(1)
    driver.execute_script("window.scrollTo(0, 3000)") 
    driver.execute_script('var element=document.getElementById("g-recaptcha-response"); element.style.display="";')   
    driver.execute_script('var element=document.getElementById("g-recaptcha-response"); element.style.display="";')
    driver.execute_script("""document.getElementById("g-recaptcha-response").innerHTML = arguments[0]""",cap_response)
    # el_recaptcha_res = driver.find_element_by_css_selector('textarea[id="g-recaptcha-response"]')

    # for character in cap_response:
    #     el_recaptcha_res.send_keys(character)
    #     sleep(0.1)
    sleep(1)
    driver.execute_script('var element=document.getElementById("g-recaptcha-response"); element.style.display="none";')
    driver.find_element_by_css_selector("#signupform > div> button[type='submit']").click()

def solve_captcha(api_key):

    captcha_element = driver.find_element_by_xpath(
        'iframe[title="reCAPTCHA"]'
    )
    captcha_img = captcha_element.screenshot_as_png

    outfile = open("captcha.png", "wb")
    outfile.write(captcha_img)
    outfile.close()

    captcha_fp = open("captcha.png", "rb")
    client = AnticaptchaClient(api_key)
    task = ImageToTextTask(captcha_fp)
    job = client.createTask(task)
    job.join()
    captcha_answer = job.get_captcha_text()
    el = driver.find_element_by_xpath("//input[@placeholder='Enter Security Code']")
    for _ in range(30):
        el.send_keys(Keys.BACKSPACE)

    driver.find_element_by_xpath(
        "//input[@placeholder='Enter Security Code']"
    ).send_keys(captcha_answer)


def accept_cookies():
    try:
        sleep(2)

        driver.execute_script(
            'document.querySelector("#gdpr-consent > div.gdpr__modal > button.gdpr__consent").click()'
        )
    except:
        pass
    sleep(2)
    try:
        driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div/div[2]/div/button[3]"
        ).click()
    except:
        pass


def us_cananda_popup():
    try:
        WebDriverWait(driver, 5).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[contains(text(), "No, thanks. Stay on the U.S. Site.")]',
                )
            )
        ).click()

    except:
        pass


def check_ip():
    try:
        with open("lastip.txt", "r") as f:
            last_used_ip = f.readline().rstrip()
    except:
        last_used_ip = ""
    current_ip = requests.get("https://httpbin.org/ip").json()["origin"]
    with open("lastip.txt", "w") as f:
        f.write(current_ip + "\n")
    if current_ip == last_used_ip:
        sleep(1 * 60)


def clear_browser(driver):

    driver.get("chrome://settings/clearBrowserData")
    sleep(4)
    print("before excute script")
    driver.execute_script(
        'document.querySelector("body > settings-ui").shadowRoot.querySelector("#main").shadowRoot.querySelector("settings-basic-page").shadowRoot.querySelector("#basicPage > settings-section:nth-child(9) > settings-privacy-page").shadowRoot.querySelector("settings-clear-browsing-data-dialog").shadowRoot.querySelector("#clearBrowsingDataConfirm").click()'
    )
    print("scirpt excute done")


def already_registred_login():
    global driver

    sleep(30)

    email_for_dollardig = account.split(",")[0]
    password_for_dollardig = account.split(",")[1]
    chrome_options = webdriver.ChromeOptions()

    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)

    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    chrome_options.add_argument(
        f"user-data-dir=C:\\Users\\{win_username}\\AppData\\Local\\Google\\Chrome\\User Data"
    )

    chrome_options.add_argument("profile-directory=Default")

    driver = webdriver.Chrome(
        ChromeDriverManager().install(), chrome_options=chrome_options
    )

    clear_browser(driver)

    driver.get("https://httpbin.org/ip")
    sleep(4)
    driver.get("https://www.cashbackmonitor.com/cashback-store/the-motley-fool")

    driver.switch_to.window(driver.window_handles[0])

    try:
        driver.maximize_window()
    except:
        pass
    sleep(random.randint(4, 7))
    accept_cookies()
    sleep(random.randint(3, 7))

    #     sleep(9999)
    driver.find_element_by_link_text("Dollar Dig").click()
    sleep(random.randint(3, 7))
    driver.switch_to.window(driver.window_handles[1])
    sleep(random.randint(10, 15))
    accept_cookies()
    sleep(random.randint(2, 5))
    us_cananda_popup()
    accept_cookies()
    sleep(random.randint(8, 14))
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(
            (By.XPATH, '//a[contains(text(), "Motley Fool")]')
        )
    )
    windows_notifaction(
        "Please dont change the screen or move mouse.Brower should be always top"
    )
    scrolling_process(driver)
    windows_notifaction(
        "Please dont change the screen or move mouse.Brower should be always top"
    )
    os.system("python ./modules/getmousepoint.py")
    sleep(30)
    sleep(random.randint(10, 15))
    driver.switch_to.window(driver.window_handles[2])


def generate_random_password():

    length = 10
    characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

    random.shuffle(characters)

    password = []
    for i in range(length):
        password.append(random.choice(characters))

    random.shuffle(password)

    return "".join(password)

def pass_reset(driver):
    global password
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="account-dropdown-button"]'))
    ).click()
    sleep(random.randint(1, 3))
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="account-menu-link-7"]'))
    ).click()
    sleep(random.randint(1, 3))
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Change password"))
    ).click()
    sleep(random.randint(1, 3))
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="change-submit"]'))
    ).click()
    sleep(random.randint(1, 3))
    driver.minimize_window()
    options = uc.ChromeOptions()

    driver2 = uc.Chrome(
        # service=ChromeService(ChromeDriverManager().install()),
        # version_main=102,
        chrome_options= options,
        user_data_dir=f"{cwd}\\gmail",
        use_subprocess=True
    )

    driver2.get("https://mail.google.com/mail/u/0/#inbox")
    sleep(10)

    driver2.switch_to.window(driver2.window_handles[0])
    sleep(9999)

def password_reset(driver):
    global password
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="account-dropdown-button"]'))
    ).click()
    sleep(random.randint(1, 3))
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="account-menu-link-7"]'))
    ).click()
    sleep(random.randint(1, 3))
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Change password"))
    ).click()
    sleep(random.randint(1, 3))
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="change-submit"]'))
    ).click()
    sleep(random.randint(1, 3))
    driver.minimize_window()
    options = uc.ChromeOptions()

    driver2 = uc.Chrome(
        # service=ChromeService(ChromeDriverManager().install()),
        # version_main=102,
        chrome_options= options,
        user_data_dir=f"{cwd}\\gmail",
        use_subprocess=True
    )

    driver2.get("https://mail.google.com/mail/u/0/#inbox")
    sleep(10)

    driver2.switch_to.window(driver2.window_handles[0])
    try:
        driver2.maximize_window()
    except:
        pass

    driver2.switch_to.window(driver2.window_handles[0])
    # try:
    #     driver2.maximize_window()
    # except:
    #     pass
    # driver2.get("https://accounts.google.com/signin")
    # driver2.get("https://gmail.com")
    # sleep(5)
    # driver2.switch_to.window(driver2.window_handles[0])

    WebDriverWait(driver2, 120).until(EC.presence_of_element_located((By.NAME, "q")))
    sleep(random.randint(4, 7))
    driver2.find_element_by_name("q").send_keys(email)
    sleep(random.randint(2, 5))
    driver2.find_element_by_name("q").send_keys(Keys.ENTER)
    try:
        WebDriverWait(driver2, 120).until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div[6]/div[2]/div/table/tbody/tr",
                )
            )
        )
        sleep(random.randint(2, 5))
        driver2.find_element_by_xpath(
            "/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div[6]/div[2]/div/table/tbody/tr"
        ).click()
        sleep(random.randint(2, 5))
        WebDriverWait(driver2, 120).until(
            EC.presence_of_element_located(
                (By.XPATH, '//a[contains(text(), "Reset your password")]')
            )
        )
        sleep(random.randint(1, 3))
        rest_link = driver2.find_element(
            By.XPATH, '//a[contains(text(), "Reset your password")]'
        ).get_attribute("href")
        driver2.close()
    except:
        try:
            driver2.quit()
        except:
            pass

        print("******Cannot find email in main gmail********")
        print("*********Please enter password rest link below**************")
        rest_link = input("Enter password reset link!!!!    ")
    sleep(random.randint(2, 5))
    driver.maximize_window()
    driver.get(rest_link)
    sleep(random.randint(1, 3))
    password = generate_random_password()
    print(f"\nGenarated fool password: {password}")
    driver.find_element(By.XPATH, '//*[@id="password-reset"]').send_keys(password)
    sleep(random.randint(1, 3))
    driver.find_element(By.XPATH, '//*[@id="re-enter-password"]').send_keys(password)
    sleep(random.randint(1, 3))
    driver.find_element(By.XPATH, '//*[@name="action"]').click()
    sleep(random.randint(1, 3))

    try:
        driver.get("https://fool.com")
        sleep(random.randint(1, 3))
        WebDriverWait(driver2, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//a[contains(text(), "Access Premium Services")]')
            )
        ).click()
    except:
        pass


def email_change(driver, gocashback_email):
    driver.get("https://www.fool.com/premium/")
    sleep(random.randint(5, 8))
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="account-dropdown-button"]'))
    ).click()
    sleep(random.randint(1, 3))
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="account-menu-link-7"]'))
    ).click()
    sleep(random.randint(1, 3))
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Change email"))
    ).click()
    sleep(random.randint(1, 3))

    WebDriverWait(driver, 120).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="email-input"]'))
    ).send_keys(gocashback_email)
    sleep(random.randint(1, 3))
    driver.find_element(By.XPATH, '//*[@id="change-submit"]').click()
    sleep(random.randint(2, 5))

    WebDriverWait(driver, 120).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Continue your journey!"))
    ).click()
    sleep(random.randint(2, 5))


def windows_notifaction(msg):
    my_notification = ToastNotifier()
    my_notification.show_toast("Alert", msg)


def desktop_aleart():

    windows_notifaction(
        "Please dont change the screen or move mouse.Brower should be always top"
    )
    sleep(10)
    windows_notifaction(
        "Please dont change the screen or move mouse.Brower should be always top"
    )
    sleep(10)
    windows_notifaction(
        "Please dont change the screen or move mouse.Brower should be always top"
    )
    sleep(random.randint(10, 15))


def getscreenshot_of_receipt(driver, gocashbackemail, foolpassword):
    sleep(random.randint(5, 8))
    clear_browser(driver)
    sleep(10)
    cwd = os.getcwd()
    if not os.path.exists(f"{cwd}\\screenshots"):
        os.makedirs(f"{cwd}\\screenshots")
    driver.get("https://www.fool.com/premium/")
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Log in!"))
    ).click()
    sleep(random.randint(5, 8))
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="usernameOrEmail"]'))
    ).clear()
    sleep(random.randint(1, 3))
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="usernameOrEmail"]'))
    ).send_keys(gocashbackemail)
    sleep(random.randint(3, 6))
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="usernameOrEmail"]'))
    ).clear()
    sleep(random.randint(5, 8))
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="usernameOrEmail"]'))
    ).send_keys(gocashbackemail)
    sleep(random.randint(3, 6))
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="password"]'))
    ).clear()
    sleep(random.randint(5, 8))
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="password"]'))
    ).send_keys(foolpassword)
    sleep(random.randint(3, 6))

    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="btn-login"]'))
    ).click()

    sleep(random.randint(5, 8))
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="account-dropdown-button"]'))
    ).click()
    sleep(random.randint(3, 5))
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="account-menu-link-7"]'))
    ).click()
    sleep(random.randint(3, 5))
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@aria-label="Receipt - opens in new tab"]')
        )
    ).click()
    sleep(random.randint(5, 8))
    driver.switch_to.window(driver.window_handles[1])
    sleep(random.randint(5, 7))
    driver.save_screenshot(f"{cwd}\\screenshots\\{gocashbackemail}.png")
    driver.close()
    try:
        driver.switch_to.window(driver.window_handles[0])
        sleep(random.randint(1, 3))
        driver.close()
    except:
        driver.quit()


def scrolling_process(driver):
    sleep(5)
    scrollpoint = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located(
            (By.XPATH, '//div[contains(text(), "Fool Rule Breakers for just")]')
        )
    )

    scroll_height = scrollpoint.location["y"]
    for scrol in range(100, scroll_height, 200):
        driver.execute_script(f"window.scrollTo(0,{scrol})")
        sleep(random.randint(1, 3) * 0.1)
    sleep(random.randint(2, 5))

def login(driver,email,password):
    i = 0
    try:
       
        while(i<4):
            el_email = driver.find_element_by_css_selector('div[class="login_box"]>form>div>input[name=email]')
            el_email.clear()

            el_pass = driver.find_element_by_css_selector('div[class="login_box"]>form>div>input[name=password]')
            el_pass.clear()


            for character in email:
                el_email.send_keys(character)
                sleep(0.1)

            # for _ in range(30):
            #                     el.send_keys(Keys.BACKSPACE)
            for character in password:
                el_pass.send_keys(character)
                sleep(0.1)
            
            driver.find_element_by_css_selector("#loginfrom > div> button[type='submit']").click()
            sleep(random.randint(2,4))

            try:
                driver.find_element_by_xpath("//*[contains(text(),'Logout')]")
                sleep(.5)
                break
            except:
                pass
            i = i + 1
    except Exception as e:
        print(e)

def email_verify(email):

    options = uc.ChromeOptions()
    # driver2 = uc.Chrome(
    #     version_main=102,
    #     user_data_dir=f"{cwd}\\gmail",
    #     options=options,
    #     use_subprocess=True,
    # )
    driver2 = uc.Chrome(
        # service=ChromeService(ChromeDriverManager().install()),
        # version_main=102,
        chrome_options= options,
        user_data_dir=f"{cwd}\\gmail",
        use_subprocess=True
    )

    print(email)
    driver2.maximize_window()
    try:
        driver2.get("https://mail.google.com/mail/u/0/#inbox")
        sleep(7)
        el_searchbox = driver2.find_element_by_css_selector(
                    'input[aria-label="Search in mail"]'
                )
        el_searchbox.clear()
        for character in email:
            el_searchbox.send_keys(character)
            sleep(0.1)
        sleep(2)
        driver2.find_element(By.XPATH,'//button[@aria-label="Search in mail"]').click()
        sleep(9)

        driver2.find_element(By.XPATH,'/html/body/div[7]/div[3]/div/div[2]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div[6]/div[2]/div/table/tbody/tr/td[5]/div/div').click()
        sleep(5)
        link = (driver2.find_element(By.XPATH,"//*[contains(text(),'Please click the following link to activate your account:')]/a")).get_attribute('href')
        sleep(1)
        driver2.close()
        return link
    except Exception as e:
        print(e)
        driver2.close()
        return NULL

def ip_change():
        print("Changing ip....")
        response=requests.get('https://api.mountproxies.com/api/proxy/620144e1814b9a5fa72d151b/rotate_ip?api_key=36a862c6affcdd47be76d413cbf9391e')
        print(response.status_code)
        sleep(50)   
counter = 0
info_i = 0

for account in gocashbackaccountlist:

    email_for_dollardig = account.split(",")[0]
    password_for_dollardig = account.split(",")[1]

    fullName = infolist[info_i].split(",")[3]
    fName = fullName.split(" ")[0]
    lName = fullName.split(" ")[1]
    country = infolist[info_i].split(",")[-1]
    if country.strip() == 'US':
        country = 'United States'
    elif country.strip() == 'CA':
        country = 'Canada'

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")

    chrome_options.add_argument(
        f"user-data-dir=C:\\Users\\{win_username}\\AppData\\Local\\Google\\Chrome\\User Data"
    )

    chrome_options.add_argument("profile-directory=Default")
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        chrome_options=chrome_options,
    )

    print("Clear browser...")
    clear_browser(driver)
    ip_change()
    sleep(2)
    check_ip()
    print("cleaning done...")

    driver.get("https://httpbin.org/ip")
    sleep(4)
    driver.get("https://www.cashbackmonitor.com/cashback-store/the-motley-fool")

    driver.switch_to.window(driver.window_handles[0])

    try:
        driver.maximize_window()
    except:
        pass
    sleep(random.randint(4, 7))
    accept_cookies()
    sleep(random.randint(3, 7))
    print("Click on Dollar Dig...")
    driver.find_element_by_xpath('//a[text()="Dollar Dig"]').click()
    sleep(random.randint(3, 7))
    driver.switch_to.window(driver.window_handles[1])
    sleep(random.randint(10, 15))
    accept_cookies()
    sleep(random.randint(2, 5))
    us_cananda_popup()

    try:
        try:
            driver.find_element_by_xpath("//*[contains(text(),'Logout')]").click()
            sleep(.5)
        except:
            pass
        driver.find_element_by_xpath("//a[text()='Sign Up']").click()
        sleep(random.randint(5, 9))
        driver.refresh()
        sleep(random.randint(5, 9))
        accept_cookies()
        sleep(random.randint(5, 9))
        sleep(4)
        loop_i = 0
        while(loop_i<4):
            el_email = driver.find_element_by_css_selector(
                'div[class="signup_box"]>form>div>input[name=email]'
            )
            el_email.clear()
            el_pass = driver.find_element_by_css_selector(
                'div[class="signup_box"]>form>div>input[name=password]'
            )
            el_pass.clear()    
            el_fname = driver.find_element_by_css_selector(
                'div[class="signup_box"]>form>div>input[name=fname]'
            )
            el_fname.clear()
            el_lname = driver.find_element_by_css_selector(
                'div[class="signup_box"]>form>div>input[name=lname]'
            )
            el_lname.clear()
            el_cpass = driver.find_element_by_css_selector(
                'div[class="signup_box"]>form>div>input[name=cpassword]'
            )
            el_cpass.clear()

            sleep(0.5)

            # el=driver.find_element_by_css_selector('div[class="signup_box"]>form>div>input[name=email]')
            # for _ in range(30):
            #                     el.send_keys(Keys.BACKSPACE)

            for character in fName:
                el_fname.send_keys(character)
                sleep(0.1)

            for character in lName:
                el_lname.send_keys(character)
                sleep(0.1)    

            for character in email_for_dollardig:
                el_email.send_keys(character)
                sleep(0.1)

            # for _ in range(30):
            #                     el.send_keys(Keys.BACKSPACE)
            for character in password_for_dollardig:
                el_pass.send_keys(character)
                sleep(0.1)

            for character in password_for_dollardig:
                el_cpass.send_keys(character)
                sleep(0.1)

            country_select = Select(
                driver.find_element_by_css_selector('select[name="country"]')
            )
            country_select.select_by_visible_text(country)

            solve_recaptcha(api_key,driver)
            sleep(random.randint(5, 9))

            try:
                try:
                    driver.find_element_by_xpath("//*[contains(text(),'Thank you for Registering')]")
                    verify_link = email_verify(email_for_dollardig)
                    sleep(5)
                    driver.execute_script("window.open('');")
                    driver.switch_to.window(driver.window_handles[2])
                    driver.get(verify_link)
                    sleep(10)
                    driver.close()
                    driver.switch_to.window(driver.window_handles[1])  

                    driver.find_element_by_css_selector(
                        'div[class="top_menu"]>ul>li:nth-child(1)'
                    ).click() 
                    try:
                        driver.find_element_by_xpath("//*[contains(text(),'Sign Up')]").click()             
                        login(driver,email_for_dollardig,password_for_dollardig)
                    except Exception as e:
                        pass
                    sleep(3)
                    break

                except:
                    driver.find_element_by_xpath("//*[contains(text(),'Email already exists.')]")
                    verify_link = email_verify(email_for_dollardig)
                    sleep(5)
                    if(verify_link != NULL):
                        driver.execute_script("window.open('');")
                        driver.switch_to.window(driver.window_handles[2])
                        driver.get(verify_link)
                        sleep(10)
                        driver.close()
                        driver.switch_to.window(driver.window_handles[1]) 
                                  
                    login(driver,email_for_dollardig,password_for_dollardig)
                    sleep(3)
                    break
            except:
                try:
                    driver.find_element_by_xpath("//*[contains(text(),'Logout')]")
                    sleep(.5)
                    break
                except:
                    pass
    
            loop_i = loop_i + 1
            

        # driver.execute_script(
        #     'document.querySelector("div.login-loginbtn.login-loginbtn-active").click()'
        # )
        sleep(random.randint(8, 12))
        
        try:
            t = driver.find_element_by_css_selector(
                'div[class="top_menu"]>ul>li:nth-child(1)'
            ).click()
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            sleep(random.randint(5,9))
            driver.refresh()
            sleep(random.randint(3,7))
            driver.find_element_by_xpath('//a[text()="Dollar Dig"]').click()
            sleep(random.randint(6,10))
            driver.switch_to.window(driver.window_handles[1])
            sleep(random.randint(8,14))
            # scrolling_process(driver)
            print('click')
            sleep(99999)
            WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//a[@class="get_deal_button green_gradient_bg float_right"]'))).click()
            print('Click done')
            sleep(random.randint(10,15))
            driver.switch_to.window(driver.window_handles[2]) 
            check_popup_box()

        except:
            pass

    except:
        t = driver.find_element_by_css_selector(
            '#menu-item-26744 > a'
        ).click()
        driver.close()
        driver.switch_to.window(driver.window_handles[0])
        driver.find_element_by_xpath('//a[text()="Dollar Dig"]').click()
        sleep(random.randint(6, 10))
        accept_cookies()

        driver.switch_to.window(driver.window_handles[1])
    
        sleep(random.randint(8, 14))
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (By.XPATH, '//a[@class="get_deal_button green_gradient_bg float_right"]')
            )
        ).click()
        windows_notifaction(
            "Please dont change the screen or move mouse.Brower should be always top"
        )
        scrolling_process(driver)
        windows_notifaction(
            "Please dont change the screen or move mouse.Brower should be always top"
        )
        os.system("python ./modules/getmousepoint.py")
        desktop_aleart()
        # driver.switch_to.window(driver.window_handles[2])
    """
    while True:
        try:
            scrollpoint = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located(
                    (
                        By.XPATH,
                        '//a[@href="https://www.fool.com/premium/rule-breakers/landing/"]',
                    )
                )
            )

            break
        except:
            driver.close()
            driver.switch_to.window(driver.window_handles[1])
            sleep(random.randint(3, 5))
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            driver.close()
            driver.quit()
            already_registred_login()

    scrollpoint = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located(
            (
                By.XPATH,
                '//a[@href="https://www.fool.com/premium/rule-breakers/landing/"]',
            )
        )
    )

    scroll_height = driver.execute_script(
        "return document.documentElement.scrollHeight"
    )
    for scrol in range(100, scroll_height, 200):
        driver.execute_script(f"window.scrollTo(0,{scrol})")
        sleep(random.randint(1, 3) * 0.1)
    sleep(random.randint(2, 5))
    try:
        driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()
    except:
        pass
    sleep(random.randint(2, 5))
    try:
        scrollpoint.click()

    except:
        sleep(random.randint(2, 5))
        driver.find_element(By.XPATH, '//*[@name="legalese_id_1"]').click()
        sleep(random.randint(1, 3))
        driver.find_element(By.XPATH, '//*[@name="legalese_id_4"]').click()
        sleep(random.randint(2, 5))
        driver.find_element(By.XPATH, '//*[@id="gdpr-submit-button"]').click()
        sleep(random.randint(10, 15))
        scrollpoint.click()
    sleep(random.randint(2, 5))
    scrollpoint = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, '//a[contains(text(), "Try Now!")]'))
    )
    scroll_height = scrollpoint.location["y"]
    for scrol in range(100, scroll_height, 200):
        driver.execute_script(f"window.scrollTo(0,{scrol})")
        sleep(random.randint(1, 3) * 0.1)

    sleep(random.randint(2, 5))
    scrollpoint.click()"""
    sleep(random.randint(2, 5))
    try:
        driver.find_element(By.XPATH,'//*[@id="onetrust-accept-btn-handler"]').click()
    except:
        pass
    sleep(random.randint(5,8))    
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.tmf-cta-container > a"))
    ).click()

    try:
        r = []
        for x in infolist:
            if x in need_to_remove_list:
                continue
            r = r + [x]
            infolist = r

    except:
        pass
    need_to_remove_list = []
  
    for info in infolist:

        driver.refresh()
        creditcardnumber = info.split(",")[0]
        creditcard_month = info.split(",")[1]
        creditcard_year = info.split(",")[2]
        csv_number = f"{random.randrange(1,10**3):03}"

        Name_on_card = info.split(",")[3]
        first_name = Name_on_card.split(" ")[0]
        last_name = Name_on_card.split(" ")[1]
        Address_1 = info.split(",")[4]
        Address_2 = info.split(",")[5]
        City = info.split(",")[6]

        State = info.split(",")[7]
        Zip_code = info.split(",")[8]
        Country = info.split(",")[9]
        email = emaillist[counter]
        password = ""
        check_popup_box()
        WebDriverWait(driver, 70).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="id_first_name"]'))
        )
        check_popup_box()
        driver.find_element_by_xpath('//*[@id="id_first_name"]').clear()
        driver.find_element_by_xpath('//*[@id="id_last_name"]').clear()
        driver.find_element_by_xpath('//*[@id="id_address_1"]').clear()
        driver.find_element_by_xpath('//*[@id="id_address_2"]').clear()
        driver.find_element_by_xpath('//*[@id="id_city"]').clear()
        driver.find_element_by_xpath('//*[@id="id_postal_code"]').clear()
        driver.find_element_by_xpath('//*[@id="id_email"]').clear()
        driver.find_element_by_xpath('//*[@id="id_confirm_email"]').clear()
        driver.find_element_by_xpath('//*[@id="id_card_name"]').clear()
        driver.find_element_by_xpath('//*[@id="id_card_number"]').clear()
        driver.find_element_by_xpath('//*[@id="id_card_security_code"]').clear()
        check_popup_box()
        el = driver.find_element_by_xpath('//*[@id="id_first_name"]')
        for character in first_name:
            el.send_keys(character)
            sleep(0.1)
        sleep(random.randint(4, 7))
        check_popup_box()
        el = driver.find_element_by_xpath('//*[@id="id_last_name"]')

        for character in last_name:
            el.send_keys(character)
            sleep(0.1)
        check_popup_box()
        el = driver.find_element_by_xpath('//*[@id="id_address_1"]')
        for character in Address_1:
            el.send_keys(character)
            sleep(0.1)
        check_popup_box()
        el = driver.find_element_by_xpath('//*[@id="id_address_2"]')

        for character in Address_2:
            el.send_keys(character)
            sleep(0.1)
        check_popup_box()
        el = driver.find_element_by_xpath('//*[@id="id_city"]')

        for character in City:
            el.send_keys(character)
            sleep(0.1)
        sleep(random.randint(1, 3))
        Select(driver.find_element_by_xpath('//*[@id="id_country"]')).select_by_value(
            Country
        )
        sleep(random.randint(1, 3))
        try:
            Select(driver.find_element_by_xpath('//*[@id="id_state"]')).select_by_value(
                State
            )
            sleep(random.randint(1, 3))
        except:
            Select(
                driver.find_element_by_xpath('//*[@id="id_province"]')
            ).select_by_value(State)
            sleep(random.randint(1, 3))
        check_popup_box()
        el = driver.find_element_by_xpath('//*[@id="id_postal_code"]')

        for character in Zip_code:
            el.send_keys(character)
            sleep(0.1)
        sleep(random.randint(1, 3))
        check_popup_box()
        el = driver.find_element_by_xpath('//*[@id="id_email"]')

        for character in email:
            el.send_keys(character)
            sleep(0.1)
        el = driver.find_element_by_xpath('//*[@id="id_confirm_email"]')
        check_popup_box()
        for character in email:
            el.send_keys(character)
            sleep(0.1)
        check_popup_box()
        el = driver.find_element_by_xpath('//*[@id="id_card_name"]')

        for character in Name_on_card:
            el.send_keys(character)
            sleep(0.1)

        check_popup_box()
        el = driver.find_element_by_xpath('//*[@id="id_card_number"]')

        for character in creditcardnumber:
            el.send_keys(character)
            sleep(0.1)
        Select(
            driver.find_element_by_xpath('//*[@id="id_card_expiration_month"]')
        ).select_by_visible_text(creditcard_month)
        Select(
            driver.find_element_by_xpath('//*[@id="id_card_expiration_year"]')
        ).select_by_value(creditcard_year)
        el = driver.find_element_by_xpath('//*[@id="id_card_security_code"]')
        check_popup_box()
        for character in csv_number:
            el.send_keys(character)
            sleep(0.1)

        sleep(random.randint(1, 3))

        check_popup_box()
        driver.find_element_by_xpath('//*[@id="agree-to-terms"]').click()
        sleep(2)
        check_popup_box()
        driver.find_element_by_xpath('//*[@id="submit-button"]').click()
        print("\n")
        print("\n")
        print(
            "-----------------------------------------------------------------------------------------------------------------------\n"
        )
        print(
            "-----------------------------------------------------------------------------------------------------------------------\n"
        )
        print(
            "--------------------------------Checking the next card info-------------------------------------------------------------"
        )
        print(
            f"{email_for_dollardig},{password_for_dollardig},{email},{creditcardnumber},{Name_on_card},{creditcard_month},{creditcard_year},{csv_number},{Address_1},{Address_2},{City},{State},{Zip_code},{Country}\n"
        )

        try:
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//a[@data-tooltip="Your account is almost ready"]')
                )
            )

            x = True

        except:
            driver.refresh()
            check_popup_box()
            sleep(10)
            driver.refresh()
            check_popup_box()
            try:
                WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located(
                        (By.XPATH, '//a[@data-tooltip="Your account is almost ready"]')
                    )
                )
                x = True
            except:
                print("\n****Above card info is wrong*******")

                with open("info.txt", "r") as f:
                    lines = f.readlines()

                with open("info.txt", "w") as f:
                    for line in lines:
                        if line.strip("\n") != info:
                            f.write(line)
                with open("Email list.txt", "r") as f:
                    lines = f.readlines()
                with open("Email list.txt", "w") as f:
                    for line in lines:
                        if line.strip("\n") != email:
                            f.write(line)
                with open("wrong.txt", "a") as f:
                    f.write(email + "," + info + "\n")

                x = False
                counter += 1
                need_to_remove_list.append(info)

        if x:
            print("\n***********************************************")
            print("\n*********Above card info is correct***********")
            print("\n***********************************************")

            print("*****************Correct info*********************")
            print(
                f"{email_for_dollardig},{password_for_dollardig},{email},{creditcardnumber},{Name_on_card},{creditcard_month},{creditcard_year},{csv_number},{Address_1},{Address_2},{City},{State},{Zip_code},{Country}\n"
            )
            sleep(120)
            WebDriverWait(driver, 15).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//a[@data-tooltip="Your account is almost ready"]')
                )
            ).click()

            try:
                sleep(random.randint(3, 5))
                WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, '#otp-form > div.text-center > a'))
                ).click()
                sleep(random.randint(3, 5))
                options = uc.ChromeOptions()
                driver2 = uc.Chrome(
                    chrome_options= options,
                    user_data_dir=f"{cwd}\\gmail",
                    use_subprocess=True
                )

                driver2.get("https://mail.google.com/mail/u/0/#inbox")
                sleep(10)

                el_searchbox = driver2.find_element_by_css_selector(
                'input[aria-label="Search in mail"]'
                )
                el_searchbox.clear()
                email_fool = 'fool@foolcs.com ' + email
                for character in email_fool:
                    el_searchbox.send_keys(character)
                    sleep(0.1)
                driver2.find_element(By.CSS_SELECTOR,'button[aria-label="Search in mail"]').click()
                sleep(random.randint(3, 6))
                driver2.find_element(By.XPATH,"/html/body/div[7]/div[3]/div/div[2]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div[6]/div[2]/div/table/tbody/tr/td[5]/div/div/div[2]/span/span").click()
                sleep(random.randint(7, 12))
                fool_link = driver2.find_element(By.XPATH,"//a[contains(text(),'Go to')]").get_attribute('href')
                sleep(random.randint(5, 7))
                print(fool_link)
        
                driver.get(fool_link)
                sleep(random.randint(3, 6))
                print('Clicked Log in button')
                driver.find_element(By.XPATH,'//*[contains(text(),"Log in")]').click()
                sleep(random.randint(3, 6))
                driver.find_element(By.XPATH,"//p[contains(text(),'sign in with a temporary passcode')]").click()
                sleep(random.randint(9, 12))

                driver.find_element_by_xpath('//*[@id="pwl-email"]').clear()
                ele_email = driver.find_element(By.XPATH,'//*[@id="pwl-email"]')
                print('clear---------------------------------------')
                for character in email:
                    ele_email.send_keys(character)
                    sleep(0.1)
                sleep(random.randint(4, 7))
                driver.find_element(By.XPATH, "//button[contains(text(),'Send a temporary passcode')]").click()
                sleep(random.randint(10, 17))

                el_searchbox = driver2.find_element_by_css_selector(
                'input[aria-label="Search in mail"]'
                )
                el_searchbox.clear()
                email_fool = 'Your Temporary Passcode ' + email
                for character in email_fool:
                    el_searchbox.send_keys(character)
                    sleep(0.1)
                driver2.find_element(By.CSS_SELECTOR,'button[aria-label="Search in mail"]').click()
                sleep(random.randint(8, 10))
                driver2.find_element(By.XPATH,"/html/body/div[7]/div[3]/div/div[2]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div[6]/div[2]/div/table/tbody/tr/td[5]/div/div/div[2]/span/span").click()
                sleep(random.randint(7, 12))

             
                # passcode = driver2.find_element(By.XPATH, "//p[contains(text(),'Dear Fool')]/b").get_attribute('innerText')
                # print('---------------------- {}-----------------'.format(passcode))
                print('passcode..........................')
                passcode = driver2.find_elements_by_xpath("//*/b")[-1].text
                print('-------------------{}---------------------------------------'.format(passcode))
                sleep(random.randint(3, 7))
                ent_passcode = driver.find_element(By.CSS_SELECTOR, '#otp-code')
                for character in passcode:
                    ent_passcode.send_keys(character)
                    sleep(0.1)
                sleep(random.randint(3, 5))
                driver2.close()
                driver.find_element(By.CSS_SELECTOR,'#btn-code').click()
                sleep(3)
                # driver2.switch_to.window(driver2.window_handles[0])

                # WebDriverWait(driver2, 120).until(
                #     EC.presence_of_element_located((By.NAME, "q"))
                # )
                # sleep(random.randint(4, 7))
                # driver2.find_element_by_name("q").send_keys(email)
                # sleep(random.randint(2, 5))
                # driver2.find_element_by_name("q").send_keys(Keys.ENTER)

                # WebDriverWait(driver2, 60).until(
                #     EC.presence_of_element_located(
                #         (
                #             By.XPATH,
                #             "/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div[6]/div[2]/div/table/tbody/tr",
                #         )
                #     )
                # )
                # sleep(random.randint(2, 5))

                # driver2.find_element_by_xpath(
                #     "/html/body/div[7]/div[3]/div/div[2]/div[1]/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[2]/div[6]/div[2]/div/table/tbody/tr"
                # ).click()
                # sleep(random.randint(2, 5))
                # WebDriverWait(driver2, 120).until(
                #     EC.presence_of_element_located((By.XPATH, "//*/b"))
                # )
                # otp = driver2.find_elements_by_xpath("//*/b")[-1].text
                # print(otp)
                # driver2.close()
                # driver.maximize_window()
                # driver.find_element_by_xpath('//*[@id="code"]').send_keys(otp)
                # driver.find_element_by_xpath('//*[@id="code-submit"]').click()
                # password = ""
            except Exception as e:
                print(e)
                try:
                    driver.find_element(By.CSS_SELECTOR,'#id_password')
                    stock_password = generate_random_password()
                    print(f"\nGenarated fool password: {stock_password}")
                    driver.find_element(By.CSS_SELECTOR, '#id_password').send_keys(stock_password)
                    sleep(random.radint(3, 5))
                                 
                    el =  driver.find_element(By.CSS_SELECTOR, '#id_confirm_password')
                    for character in stock_password:
                        el.send_keys(character)
                        sleep(0.1)
                    sleep(random.radint(1, 3))
                    driver.find_element(By.CSS_SELECTOR, '#pw-submit')
                    sleep(random.radint(1, 3))

                    driver.get("https://fool.com")
                    sleep(random.randint(1, 3))
                    WebDriverWait(driver2, 10).until(
                        EC.presence_of_element_located(
                            (By.XPATH, '//a[contains(text(), "Access Premium Services")]')
                        )
                    ).click()
                except:
                    pass

                print("******Cannot find email in main gmail********")
                print("*********Please enter otp below**************")
                # otp = input("Enter otp!!!!    ")

            try:
                WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located(
                        (By.XPATH, '//button[contains(text(), "Continue")]')
                    )
                ).click()
                WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located(
                        (By.XPATH, '//button[contains(text(), "Next")]')
                    )
                ).click()
                WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located(
                        (By.XPATH, '//button[contains(text(), "I Agree")]')
                    )
                ).click()

                WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located(
                        (By.XPATH, '//button[contains(text(), "Get Started")]')
                    )
                ).click()
                sleep(random.randint(1, 3))
                driver.find_elements(By.NAME, "experience_level")[1].click()
                sleep(random.randint(1, 3))
                WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located(
                        (By.XPATH, '//button[contains(text(), "Next")]')
                    )
                ).click()

                sleep(random.randint(1, 3))
                driver.find_elements(By.NAME, "risk_level")[
                    random.randint(0, 2)
                ].click()
                sleep(random.randint(1, 3))
                WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located(
                        (By.XPATH, '//button[contains(text(), "Next")]')
                    )
                ).click()
                sleep(random.randint(1, 3))
                driver.find_elements(By.NAME, "investment_frequency")[
                    random.randint(0, 3)
                ].click()
                sleep(random.randint(1, 3))
                WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located(
                        (By.XPATH, '//button[contains(text(), "Next")]')
                    )
                ).click()
                sleep(random.randint(1, 3))
                driver.find_elements(By.NAME, "preferred_channels")[
                    random.randint(0, 3)
                ].click()
                sleep(random.randint(1, 3))
                WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located(
                        (By.XPATH, '//button[contains(text(), "Next")]')
                    )
                ).click()
                sleep(random.randint(1, 3))
                driver.find_elements(By.NAME, "investing_goals")[
                    random.randint(0, 4)
                ].click()
                sleep(random.randint(1, 3))
                WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located(
                        (By.XPATH, '//button[contains(text(), "Next")]')
                    )
                ).click()
                sleep(random.randint(1, 5))
                WebDriverWait(driver, 15).until(
                    EC.presence_of_element_located(
                        (By.XPATH, '//button[contains(text(), "Some Stock Ideas!")]')
                    )
                ).click()
                pass_reset(driver)
                sleep(random.randint(5, 7))
                email_change(driver, email_for_dollardig)

                sleep(random.randint(3, 5))
                driver.close()

                try:
                    driver.switch_to.window(driver.window_handles[1])

                    driver.close()
                except:
                    pass

                try:
                    driver.switch_to.window(driver.window_handles[0])

                except:
                    pass
                sleep(random.randint(3, 5))
                getscreenshot_of_receipt(driver, email_for_dollardig, password)
            except:
                password_reset(driver)
                sleep(random.randint(5, 7))
                email_change(driver, email_for_dollardig)

                sleep(random.randint(3, 5))
                driver.close()

                try:
                    driver.switch_to.window(driver.window_handles[1])

                    driver.close()
                except:
                    pass

                try:
                    driver.switch_to.window(driver.window_handles[0])

                except:
                    pass
                sleep(random.randint(3, 5))
                getscreenshot_of_receipt(driver, email_for_dollardig, password)

            with open("result.txt", "a") as f:
                f.write(
                    f"{email_for_dollardig},{password_for_dollardig},{email},{creditcardnumber},{Name_on_card},{creditcard_month},{creditcard_year},{csv_number},{Address_1},{Address_2},{City},{State},{Zip_code},{Country},{password}\n"
                )
            print("*****************Correct info*********************")
            print(
                f"{email_for_dollardig},{password_for_dollardig},{email},{creditcardnumber},{Name_on_card},{creditcard_month},{creditcard_year},{csv_number},{Address_1},{Address_2},{City},{State},{Zip_code},{Country},{password}\n"
            )
            with open("dollardig.txt", "r") as f:
                lines = f.readlines()
            with open("dollardig.txt", "w") as f:
                for line in lines:
                    if line.strip("\n") != account:
                        f.write(line)
            with open("info.txt", "r") as f:
                lines = f.readlines()
            with open("info.txt", "w") as f:
                for line in lines:
                    if line.strip("\n") != info:
                        f.write(line)
            with open("Email list.txt", "r") as f:
                lines = f.readlines()
            with open("Email list.txt", "w") as f:
                for line in lines:
                    if line.strip("\n") != email:
                        f.write(line)
            counter += 1
            need_to_remove_list.append(info)

            print("\n***********************************************\n")
            print("**********Succesful registration!!!!!*************")
            break

    else:
        print(
            "\n**********************************************************************\n"
        )
        print(
            "\n**********************************************************************\n"
        )
        print(
            "*****Card info all read in info.txt.Please add some info and re-run it****"
        )
        print(
            "\n**********************************************************************\n"
        )
        print(
            "\n**********************************************************************\n"
        )
        break
