import logging, time
from Common.function import projectPath


class framelog():
    def __init__(self, logger=None):
        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)
        # 创建一个handler，用于写入日志文件
        self.log_time = time.strftime("%Y_%m_%d_")
        # 路径需要修改
        self.log_path = projectPath() + "/Logs/"
        self.log_name = self.log_path + self.log_time + 'log.log'
        print(self.log_name)
        fh = logging.FileHandler(self.log_name, 'a', encoding='utf-8')
        fh.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter(
            '[%(asctime)s] %(filename)s->%(funcName)s line:%(lineno)d [%(levelname)s]%(message)s')
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)

        #  添加下面一句，在记录日志之后移除句柄

        #   self.logger.removeHandler(fh)
        # 关闭打开的文件
        fh.close()

    def log(self):
        return self.logger

