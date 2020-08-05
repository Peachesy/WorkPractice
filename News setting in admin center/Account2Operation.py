from selenium import webdriver
import time


# 用chrome测试

driver = webdriver.Chrome()
driver.get("https://admin.microsoft.com/Adminportal/Home#/Settings/Services/:/Settings/L1/BingNews")

account = "admin@newstestadmincenter01.onmicrosoft.com"
password = "Datou123"

driver.find_element_by_name("loginfmt").send_keys(account)

driver.find_element_by_id("idSIButton9").click()

driver.find_element_by_name("passwd").send_keys(password)
time.sleep(5)
driver.find_element_by_id("idSIButton9").submit()
time.sleep(5)
driver.find_element_by_id("idSIButton9").submit()

js="""
var span = document.createElement('span');
        span.innerHTML = 'We will clear all the old options!';
        span.style.position = 'absolute';
        span.style.top = '49%';
        span.style.left = '47%';
        span.style.color = 'red';
        span.style.fontSize = '20px';
        document.body.appendChild(span);
        setTimeout(function() {document.body.removeChild(span)},9000);
"""
# driver.execute_script(js)
# # Clear all options 得用xpath
# # driver.find_element_by_xpath("//*[@]")
# # Industry drop-down list
# driver.find_element_by_id("Dropdown157-option").clear()
# # Topic input box
# driver.find_element_by_class_name("ms-BasePicker-input input-615").clear()

# check Include on Bing homepage and do nothing.
driver.find_element_by_class_name("ms-Checkbox-checkmark checkmark-310").click()
driver.find_element_by_class_name("ms-Button-flexContainer flexContainer-145").click()
# check Include on Bing homepage and select an industry no topics.
# check Include on Bing homepage and select an industry and a topics.
# check Include on Bing homepage and select several industries no topics.
# check Include on Bing homepage and select several industries and a topic.
# check Include on Bing homepage and select several industries and several topics.


# # Clear all options
# def ClearOptions(driver):
#     # Check button
#     driver.find_element_by_class_name("ms-Checkbox-checkmark checkmark-591").clear()
#     # Industry drop-down list
#     driver.find_element_by_id("Dropdown157-option").clear()
#     # Topic input box
#     driver.find_element_by_class_name("ms-BasePicker-input input-615").clear()