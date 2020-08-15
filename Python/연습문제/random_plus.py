import random  # 랜덤 기능을 가진 모듈을 불러온다

a = random.randint(1, 10)  # a 변수에 1~10까지의 수 중 임의의 수를 저장
b = random.randint(1, 10)  # b 변수에 1~10까지의 수 중 임의의 수를 저장

print('{} + {} = ??'.format(a, b)) 

c = int(input('정답은 무엇입니까?? '))  # 정답이 될 수를 입력 받는다
ans = a + b

if ans == c:    # 컴퓨터가 a, b변수를 더한 것과 사용자가 입력한 정답을 비교
    print('정답입니다!')
elif abs(ans - c) <= 2:  # 오차 범위 +2 -2
    print('어느정도 맞추었습니다.')
else:
    print('틀렸습니다~~')
