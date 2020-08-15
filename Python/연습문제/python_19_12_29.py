# 반복문 (while)
'''
조건문을 확인하여 '참'인 동안 계속 반복하여 수행

<형식>
변수 = 시작값
while 변수값 < 끝값:
    이 부분을 반복
    변수 = 변수 + 증가값


ex) 100번 출력
i = 0                      # 시작값(초기식)
while i < 100:             # while 조건식
    print('Hello, world!') # 참일 경우 반복할 코드
    i = i + 1              # 변화식. 변수 i가 1씩 증가. i += 1


ex) 무한 반복
while True:             # True 대신에 숫자1을 적어도 된다
    print('ㅋ', end='') # 실행시 ctrl + c를 누르면 종료(idle 해당)

'''

# break 구문
'''
반복문에서 제어 흐름을 중단하고 빠져나온다 (반복문을 끝냄)


ex) 무한 반복을 하다가 변수 i가 100이 되면 반복문을 종료(0부터 99까지 출력)
i = 0
while True:           # 무한 루프
    print(i, end=' ')
    i += 1            # i = i + 1. i를 1씩 증가
    if i == 100:      # i가 100이 되면
        break         # 반복문을 종료(제어흐름을 빠져나온다)

'''

# continue 구문
'''
while문 수행시 조건에 맞지 않으면 while문을 빠져나오고 반복을 종료하는데
이 때 while문을 빠져나가지 않고, while문 맨 처음 조건문으로 다시 돌아가고 싶은 경우 사용
break와 다르게 제어 흐름을 유지. 코드 실행만 건너뜀


ex) 1부터 10까지의 숫자 중에서 홀수만 출력
a = 0
while a < 10:
    a += 1        # a = a + 1
    if a % 2 == 0: # a를 2로 나누었을 때 나머지가 0이면 while문 맨 처음(조건문)으로 돌아간다
        continue
    print(a)

'''

# while 문을 이용한 커피자판기 프로그램
'''
coffee = 10 # 커피의 개수
while True: # 무한 반복
    money = int(input('돈을 넣어주세요 : '))
    if money == 300:            # 커피값이 300원이라고 가정했을 경우
        print('커피를 줍니다!')
        coffee = coffee - 1     # 커피를 줬으니 커피 개수를 하나 줄여준다. coffee -= 1
        print('남은 커피의 양은 {}개 입니다.'.format(coffee))
    elif money > 300:           # 돈을 300원보다 더 많이 넣었을 경우
        print('거스름돈 {}원을 주고 커피를 줍니다.'.format(money - 300))
        coffee = coffee - 1
        print('남은 커피의 양은 {}개 입니다.'.format(coffee))
    else:
        print('돈을 다시 돌려주고 커피를 주지 않습니다.!!')
        print('남은 커피의 양은 {}개 입니다.'.format(coffee))

    if coffee == 0:   # 커피의 개수가 0이면 더이상 커피를 팔 수 없으므로 중단
        print('커피가 다 떨어졌습니다. 판매를 중지합니다.')
        break  # 반복문을 빠져나온다

'''


