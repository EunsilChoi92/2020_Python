# 터틀 그래픽스 모듈로 그림 그리기

import turtle
또는
import turtle as t --> 별칭을 t로 정함

거북이 모양 : arrow(큰 화살표), triangle(삼각형), circle(원), blank(빈칸), turtle(거북이), 생략하면 기본화살표 

앞으로 이동 : forward, fd
뒤로 이동 : backward, bk, back
왼쪽으로 회전 : left, lt
오른쪽으로 회전 : right, rt


ex)
import turtle as t
t.shape('turtle') # 거북이 모양
t.right(90)       # 오른쪽으로 90도 
t.forward(100)    # 앞으로 100픽셀 
t.right(90)     
t.forward(100)


ex) 사각형 그리기

import turtle as t

t.shape('arrow')  # 화살표모양
t.fd(100)         # 앞으로 100픽셀
t.rt(90)          # 오른쪽으로 90도
t.fd(100)
t.rt(90)
t.fd(100)
t.rt(90)
t.fd(100)


ex) 삼각형 그리기

import turtle as t

t.shape('blank')  # 화살표 모양 안나옴
t.fd(100)   
t.lt(120)         # 왼쪽으로 120도
t.fd(100)
t.lt(120)
t.fd(100)
t.lt(120)
    

ex) 오각형 그리기

import turtle as t

t.shape('turtle')
for i in range(5):    # 오각형이므로 5번 반복
    t.fd(100)
    t.rt(360 / 5)     # 360을 5로 나누어서 외각을 구함


ex) 값을 입력받아 다각형 그리기

import turtle as t

n = int(input('몇 각형을 그리시겠습니까 : '))  # 사용자의 입력을 받음
t.shape('turtle')
for i in range(n):                             # n번 반복
    t.fd(100)
    t.rt(360 / n)                              # 360을 n으로 나누어서 외각을 구함


ex) 반복문을 이용해서 원 그리기

import turtle as t

for i in range(360):
    t.fd(1)
    t.lt(1)
    

ex) 선 굵기와 색을 바꾸고 원 그리기

import turtle as t

t.shape('circle') # 원모양
t.color('blue')   # 색깔을 파란색으로 
t.pensize(5)      # 굵기를 5
t.circle(50)


ex) 육각형에 색칠하기

import turtle as t

n = 6                  # 육각형
t.shape('turtle')
t.color('red')         # 펜의 색을 빨강으로 지정
t.begin_fill()         # 색칠할 영역 시작 
for i in range(n):     # n번 반복(6번 반복)
    t.fd(100)
    t.rt(360 / n)
t.end_fill()           # 색칠할 영역 끝


ex) 반복문으로 다양한 모양 그리기

import turtle as t

t.speed(0)
for i in range(100):
    t.fd(100)
    t.lt(89)


ex) 원을 반복해서 복잡한 도형 그리기

import turtle as t

n = 60                     # 원을 60번 그림
t.shape('turtle')
t.speed('fastest')         # 거북이 속도를 가장 빠르게 설정
for i in range(n):
    t.circle(120)          # 반지름이 120인 원을 그림
    t.rt(360 / n)          # 오른쪽으로 6도 회전
    

ex) 선으로 복잡한 무늬 그리기

import turtle as t

t.shape('turtle')
t.bgcolor('black')   # 배경색을 검정으로
t.color('yellow')    # 펜 색을 노랑으로
t.speed(0)           # 거북이 속도를 가장 빠르게 설정 (fastest와 같다) 0 ~ 10 
for i in range(300): # 300번 반복
    t.fd(i)          # i만큼 앞으로 이동, 반복할 때마다 선이 길어짐
    t.rt(91)         # 오른쪽으로 91도 회전


ex) 별 모양 그리기

import turtle as t

t.shape('turtle')
for i in range(5):
    t.fd(100)
    t.lt(144)
    

ex) 미로 그리기

import turtle as t

t.shape('turtle')
t.speed(0)
for i in range(100):
    t.fd(i)
    t.lt(90)


ex) 문자열을 입력 받고 출력하면서 사각형 그리기

import turtle as t

t.shape('turtle')
name = t.textinput('창 제목','당신의 이름은 무엇입니까?' )     # 입력 창을 띄운다. name변수에 입력한 내용을 담는다
t.write('안녕하세요??'+name+'씨, 저는 터틀입니다! 반가워요!!') # 화면에 출력
for i in range(4):
    t.lt(90)
    t.fd(100)


ex) 오륜기 그리기

import turtle as t

