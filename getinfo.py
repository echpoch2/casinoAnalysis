from selenium.webdriver import Opera
from selenium.webdriver.opera.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
browser = Opera(executable_path='D:\web\operadriver.exe')
f = open('info.txt', 'a')

for i in range(1415845,1415944):
    browser.get('https://csgorun.pro/games/'+str(i))
    el = 0
    try:
        WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "game-stats-list"))
        )
        el = browser.find_elements_by_class_name("round-item--green")
        for x in el:
            price=x.find_element_by_class_name('price').text[:-2]
            statusLabel=x.find_element_by_class_name('status-label').text[:-1]
            round=x.find_element_by_class_name('round-item-selected-price').text[:-2]
            f.write(str(i)+","+price+","+statusLabel+","+round+","+'Win' + '\r\n')
            print(i)
        el = browser.find_elements_by_class_name("round-item--red")
        for x in el:
            f.write(str(i)+", "+x.find_element_by_class_name('price').text[:-2]+","+x.find_element_by_class_name('status-label').text[:-1]+",0,"+'Lose'+'\r\n')



    except Exception as e:
        print(e.message, e.args)

    print(len(el))


print(1)