# 반복문 (for)
'''
반복 횟수가 정해져 있을 때 사용

<형식>
for 변수 in range(횟수):
    반복할 코드

for 변수 in range(시작값, 끝값):
    반복할 코드

for 변수 in range(시작값, 끝값, 증가폭):
    반복할 코드

for _ in range(횟수):  # 반복할 변수 생략
    반복할 코드

ex)
for i in range(10):  # 10번 반복. 초기 i는 0
    print(f'{i}번째 문장입니다!') # f 문자열 포매팅(파이썬 3.6버전이상)
print()

for i in range(1, 11):  # 1부터 10(11-1)까지 반복. 10번
    print(f'{i}번째 문장입니다!')
print()

for i in range(1, 10, 2): # 1부터 9까지 홀수만 반복. 초기값=1, 끝값=9(10-1), 증가값=2
    print(f'{i}번째 문장입니다!')
print()

for i in range(10, 0, -1): # 10부터 1까지 1씩 감소
    print(f'{i}번째 문장입니다!')
print()

for i in reversed(range(10)):  # reversed : 반전(반대)
    print(f'{i}번째 문장입니다!')



ex) 입력한 횟수대로 반복하기
count = int(input('반복할 횟수를 입력하세요 : '))
for i in range(count):
    print(f'{i}번째 문장입니다!')


ex) 1부터 100까지의 수 중 3 또는 5의 배수 출력하기
for i in range(1, 101):
    if i % 3 == 0:
        print(f'{i} : 3의 배수')
    elif i % 5 == 0:
        print(f'{i} : 5의 배수')
    else:
        print(i)

ex) 1부터 100까지의 수 중 3과 5의 공배수와 3 또는 5의 배수 출력하기
for i in range(1, 101):  # 1씩 증가는 생략
    if i % 3 == 0 and i % 5 == 0:  # 만약 변수 i가 3과 5 모두 나누어 떨어졌다면
        print(f'{i} : 3과 5의 공배수')
    elif i % 3 == 0:               # 만약 변수 i가 3으로 나누어 떨어졌다면
        print(f'{i} : 3의 배수')
    elif i % 5 == 0:               # 만약 변수 i가 5로 나누어 떨어졌다면
        print(f'{i} : 5의 배수')
    else:
        print(i)

'''

# 구구단 만들기(for문 사용)
'''
ex) 2단
for i in range(1, 10, 1):
    print(f'2 x {i} = {2 * i}')


ex) 단을 입력받아 구구단
dan = int(input('원하는 단을 입력하세요 : '))
for i in range(1, 10, 1):
    print(f'{dan} x {i} = {dan * i}')

'''
# 중첨 for문을 사용한 구구단 만들기
'''
for i in range(2, 10, 1):             # 2~9단까지 반복
    for k in range(1, 10, 1):         # 각 단의 뒷자리 숫자 1~9까지 반복
        print(f'{i} x {k} = {i * k}') # 구구단 형식에 맞게 출력
    print()                           # 각 단이 끝나면 한 줄 띄우려고 작성

'''

