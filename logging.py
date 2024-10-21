
from datetime import datetime
import inspect
import ultraprint.common as p

class logger:
    
    def __init__(self, name, filename=None, include_extra_info=False, write_to_file=True, log_level='INFO'):
        self.name = name
        self.include_extra_info = include_extra_info
        self.write_to_file = True

        if filename:
            self.filename = filename
        else:
            self.filename = f'{name}.log'

        self.log_levels = {
            'DEBUG': 0,
            'INFO': 1,
            'SUCCESS': 2,
            'WARNING': 3,
            'ERROR': 4,
            'CRITICAL': 5
        }

        self.current_log_level = self.log_levels[log_level]

    def set_log_level(self, log_level = 'INFO'):
        self.current_log_level = self.log_levels[log_level]
    
    def set_write_to_file(self, write_to_file):
        self.write_to_file = write_to_file

    def _get_extra_info(self):
        frame = inspect.currentframe().f_back.f_back
        info = inspect.getframeinfo(frame)
        return f'{info.filename}:{info.function}:{info.lineno}'

    def _log(self, level, msg, color_func):
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        extra_info = self._get_extra_info() if self.include_extra_info else ''
        if self.include_extra_info:
            extra_info = self._get_extra_info()
            formatted_msg = f'[{current_time}] [{level}] [{self.name}] {msg} [{extra_info}]'
        else:
            formatted_msg = f'[{current_time}] [{level}] [{self.name}] {msg}'
        
        if self.log_levels[level] >= self.current_log_level:
            color_func(formatted_msg)
        
        if self.write_to_file:
            with open(self.filename, 'a') as f:
                f.write(f'{formatted_msg}\n')

    def info(self, msg):
        self._log('INFO', msg, p.cyan)

    def error(self, msg):
        self._log('ERROR', msg, p.red)

    def warning(self, msg):
        self._log('WARNING', msg, p.yellow)

    def success(self, msg):
        self._log('SUCCESS', msg, p.green)

    def debug(self, msg):
        self._log('DEBUG', msg, p.dgray)

    def critical(self, msg):
        self._log('CRITICAL', msg, p.red_bg)