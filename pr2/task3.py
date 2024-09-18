import re

pattern = r'^(\d{1,3}\.){3}\d{1,3}$'

testDataArr = [
    "192.168.0.1",
    "127.0.0.1",
    "0.0.0.0",
    "0.100.200.300",
    "192.168.0",
    "a.b.c.d",
    "",
    "abc.def.ghi.jkl",
    "1234.2345.3456.4567"
]

def validateIp(ip, regExp):
    if (re.match(regExp, ip)):
        return f"адрес {ip} прошёл валидацию"
    else:
        return f"адрес {ip} не прошёл валидацию"
        

for i in testDataArr:
    print("\n", validateIp(i, pattern))
