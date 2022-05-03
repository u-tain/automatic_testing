import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


def line():
    print('______________________________________________________')


def test_adress():
    print('Тестирование поля "Адрес"')
    adr = driver.find_element_by_name('address')
    text_try = (" ", 'петергоф Ботаническая 66', "%^&&")
    for i in range(len(text_try)):
        adr.click()
        adr.send_keys(text_try[i])
        driver.implicitly_wait(5)
        driver.find_element_by_id('downshift-0-input').click()
        if "Неправильно введён адрес" in driver.page_source:
            print('"{}" : Passed\n'.format(text_try[i]))
            adr.send_keys(Keys.CONTROL + 'A', Keys.BACKSPACE)
        else:
            print('"{}" : Failed\n'.format(text_try[i]))
            adr.send_keys(Keys.CONTROL + 'A', Keys.BACKSPACE)
    adr.send_keys('петергоф Ботаническая 66')
    adr.click()
    driver.implicitly_wait(20)
    pl = driver.find_element_by_xpath("//*[contains(text(), 'г Санкт-Петербург," +
                                      " г Петергоф, ул Ботаническая, д. 66," +
                                      " литера А, корп. 2')]")
    pl.click()
    driver.find_element_by_id('downshift-0-input').click()
    if "Неправильно введён адрес" in driver.page_source:
        print('"{}" : Failed\n'.format('Вводим данные корректно'))
    else:
        print('"{}" : Passed\n'.format('Вводим данные корректно'))
    line()


def test_vrem():
    print('Тестирование поля "Дата и время приезда курьера"')
    adr = driver.find_element_by_name('address')
    adr.send_keys(Keys.CONTROL + 'A', Keys.BACKSPACE)
    dat = driver.find_element_by_id('downshift-2-input')
    adr.send_keys('петергоф Ботаническая 66')
    adr.click()
    driver.implicitly_wait(20)
    pl = driver.find_element_by_xpath("//*[contains(text(), 'г Санкт-Петербург," +
                                      " г Петергоф, ул Ботаническая, д. 66," +
                                      " литера А, корп. 2')]")
    pl.click()
    dat.click()
    if not driver.find_elements_by_id('downshift-2-item-0'):
        print('"{}" : Failed\n'.format('Работа поля с введенным адресом'))
    else:
        print('"{}" : Passed\n'.format('Работа поля с введенным адресом'))
    adr.send_keys(Keys.CONTROL + 'A', Keys.BACKSPACE)
    dat.click()
    if not driver.find_elements_by_id('downshift-2-item-0'):
        print('"{}" : Passed\n'.format('Работа поля без введенного адреса'))
    else:
        print('"{}" : Failed\n'.format('Работа поля без введенного адреса'))
    line()


def test_imf():
    print('Тестирование поля "Имя и фамилия"')
    name = driver.find_element_by_name('name')
    input = ('', 'ывоарпгыарпылоа', '&&$^%&*&#^%', 'Ivan', 'Иванов Иван Иванович')
    for i in range(len(input)):
        name.click()
        name.send_keys(input[i])
        driver.find_element_by_id('downshift-0-input').click()
        if "Укажите имя и фамилию" in driver.page_source:
            print('"{}" : Passed\n'.format(input[i]))
            name.send_keys(Keys.CONTROL + 'A', Keys.BACKSPACE)
        else:
            print('"{}" : Failed\n'.format(input[i]))
            name.send_keys(Keys.CONTROL + 'A', Keys.BACKSPACE)
    name.click()
    name.send_keys('Иван Иванов')
    driver.find_element_by_id('downshift-0-input').click()
    if "Укажите имя и фамилию" in driver.page_source:
        print('"{}" : Failed\n'.format('Вводим данные корректно'))
    else:
        print('"{}" : Passed\n'.format('Вводим данные корректно'))
    line()


