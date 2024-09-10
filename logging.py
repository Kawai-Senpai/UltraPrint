import ultraprint.common as p

class logger:
    def __init__(self, name, filename=None):
        self.name = name
        if filename:
            self.filename = filename
        else:
            self.filename = f'{name}.log'

    def info(self, msg):
        p.cyan(f'INFO: {self.name}: {msg}')
        with open(self.filename, 'a') as f:
            f.write(f'INFO: {self.name}: {msg}\n')

    def error(self, msg):
        p.red(f'ERROR: {self.name}: {msg}')
        with open(self.filename, 'a') as f:
            f.write(f'ERROR: {self.name}: {msg}\n')

    def warning(self, msg):
        p.yellow(f'WARNING: {self.name}: {msg}')
        with open(self.filename, 'a') as f:
            f.write(f'WARNING: {self.name}: {msg}\n')

    def success(self, msg):
        p.green(f'SUCCESS: {self.name}: {msg}')
        with open(self.filename, 'a') as f:
            f.write(f'SUCCESS: {self.name}: {msg}\n')

    def debug(self, msg):
        p.dgray(f'DEBUG: {self.name}: {msg}')
        with open(self.filename, 'a') as f:
            f.write(f'DEBUG: {self.name}: {msg}\n')

    def critical(self, msg):
        p.red_bg(f'CRITICAL: {self.name}: {msg}')
        with open(self.filename, 'a') as f:
            f.write(f'CRITICAL: {self.name}: {msg}\n')