import re

# def cleanText(readData):
#     # 텍스트에 포함되어 있는 특수 문자 제거
#     text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', readData)
#
#     return print(text)
#
# cleanText('...!@BaT#*..y.abcdefghijklm')


import re

def solution(new_id):

    # 1. 특수문자 제거
    text = re.sub(r'[~!@#$%^&*()=+\[{}\]:?,<>/]', '', new_id)
    # 2. 대문자 -> 소문자로 변경
    text = text.lower()
    # 3. .. ... -> . 으로 변경
    text = re.sub(r'\.+','.',text)
    # 4. 맨앞 맨뒤 . 제거
    text = re.sub(r'^\.|\.$','',text)
    # 5. 맨뒤에 . 있을시 제거, 문자 길이는 15자 로 표현
    text = re.sub(r'\.$', '', text[0:15])
    # 6. 아이디가 정보가 아무것도 없을때 'a'로 저장
    if text == '':
        text = 'a'
    # 7. 아이디의 길이가 3자 이하일경우 맨뒤글자 반복에서 3자 이상으로 만들어준다.
    while len(text) < 3:
        text += text[-1]

    return print(text)

solution('[z]-+.^.')