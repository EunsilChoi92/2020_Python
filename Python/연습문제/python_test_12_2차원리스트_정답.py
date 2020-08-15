# 2차원 리스트
'''
[문제]

중첩 for문을 이용해서 3행 4열짜리 2차원 리스트 생성하기


[출력결과]

  1  2  3  4
  5  6  7  8
  9 10 11 12


[정답]

list1 = []                    # 빈 리스트 하나 생성-가로
list2 = []                    # 빈 리스트 하나 생성-세로(가로 포함)
value = 1
for i in range(3):            # 가로 3행 
    for k in range(4):        # 세로 4열
        list1.append(value)   # 가로로 4개 숫자를 리스트1에 추가
        value += 1
    list2.append(list1)       # 가로 1줄(1행) 리스트2에 추가
    list1 = []                # 가로줄 새로 넣기 위해 리스트1을 다시 비워둠

for i in range(3):            # 출력을 가로 3행
    for k in range(4):        # 출력을 세로 4열
        print(f'{list2[i][k]:3d}', end='')    # 앞에 3칸 띄우도록, # print('{:3d}'.format(list2[i][k]), end='')와 같다
    print()
    
'''



'''
[문제]

중첩 for문을 이용해서 4행 5열짜리 2차원 리스트를 만들고 0부터 3의 배수가 출력되도록 하기


[출력결과]

  0  3  6  9 12
 15 18 21 24 27
 30 33 36 39 42
 45 48 51 54 57


[정답]

list1 = []                    # 빈 리스트 하나 생성-가로
list2 = []                    # 빈 리스트 하나 생성-세로(가로 포함)
value = 0
for i in range(4):            # 가로 4행 
    for k in range(5):        # 세로 5열
        list1.append(value)   # 가로로 4개 숫자를 리스트1에 추가
        value += 3
    list2.append(list1)       # 가로 1줄(1행) 리스트2에 추가
    list1 = []                # 가로줄 새로 넣기 위해 리스트1을 다시 비워둠

for i in range(4):            # 출력을 가로 4행
    for k in range(5):        # 출력을 세로 5열
        print(f'{list2[i][k]:3d}', end='')    # 앞에 3칸 띄우도록, # print('{:3d}'.format(list2[i][k]), end='') 와 같다
    print()

'''
