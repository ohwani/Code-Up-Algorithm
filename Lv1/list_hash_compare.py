import time
import random

'''
Dictionary 와 List에서 탐색 성능 비교
random 모듈을 이용해서 임의의 키값 섞기 
'''

def create_data(n):
    keys = [i for i in range(n)]
    random.shuffle(keys)
    values = [random.randrange(0,100) for i in range(n)]
    data = [[keys[i],values[i]] for i in range(n)]
    return data

def create_dict(n1):
    dict = {}
    KEY = 0
    VALUE = 1
    for i in n1:
        dict[i[]]
