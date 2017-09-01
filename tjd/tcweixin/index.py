import time;
import tjdUtils;

browser = tjdUtils.getChromeBrower();


# 跳转登录页面并登陆
def login(phone):

    browser.get('http://prep.tingjiandan.com/tcweixin/letter/login/login')

    phoneInput= browser.find_element_by_class_name('yzm-phone')
    yzmInput=   browser.find_element_by_class_name('yzm-yzm')
    getYzmBtn=  browser.find_element_by_class_name('yzm-get-yzm')
    confirmBtn= browser.find_element_by_class_name('yzm-btn')

    phoneInput.send_keys(phone);
    time.sleep(1)
    getYzmBtn.click()
    time.sleep(1)
    yzmInput.send_keys('1025')
    time.sleep(1)

    # 如果此用户没有车辆信息，则跳转到添加汽车页面，否则跳转到订单列表页面
    confirmBtn.click()
    time.sleep(1)

# 跳转到个人中心
def go2Center():
    browser.get('http://prep.tingjiandan.com/tcweixin/letter/center/newCenter')

# 跳转到我的汽车
def go2MyCar():
    browser.get('http://prep.tingjiandan.com/tcweixin/letter/myCar/myCar')

# 跳转到订单列表页面
def go2MyOrder():
    browser.get('http://prep.tingjiandan.com/tcweixin/letter/myOrder/myOrder')

# 当前页面是否是车辆列表页面
def isNowCarList():
    index=browser.current_url.find('myCar/myCar')
    if index>-1:
        return True;
    else:
        return False;

# 新增车辆和修改车辆时输入车牌号
def fillCarNum(carNum):
    for index in range(len(carNum)):
        time.sleep(1)
        if index == 0:
            browser.find_element_by_css_selector('.tjd_carnum_one input[value="' + carNum[index] + '"]').click()
        else:
            browser.find_element_by_css_selector('.tjd_carnum_two input[value="' + carNum[index] + '"]').click()

# 添加车辆
def addCar(carNum):
    try:
        # 如果此时在addCar页面，则直接输入车牌；如果在myCar页面，则点击添加车辆按钮
        time.sleep(1)
        if isNowCarList():
            addBtn = browser.find_element_by_css_selector('#content > div > a > img')
            addBtn.click()

        fillCarNum(carNum)

        confirmBtn = browser.find_element_by_class_name('sure')
        modalConfirmBtn = browser.find_element_by_class_name('tjd_confirm')
        confirmBtn.click()
        time.sleep(1)
        modalConfirmBtn.click();
        time.sleep(1)
        modalConfirmBtn.click()
    except Exception as e:
        tjdUtils.error('添加车辆功能异常', e)


# 删除车辆
def delCar(carNum):

    try:
        time.sleep(1)
        delBtn = browser.find_element_by_css_selector('article[delCarNum="' + carNum + '"] .delete')
        modalConfirmBtn = browser.find_element_by_class_name('tjd_confirm')
        delBtn.click()
        time.sleep(1)
        modalConfirmBtn.click()
        time.sleep(1)
        modalConfirmBtn.click()
    except Exception as e:
        tjdUtils.error('删除车辆功能异常', e)

# 修改车辆
def modifyCar(oldCarNum,newCarNum):

    try:
        time.sleep(1)
        # TODO 此处不知为何用nth-child()定位不好使
        modifyBtn = browser.find_elements_by_css_selector('article[delCarNum="' + oldCarNum + '"] .carState a:last-child')[1];
        modifyBtn.click()
        time.sleep(1)
        confirmBtn = browser.find_element_by_class_name('sure')
        fillCarNum(newCarNum)
        confirmBtn.click()
        time.sleep(1)
        modalConfirmBtn = browser.find_element_by_class_name('tjd_confirm')
        modalConfirmBtn.click();
        time.sleep(1)
        modalConfirmBtn.click();
    except Exception as e:
        tjdUtils.error('修改车辆功能异常', e)

