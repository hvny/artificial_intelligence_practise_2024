import re

pattern = r'\s\d{2}\.\d{2}\.\d{4}\s'

testDataArr = [
    " 12.03.2016 ",
    " 40.02.1232 ",
    " 02.05.1928 ",
    " 12/03/2016 ",
    " 12-03-2016 ",
    " 2016.03.12 ",
    " 2016 03 12 ",
    " 5.3.2016 "
]

def validateDate(date, regExp):
    if (re.search(regExp, date)):
        return f"дата {date} прошла валидацию"
    else:
        return f"дата {date} не прошла валидацию"


for i in testDataArr:
    print(validateDate(i, pattern))