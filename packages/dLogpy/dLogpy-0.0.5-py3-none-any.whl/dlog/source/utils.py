import traceback
from datetime import datetime
from random import choices
from string import ascii_letters, digits
from time import time
from . import values


class NoData: pass

def unix_to_utc(unix_time=None, format:str=None):
    """ if unix_time is not passed, returns current UTC datetime.
        if format string passed, formats and returns string """
    if unix_time == None:
        unix_time = time()
    if not format:
        return datetime.utcfromtimestamp(unix_time)
    return datetime.utcfromtimestamp(unix_time).strftime(format)

def unix_to_local(unix_time=None, format:str=None):
    """ if unix_time is not passed, returns current local datetime.
        if format string passed, formats and returns string """
    if unix_time == None:
        unix_time = time()
    if not format:
        return datetime.fromtimestamp(unix_time)
    return datetime.fromtimestamp(unix_time).strftime(format)

def get_exception_traceback(exc:Exception) -> str:
    """ returns printable exception data with traceback """
    tb_list = traceback.extract_tb(exc.__traceback__)
    exc_data = f" EXCEPTION: {exc}\n"
    exc_data += " TRACEBACK:\n *\t" + " *\t".join(
        traceback.StackSummary.from_list(tb_list).format())
    exc_data = f"\n{exc_data}"
    return exc_data

def uid(length=8) -> str:
    """ returns a random string of specified length """
    return "".join(choices(ascii_letters + digits, k=length))

def trim_data(data:str|list|dict|set|tuple, size_limit=values.DATA_MAX_SIZE):
    """ `logger_instance` - if passed, logs info that the data was oversized
        returns: `{"data": <new_data>, "data_trimmed": T/F}`
                 or 'None' if data is NoData or None
    """
    if data is NoData: data = None
    data_types = (str, list, dict, set, tuple)
    data_too_large = False
    if data is None or type(data) not in data_types:
        if len(str(data)) > size_limit:
            data = str(data)
    if type(data) == str:
        data_new = data[:size_limit]
        if len(data_new) != len(data): data_too_large = True
        data = data_new
    elif type(data) == dict:
        data_new = {}
        for k, v in data.items():
            if len(str(data_new)) + len(str(k)) + len(str(v)) < size_limit:
                data_new[k] = v
            else: 
                data_too_large = True
                break
        data = data_new
    elif type(data) in (list, set, tuple):
        data_new = []
        for v in data:
            if len(str(data_new)) + len(str(v)) < size_limit:
                data_new.append(v)
            else: 
                data_too_large = True
                break
        data = data_new
    return {"data": data, "data_trimmed": data_too_large}

def fill(string:str, length:int, fill_chars:str=" ") -> str:
    """ returns string filled with `fill_chars` to specified `length` """
    if len(string) >= length: return string
    return string + fill_chars * ((length - len(string)) // len(fill_chars))

def write_to_file(record:str, filename:str):
    with open(filename, "a") as f:
        f.write(record + "\n")

