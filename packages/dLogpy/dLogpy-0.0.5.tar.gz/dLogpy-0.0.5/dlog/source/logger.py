import json
import multiprocessing
import threading
from inspect import getframeinfo, stack
from time import time
from pprint import pformat
from threading import Lock as ThreadLock
from multiprocessing import Lock as ProcessLock
from multiprocessing.synchronize import Lock as ProcessLockType
from typing import Any

from . import utils, values
from .record import Record
from .values import (RED, GRN, BLU, YEL, CYN, MAG, LGR, DGR, WHT, 
                     BLD, ITL, UND, STR, RST,
                     INF, DEB, WRN, ERR, CRI)
from .utils import NoData
from .styles import (STYLE_0)


class Logger:
    INFO, DEBUG, WARNING, ERROR, CRITICAL = INF, DEB, WRN, ERR, CRI
    from .values import (RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA,
                         LIGHT_GRAY, DARK_GRAY, WHITE,
                         GRN, BLU, YLW, YEL, CYN, MAG, LGR, DGR, WHT,
                         BOLD, ITALIC, UNDERLINE, STRIKETHROUGH,
                         BLD, ITL, UND, STR, RST, ENDC)
    STYLE_DEFAULT = STYLE_0
    STYLE_0 = STYLE_0
    TIME_FORMAT_CLOCK = "%H:%M:%S"

    def __init__(self, 
                 name:str=None,
                 line_length:int=None,
                 time_format:str=None,
                 time_local:bool=False,
                 compact:bool=None,
                 colored:bool=True,
                 style:dict=STYLE_DEFAULT,
                 show_log_number:bool=None,
                 show_log_levels:bool=None,
                 hide_log_level:list=None,
                 show_time:bool=None,
                 show_logger_name:bool=None,
                 show_source_name:bool=None,
                 show_file_name:bool=None,
                 show_line_number:bool=None,
                 wrap_log_message:bool=None,
                 data_max_size:int=None,
                 max_logs_to_store:int=-1,
                 logger_uid:str=None,
                 filename:str=None,
                 prepend_logger_uid_to_filename:bool=False,
                 **kwargs
    ) -> None:
        """
        param: `time_local` (bool):
            - If True, time will be printed in local time.
            - If False, time will be printed in UTC.
            - Alternatively, you can pass a `time_format` string that starts
            with `"local-"` and the time will be printed in local time.

        param: `colored` (bool):
            - If True, logs will be printed with colors / bold / styles.
            - If False, logs will be printed without colors / bold / styles.
        
        param: `compact` (bool):
            - If True, metadata will be printed compactly.
            - If False, metadata will be printed with spaces between them.
            - If None, the default value from the `style` param will be used.

        param: `wrap_log_message` (bool):
            - If True, wraps the log message to the line length.
            - If False, the log message will be printed as is.
            - If None, the default value from the `style` param will be used.
        
        param: `max_logs_to_store` (int):
            - The maximum number of logs to store in memory.
            - If -1, all logs will be stored.
        
        param: `prepend_logger_uid_to_filename` (bool):
            - If True, the logger uid will be prepended to the filename if logs
            are written in files.
        
        param: `filename` (str):
            - If passed, logs will be written to the specified file.

        param: `style` (dict):
            ```python 
            style = {
                # metadata_display_flags
                "show_log_number": True,
                "show_log_levels": True,
                "hide_log_level": [INF],  # hide label ex: '[INFO]'
                "show_time": True,
                "show_logger_name": True,
                "show_source_name": True,
                "show_file_name": True,
                "show_line_number": True,
                
                # metadata_style
                "line_length": 120,
                "divider_length": 80,  # divider dashed lines
                "wrap_log_message": False,  # wrap if it's longer
                "wrap_prefix": f"{UND}{BLD}>{RST} ",  # if wrap True
                "colorless_wrap_prefix": "> ",  # if wrap True
                "compact_labels": False,  # compactly printed metadata
                "label_spacings": {  # if not compact
                    "log_number": 7,
                    "log_level": 11,
                }
                "time_format": "%Y-%b-%d %H:%M:%S",
                "level_colors": {INF: CYN, DEB: GRN, WRN: YEL, 
                                 ERR: RED, CRI: RED},
                
                # data_style
                "data_indent": 1,  # pformat indent
                "data_compact": True,  # pformat compact
                "data_sort_dicts": False,
                "data_width": "line_length",  # same as line length
                "data_underscore_numbers": True,  # 1_000_000
                "data_colorize": True,  # colorized data structures
                "data_color_schema": {
                    "string_schema": {'quotes': RED+ITL, 'string': DGR},
                    "struct_colors": [BLD+CYN, BLD+GRN, BLD+BLD, 
                                      BLD+MAG, BLD+BLU, BLD+RED],
                    "symbol_colors": {':': CYN, ',': CYN}
                }
                "data_max_size": DATA_MAX_SIZE,  # max bytes to print/keep
            }
            ```

            - If you want to override style params directly from the `__init__`,
            pass those params as arguments. 
            
            Ex: 
            ```python 
            logger = Logger("My Logger", 
                            data_colorize=False, 
                            data_width=80,
                            style=Logger.STYLE_7)
            ```
            - This will take builtin `STYLE_7` as default and override its
            `data_colorize` and `data_width` params with the given values.
        """
        self.init_time:float = time()
        self.logs:list[Record] = []
        self.logger_uid:str = logger_uid or utils.uid()
        self.log_count:int = 0

        style.update({**Logger.STYLE_DEFAULT, **style, **kwargs})  # override
        # if some lengths refer to other (specifically to "line_length")
        if type(style['divider_length']) == str:
            style['divider_length'] = style[style['divider_length']]
        if type(style['data_width']) == str:
            style['data_width'] = style[style['data_width']]
        self.style:dict = style
        self.colored:bool = colored
        self.display_flags = {
            key: (value if value is not None else style[key])
            for key, value in {
                "show_log_number": show_log_number,
                "show_log_levels": show_log_levels,
                "hide_log_level": hide_log_level,
                "show_time": show_time,
                "show_logger_name": show_logger_name,
                "show_source_name": show_source_name,
                "show_file_name": show_file_name,
                "show_line_number": show_line_number}.items()
        }

        self.name:str = name or values.DEF_LOGGER_NAME
        self.line_length:int = line_length or style["line_length"]
        self.divider_length:int = style["divider_length"]
        self.wrap_log_message:bool = (wrap_log_message 
                                      if wrap_log_message is not None 
                                      else style["wrap_log_message"])
        self.wrap_prefix:str = style["wrap_prefix"]
        self.colorless_wrap_prefix:str = style["colorless_wrap_prefix"]
        self.compact_labels:bool = (compact if compact is not None
                                    else style["compact_labels"])
        if time_format and time_format.startswith("local-"):
            time_format = time_format.replace("local-", "")
            time_local = True
        self.style['timezone'] = 'local' if time_local else 'utc'
        self.time_format:str = time_format or style["time_format"]
        self.time_local:bool = time_local
        self.level_colors:dict = style["level_colors"]
        
        self.data_indent:int = style["data_indent"]
        self.data_compact:bool = style["data_compact"]
        self.label_spacings:dict = style["label_spacings"]
        self.data_sort_dicts:bool = style["data_sort_dicts"]
        self.data_width:int = style["data_width"]
        self.data_underscore_numbers:bool = style["data_underscore_numbers"]
        self.data_colorize:bool = style["data_colorize"]
        self.data_color_schema:dict = style["data_color_schema"]
        self.data_max_size:int = data_max_size or style["data_max_size"]
        self.max_logs_to_store:int = max_logs_to_store
        self.filename:str = filename
        self.prepend_logger_uid_to_filename:bool = prepend_logger_uid_to_filename

        self._thread_lock:threading.Lock = ThreadLock()
    
    def log(self, 
            message:str="",
            data:Any=NoData, 
            level:str=INFO,
            exc:Exception=None,
            source_name:str=None,
            color:str=None,
            display:bool=True,
            caller_frame=None,
            divider:str=None,
            colorless:bool=False,
            show_metadata:bool=True,
            metadata_color_override:str=None,
            processing_lock:ProcessLockType=None,
            filename:str=None,
            ignore_logfile_headers:bool=False,
            **kwargs):
        """  
        param: `colorless` (bool):
            - If True, the log will be printed without colors / bold / styles.
        
        param: `show_metadata` (bool):
            - If False, metadata will not be printed (levels, time, filename...)
        """
        if 'div' in kwargs and not divider: divider = kwargs.pop('div')
        if 'c' in kwargs and not color: color = kwargs.pop('c')
        processing_lock = processing_lock or kwargs.get('lock')
        message = str(message)
        color = color or ""
        if data is not NoData:
            trim_resp = utils.trim_data(data, self.data_max_size)
            data = trim_resp["data"]
            if trim_resp['data_trimmed'] is True:
                message += (f'{RED+BLD}NOTE: {YEL}the data was too large '
                        f'to display so it was trimmed.{color or RST}')
        # generate record
        filename = filename or self.filename
        if filename and self.prepend_logger_uid_to_filename:
            # split with "/" or "\"
            filename = filename.replace("\\", "/")
            folders = filename.split("/")
            # prepend logger uid to filename and join everything
            filename = f"{"/".join(folders[:-1])}/{self.logger_uid}.{folders[-1]}"

        caller_frame = caller_frame or getframeinfo(stack()[1][0])
        record = Record(message=message,
                        data=data,
                        level=level,
                        exc=exc,
                        logger_name=self.name,
                        source_name=source_name,
                        color=color,
                        log_id=utils.uid(),
                        log_idx=self.log_count,
                        logger_uid=self.logger_uid,
                        caller_filename=caller_frame.filename,
                        caller_line=caller_frame.lineno,
                        divider=divider,
                        display=display,
                        colorless=colorless,
                        show_metadata=show_metadata,
                        metadata_color_override=metadata_color_override,
                        filename=filename,
                        **kwargs)
        with self._thread_lock:
            if processing_lock:
                processing_lock.acquire()
            self.log_count += 1
            self.logs.append(record)
            if self.max_logs_to_store > 0:
                while len(self.logs) > self.max_logs_to_store:
                    self.logs.pop(0)
            if display:
                record_str = self.format_record(record)
                print(record_str, end=kwargs.get('end') or "\n",
                      flush=kwargs.get('flush') or False)
            
            if filename and not kwargs.get('disable_file_writes'):
                # if it's the first log, write the header
                if self.log_count == 1 and not ignore_logfile_headers:
                    utils.write_to_file(self._header(), filename)
                utils.write_to_file(self.format_record(record, True), filename)

            if processing_lock:
                processing_lock.release()
    
    def info(self,
             message:str="",
             data:Any=NoData,
             exc:Exception=None,
             source_name:str=None,
             color:str=None,
             display:bool=True,
             divider:str=None,
             colorless:bool=False,
             show_metadata:bool=True,
             metadata_color_override:str=None,
             processing_lock:ProcessLockType=None,
             filename:str=None,
             ignore_logfile_headers:bool=False,
             **kwargs):
        """
        param: `display` (bool):
            - If False, the log will not be printed.

        param: `divider` (str):
            - If color string is passed, prints dashed lines with that color.

        param: `colorless` (bool):
            - If True, the log will be printed without colors / bold / styles.
        
        param: `show_metadata` (bool):
            - If False, metadata will not be printed (levels, time, filename...)

        param: `source_name` (str):
            - If passed, the source name will be printed. useful if custom
                package is using instance of your logger.
        
        param: `processing_lock` (multiprocessing.Lock):
            - If loggers will be used in multiple processes, you must pass
            a multiprocessing lock that will be shared by the logger instances.
            `from multiprocessing import Lock; lock = Lock()`
        
        param: `filename` (str):
            - If passed, logs will be written to the specified file.
        
        param: `ignore_logfile_headers` (bool):
            - If True, the header will not be written to the file.

        params passed as kwargs will be stored in the record.
        """
        if 'div' in kwargs and not divider: divider = kwargs.pop('div')
        if 'c' in kwargs and not color: color = kwargs.pop('c')     
        caller_frame = getframeinfo(stack()[1+kwargs.get("f_up", 0)][0])
        self.log(message=message,
                 data=data,
                 level=INF,
                 exc=exc,
                 source_name=source_name,
                 color=color,
                 display=display,
                 caller_frame=caller_frame,
                 divider=divider,
                 colorless=colorless,
                 show_metadata=show_metadata,
                 metadata_color_override=metadata_color_override,
                 processing_lock=processing_lock,
                 filename=filename,
                 ignore_logfile_headers=ignore_logfile_headers,
                 **kwargs)
    
    def __call__(self, *args, **kwargs):
        """ alias for `info` """
        self.info(*args, f_up=1, **kwargs)
    
    def debug(self,
              message:str="",
              data:Any=NoData,
              exc:Exception=None,
              source_name:str=None,
              color:str=None,
              display:bool=True,
              divider:str=None,
              colorless:bool=False,
              show_metadata:bool=True,
              metadata_color_override:str=None,
              processing_lock:ProcessLockType=None,
              filename:str=None,
              ignore_logfile_headers:bool=False,
              **kwargs):
        """
        param: `display` (bool):
            - If False, the log will not be printed.

        param: `divider` (str):
            - If color string is passed, prints dashed lines with that color.

        param: `colorless` (bool):
            - If True, the log will be printed without colors / bold / styles.
        
        param: `show_metadata` (bool):
            - If False, metadata will not be printed (levels, time, filename...)

        param: `source_name` (str):
            - If passed, the source name will be printed. useful if custom
                package is using instance of your logger.
        
        param: `processing_lock` (multiprocessing.Lock):
            - If loggers will be used in multiple processes, you must pass
            a multiprocessing lock that will be shared by the logger instances.
            `from multiprocessing import Lock; lock = Lock()`
        
        param: `filename` (str):
            - If passed, logs will be written to the specified file.

        param: `ignore_logfile_headers` (bool):
            - If True, the header will not be written to the file.

        params passed as kwargs will be stored in the record.
        """
        if 'div' in kwargs and not divider: divider = kwargs.pop('div')
        if 'c' in kwargs and not color: color = kwargs.pop('c')     
        caller_frame = getframeinfo(stack()[1+kwargs.get("f_up", 0)][0])
        self.log(message=message,
                 data=data,
                 level=DEB,
                 exc=exc,
                 source_name=source_name,
                 color=color,
                 display=display,
                 caller_frame=caller_frame,
                 divider=divider,
                 colorless=colorless,
                 show_metadata=show_metadata,
                 metadata_color_override=metadata_color_override,
                 processing_lock=processing_lock,
                 filename=filename,
                 ignore_logfile_headers=ignore_logfile_headers,
                 **kwargs)
        
    def warning(self,
                message:str="",
                data:Any=NoData,
                exc:Exception=None,
                source_name:str=None,
                color:str=None,
                display:bool=True,
                divider:str=None,
                colorless:bool=False,
                show_metadata:bool=True,
                metadata_color_override:str=None,
                processing_lock:ProcessLockType=None,
                filename:str=None,
                ignore_logfile_headers:bool=False,
                **kwargs):
        """
        param: `display` (bool):
            - If False, the log will not be printed.

        param: `divider` (str):
            - If color string is passed, prints dashed lines with that color.

        param: `colorless` (bool):
            - If True, the log will be printed without colors / bold / styles.
        
        param: `show_metadata` (bool):
            - If False, metadata will not be printed (levels, time, filename...)

        param: `source_name` (str):
            - If passed, the source name will be printed. useful if custom
                package is using instance of your logger.
        
        param: `processing_lock` (multiprocessing.Lock):
            - If loggers will be used in multiple processes, you must pass
            a multiprocessing lock that will be shared by the logger instances.
            `from multiprocessing import Lock; lock = Lock()`

        param: `filename` (str):
            - If passed, logs will be written to the specified file.

        param: `ignore_logfile_headers` (bool):
            - If True, the header will not be written to the file.

        params passed as kwargs will be stored in the record.
        """
        if 'div' in kwargs and not divider: divider = kwargs.pop('div')
        if 'c' in kwargs and not color: color = kwargs.pop('c')     
        caller_frame = getframeinfo(stack()[1+kwargs.get("f_up", 0)][0])
        self.log(message=message,
                 data=data,
                 level=WRN,
                 exc=exc,
                 source_name=source_name,
                 color=color,
                 display=display,
                 caller_frame=caller_frame,
                 divider=divider,
                 colorless=colorless,
                 show_metadata=show_metadata,
                 metadata_color_override=metadata_color_override,
                 processing_lock=processing_lock,
                 filename=filename,
                 ignore_logfile_headers=ignore_logfile_headers,
                 **kwargs)
    
    def warn(self, *args, **kwargs):
        """ alias for `warning` """
        self.warning(*args, f_up=1, **kwargs)
                
    def error(self,
              message:str="",
              data:Any=NoData,
              exc:Exception=None,
              source_name:str=None,
              color:str=None,
              display:bool=True,
              divider:str=None,
              colorless:bool=False,
              show_metadata:bool=True,
              metadata_color_override:str=None,
              processing_lock:ProcessLockType=None,
              filename:str=None,
              ignore_logfile_headers:bool=False,
              **kwargs):
        """
        param: `display` (bool):
            - If False, the log will not be printed.

        param: `divider` (str):
            - If color string is passed, prints dashed lines with that color.

        param: `colorless` (bool):
            - If True, the log will be printed without colors / bold / styles.
        
        param: `show_metadata` (bool):
            - If False, metadata will not be printed (levels, time, filename...)

        param: `source_name` (str):
            - If passed, the source name will be printed. useful if custom
                package is using instance of your logger.
        
        param: `processing_lock` (multiprocessing.Lock):
            - If loggers will be used in multiple processes, you must pass
            a multiprocessing lock that will be shared by the logger instances.
            `from multiprocessing import Lock; lock = Lock()`
        
        param: `filename` (str):
            - If passed, logs will be written to the specified file.

        param: `ignore_logfile_headers` (bool):
            - If True, the header will not be written to the file.

        params passed as kwargs will be stored in the record.
        """
        if 'div' in kwargs and not divider: divider = kwargs.pop('div')
        if 'c' in kwargs and not color: color = kwargs.pop('c')     
        caller_frame = getframeinfo(stack()[1+kwargs.get("f_up", 0)][0])
        self.log(message=message,
                 data=data,
                 level=ERR,
                 exc=exc,
                 source_name=source_name,
                 color=color,
                 display=display,
                 caller_frame=caller_frame,
                 divider=divider,
                 colorless=colorless,
                 show_metadata=show_metadata,
                 metadata_color_override=metadata_color_override,
                 processing_lock=processing_lock,
                 filename=filename,
                 ignore_logfile_headers=ignore_logfile_headers,
                 **kwargs)


    def critical(self,
                 message:str="",
                 data:Any=NoData,
                 exc:Exception=None,
                 source_name:str=None,
                 color:str=None,
                 display:bool=True,
                 divider:str=None,
                 colorless:bool=False,
                 show_metadata:bool=True,
                 metadata_color_override:str=None,
                 processing_lock:ProcessLockType=None,
                 filename:str=None,
                 ignore_logfile_headers:bool=False,
                 **kwargs):
        """
        param: `display` (bool):
            - If False, the log will not be printed.

        param: `divider` (str):
            - If color string is passed, prints dashed lines with that color.

        param: `colorless` (bool):
            - If True, the log will be printed without colors / bold / styles.
        
        param: `show_metadata` (bool):
            - If False, metadata will not be printed (levels, time, filename...)

        param: `source_name` (str):
            - If passed, the source name will be printed. useful if custom
                package is using instance of your logger.
            
        param: `processing_lock` (multiprocessing.Lock):
            - If loggers will be used in multiple processes, you must pass
            a multiprocessing lock that will be shared by the logger instances.
            `from multiprocessing import Lock; lock = Lock()`
        
        param: `filename` (str):
            - If passed, logs will be written to the specified file.

        param: `ignore_logfile_headers` (bool):
            - If True, the header will not be written to the file.

        params passed as kwargs will be stored in the record.
        """
        if 'div' in kwargs and not divider: divider = kwargs.pop('div')
        if 'c' in kwargs and not color: color = kwargs.pop('c')     
        caller_frame = getframeinfo(stack()[1+kwargs.get("f_up", 0)][0])
        self.log(message=message,
                 data=data,
                 level=CRI,
                 exc=exc,
                 source_name=source_name,
                 color=color,
                 display=display,
                 caller_frame=caller_frame,
                 divider=divider,
                 colorless=colorless,
                 show_metadata=show_metadata,
                 metadata_color_override=metadata_color_override,
                 processing_lock=processing_lock,
                 filename=filename,
                 ignore_logfile_headers=ignore_logfile_headers,
                 **kwargs)
    
    def crit(self, *args, **kwargs):
        """ alias for `critical` """
        self.critical(*args, f_up=1, **kwargs)
    
    def json(self, data:Any, pretty=False, color:str=None, msg:str=""):
        """ tries to convert data to json so you can copy paste """
        try:
            if pretty:
                self.info(msg+ "\n" + json.dumps(data, indent=4), 
                          metadata_color_override=BLD+BLU, color=color,
                          disable_file_writes=True, f_up=1)
            else:
                self.info(msg + "\n" + json.dumps(data), 
                          metadata_color_override=BLD+BLU, color=color,
                          disable_file_writes=True, f_up=1)
        except Exception as e:
            self.error(f"Couldn't convert data to json: {e}", data=data, exc=e,
                       f_up=1)


    def format_record(self, record:Record, force_colorless:bool=False):

        def _get_space(param_name):
            if self.compact_labels: return 0
            return self.label_spacings.get(param_name, 0)
        
        def _format_filename(filename:str):
            filename = filename.replace("\\", "/")
            return filename.split("/")[-1]
        
        def _colors_allowed():
            if force_colorless: return False
            return not record.colorless and self.colored

        def get_log_number():
            if not self.display_flags['show_log_number']: return ""
            return utils.fill(f"[{record.log_idx}] ", _get_space("log_number"))
        
        def get_log_level():
            if not self.display_flags['show_log_levels']: return ""
            if record.level in self.display_flags['hide_log_level']: return ""
            return utils.fill(f"[{record.level}] ", _get_space("log_level"))
        
        def get_time():
            if not self.display_flags['show_time']: return ""
            if self.time_local:
                return f"{utils.unix_to_local(record.time, self.time_format)} "
            return f"{utils.unix_to_utc(record.time, self.time_format)} "
        
        def get_extras():
            if all([not self.display_flags['show_logger_name'],
                    not self.display_flags['show_source_name'],
                    not self.display_flags['show_file_name'],
                    not self.display_flags['show_line_number']]):
                return ""
            extras = "("
            added = set()
            if self.display_flags['show_logger_name']:
                extras += f"{record.logger_name}"
                added.add(record.logger_name)
            elif self.display_flags['show_source_name'] and record.source_name:
                extras += f"{record.source_name}"
                added.add(record.source_name)
            if (self.display_flags['show_logger_name'] and
                self.display_flags['show_source_name']):
                if record.source_name:
                    extras += f"::{record.source_name}"
                    added.add(record.source_name)
            if self.display_flags['show_file_name']:
                if added: extras += " "
                extras += f"'{_format_filename(record.caller_filename)}'"
            if self.display_flags['show_line_number']:
                extras += f":{record.caller_line}"
            extras += ")"
            return extras
        
        def get_metadata_suffix(log_number, log_level, log_time, log_extras):
            if not any([log_number, log_level, log_time, log_extras]):
                return ""
            return " | "
        
        def get_message(metadata_length:int):
            if not self.wrap_log_message:
                return record.message
            wrap_prefix = (self.wrap_prefix if _colors_allowed() 
                           else self.colorless_wrap_prefix)
            message = ""
            words = record.message.split(" ")
            line_space_used = self.line_length - metadata_length
            for word in words:
                if line_space_used + len(word) > self.line_length:
                    message += "\n" + wrap_prefix
                    if _colors_allowed(): message += record.color
                    line_space_used = len(wrap_prefix)
                message += word + " "
                line_space_used += len(word) + 1
            if message.endswith(" "): message = message[:-1]
            return message
        
        def get_data():
            if record.data is NoData: return ""
            data_str = self.data_to_str(record.data)

            if _colors_allowed(): 
                data_colorized = self.colorize_data(
                    data_as_str=data_str,
                    record_color=record.color,
                    string_schema=self.data_color_schema['string_schema'],
                    struct_colors=self.data_color_schema['struct_colors'],
                    symbol_colors=self.data_color_schema['symbol_colors']
                )
                newlines = data_colorized.count("\n")
                if newlines > 0:
                    data_colorized = "\n" + data_colorized
                label_color = self.level_colors.get(record.level, record.color)
                data_str = (f"\n{UND}{label_color}DATA{RST}{label_color}: "
                            f"{data_colorized}")
            else: 
                newlines = data_str.count("\n")
                if newlines > 0:
                    data_str = "\n" + data_str
                data_str = f"\nDATA: {data_str}"
            return data_str
        
        def get_divider():
            if record.divider is None: return ""
            divider = "-" * self.divider_length
            if _colors_allowed():
                divider = f"{record.divider}{divider}{RST}"
            return f"{divider}\n"
        
        def get_traceback():
            if record.exc is None: return ""
            return record.traceback
        
        def combine(log_number, log_level, log_time, log_extras, log_suffix,
                    log_message, log_data, log_divider, s_log_traceback, 
                    metadata_length):
            if not _colors_allowed():
                return (f"{log_divider}{log_number}{log_level}{log_time}"
                        f"{log_extras}{log_suffix}{log_message}{log_data}"
                        f"{s_log_traceback}")
            
            color = record.color
            metadata_color = self.level_colors.get(record.level, color)
            if record.metadata_color_override:
                metadata_color = record.metadata_color_override

            if metadata_length == 0:
                return f"{log_divider}{color}{log_message}{log_data}{RST}"
            
            return (f"{log_divider}{metadata_color}"
                    f"{log_number}{log_level}{log_time}{log_extras}{log_suffix}"
                    f"{RST}{color}{log_message}{log_data}"
                    f"{RED}{s_log_traceback}{RST}")

        s_log_number = get_log_number()
        s_log_level = get_log_level()
        s_log_time = get_time()
        s_log_extras = get_extras()
        s_log_suffix = get_metadata_suffix(s_log_number, s_log_level,
                                           s_log_time, s_log_extras)
        if not record.show_metadata:
            (s_log_number, s_log_level, s_log_time, 
             s_log_extras, s_log_suffix) = "", "", "", "", ""
        metadata_length = (len(s_log_number) + len(s_log_level) +
                           len(s_log_time) + len(s_log_extras) +
                           len(s_log_suffix))
        s_log_message = get_message(metadata_length=metadata_length)
        s_log_data = get_data()
        s_log_divider = get_divider()
        s_log_traceback = get_traceback()

        to_print = combine(
            s_log_number, s_log_level, s_log_time, s_log_extras, s_log_suffix,
            s_log_message, s_log_data, s_log_divider, s_log_traceback,
            metadata_length)
        return to_print

    def print_current_style(self):
        try: print(pformat(self.style, sort_dicts=False))
        except: print(self.style)

    def data_to_str(self, data:Any):
        if type(data) == str:
            return data
        if type(data) not in (int, float, bool, 
                              str, list, dict, set, tuple, type(None),
                              NoData):
            return str(data)
        try: data_str = pformat(
            data, indent=self.data_indent, width=self.data_width, 
            compact=self.data_compact, sort_dicts=self.data_sort_dicts,
            underscore_numbers=self.data_underscore_numbers)
        except:
            try: data_str = pformat(data)
            except: data_str = str(data_str)
        return data_str

    def colorize_data(self,
                      data_as_str:str, 
                      record_color=YEL,
                      string_schema={'quotes': RED+ITL, 'string': DGR},
                      struct_colors=[BLD+CYN, BLD+GRN, BLD+YEL, 
                                     BLD+MAG, BLD+BLU, BLD+RED],
                      symbol_colors={':': CYN, ',': CYN}
    ):
        struct_colors = struct_colors or [""]
        N = len(struct_colors)
        struct_starters = '{[('; struct_enders = '}])'
        string_started:str = None  # has ' or " depending on what started str
        if not record_color.startswith(RST): record_color = RST + record_color
        result = [record_color]
        depth = 0
        for c in data_as_str:
            # check for internal strings
            if not string_started and c in ["'", '"']:
                string_started = c
                result.append(string_schema['quotes'] + c + 
                              string_schema['string'])
            elif c == string_started:
                string_started = None
                result.append(string_schema['quotes'] + c + record_color)
            elif string_started:
                result.append(c)
            # check for structs (list, dict/set, tuple)
            elif c in struct_starters:
                result.append(struct_colors[depth % N] + c + record_color)
                depth += 1
            elif c in struct_enders:
                depth -= 1
                result.append(struct_colors[depth % N] + c + record_color)
            elif c in symbol_colors:
                result.append(symbol_colors[c] + c + record_color)
            else:
                result.append(c)
        return ''.join(result)

    def _header(self):
        """ returns string header for log file """
        return (f"{'-'*80}\n"
                f"{' '*((80-len(self.name) - 6)//2)}dLog: {self.name}\n"
                f'Logger UID: "{self.logger_uid}". '
                f"Created at: {int(self.init_time)}.\n"
                f"{self.style}\n"
                f"{'-'*80}\n")
