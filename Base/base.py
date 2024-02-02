from Common.Log import framelog


class base():
    def __init__(self, driver):
        self.driver = driver
        self.log = framelog().log()
        self.log.info("info")

    # 把八大定位放在一个函数里面
    def find_ele(self, dic):
        # 传递过来字典第一个即为定位方式
        by = list(dic.keys())[0];
        print("by" + by)
        # 传递过来字典第二个为具体的元素
        ele = list(dic.values())[0];
        self.log.info("id")
        self.log.info("元素" + ele)
        try:
            if by == 'id':
                return self.driver.find_element_by_id(ele)
            elif by == 'name':
                return self.driver.find_element_by_name(ele)
            elif by == 'className':
                return self.driver.find_element_by_class_name(ele)
            elif by == 'linktext':
                return self.find_element_by_link_text(ele)
            elif by == 'partial':
                return self.find_element_by_partial_link_text(ele)
            elif by == "css":
                return self.driver.find_element_by_css_selector(ele)
            elif by == "xpath":
                return self.driver.find_element_by_xpath(ele)
            else:
                return self.driver.find_element_by_tag_name(ele)
        except:
            return None

    # 输入值
    def send_key(self, ele):
        print(ele)
        return self.find_ele(ele)

    # 后退
    def back(self):
        self.driver.back()

    # 前进
    def forword(self):
        self.driver.forward()

    # 当前窗口url
    def url(self):
        self.driver.current_url
