from time import time
from typing import Any
from . import utils


class Record:
    def __init__(self,
                 message:str,
                 data:Any,
                 level:str,
                 exc:Exception,
                 logger_name:str,
                 source_name:str,
                 color:str,
                 log_id:str,
                 log_idx:int,
                 logger_uid:str,
                 caller_filename:str,
                 caller_line:str,
                 divider:str,
                 display:bool,
                 colorless:bool,
                 show_metadata:bool,
                 metadata_color_override:bool,
                 filename:str,
                 **kwargs
    ):
        self.time:float = time()
        self.message:str = str(message)
        self.data:Any = data
        self.level:str = level
        self.exc:Exception = exc
        self.traceback:str = utils.get_exception_traceback(exc) if exc else None
        self.logger_name:str = logger_name
        self.source_name:str = source_name
        self.color:str = color
        self.log_id:str = log_id
        self.log_idx:int = log_idx
        self.logger_uid:str = logger_uid
        self.caller_filename:str = caller_filename
        self.caller_line:str = caller_line
        self.divider:str = divider
        self.display:bool = display
        self.colorless:bool = colorless
        self.show_metadata:bool = show_metadata
        self.metadata_color_override:bool = metadata_color_override
        self.filename = filename
        self.kwargs:dict = kwargs
    
    def to_dict(self):
        return {
            "time": self.time,
            "message": self.message,
            "data": self.data,
            "level": self.level,
            "exc": self.exc,
            "traceback": self.traceback,
            "logger_name": self.logger_name,
            "source_name": self.source_name,
            "color": self.color,
            "log_id": self.log_id,
            "log_idx": self.log_idx,
            "logger_uid": self.logger_uid,
            "caller_filename": self.caller_filename,
            "caller_line": self.caller_line,
            "divider": self.divider,
            "display": self.display,
            "colorless": self.colorless,
            "show_metadata": self.show_metadata,
            "metadata_color_override": self.metadata_color_override,
            "filename": self.filename,
            "kwargs": self.kwargs,
        }

    def __str__(self) -> str:
        return f"{self.message}"
