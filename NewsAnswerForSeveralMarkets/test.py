
from selenium import webdriver

import time


driver = webdriver.Chrome()

driver.get("https://www.bing.com/search?q=trump&setflight=NAMktPref&mkt=co-fr")
driver.maximize_window()
time.sleep(2)
#
# # driver.find_element_by_class_name("b_searchbox").clear()
# # driver.find_element_by_class_name("b_searchbox").send_keys(KeyWordsList[i])
# # driver.find_element_by_class_name("b_searchboxSubmit").click()
#
# # Slide page to news answer
# div = driver.find_element_by_xpath('//div[@class="ans_nws"]')
# # Slide to specific place
# js4 = "arguments[0].scrollIntoView();"
# # Slide to previous div area
# driver.execute_script(js4, div)
#
# # Page jump
# # 3 kinds news answer:
# # 1.smab na_overlay_softopt, named overlaySoftopt
# # 2.Hero card,smab na_overlay_softopt下面的na_ti  overlaySoftopt.find_element_by_xpath('//div[@class="na_ti"]').click()
# # overlaySoftopt.find_element_by_xpath('//div[@class="na_cl"]').click() 或 overlaySoftopt.find_element_by_xpath('//div[@class="b_overlay"]').click()
# # 3.
# overlaySoftopt = div.find_element_by_xpath('//div[@class="smab na_overlay_softopt"]')
#
# overlaySoftopt.find_element_by_xpath('//div[@class="b_overlay"]').click()
# # b_overlay = overlaySoftopt.find_element_by_xpath('//div[@class="b_overlay"]')
# time.sleep(5)
# driver.back()
# time.sleep(2)
# # Turn page
# for i in range(3):
#     driver.find_element_by_xpath('//div[@class="b_overlay"]/div[@class="btn next rounded bld"]').click()
#     time.sleep(1)
# time.sleep(1)
# # driver.find_element_by_class_name("b_moreLink rndChev")
# overlaySoftopt.find_element_by_xpath('//div[@class="b_overlay"]/a[@class="b_moreLink rndChev"]').click()  # Not work
#
# # def DetectLang():
# #     DetectorFactory.seed=0   # Make the result unique.
# #     ExpText = "¡Beijing le da la bienvenida!"
# #
# #     print(detect(ExpText))        # Langs
# #   print(detect_langs(ExpText))  # Langs and its probability

# eleNews->hero card
driver.find_element_by_xpath('//div[@class="elec-modRoot elec-newsMod  b_canvas"]/div[@class="elec-modRoot-data"]/div[@class="elec-newsMod-hero"]/')
# eleNews->hero card->normal news
driver.find_element_by_xpath('//div[@class="elec-modRoot elec-newsMod  b_canvas"]/div[@class="elec-modRoot-data"]/div[@class="b_canvas b_slideexp"]/div[@class="b_overlay"]')
# eleNews->hero card->normal news->page turn button
driver.find_element_by_xpath('//div[@class="elec-modRoot elec-newsMod  b_canvas"]/div[@class="elec-modRoot-data"]/div[@class="b_canvas b_slideexp"]/div[@class="b_overlay"]/div[@class="btn next rounded bld"]')
driver.find_element_by_xpath('//div[@class="elec-modRoot elec-newsMod  b_canvas"]/div[@class="elec-modRoot-data"]/div[@class="b_canvas b_slideexp"]/div[@class="b_overlay"]/div[@class="btn prev rounded bld"]')

# heroCard
driver.find_element_by_xpath('//div[@class="ans_nws"]/div[@class="smab na_overlay_softopt"]/div[@class="na_cnt"]/div[@class="na_ti"]')
# heroCard->normal news
driver.find_element_by_xpath('//div[@class="ans_nws"]/div[@class="smab na_overlay_softopt"]/div[@class="na_cnt"]/div[@id="na_cl"]')
# heroCard->normal news->page turn button
driver.find_element_by_xpath('//div[@class="ans_nws"]/div[@class="smab na_overlay_softopt"]/div[@class="na_cnt"]/div[@id="na_cl"]/div[@class="b_canvas b_slideexp"]/div[@class="b_overlay"]/div[@class="btn next rounded bld"]')
driver.find_element_by_xpath('//div[@class="ans_nws"]/div[@class="smab na_overlay_softopt"]/div[@class="na_cnt"]/div[@id="na_cl"]/div[@class="b_canvas b_slideexp"]/div[@class="b_overlay"]/div[@class="btn prev rounded bld"]')

# normal news
driver.find_element_by_xpath('//div[@class="ans_nws"]/div[@class="smab na_overlay_softopt"]/div[@class="na_cnt"]/div[@id="na_cl"]/div[@class="b_canvas b_slideexp"]/div[@class="b_overlay"]')
# normal news-page turn button
driver.find_element_by_xpath('//div[@class="ans_nws"]/div[@class="smab na_overlay_softopt"]/div[@class="na_cnt"]/div[@id="na_cl"]/div[@class="b_canvas b_slideexp"]/div[@class="b_overlay"]/div[@class="btn next rounded bld"]')
driver.find_element_by_xpath('//div[@class="ans_nws"]/div[@class="smab na_overlay_softopt"]/div[@class="na_cnt"]/div[@id="na_cl"]/div[@class="b_canvas b_slideexp"]/div[@class="b_overlay"]/div[@class="btn prev rounded bld"]')
