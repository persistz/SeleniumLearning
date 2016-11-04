from selenium import webdriver

def calcRowAndColumn(): #计算整个表格的行和列
    row_count = len(driver.find_elements_by_xpath("//table/tbody/tr"))
    column_count = int(len(driver.find_elements_by_xpath("//table/tbody/tr/td")) / row_count)
    return row_count, column_count

def calcAge(name): #先计算出Name和Age之间列的差值，随后根据输入的Name计算出Age
    xpath = "//tr[]td[]"
    row_count, column_count = calcRowAndColumn()

    for i in range(column_count):
        j = str(i+1)
        xpath = "//tr[1]/td["+j+"]"
        if (driver.find_element_by_xpath(xpath).text == "Name"):
            name_column = i+1
        if (driver.find_element_by_xpath(xpath).text == "Age"):
            age_column = i+1

    for i in range(row_count):
        j = str(i+1)
        xpath = "//tr["+j+"]/td["+str(name_column)+"]"
        if (driver.find_element_by_xpath(xpath).text == name):
            xpath = "//tr[" + j + "]/td[" + str(age_column) + "]"
            return driver.find_element_by_xpath(xpath).text

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.get("file:///C:/Users/zhaoge/Desktop/test.html") #URL
    name = input("Please input the name:")
    print(calcAge(name))