t.shape('turtle')
t.speed(0)
t.pensize(10)

t.penup()       # 펜을 올려서 그림이 그려지지 않게 한다 
t.goto(-100, 0) # 첫번째 원
t.pendown()     # 펜을 내려서 그림이 그려지게 한다
t.color('blue')
t.circle(50)

t.penup()       # 펜을 올려서 그림이 그려지지 않게 한다
t.goto(-50, -50) # 두번째 원
t.pendown()     # 펜을 내려서 그림이 그려지게 한다
t.color('yellow')
t.circle(50)

t.penup()       # 펜을 올려서 그림이 그려지지 않게 한다
t.goto(0, 0) # 세번째 원
t.pendown()     # 펜을 내려서 그림이 그려지게 한다
t.color('black')
t.circle(50)

t.penup()       # 펜을 올려서 그림이 그려지지 않게 한다
t.goto(50, -50) # 네번째 원
t.pendown()     # 펜을 내려서 그림이 그려지게 한다
t.color('green')
t.circle(50)

t.penup()       # 펜을 올려서 그림이 그려지지 않게 한다
t.goto(100, 0) # 다섯번째 원
t.pendown()     # 펜을 내려서 그림이 그려지게 한다
t.color('red')
t.circle(50)


ex) 별 그리기(2)

import turtle as t

n = 5
t.shape('turtle')
for i in range(n):        # 5번 반복
    t.fd(100)
    t.rt((360 / n) * 2)   # 오른쪽으로 144(72 * 2)도 회전
    t.fd(100)
    t.lt(360 / n)         # 왼쪽으로 72도 회전
    

ex) 정수를 입력받아 부호에 따라 거북이를 이동시키기

import turtle as t

t.shape('turtle')
t.penup()                                         # 펜을 올려서 그림이 그려지지 않게 한다
t.goto(100, 100)                                  # 거북이를 (100, 100)으로 이동시킨다 x축 : 100, y축 : 100
t.write('거북이가 여기로 오면 양수입니다!')
t.goto(100, 0)
t.write('거북이가 여기로 오면 0입니다!')
t.goto(100, -100)
t.write('거북이가 여기로 오면 음수입니다!')

t.goto(0, 0)                                      # 거북이를 (0, 0)으로 이동시킨다. 정가운데
t.pendown()                                       # 펜을 내려서 그림이 그려지게 한다
n = int(t.textinput('', '숫자를 입력하세요 : '))  # 텍스트 창에 정수인 숫자를 입력받는다

if n > 0:                                         # 0보다 크면
    t.goto(100, 100)                              # 거북이가 100, 100으로 이동
elif n == 0:                                      # 0과 같으면
    t.goto(100, 0)                                # 거북이가 100, 0으로 이동
else:                                             # 0보다 작으면
    t.goto(100, -100)                             # 거북이가 100, -100으로 이동


ex) 명령어를 입력받아 거북이 제어하기

import turtle as t

t.shape('turtle')
t.pensize(3)
t.shapesize(3, 3)  # 거북이를 3배 확대한다

while True:
    cmd = input('명령을 입력하세요 : ')  # 명령을 입력받는다
    if cmd == 'l':   
        t.lt(90)
        t.fd(100)
    if cmd == 'r':
        t.rt(90)
        t.fd(100)
    if cmd == 'u':
        t.setheading(90)    # 거북이의 머리를 북쪽으로 (동쪽 : 0, 서쪽 : 180)
        t.fd(100)
    if cmd == 'd':
        t.setheading(270)   # 거북이의 머리를 남쪽으로 
        t.fd(100)


ex) 사용자가 입력한 도형 그리기

import turtle as t

t.shape('turtle')
n = t.textinput('', '도형을 입력하세요 : ')   # 도형을 입력받는다(문자)
if n == '사각형':                             # 사각형이라면
    w = int(t.textinput('', '가로 : '))       # w변수에 가로변을 입력받는다(정수)
    h = int(t.textinput('', '세로 : '))       # h변수에 세로변을 입력받는다(정수)
    for i in range(2):
        t.fd(w)                               # 가로
        t.lt(90)
        t.fd(h)                               # 세로
        t.lt(90)
'''
---->여기서 부터는 문제에 있음
elif n == '삼각형':
    line = int(t.textinput('', '한 변의 길이 : '))
    for i in range(3):
        t.fd(line)
        t.lt(120)
elif n == '원':
    size = int(t.textinput('', '원의 크기 : '))
    t.circle(size)
else:
    print('잘못 입력 하셨습니다!')
'''
