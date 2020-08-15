# 터틀 그래픽스
'''
[문제] 터틀 그래픽스 모듈을 이용해서 삼각형 그리기(for문 이용)
힌트 : 수업시간에 한 반복문을 적용하지 않은 코드 참고

[정답]
import turtle as t

for i in range(3):
    t.fd(100)
    t.lt(120)
    
'''
import turtle as t

for i in range(3):
    t.fd(100)
    t.lt(120)


'''
[문제] 터틀 그래픽스 모듈을 이용해서 사각형 그리기(for문 이용)
힌트 : 수업시간에 한 반복문을 적용하지 않은 코드 참고
배경색은 검정, 펜 색은 노랑, 거북이 모양으로

[정답]
import turtle as t

t.shape('turtle')
t.bgcolor('black')
t.color('yellow')
for i in range(4):
    t.fd(100)
    t.rt(90)

'''



'''
[문제] 터틀 그래픽스 모듈을 이용해서 크기를 입력받아 삼각형과 사각형으로 이루어진 집 만들기
힌트 : 수업시간에 한 삼각형과 사각형 코드 참고

[정답1]
import turtle as t

t.shape('turtle')  # 거북이 모양

size = int(input('집의 크기는 얼마로 할까요? '))  # 크기 입력 받기

t.fd(size)  # size만큼 앞으로 이동
t.rt(90)    # 오른쪽으로 90도 회전
t.fd(size)
t.rt(90)
t.fd(size)
t.rt(90)
t.fd(size)
t.right(90)

t.fd(size) # size만큼 앞으로 이동
t.lt(120)  # 왼쪽으로 120도 회전
t.fd(size)
t.lt(120)
t.fd(size)
t.lt(120)

[정답2] for문 이용
import turtle as t

t.shape('turtle')

size = int(input('집의 크기는 얼마로 할까요? '))

for i in range(4):
    t.fd(size)
    t.rt(90)

for i in range(3):
    t.fd(size)
    t.lt(120)
    
'''



'''
[문제] 터틀 그래픽스 모듈을 이용해서 사용자가 입력한 도형 그리기
기존 수업시간에 한 사각형 코드에 추가하여 삼각형, 원, 그 외 도형을 입력했을 때의 조건에 맞추어 결과가 나오도록 할 것

[정답]
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
elif n == '삼각형':
    line = int(t.textinput('', '한 변? '))
    for i in range(3):
        t.fd(line)
        t.lt(120)
elif n == '원':
    size = int(t.textinput('', '반지름 : '))
    t.circle(size)
elif n == '별':
    size = int(t.textinput('', '크기 : '))
    for i in range(5):
        t.fd(size)
        t.rt(144)
        t.fd(size)
        t.lt(72)
elif n == '스타':
    size = int(t.textinput('', '크기 : '))
    for i in range(5):
        t.fd(size)
        t.lt(144)
else:
    print('잘못 입력하셨습니다!!')

'''
