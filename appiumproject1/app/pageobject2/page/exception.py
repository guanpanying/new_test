from app.pageobject2.page.base import BasePage


def exception_handles(fun):
    def magic(*args,**kwargs):
        #取 args[0] ，即函数 func 的第一个入参 self
        instance: BasePage=args[0]
        try:
            result=fun(*args,**kwargs)
            instance._retry=0
            return result
        except Exception as e:
            instance._retry+=1
            if instance._retry>10:
                raise e
            instance.driver.implicitly_wait(0)
            for e in instance._black_list:
                elements=instance.driver.find_elements(*e)
                if len(elements)>0:
                    elements[0].click()
                    instance.driver.implicitly_wait(5)
                    return fun(*args,**kwargs)
    return magic