# 验证车辆
def verifyCar(carNum,motorNum,viNum):

    try:
        time.sleep(1)
        verifyBtns = browser.find_elements_by_css_selector('article[delCarNum="' + carNum + '"] .carState a:first-child');
        verifyBtn='';
        for btn in verifyBtns:
            if tjdUtils.isElementVisible(btn):
                verifyBtn=btn;
                break;

        verifyBtn.click()
        time.sleep(1)
        motorNumInput=browser.find_element_by_css_selector('#content input:first-child');
        viNumInput=browser.find_element_by_css_selector('#content input:last-child');
        if tjdUtils.isElementVisible(motorNumInput):
            time.sleep(1)
            print(55555)
            motorNumInput.send_keys(motorNum)
        if tjdUtils.isElementVisible(viNumInput):
            print(22222222)
            time.sleep(1)
            viNumInput.send_keys(viNum)


        print(111)
        confirmBtn = browser.find_element_by_class_name('verified')
        confirmBtn.click()
        time.sleep(1)
    except Exception as e:
        tjdUtils.error('验证车辆功能异常', e)


# 进行待还款订单一系列的操作，除了真正的支付；当有多条待还款订单时，由于页面back后WebElement的状态发生改变，没法继续遍历，故目前只操作第一条单子
def handleToPayOrders():
    toPayOrders=browser.find_elements_by_class_name('toPayment')
    if len(toPayOrders)>0:
        for index in range(len(toPayOrders)):
            if index==0:
                order=toPayOrders[0];
                time.sleep(1)
                order.click();
                time.sleep(1)
                payBtn=browser.find_element_by_class_name('surePayBtn')
                if tjdUtils.isElementVisible(payBtn):
                    payBtn.click();
                    time.sleep(1)
                    closeBtn=browser.find_element_by_class_name('closeBox')
                    closeBtn.click()
                    time.sleep(1)
                    orderHandleBtn=browser.find_element_by_class_name('orderOption');
                    orderHandleBtn.click();
                    time.sleep(1);
                    questBackBtn = browser.find_element_by_css_selector('.operateItem li:last-child')
                    questBackBtn.click()
                    time.sleep(1)
                    ghostOrderBtn = browser.find_element_by_css_selector('.operateItem li:last-child')
                    ghostOrderBtn.click()
                    time.sleep(1)
                    browser.back()
                    time.sleep(1)
                    browser.back()
                    time.sleep(1)
                    browser.back()
                    time.sleep(1)
                    browser.back()

# 进行当前订单的一系列操作
def handleCurOrders():
    curOrders = browser.find_elements_by_class_name('prepay_open_side')

    if len(curOrders) > 0:
        for index in range(len(curOrders)):
            order = curOrders[index];
            if tjdUtils.isElementVisible(order):

                time.sleep(1)
                order.click();
                time.sleep(1)
                payBtn = browser.find_element_by_css_selector('#content > div.orderDetailContent > article.payAmountInfo > input:nth-child(2)');
                if tjdUtils.isElementVisible(payBtn):
                    payBtn.click();
                    time.sleep(1)
                    closeBtn = browser.find_element_by_class_name('closeBox')
                    closeBtn.click()
                    time.sleep(1)
                    orderHandleBtn = browser.find_element_by_class_name('orderOption');
                    orderHandleBtn.click();
                    time.sleep(1);
                    questBackBtn = browser.find_element_by_css_selector(
                        '.operateItem li:last-child')
                    questBackBtn.click()
                    time.sleep(1)
                    ghostOrderBtn = browser.find_element_by_css_selector(
                        '.operateItem li:last-child')
                    ghostOrderBtn.click()
                    time.sleep(1)
                    browser.back()
                    time.sleep(1)
                    stillChargingBtn = browser.find_element_by_css_selector(
                        '#content > ul > li:nth-child(1)')
                    stillChargingBtn.click()
                    time.sleep(1)
                    deleteBtn =browser.find_element_by_class_name('sureQuestion')
                    deleteBtn.click()
                    time.sleep(1)
                    modalCancelBtn=browser.find_element_by_class_name('tjd_cancel')
                    modalCancelBtn.click();
                    time.sleep(1)
                    browser.back()
                    browser.back()
                    time.sleep(1)
                    cashPayBtn=browser.find_element_by_css_selector(
                        '#content > ul > li:nth-child(1)')
                    cashPayBtn.click()
                    time.sleep(1)

                    # 执行两遍，测试开关是否好用
                    for index in range(2):
                        cashPayBtn=browser.find_element_by_class_name('onoffswitchtjd-label');
                        cashPayBtn.click();
                        time.sleep(1)
                        modalConfirmBtn = browser.find_element_by_class_name('tjd_confirm')
                        modalConfirmBtn.click();
                        time.sleep(1)
                        modalConfirmBtn.click();
                        time.sleep(1)
                    browser.back()
                    time.sleep(1)
                    browser.back()
                    time.sleep(1)
                    browser.back()
                break;

