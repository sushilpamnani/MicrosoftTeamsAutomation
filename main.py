# Enter Teams ID on line 38
# Enter your Password on line 44


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

import time

PATH = "C:\Program Files (x86)\chromedriver.exe"

opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")

opt.add_experimental_option("prefs", { \
"profile.default_content_setting_values.media_stream_mic": 1, 
"profile.default_content_setting_values.media_stream_camera": 1,
"profile.default_content_setting_values.geolocation": 0, 
"profile.default_content_setting_values.notifications": 1 
})


driver = webdriver.Chrome(chrome_options=opt, executable_path=PATH)

#**********************************JOIN VIA CALENDAR*********************************

driver.get('https://login.microsoftonline.com/common/oauth2/authorize?response_type=id_token&client_id=5e3ce6c0-2b1f-4285-8d4b-75ee78787346&redirect_uri=https%3A%2F%2Fteams.microsoft.com%2Fgo&state=c928856a-54b2-469c-a938-30b878f508ae&client-request-id=9d975270-1839-4da8-980a-e65a46b21631&x-client-SKU=Js&x-client-Ver=1.0.9&nonce=16e1d9f7-f62b-468f-a1a2-35c743aa9669&domain_hint=&sso_reload=true')
print(driver.title)

search = driver.find_element_by_id("i0116")
search.send_keys("")                                                        # Enter your Teams ID here
search.send_keys(Keys.RETURN)

time.sleep(2)

search = driver.find_element_by_id("i0118")
search.send_keys("")                                                        # Enter your Password Here
search.send_keys(Keys.RETURN)

time.sleep(2)

search = driver.find_element_by_id("idSIButton9")
search.send_keys(Keys.RETURN)

tiem.sleep(2)

try:
    element = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "app-bar-ef56c0de-36fc-4ef8-b417-3d82ba9d073c"))
    )
    element.click()

    
except:
    driver.quit()

time.sleep(10)

element = driver.find_element_by_class_name("node_modules--msteams-bridges-components-calendar-event-card-dist-es-src-renderers-event-card-renderer-event-card-renderer__joinButton--1AeXc")
element.send_keys(Keys.RETURN)

time.sleep(2)

actions = ActionChains(driver)
actions.send_keys(Keys.TAB + Keys.RETURN + Keys.TAB + Keys.RETURN + Keys.TAB * 10 + Keys.RETURN)
actions.perform()
# element = driver.find_element_by_class_name("app-svg icons-call-microphone")
# element.send_keys(Keys.RETURN)

# ********************JOIN DIRECTLY USING MEETING LINK************************

# driver.get("https://teams.microsoft.com/l/meetup-join/19%3ameeting_MjU4MTk1MWUtNzcyNC00Y2E4LWEzM2EtMTRmY2M4MzZlOWY3%40thread.v2/0?context=%7b%22Tid%22%3a%2276bed47f-8633-49b2-8de1-35950dd0251c%22%2c%22Oid%22%3a%22082845a1-8a9b-4eaa-95a3-643090839eb4%22%7d")
# time.sleep(5)

# alert = WebDriverWait(driver, 5).until(
#     EC.alert_is_present()
# )

# driver.switch_to_alert().dismiss()
