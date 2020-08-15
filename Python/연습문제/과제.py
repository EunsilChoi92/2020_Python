import turtle, random

#t = turtle.Turtle()

turtle.shape('turtle')
def color():
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.color(r, g, b)

def t():
    turtle.clear()
    color()
    for i in range(3):
        turtle.forward(100)
        turtle.left(360/3)
    
def s():
    turtle.clear()
    color()
    for i in range(4):
        turtle.forward(100)
        turtle.left(360/4)

def p():
    turtle.clear()
    color()
    for i in range(5):
        turtle.forward(100)
        turtle.left(360/5)

def star():
    turtle.clear()
    color()
    for i in range(5):
        turtle.forward(100)
        turtle.right((360/5)*2)
        turtle.forward(100)
        turtle.left(360/5)

def h():
    turtle.clear()
    color()
    for i in range(4):
        turtle.forward(100)
        turtle.right(360/4)
    for i in range(3):
        turtle.forward(100)
        turtle.left(360/3)

def o():
    turtle.clear()
    
    turtle.pensize(5)
    turtle.penup()       # 펜을 올려서 그림이 그려지지 않게 한다 
    turtle.goto(-100, 0) # 첫번째 원
    turtle.pendown()     # 펜을 내려서 그림이 그려지게 한다
    turtle.color('blue')
    turtle.circle(50)

    turtle.penup()       # 펜을 올려서 그림이 그려지지 않게 한다
    turtle.goto(-50, -50) # 두번째 원
    turtle.pendown()     # 펜을 내려서 그림이 그려지게 한다
    turtle.color('yellow')
    turtle.circle(50)

    turtle.penup()       # 펜을 올려서 그림이 그려지지 않게 한다
    turtle.goto(0, 0) # 세번째 원
    turtle.pendown()     # 펜을 내려서 그림이 그려지게 한다
    turtle.color('black')
    turtle.circle(50)

    turtle.penup()       # 펜을 올려서 그림이 그려지지 않게 한다
    turtle.goto(50, -50) # 네번째 원
    turtle.pendown()     # 펜을 내려서 그림이 그려지게 한다
    turtle.color('green')
    turtle.circle(50)

    turtle.penup()       # 펜을 올려서 그림이 그려지지 않게 한다
    turtle.goto(100, 0) # 다섯번째 원
    turtle.pendown()     # 펜을 내려서 그림이 그려지게 한다
    turtle.color('red')
    turtle.circle(50)

num = 0
while num < 3:
    n = turtle.textinput('', '무엇을 그릴까요?(삼각형, 사각형, 오각형, 별, 집, 오륜기 중 고르세요)')
#print('무엇을 그릴까요?(삼각형=1, 사각형=2, 오각형=3, 별=4, 오륜기=5 중 고르세요)')
#n = input()
    if n == '삼각형':
        t()
    elif n == '사각형':
        s()
    elif n == '오각형':
        p()
    elif n == '별':
        star()
    elif n == '집':
        h()
    elif n == '오륜기':
        o()
    else:
        print('잘못 입력하셨습니다. 다시 입력해주세요!')
    
    num += 1


print('수고하셨습니다!! 재미있는 파이썬!!')
