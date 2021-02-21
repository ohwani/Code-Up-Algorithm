import re

# def cleanText(readData):
#     # 텍스트에 포함되어 있는 특수 문자 제거
#     text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', readData)
#
#     return print(text)
#
# cleanText('...!@BaT#*..y.abcdefghijklm')


import re

def solution(newid):
    text = re.sub('[-_~!@#$%^&*()=+{}:?,<>/]', '', newid)
    text = text.lower()
    if text[0] == '.':
        print("아")
    return print(text)

solution('...!@BaT#*..y.abcdefghijklm')