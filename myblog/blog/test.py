# coding=utf-8
import re
a = '12345623'
# b = '[a-zA-z]\\w{0,9}'
value = re.compile(r'^[a-zA-Z\d]{6,16}$')
s = value.match(a)
print s