# 터틀 그래픽스 모듈로 그림 그리기
'''
<형식>
import turtle
또는
import turtle as t -->별칭을 t로 정함

거북이 모양 : arrow(큰 화살표), triangle(삼각형), circle(원), blank(빈 칸), turtle(거북이),
              생략하면 기본 화살표 모양

앞으로 이동 : forward, fd
뒤로 이동 : backward, bk, back
왼쪽으로 회전 : left, lt
오른쪽으로 회전 : right, rt


ex) 사각형 그리기
import turtle as t # 별칭 t를 가진 터틀 라이브러리를 불러온다

t.shape('turtle') # 화살표 모양을 거북이 모양
t.right(90)       # 오른쪽으로 90도 회전
t.forward(100)    # 앞으로 100픽셀
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)
t.right(90)
t.forward(100)


ex) 삼각형 그리기
import turtle as t

t.shape('arrow')
t.fd(100)
t.lt(120)
t.fd(100)
t.lt(120)
t.fd(100)
t.lt(120)


ex) 값을 입력받아 다각형 그리기
import turtle as t

n = int(input('몇 각형을 그리시겠습니까? : '))  # 사용자의 입력을 받은 것을 변수 n에 담는다
t.shape('turtle')
for i in range(n):  # n번 반복-->n각형
    t.fd(100)
    t.rt(360/n)     # 외각 구하는 공식 = 360 / 각형


ex) 반복문을 이용해서 원 그리기
import turtle as t

for i in range(360):
    t.fd(1)
    t.lt(1)


ex) 원 그리고 영역 색칠하기
import turtle as t

t.shape('circle') 
t.color('blue')  # 선 색깔을 파란색으로
t.begin_fill()   # 색칠할 면 영역 시작
t.circle(100)    # 반지름이 100픽셀인 원
t.end_fill()     # 색칠할 영역 끝



ex) 별 모양 그리기 (1)
import turtle as t

t.shape('turtle')
for i in range(5):
    t.fd(200)
    t.lt(144)


ex) 별 모양 그리기 (2)
import turtle as t

t.shape('turtle')
for i in range(5):
    t.fd(200)
    t.rt(144)  # 오른쪽으로 144(72 * 2)도 회전
    t.fd(200)
    t.lt(72)   # 왼쪽으로 72(360 / 5)도 회전


ex) 반복문을 이용해서 다양한 모양 그리기
import turtle as t

t.speed(0)   # 거북이의 속도를 가장 빠르게 설정(0 ~ 10. 0이 가장 빠르고, 10이 가장 느림)
for i in range(100):  # 100개 도형
    t.fd(100)
    t.lt(89)


ex)
import turtle as t

t.shape('turtle')
t.speed(0)
for i in range(60):  # 원을 60번 그림
    t.circle(120)    # 반지름이 120 픽셀인 원을 그림
    t.rt(360 / 60)   # 오른쪽으로 6도 회전


ex)미로 모양 그리기
import turtle as t

t.shape('turtle')
t.speed(2)
for i in range(100):  # 100번 반복
    t.fd(i)           # i만큼 앞으로 이동. 반복할 때마다 선이 길어짐(1씩 증가하므로)
    t.lt(90)

'''
# 정수를 입력받아 부호에 따라 거북이를 이동 시키기
'''
import turtle as t

t.shape('turtle')
t.penup()        # 펜을 올려서 그림이 그려지지 않게 한다
t.goto(100, 100) # 거북이를 x축 100, y축 100으로 이동 시킨다
t.write('거북이가 여기로 오면 양수입니다!')  # 화면에 글자가 출력
t.goto(100, 0)   # 거북이를 x축 100, y축 0으로 이동 시킨다
t.write('거북이가 여기로 오면 0입니다!')
t.goto(100, -100)# 거북이를 x축 100, y축 -100으로 이동 시킨다
t.write('거북이가 여기로 오면 음수입니다!')

t.goto(0, 0)  # 거북이를 다시 정가운데로 위치
t.pendown()   # 펜을 내려서 그림이 그려지게 한다

n = int(t.textinput('창제목', '숫자로 입력하세요 : '))  # 텍스트 창에 정수인 숫자를 입력받는다

if n > 0:              # n이 0보다 크면
    t.goto(100, 100)   # 거북이를 x축 100, y축 100으로 이동시킨다
elif n == 0:           # n이 0과 같다면
    t.goto(100, 0)     # 거북이를 x축 100, y축 0으로 이동시킨다
else:                  # n이 0보다 작다면
    t.goto(100, -100)  # 거북이를 x축 100, y축 -100으로 이동시킨다

'''

# 사용자가 입력한 도형 그리기
'''
import turtle as t

t.shape('turtle')
t.pensize(3)       # 펜 크기를 3으로 한다 (선굵기)
t.shapesize(3, 3)  # 거북이를 3배 확대

n = t.textinput('', '도형을 입력하세요 : ')  # 도형을 입력받는다(문자로)

if n == '정사각형':
    for i in range(4):
        t.fd(100)
        t.rt(90)
elif n == '사각형':
    w = int(t.textinput('', '가로 : '))   # w변수에 가로변을 입력받는다(정수로)
    h = int(t.textinput('', '세로 : '))   # h변수에 세로변을 입력받는다(정수로)
    for i in range(2):   # 직사각형이므로 2번만 반복
        t.fd(w)          # 가로
        t.lt(90)
        t.fd(h)          # 세로
        t.lt(90)
elif n == '삼각형':
    l = int(t.textinput('', '한 변의 길이 : '))
    for i in range(3):
        t.fd(l)
        t.rt(120)

'''