def handleHistoryOrders():
    # 先滚动到最底部
    tjdUtils.scrollBottom(browser,1500);
    time.sleep(2)
    moreHistoryBtn=browser.find_element_by_id('pullUp');
    if tjdUtils.isElementVisible(moreHistoryBtn):
        moreHistoryBtn.click();
        time.sleep(1)

    historyBtns=browser.find_elements_by_class_name('historyment');
    if len(historyBtns)>0:
        historyBtn=historyBtns[0];
        historyBtn.click();
        time.sleep(1)
        orderOperateBtn=browser.find_element_by_class_name('orderOption');
        orderOperateBtn.click();
        time.sleep(1)
        questionBackBtn=browser.find_element_by_css_selector('.operateItem li:last-child')
        questionBackBtn.click()
        time.sleep(1)
        ghostOrderBtn=browser.find_element_by_css_selector('.operateItem li:last-child');
        ghostOrderBtn.click();
        time.sleep(1)
        browser.back()
        time.sleep(1)
        stillChargingBtn = browser.find_element_by_css_selector('.operateItem li:first-child');
        stillChargingBtn.click();
        time.sleep(1)
        deleteBtn=browser.find_element_by_class_name('sureQuestion')
        deleteBtn.click();
        time.sleep(1)
        modalConfirmBtn = browser.find_element_by_class_name('tjd_confirm')
        modalConfirmBtn.click();
        time.sleep(1)
        modalConfirmBtn.click();

def go2ParkList():
    browser.get('http://prep.tingjiandan.com/tcweixin/letter/myOrder/parkList')


# 订单列表页面相关操作：遍历所有的当前单子和待还款单子和一条历史订单
def handleOrders():
    # handleCurOrders()
    # handleToPayOrders()
    handleHistoryOrders()

def handleParkList():
    while True:
        searchInput = browser.find_element_by_id('searchInput')
        if tjdUtils.isElementVisible(searchInput):
            searchInput.send_keys('测试');
            time.sleep(2)
            break;
    suggestList=browser.find_elements_by_class_name('ui-menu-item')
    if len(suggestList)>0:
        for index in range(len(suggestList)):
            suggest=suggestList[index]
            if(tjdUtils.isElementVisible(suggest)):
                suggest.click();
                time.sleep(5)
                break;
    parkList=browser.find_elements_by_class_name('parkingDetail');
    if len(parkList)>0:
        parkList[0].click();
    time.sleep(1)
    # TODO此处滚动不起作用，查下原因
    tjdUtils.scrollBottom(browser, 300)
    # browser.back()
    # time.sleep(5)








# 切换用户
def switchUser():
    switchUserBtn=browser.find_element_by_class_name('unbind')
    time.sleep(1)
    switchUserBtn.click()

login('18511498555')
# go2Center()
# switchUser()
# login('18210676127')
# go2MyCar()
# addCar('京BBBAAA')
# modifyCar('豫A99FFS','豫A99FFF')
# verifyCar('京BBBAAA','111AAA',1)
# delCar('京A11311');
# handleOrders()
go2ParkList();
handleParkList();


