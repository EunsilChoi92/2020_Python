'''
[모듈과 패키지]
    모듈(module)
        -변수,함수,클래스 등을 모아놓은 소스파일
        -간단한 기능을 담을 때 사용
        -파이썬에서는 파일 하나하나가 모듈
        -다른 파이썬 프로그램에서 블러와 사용할 수 있도록
        만들어진 소스파일
    패키지(pakage)
        -여러모들을 묶은 것
        -코드가 많고 복잡할 때 사용
        -관련 모듈(소스파일)끼리 한 폴더에 넣어놓은 형태(폴더=패키지)
        -폴더 안에 __init__.py 파일이 있어야 패키지 됐었다
        -파이썬 3.3버전 부터는 생략 가능
        (하의버전 호환을 위해 가급적 만들어 두는게 좋다.)
'''
#모듈불러오기 (1) - 모듈명 그대로 사용하기
import koreaIt_module

print(koreaIt_module.my_str)
print(koreaIt_module.add(1,2))

import random
print(random.randint(1,7))

#모듈불러오기 (2) - as 별칭 주기
import koreaIt_module as km
print(km.my_str)


#모듈불러오기 (3) - 모듈에서 일부만 사용
from koreaIt_module import my_str,add

print(my_str)
print(add(1,2))
#print(mul(3,4))

#모듈불러오기 (4) - 모듈에서 전체 사용
from koreaIt_module import *

print(my_str)
print(add(1,2))
print(mul(3,4))

#(3),(4) 방식은 좋지 않다.
#왜? 모듈을 여러개 import 하다보면 모듈끼리 중복발생 가능
#2번 추천


import sys
print(sys.path)

#help("modules")


#미리 정의된 함수 집합 - 라이브러리
import math

num = math.sqrt(5)

print(num)

num = math.factorial(5)
print(num)




































