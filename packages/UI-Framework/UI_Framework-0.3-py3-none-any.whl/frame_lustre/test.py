import pytest, allure
from frame_lustre.Framework import keyboard
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(scope="session")
def driver():
    global driver
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

    kb = keyboard
    test_data_test_case_1 = kb.read_all_sheets('dataDriverTest.xlsx')
    print(test_data_test_case_1,)
@allure.feature("登录功能")
@allure.story("用户登录")
def test_RB_login(driver):
    kb = keyboard(driver)
    kb.open("http:60.204.202.133:10203/#/login")
    kb.pause(5)
    kb.entered(By.XPATH,
               "/html/body/div/div[3]/div/form/div[1]/div[2]/div/span/input",
               "admin")
    kb.entered(By.XPATH,
               "/html/body/div/div[3]/div/form/div[2]/div[2]/div/span/span/input",
               "123456")
    kb.enter(By.XPATH,
             "/html/body/div[1]/div[3]/div/form/div[3]/div/div/span/button")
    kb.pause(3)
    kb.assert_text(kb.get_text(By.XPATH,
                               "/html/body/div[1]/section/header/div[1]"),
                   "统一应用管理平台")

@allure.feature("下拉框选择")
@allure.story("黑名单分页")
def test_check_options_type(driver):
    kb = keyboard(driver)
    test_RB_login(driver)
    kb.pause(3)
    kb.open("http://60.204.202.133:10203/#/systems/log")
    kb.pause(3)
    kb.click(By.XPATH,
             "/html/body/div[1]/section[@class='ant-layout']/section[@class='ant-layout ant-layout-has-sider']/section[@class='ant-layout']/main[@class='ant-layout-content']/div/div[@class='gkp-search-box-wrap']/div[@class='gkp-search-box']/div[@class='ant-row']/div[@class='item-wrap']/div[@class='ant-col ant-col-18 ant-col-xs-6 ant-col-sm-6 ant-col-md-6 ant-col-lg-6 ant-col-xl-6']/div[@class='ant-select ant-select-enabled']/div[@class='ant-select-selection ant-select-selection--single']/span[@class='ant-select-arrow']/i[@class='anticon anticon-down ant-select-arrow-icon']")
    kb.pause(3)
    kb.drop_down_box(By.XPATH, "/html/body/div[3]/div/div/div/ul/li", "黑名单分页")
    kb.click(By.XPATH, "/html/body/div[1]/section/section/section/main/div/div[1]/div/div[2]/button[1]")
    kb.pause(1)
    kb.screenshot("黑名单分页查询.png")
    kb.pause(5)


@allure.feature("测试")
@allure.story("测试")
def test_test(driver):
    kb = keyboard(driver)
    test_RB_login(driver)
    kb.open("http://60.204.202.133:10203/#/systems/log")
    kb.pause(3)
    kb.click(By.XPATH,
              "/html/body/div[1]/section[@class='ant-layout']/section[@class='ant-layout ant-layout-has-sider']/section[@class='ant-layout']/main[@class='ant-layout-content']/div/div[@class='gkp-search-box-wrap']/div[@class='gkp-search-box']/div[@class='ant-row']/div[@class='item-wrap']/div[@class='ant-col ant-col-18 ant-col-xs-6 ant-col-sm-6 ant-col-md-6 ant-col-lg-6 ant-col-xl-6']/div[@class='ant-select ant-select-enabled']/div[@class='ant-select-selection ant-select-selection--single']/span[@class='ant-select-arrow']/i[@class='anticon anticon-down ant-select-arrow-icon']")
    kb.click(By.XPATH, "/html/body/div[3]/div/div/div/ul/li[1]")
    kb.pause(5)
