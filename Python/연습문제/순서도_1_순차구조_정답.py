# 사각형 넓이 구하기

a = int(input("가로: "))
b = int(input("세로: "))
print("사각형 넓이:", a*b)


# 원 넓이 구하기

pi = 3.14159
r = int(input("반지름: "))
print("원의 넓이:", r*r*pi)


# 총점과 평균 구하기

a = int(input("성적1: "))
b = int(input("성적2: "))
c = int(input("성적3: "))
sum = a+b+c
print("총점:", sum, "평균:", sum/3)


# 센티미터 단위의 길이를 미터와 센티미터로 변환하기

cm = int(input("센티미터 단위의 길이: "))
m = cm//100
cm = cm%100
print(m, "미터", cm, "센티미터")


# 초 단위의 시간을 시간, 분, 초로 변환하기

s = int(input("초 단위의 시간: "))
h = s//3600
s = s%3600
m = s//60
s = s%60
print(h, "시간", m, "분", s, "초")
