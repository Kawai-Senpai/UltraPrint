from datetime import datetime
import inspect
import ultraprint.common as p

class logger:
    def __init__(self, name, filename=None, include_extra_info=False):
        self.name = name
        self.include_extra_info = include_extra_info
        if filename:
            self.filename = filename
        else:
            self.filename = f'{name}.log'

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
        color_func(formatted_msg)
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
