import os,sys,time,struct,glob, shutil, re, copy

"""
    判断一个给定的字符串是否是合法的宏定义名字
"""
def is_valid_macro_identifier(identifier):
    import re
    pattern = r'^[a-zA-Z_]\w*$'
    match = re.match(pattern, identifier)
    return match is not None