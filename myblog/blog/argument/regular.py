# coding=utf-8
import re

re_email = r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net,org]{1,3}$'  #注册时验证邮箱格式
re_passwd = r'^[a-zA-Z\d]{6,16}$'  #注册时验证密码,包含字母加数字6-16位


def regul(regul_data, data):
    value = re.compile(regul_data)
    result = value.match(data)
    return result

