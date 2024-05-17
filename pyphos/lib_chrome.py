import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import lib_phos

# from Phos import SM

# 2021-01-17 disable for debugging
# browser = webdriver.Firefox(executable_path="./drivers/geckodriver")
#browser = webdriver.Chrome(executable_path=r"./drivers/chromedriver")

# 2023-12-02 Latest Selenium no need chromedriver ??
browser = webdriver.Chrome()
driver    = browser # code compatibililty

S = lib_phos.S

# browser.get('http://www.google.com')
def f_get():
  browser.get( S.pop() )
   

def f_js():
  driver.execute_script( S.pop() )
  
def f_ac(): # appendChild()
  driver.execute_script( 'f_appc("'+ S.pop() +'")' )

JS_AC = "function f_appc( s ) { var body=document.getElementsByTagName('body')[0]; var B=document.createElement('div'); B.innerHTML=s; body.appendChild(B); }"
driver.execute_script( JS_AC )

# windows_before = driver.current_window_handle   

def f_tab():
  S.append( driver.current_window_handle )
  
def f_tabs():
  S.append( driver.window_handles )
  
#  driver.execute_script("window.open('http://phos.epizy.com/phos/post_rc.php?r=&c=')")

def f_newtab():
  driver.execute_script("window.open('"+ S.pop() +"')")
  #driver.execute_script('window.open('+ S.pop() +')')

def f_switch():
  driver.switch_to.window(S.pop())

def f_utabs(): # get URL of tabs
    f_tabs()
    L = S[-1]
    L_U = []
    for x in L:
      driver.switch_to.window(x)
      print(driver.current_url)
      L_U.append(driver.current_url)
    
    S.append(L_U)


# print('Title: %s' % browser.title)

def wait_alert(browser):
    while (1): # loop indefinite wait = indefinite + wait
        try:
            WebDriverWait(browser, 30).until(EC.alert_is_present(), 'Timed out waiting for PA creation ' + 'confirmation popup to appear.')
            alert = browser.switch_to.alert
            alert.accept()
            print("alert accepted")
            break
        except TimeoutException:
            print("no alert")



