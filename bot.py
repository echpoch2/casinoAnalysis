from selenium.webdriver import Opera
from selenium.webdriver.opera.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

bank=10
bet = False
while True:
    browser = Opera()
    mort=1
    browser.get('https://csgorun.pro/')
    try:

        WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "graph-label"))
        )
        lem = browser.find_element_by_class_name('graph-label')
        attr_value = lem.get_attribute("href")
        print('find')
        print(attr_value[26:])
        el=WebDriverWait(browser, 75).until(
            EC.presence_of_element_located((By.XPATH, '//a[@href="/games/'+str(int(attr_value[26:])+1)+'"]'))
        )
        coef=el.text[:-1]
        el.click()
        print(bet)
        if ((bet) & (float(coef)>=2)):
            bank+=0.5*2**mort
            mort=1
            bet=False
        if((bet) & (float(coef)<2)):
            bank -= 0.5*2**mort
            mort+=1
            bet = False
        print("bank - ", bank)

        WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "game-stats-list"))
        )
        sum = 0;
        el = browser.find_elements_by_class_name("round-item--green")
        for x in el:
            round=x.find_element_by_class_name('round-item-selected-price').text[:-2]
            sum+=float(round)
        res=float(browser.find_element_by_xpath('//*[@id="root"]/div[1]/div[2]/div[1]/div[2]/div[1]/div/ul/li[1]/b/span').text)-sum
        print(res)
        if(res>=-1000):
            bet=True
        browser.close()
    except Exception as e:
        print(" ")
