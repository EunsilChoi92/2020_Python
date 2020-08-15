
score = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100, 60, 85]  #score라는 리스트로 점수를 받음
total = 0 #총점을 0으로 초기화
#for i in score:
#    total = total + i   
#print('총점 : ', total)
#average = total / len(score)  # 평균은 score리스트의 개수(len함수)로 나누어서 구함
#print('평균 : ',  average)

for index, value in enumerate(score):
    print(f'{index} : {value}')
    total = total + value
print('총점 : ', total)
average = total // len(score)  
print('평균 : ',  average)

[출력결과]
0 : 70
1 : 60
2 : 55
3 : 75
4 : 95
5 : 90
6 : 80
7 : 80
8 : 85
9 : 100
10 : 60
11 : 85
총점 :  935
평균 :  77


# 리스트 복사

list1 = [1, 2, 3]
list2 = list1[:]
list3 = list1.copy()
print('list1 : ', list1)
print('list2 : ', list2)
print('list3 : ', list3)
print('id(list1) : ', id(list1))
print('id(list2) : ', id(list2))
print('id(list3) : ', id(list3))

[출력결과]

list1 :  [1, 2, 3]
list2 :  [1, 2, 3]
list3 :  [1, 2, 3]
id(list1) :  53209488
id(list2) :  53209408
id(list3) :  53209568


# 리스트 할당

list4 = [4, 5, 6]
list5 = list4
print('list4 : ', list4)
print('list5 : ', list5)
print('id(list4) : ', id(list4))
print('id(list5) : ', id(list5))

[출력결과]

list4 :  [4, 5, 6]
list5 :  [4, 5, 6]
id(list4) :  53209728
id(list5) :  53209728


# 리스트에서 인덱스번호와 요소를 함께 출력하기

'''
<형식>
for 인덱스번호, 요소 in enumerate(리스트명):

'''

a = [10, 20, 30]
for index, value in enumerate(a):
    print(index, value)

for index, value in enumerate(a, start=1):
    print(f'{index} : {value}')

b = [50, 30, 40]
for i in range(len(b)):
    print(b[i])

[출력결과]

0 10
1 20
2 30
1 : 10
2 : 20
3 : 30
50
30
40
