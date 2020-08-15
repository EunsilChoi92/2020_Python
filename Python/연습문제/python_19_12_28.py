# 문자열 포매팅(formatting)
'''
%s : 문자열(string)
%c : 문자 1개(character)
%d : 정수(integer)
%f : 실수(부동소수(floating-point)
%o : 8진수
%x : 16진수
%% : 문자 '%'


ex)
print('I eat %d apples.' % 3)
print('I eat %s apples.' % 'five')

number = 6
print('I eat %d apples.' % number)

print('Error is %d%%.' % 99)

print('%10s' % 'Hi')  # 전체 길이 10에서 오른쪽으로 정렬하고 앞의 나머지는 공백으로 표현
print('%0.3f' % 3.14159) # 실수, 소수 셋째자리까지 출력되도록 반올림


'''

# format 함수를 사용한 포매팅
'''
중괄호 포함한 문자열 뒤에 마침표 찍고 format() 함수 사용하되,
중괄호 개수와 format 함수 안 매개변수의 개수는 반드시 같아야 함.
문자열의 중괄호 기호가 format 함수 괄호 안의 매개변수로 차례로 대치되면서 숫자가 문자열이 됨.

<형식>
'문자열 {}'.format(변수 또는 상수)


ex)
print('I eat {} apples.'.format(2))

num1 = 4
num2 = 2

print('I eat {0} apples. You eat {1} apples.'.format(num1, num2))
print('I eat {1} apples. You eat {0} apples.'.format(num1, num2))
print('I eat {num1} apples. You eat {num2} apples.'.format(num1=6, num2=3))
print('I eat {0} apples. You eat {num} apples.'.format(7, num=8))

print('{0:<10}'.format('Hi')) # 왼쪽 정렬
print('{0:>10}'.format('Hi')) # 오른쪽 정렬
print('{0:^10}'.format('Hi')) # 가운데 정렬
print('{0:=^30}'.format('Python'))

n = 3.14159
print('{:0.3f}'.format(n)) # 소수 셋째자리까지 반올림

print('{{ python }}'.format()) # 중괄호 {} 표현

a = 30.0
print('{:g}'.format(a)) # 의미없는 소수점 제거


ex)
a = '{}만원'.format(5000)
b = '파이썬 열공하여 첫 연봉 {}만원 만들기'.format(5000)
c = '{} {} {}'.format(3000, 4000, 5000)
d = '{} {} {}'.format(1, '파이썬', True)

print(a)
print(b)
print(c)
print(d)

'''

# f 문자열 포매팅(파이썬 3.6버전 이상)
'''
<형식>
f'문자열 {변수명} 문자열'


ex)
name = '홍길동'
age = 20

print(f'나의 이름은 {name}입니다. 나이는 {age}입니다.')
print(f'나는 내년이면 {age+1}살이 됩니다.')

print(f'{"Hi":=^30}')
print(f'{"Hi":!<20}')

n = 3.14159
print(f'{n:0.3f}')
print(f'{{ python }}')


'''

# 포매팅 비교하기
'''
n = 3
print('I eat', n, 'apples.')
print('I eat %d apples.' % n)
print('I eat {} apples.'.format(n))
print(f'I eat {n} apples.')

'''

# 값을 입력받아 연산자를 이용하여 동전교환 프로그램 만들기
'''
money, a500, a100, a50, a10 = 0, 0, 0, 0, 0

money = int(input('교환할 돈은 얼마입니까?? '))

a500 = money // 500
money = money % 500  # money %= 500

a100 = money // 100
money = money % 100 # money %= 100

a50 = money // 50
money = money % 50 # money %= 50

a10 = money // 10
money = money % 10 # money %= 10

print('500원짜리 --> %d개' % a500)   # 기본포매팅
print('100원짜리 --> %d개' % a100)
print('50원짜리 --> %d개' % a50)
print('10원짜리 --> %d개' % a10)
print('바꾸지 못한 잔돈 --> %d원' % money)
print()
print('500원짜리 --> {}개'.format(a500)) # format 함수 포매팅
print('100원짜리 --> {}개'.format(a100))
print('50원짜리 --> {}개'.format(a50))
print('10원짜리 --> {}개'.format(a10))
print('바꾸지 못한 잔돈 --> {}원'.format(money))
print()
print(f'500원짜리 --> {a500}개') # f 문자열 포매팅
print(f'100원짜리 --> {a100}개')
print(f'50원짜리 --> {a50}개')
print(f'10원짜리 --> {a10}개')
print(f'바꾸지 못한 잔돈 --> {money}원')

'''

# 조건문 (if)
'''
제시한 명제(조건)가 참인지 거짓인지 판단하고 판단에 따른 명령을 내리는 것

<형식>
if 조건문:
    실행할 문장


ex)
a = 99
if a < 100:
    print('100보다 작군요!')


ex) 값을 입력받아 양수인지 음수인지 판별
num = int(input('정수를 입력하세요 : '))
if num > 0:
    print('양수입니다!')
if num < 0:
    print('음수입니다!')
if num == 0:
    print('0입니다!!')


'''

