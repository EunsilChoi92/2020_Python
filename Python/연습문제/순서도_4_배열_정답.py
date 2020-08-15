# 1부터 10까지의 수 저장하고 출력하기

a = []
for i in range(1, 11):
    a.append(i)
print(a)



# 10, 20, 30.....100 저장하고 거꾸로 출력하기

a = []
for i in range(10, 101, 10):
    a.append(i)
for i in range(9, -1, -1):
    print(a[i], end=" ")



# 배열 요소 거꾸로 뒤집기

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(0, 5):
    temp = a[i]
    a[i] = a[9-i]
    a[9-i] = temp
print(a)



# 배열 a 요소 배열 b에 거꾸로 저장하기

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = []
for i in range(0, 10):
    b.append(a[9-i])
print(b)



# 배열 요소 왼쪽으로 한 칸씩 원형으로 이동하기

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
temp = a[0]
for i in range(0, 9):
    a[i] = a[i+1]
a[9] = temp
print(a)



# 배열 최댓값 구하기

import random
a = []
for i in range(10):
    a.append(random.randint(1, 100))
print(a)
m = a[0]
for i in range(1, 10):
    if m<a[i]:
        m = a[i]
print("최댓값:", m)



# 10진수를 2진수로 변환하여 배열에 저장하기

b = []
n = int(input("10진수: "))
while n!=0:
    b.append(n%2)
    n = n//2
for i in range(len(b)-1, -1, -1):
        print(b[i], end=" ")



# 배열에 저장된 2진수를 10진수로 변환하기

b = [1,1,0,0,1]
n = 0
for i in range(0, 5):
    n = n + b[i]*(2**(4-i))
print(n)


