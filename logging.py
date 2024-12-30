from datetime import datetime
import inspect
import ultraprint.common as p
import threading
import os
import sys
from pathlib import Path

class logger:
    
    def __init__(self, name, filename=None, include_extra_info=False, write_to_file=True, log_level='INFO', log_format=None, max_file_size=None, backup_count=0, log_to_console=True):
        self.name = name
        self.include_extra_info = include_extra_info
        self.write_to_file = write_to_file

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
        self.log_format = log_format or '[{time}] [{level}] [{name}] {message}'
        self.max_file_size = max_file_size
        self.backup_count = backup_count
        self.log_to_console = log_to_console
        self.lock = threading.Lock()
        
        # Add separator if file exists and write_to_file is True
        if self.write_to_file:
            self._write_separator_if_exists()

    def set_log_level(self, log_level = 'INFO'):
        self.current_log_level = self.log_levels[log_level]
    
    def set_write_to_file(self, write_to_file):
        self.write_to_file = write_to_file

    def _safe_str(self, obj, max_depth=3):
        """Safely convert any object to string with circular reference protection"""
        if max_depth <= 0:
            return "..."
        try:
            if isinstance(obj, (str, int, float, bool)):
                return str(obj)
            elif isinstance(obj, (list, tuple)):
                return f"[{', '.join(self._safe_str(x, max_depth-1) for x in obj[:100])}{'...' if len(obj) > 100 else ''}]"
            elif isinstance(obj, dict):
                return f"{{{', '.join(f'{k}: {self._safe_str(v, max_depth-1)}' for k, v in list(obj.items())[:100])}}}"
            return str(obj)
        except Exception:
            return "[Unstringifiable Object]"

    def _safe_color_print(self, msg, color_func):
        """Safely print colored text with fallback"""
        try:
            color_func(msg)
        except Exception:
            try:
                print(msg)  # Fallback to normal print
            except Exception:
                sys.stderr.write(f"{msg}\n")  # Ultimate fallback

    def _ensure_log_directory(self):
        """Ensure log directory exists"""
        try:
            Path(self.filename).parent.mkdir(parents=True, exist_ok=True)
        except Exception:
            pass  # If we can't create directory, we'll fail at file write anyway

    def _get_extra_info(self):
        try:
            frame = inspect.currentframe()
            if frame is None:
                return "unknown:unknown:0"
            caller = frame.f_back.f_back
            if caller is None:
                return "unknown:unknown:0"
            info = inspect.getframeinfo(caller)
            return f'{info.filename}:{info.function}:{info.lineno}'
        except Exception:
            return "unknown:unknown:0"
        finally:
            del frame  # Prevent reference cycles

    def _format_message(self, *args):
        try:
            # Convert all arguments to strings safely
            msg = ' '.join(self._safe_str(arg) for arg in args)
            return msg[:1000000]  # Limit message size to prevent memory issues
        except Exception as e:
            return f"[Message Formatting Error: {str(e)}]"

    def _log(self, level, *args, color_func):
        try:
            msg = self._format_message(*args)
            current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            extra_info = self._get_extra_info() if self.include_extra_info else ''
            
            try:
                formatted_msg = self.log_format.format(
                    time=current_time,
                    level=level,
                    name=self.name,
                    message=msg,
                    extra_info=extra_info
                )
            except Exception:
                formatted_msg = f"[{current_time}] [{level}] [{self.name}] {msg}"

            if self.log_levels.get(level, 0) >= self.current_log_level:
                if self.log_to_console:
                    self._safe_color_print(formatted_msg, color_func)

            if self.write_to_file:
                with self.lock:
                    self._write_to_file(formatted_msg)
                    
        except Exception as e:
            emergency_msg = f"[EMERGENCY LOG] {datetime.now()} - {str(e)}"
            self._safe_color_print(emergency_msg, p.red)

    def _write_to_file(self, msg):
        try:
            self._ensure_log_directory()
            
            # Check file size before writing
            try:
                if self.max_file_size and os.path.exists(self.filename):
                    if os.path.getsize(self.filename) >= self.max_file_size:
                        self._rotate_logs()
            except Exception:
                pass  # Continue even if rotation fails

            # Try to write with multiple fallbacks
            try:
                with open(self.filename, 'a', encoding='utf-8') as f:
                    f.write(f'{msg}\n')
            except PermissionError:
                alt_file = f"emergency_{self.name}.log"
                try:
                    with open(alt_file, 'a', encoding='utf-8') as f:
                        f.write(f'{msg}\n')
                except Exception:
                    pass  # If all file operations fail, we'll still have console output
        except Exception as e:
            self._safe_color_print(f"[Logger File Write Error: {str(e)}]", p.red)

    def _rotate_logs(self):
        if self.backup_count > 0:
            for i in range(self.backup_count - 1, 0, -1):
                sfn = f"{self.filename}.{i}"
                dfn = f"{self.filename}.{i+1}"
                if os.path.exists(sfn):
                    os.rename(sfn, dfn)
            os.rename(self.filename, f"{self.filename}.1")
        else:
            os.remove(self.filename)

    def _write_separator_if_exists(self):
        """Write a separator to the log file if it already exists"""
        try:
            if os.path.exists(self.filename):
                separator = "\n" + "="*50 + "\n"
                timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                separator_msg = f"{separator}New logging session started at {timestamp}{separator}"
                
                with self.lock:
                    with open(self.filename, 'a', encoding='utf-8') as f:
                        f.write(separator_msg)
        except Exception as e:
            self._safe_color_print(f"[Logger Separator Write Error: {str(e)}]", p.red)

    def exception(self, *args):
        import traceback
        exc_info = traceback.format_exc()
        msg = self._format_message(*args)
        full_msg = f"{msg}\n{exc_info}"
        self._log('ERROR', full_msg, color_func=p.red)

    def info(self, *args):
        self._log('INFO', *args, color_func=p.cyan)

    def error(self, *args):
        self._log('ERROR', *args, color_func=p.red)

    def warning(self, *args):
        self._log('WARNING', *args, color_func=p.yellow)

    def success(self, *args):
        self._log('SUCCESS', *args, color_func=p.green)

    def debug(self, *args):
        self._log('DEBUG', *args, color_func=p.dgray)

    def critical(self, *args):
        self._log('CRITICAL', *args, color_func=p.red_bg)