# 조건문 (if ~ else)
'''
else구문 : if 조건문 뒤에 사용하며, if 조건문의 조건이 거짓일 때 실행되는 부분

<형식>
if 조건문:
    실행할 문장1
else:
    실행할 문장2
    

ex)
a = 200
if a < 100:
    print('100보다 작군요!') # 참
else:
    print('100보다 크거나 같군요!!') # 거짓
    

ex)
num = int(input('정수를 입력하세요 : '))
if num % 2 == 0:
    print('짝수입니다')
else:
    print('홀수입니다')

ex)
num = int(input('정수를 입력하세요 : '))
if num % 2 == 0:
    print('짝수입니다')
if num % 2 == 1:
    print('홀수입니다')


ex) 값을 입력받아 in연산자를 활용해서 짝수, 홀수 판별하기
num = input('정수를 입력하세요 : ')  # 문자형식으로 입력받을 것이기 때문에 int를 붙이지 않음
a = num[-1] # 맨 끝 글자(숫자)를 a변수에 담는다

if a in '02468':  # 만약 맨 끝 글자가 02468안에 있는 글자라면
    print('짝수입니다~')  # 참인 경우 짝수가 된다
else:
    print('홀수입니다~')  # 거짓인 경우 홀수가 된다

'''

# 조건문 (if ~ elif ~ else) 다중조건
'''
elif 구문 : 세 개 이상의 조건을 연결해서 사용(다중 조건 판단 가능)
            if 조건문과 else 구문 사이에 입력, 개수 제한이 없다

<형식>
if 조건문1:
    실행할 문장1
elif 조건문2:
    실행할 문장2
else:
    실행할 문장3
    

ex)
score = int(input('점수를 입력하세요 : '))
if score >= 90:
    print('A학점입니다~!')
elif score >= 80:
    print('B학점입니다!')
elif score >= 70:
    print('C학점입니다!')
elif score >= 60:
    print('D학점입니다~!')
else:
    print('F학점입니다!')

ex)
num = int(input('정수를 입력하세요 : '))
if num > 0:
    print('양수입니다!')
elif num < 0:
    print('음수입니다!')
else:
    print('0입니다!!')

'''

# pass 구문
'''
나중에 구현하고자 할 때 아무것도 작성하지 않고 비워둘 경우 쓴다

ex)
score = 59
if score >= 60:
    print('합격!!')
else:
    pass

'''

# 모듈
'''
각종 변수, 함수, 클래스 등을 모아 놓은 파일
다른 파이썬 프로그램에서 불러와 사용할 수 있게끔 만든 파이썬 파일
다른 사람들이 이미 만들어놓은 모듈을 사용할 수도 있고,
우리가 직접 만들어서도 사용 가능
모듈을 여러개 가져올 때는 모듈을 콤마로 구분
.py 파일 단위로 저장

<형식>
import 모듈이름
import 모듈이름 as 별명(이름)

모듈.변수
모듈.함수()
모듈.클래스()


ex) 모듈과 조건문을 이용한 계절구하기
import datetime # 날짜, 시간과 관련된 기능(모듈)을 가져온다

now = datetime.datetime.now() # 현재 날짜와 시간을 가져온다(pc)
m = now.month  # 추출한 현재 날짜 시간변수에 있는 월을 따로 m변수에 저장

if 3 <= m <= 5:     # 만약 월이 3,4,5월이라면
    print('봄!')
elif 6 <= m <= 8:   # 만약 월이 6,7,8월이라면
    print('여름!!')
elif 9 <= m <= 11:  # 만약 월이 9,10,11월이라면
    print('가을!!!')
else:               # 만약 월이 12,1,2월이라면
    print('겨울!!!!')


ex) 무작위로 덧셈 문제를 만들어서 맞추기
import random  # 랜덤 기능을 가진 모듈을 불러온다

a = random.randint(1, 10)  # a 변수에 1~10까지의 수 중 임의의 수를 저장
b = random.randint(1, 10)  # b 변수에 1~10까지의 수 중 임의의 수를 저장

print('{} + {} = ??'.format(a, b)) 

c = int(input('정답은 무엇입니까?? '))  # 정답이 될 수를 입력 받는다

if a + b == c:    # 컴퓨터가 a, b변수를 더한 것과 사용자가 입력한 정답을 비교
    print('정답입니다!')
else:
    print('틀렸습니다~~')


# 패키지 : 특정 기능과 관련된 여러 모듈을 묶은 것(비슷한 의미로 라이브러리, 프레임워크)
# 파이썬 표준 라이브러리 : 파이썬에 기본으로 설치된 모듈과 패키지. 내장 함수를 묶은 것도 포함


'''































































