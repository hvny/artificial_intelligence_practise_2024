import re

pattern = r'\s(\d+(\.\d+)?)\s'

testDataArr = [
    "some text 5678.23 some text",
    "some text 0 some text",
    "some text 0.15 some text",
    "some text123some text",
    "text 123,4 text",
    "text -123.4 text"
]

def validateString(str, regExp):
    matches = re.findall(regExp, str)
    if (matches):
        return f"строка '{str}' содержит положительные числа:  {', '.join([match[0] for match in matches])}"
    else:
        return f"строка '{str}' не содержит положительных чисел"
    
for i in testDataArr:
    print("\n", validateString(i, pattern))