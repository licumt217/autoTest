from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

# 启动一个chrome浏览器
def getChromeBrower():
    option = webdriver.ChromeOptions()
    option.add_argument('--path=D:\python\Scripts\chromedriver.exe')
    option.add_argument('disable-infobars')
    mobileEmulation = {'deviceName': 'iPhone 5'}
    option.add_experimental_option('mobileEmulation', mobileEmulation)
    browser = webdriver.Chrome(chrome_options=option)
    return browser;

# 用红色输出错误日志
def error(msg,e):
    print('\033[0;31;40m =========>'+msg+'\033[0m', e.args)

# 判断给定的元素是否可见
def isElementVisible( element):
    try:
        the_element = EC.visibility_of(element)
        assert the_element(webdriver)
        flag = True
    except:
        flag = False
    return flag

# 将当前页面向下滚动给定的像素
def scrollBottom(browser,num):
    scriptStr='document.documentElement.scrollTop='+str(num);
    browser.execute_script(scriptStr)



