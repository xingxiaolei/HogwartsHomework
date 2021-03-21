
import logging
import sys, datetime, os


def log(message):

    # 获取logger实例，如果参数为空则返回root logger
    logger = logging.getLogger("AppAPI")

    # 指定logger输出格式
    formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')

    # 文件日志
    test_log = os.path.abspath(os.path.dirname(os.path.dirname(__file__)) + "//logs//")
    today = datetime.date.today()
    file_name = str(today) + '_log.txt'
    file_path = os.path.join(test_log, file_name)
    file_handler = logging.FileHandler(file_path, encoding='utf=8')
    file_handler.setFormatter(formatter)  # 可以通过setFormatter指定输出格式

    # 控制台日志
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.formatter = formatter  # 也可以直接给formatter赋值

    # 为logger添加的日志处理器，可以自定义日志处理器让其输出到其他地方
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    # 指定日志的最低输出级别，默认为WARN级别
    logger.setLevel(logging.INFO)

    # 输出不同级别的log
    # logger.debug(message)
    logger.info(message)
    # logger.warn(message)
    # logger.error(message)
    # logger.fatal(message)
    # logger.critical(message)

    #  在记录日志之后移除句柄
    logger.removeHandler(file_handler)
    logger.removeHandler(console_handler)


if __name__ == '__main__':
    log('a')
