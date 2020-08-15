# 1부터 10까지 출력하기(1)

i=1
while i<=10:
    print(i, end=" ")
    i = i+1



# 1부터 10까지 출력하기(2)

for i in range(1, 11):
    print(i, end=" ")



# 10부터 1까지 출력하기

for i in range(10, 0, -1):
    print(i, end=" ")



# 1부터 100까지 합 구하기

sum = 0
for i in range(1, 101):
    sum = sum+i
print(sum)



# 1부터 100까지의 수 중 짝수의 합 구하기(1)

sum = 0
for i in range(2, 101, 2):
    sum = sum+i
print(sum)



# 1부터 100까지의 수 중 짝수의 합 구하기(2)

sum = 0
for i in range(1, 101):
    if i%2==0:
        sum = sum+i
print(sum)



# 1, -2, 3, -4, ....99, -100의 합 구하기

sum = 0
for i in range(1, 101):
    if i%2==0:
        sum=sum-i
    else:
        sum=sum+i
print(sum)



# 계승 구하기(팩토리얼)

fact = 1
for i in range(5, 0, -1):
    fact = fact*i
print(fact)



# 약수구하기

n = int(input("정수: "))
for i in range(1, n+1):
    if n%i == 0:
        print(i, end=" ")



# 공약수 구하기

n1 = int(input("정수: "))
n2 = int(input("정수: "))
for i in range(1, n1+1):
    if n1%i == 0 and n2%i == 0:
        print(i, end=" ")



# 최대 공약수 구하기

n1 = int(input("정수: "))
n2 = int(input("정수: "))
for i in range(n1, 0, -1):
    if n1%i==0 and n2%i==0:
        print(i)
        break



# 소수 판별하기

chk = 1
n = int(input("정수: "))
for i in range(2, n):
    if n%i == 0:
        chk = 0
        break
if chk==1:
    print(n, ": 소수임")
else:
    print(n, ": 소수아님")



# 피보나치 수열 구하기

a = 1
b = 1
print(a, b, end=" ")
for i in range(3, 21):
    c = a+b
    print(c, end=" ")
    a = b
    b = c



# 최대값 구하기

a = int(input("정수: "))
m = a
while a!=0:    
    if a>m:
        m = a
    a = int(input("정수: "))
print("최댓값 :", m)



# 직각 삼각형 모양으로 수 출력하기

for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()



# 1부터 10까지의 정수에 대한 약수 구하기

for i in range(1, 11):
    print(i, "약수:", end=" ")
    for j in range(1, i+1):
        if i%j==0:
            print(j, end=" ")
    print()



# 2부터 100까지의 소수 구하기

for i in range(2, 101):
    chk = 1
    for j in range(2, i):
        if i%j==0:
            chk = 0
            break
    if chk==1:
        print(i, end=" ")



# 1, (1+2), (1+2+3),....(1+2+..9+10)의 합 구하기

n = 0
sum = 0
for i in range(1, 11):
    n = n+i
    sum = sum+n
print(sum)



# 구구단

for i in range(2, 10):
    for j in range(1, 10):
        print(i, "*", j, "=", i*j, end=" ")
    print()