def test_telef():
    print('Тестирование поля "Телефон отправителя"')
    tef = driver. find_element_by_name('phone')
    input = ('Иван', '3458247', '&^%$#', 'sfdhdhf', '30867868628745067', '8919058735')
    for i in range(len(input)):
        tef.click()
        tef.send_keys(input[i])
        driver.find_element_by_name('documentNumber').click()
        if "Неверный формат телефона" in driver.page_source:
            print('"{}" : Passed\n'.format(input[i]))
            tef.send_keys(Keys.CONTROL + 'A', Keys.BACKSPACE)
        else:
            print('"{}" : Failed\n'.format(input[i]))
            tef.send_keys(Keys.CONTROL + 'A', Keys.BACKSPACE)
    tef.click()
    tef.send_keys('9190587353')
    driver.find_element_by_name('documentNumber').click()
    if "Неверный формат телефона" in driver.page_source:
        print('"{}" : Failed\n'.format('Вводим данные корректно'))
    else:
        print('"{}" : Passed\n'.format('Вводим данные корректно'))
    line()


def test_doq():
    print('Тестирование поля "Номер договора"')
    dock = driver.find_element_by_name('documentNumber')
    dock.click()
    input = ('1234567890987654321123456789098765432112345678',
             '#$%^&*()(*&^%$#', 'эфывапролдджжэжжд')
    for i in range(len(input)):
        dock.send_keys(input[i])
        driver.find_element_by_name('organizationName').click()
        if dock.get_attribute('value') == '' or\
                dock.get_attribute('value').isdigit() == True:
            if len(input[i]) <= 30:
                print('"{}" : Passed\n'.format(input[i]))
            else:
                print('"{}" : Failed\n'.format(input[i]))
            dock.send_keys(Keys.CONTROL + 'A', Keys.BACKSPACE)
        else:
            print('"{}" : Failed\n'.format(input[i]))
            dock.send_keys(Keys.CONTROL + 'A', Keys.BACKSPACE)
    line()


def test_org():
    list = ('Тестирование поля "Наименование организации"',
            'Тестирование поля "Комментарий"')
    id = ('organizationName', 'comment')
    for i in range(len(list)):
        print(list[i])
        pol = driver.find_element_by_id(id[i])
        pol.send_keys('@#$%^&*(')
        if pol.get_attribute('value') == '':
            print('"{}" : Passed\n'.format('@#$%^&*('))
        else:
            print('"{}" : Failed\n'.format('@#$%^&*('))
        line()


def test_ves():
    print('Тестирование поля "Вес"')
    v = driver.find_element_by_name('weight')
    v.click()
    input = ('123456', 'dfgskjh', '@#$%^&*(', '45000')
    for i in range(len(input)):
        v.send_keys(input[i])
        driver.find_element_by_name('organizationName').click()
        if "Вес не соответствует допустимому" in driver.page_source or\
                "Укажите вес" in driver.page_source:
            print('"{}" : Passed\n'.format(input[i]))
            v.send_keys(Keys.CONTROL + 'A', Keys.BACKSPACE)
        else:
            if len(input[i]) >= 5:
                print('"{}" : Passed\n'.format(input[i]))
            else:
                print('"{}" : Failed\n'.format(input[i]))
            v.send_keys(Keys.CONTROL + 'A', Keys.BACKSPACE)
    v.send_keys('50')
    driver.find_element_by_name('organizationName').click()
    if "Вес не соответствует допустимому" in driver.page_source or \
            "Укажите вес" in driver.page_source:
        print('"{}" : Failed\n'.format('Вводим данные корректно'))
    else:
        print('"{}" : Passed\n'.format('Вводим данные корректно'))
    line()


if __name__ == "__main__":
    driver = webdriver.Chrome()
    driver.set_window_size(1000, 700)
    driver.implicitly_wait(20)
    driver.get('https://www.pochta.ru/courier')
    ActionChains(driver).move_by_offset(300, 500).click().perform()
    driver.implicitly_wait(10)
    start_time = time.time()
    test_adress()   # тестирование поля "Адрес"
    test_vrem()     # тестирование поля "Дата и время приезда курьера"
    test_imf()      # тестирование поля "Имя и фамилия отправителя"
    test_telef()    # тестирование поля "Телефон отправителя"
    test_doq()      # тестирование поля "Номер договора"
    test_org()      # тестирование полей "Наименование организации" и "Комментарий"
    test_ves()      # тестирование поля "Вес отправления"
    driver.close()
    print("--- %s seconds ---" % (time.time() - start_time))

