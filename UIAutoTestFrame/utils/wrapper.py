from UIAutoTestFrame.utils.log import log
import allure

# 在BasePage中使用该装饰器操作弹窗黑名单，同时需要使用basepage中的find方法操作弹窗，
def handle_black(func):

    def wrapper(*args, **kwargs):
        # 要在方法内部导入BasePage，如果在文件顶部导入 会发生导包层级错误
        from UIAutoTestFrame.page.base_page import BasePage
        _black_list = [
            ["xpath", '//*[@resource-id="com.xueqiu.android:id/tv_agree"]'],
            ]
        # 获取basepage对象
        instance: BasePage = args[0]

        # 如果弹窗出现后，操作弹窗失败，或者一个页面出现多个弹窗，就会进入死循环
        _max_num = 3
        _error_num = 0

        try:
            element = func(*args, **kwargs)
            _error_num = 0
            return element
        except Exception as e:
            log(f'操作元素失败，开始循环处理弹窗黑名单')
            instance.get_screenshot('errorImg/tmp.png')
            with open('errorImg/tmp.png', 'rb') as f:
                pic = f.read()
            allure.attach(pic, attachment_type=allure.attachment_type.PNG)
            if _error_num > _max_num:
                raise e
            _error_num += 1

            for ele in _black_list:
                elelist = instance.finds(ele)
                if len(elelist) > 0:
                    elelist[0].click()
                    return wrapper(*args, **kwargs)
            raise e
    return wrapper