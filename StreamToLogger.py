# модули для записи логов с временными метками - ВДОРАБОТКЕ
import sys
import logging
from datetime import datetime

 # Определяем класс для перенаправления вывода
class StreamToLogger:
    def __init__(self, a, log_level=logging.INFO):
        self.logger = a
        self.log_level = log_level
        self.linebuf = ''

    def write(self, buf):
        for line in buf.rstrip().splitlines():
            self.logger.log(self.log_level, line.rstrip())

    def flush(self):
        pass


