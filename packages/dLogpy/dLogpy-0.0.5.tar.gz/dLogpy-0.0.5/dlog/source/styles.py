from .values import *

STYLE_0 = {
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
    "divider_length": "line_length",  # 80. divider dashed lines
    "wrap_log_message": False,  # wrap if it's longer
    "wrap_prefix": f"{UND}{BLD}>{RST} ",  # if wrap True
    "colorless_wrap_prefix": "> ",  # if wrap True
    "compact_labels": True,  # compactly printed metadata
    "label_spacings": {  # if not compact
        "log_number": 7,
        "log_level": 11,
    },
    "time_format": "%Y-%b-%d %H:%M:%S",
    "level_colors": {INF: CYN, DEB: GRN+BLD, WRN: YEL+ITL, 
                     ERR: RED, CRI: RED+BLD},
    
    # data_style
    "data_indent": 1,  # pformat indent
    "data_compact": True,  # pformat compact
    "data_sort_dicts": False,
    "data_width": "line_length",  # same as line length
    "data_underscore_numbers": True,  # 1_000_000
    "data_colorize": True,  # colorized data structures
    "data_color_schema": {
        "string_schema": {'quotes': RED+ITL, 'string': DGR},
        "struct_colors": [BLD+CYN, BLD+GRN, BLD+YEL,
                          BLD+MAG, BLD+BLU, BLD+RED],
        "symbol_colors": {':': CYN, ',': CYN}
    },
    "data_max_size": DATA_MAX_SIZE,  # to not print too large data (bytes)
}
