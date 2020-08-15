#모듈 코드 작성

#변수
my_str = "koreaIt_module 문자열"
#함수
def add(a,b):
    return a+b
def mul(a,b):
    return a*b

#클래스
class Dog:
    def __init__(self,name):
        self.name = name
    def cry(self):
        print("{}:멍멍!".format(self.name))
