# 함수

'''
[문제] 사칙 연산 함수 만들기

숫자 두개로 덧셈, 뺄셈, 곱셈, 나눗셈의 결과가 나오도록 하시오.
(단, 각각의 연산은 함수를 이용해서 만들것)

예) 덧셈코드

def add(x, y):
    덧셈 계산 코드 넣기

나머지 계산코드도 이런식으로 만들기


[출력결과] (매개변수 x를 10으로, 매개변수 y를 20으로 한 결과)
30
-10
200
0.5


[정답1]
def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

a = add(10, 20)
b = sub(10, 20)
c = mul(10, 20)
d = div(10, 20)

print(a, b, c, d, sep='\n')


[정답2]
def add(x, y):
    print(x + y)

def sub(x, y):
    print(x - y)

def mul(x, y):
    print(x * y)

def div(x, y):
    print(x / y)

x = 10
y = 20

add(x, y)
sub(x, y)
mul(x, y)
div(x, y)


[정답3]
def add(x, y):
    print(x + y)

def sub(x, y):
    print(x - y)

def mul(x, y):
    print(x * y)

def div(x, y):
    print(x / y)

add(10, 20)
sub(10, 20)
mul(10, 20)
div(10, 20)

'''



'''
[문제]

회원등급에 따른 할인율 계산하여 출력하기
매개변수가 2개인(회원등급, 가격)
하나의 함수로 만들어보기

'S' --> 할인율 5%
'G' --> 할인율 10%
'V' --> 할인율 15%


[출력결과]
회원 등급을 입력하세요 : V
가격을 입력하세요 : 20000
3000 원입니다.


[정답]
grade = input('회원 등급을 입력하세요 : ')
price = int(input('가격을 입력하세요 : '))

def solution(grade, price):
    answer = 0
    if grade == 'S':
        answer = int(price * 0.05)
    elif grade == 'G':
        answer = int(price * 0.1)
    elif grade == 'V':
        answer = int(price * 0.15)
    else:
        print('할인율이 없습니다')
    return answer

print(solution(grade, price),'원입니다.')

'''
