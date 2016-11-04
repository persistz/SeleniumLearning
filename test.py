from selenium import webdriver

driver = webdriver.Firefox()
driver.get("file:///C:/Users/zhaoge/Desktop/test.html")
name = "tank Xiao"

#print(driver.find_element_by_xpath("//td[contains(.,'tank')]").text)
#print(driver.find_element_by_xpath("//td[contains(..,'tank')]").text)
row_count = len(driver.find_elements_by_xpath("//table/tbody/tr"))
column_count = int(len(driver.find_elements_by_xpath("//table/tbody/tr/td"))/row_count)

print(row_count, column_count)

xpath = "//tr[]td[]"
global name_column
global age_column
global name_age_column


for i in range(column_count):
    j = str(i+1)
    xpath = "//tr[1]/td["+j+"]"
    if (driver.find_element_by_xpath(xpath).text == "Name"):
        name_column = i+1
    if (driver.find_element_by_xpath(xpath).text == "Age"):
        age_column = i+1
        name_age_column = i+1-name_column

print(name_column, age_column, name_age_column)

for i in range(row_count):
    j = str(i+1)
    xpath = "//tr["+j+"]/td["+str(name_column)+"]"
    if (driver.find_element_by_xpath(xpath).text == name):
        xpath = "//tr[" + j + "]/td[" + str(age_column) + "]"
        print(driver.find_element_by_xpath(xpath).text)