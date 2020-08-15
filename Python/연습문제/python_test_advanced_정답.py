# 중급 이상의 응용 문제
'''
[문제] 완전수 구하기

자기 자신을 제외한 모든 양의 약수들의 합이 자기 자신이 되는 자연수를 완전수라고 한다.
예를 들면, 6과 28은 완전수이다.
6 = 1 + 2 + 3
1, 2, 3은 6의 약수
28 = 1 + 2 + 4 + 7 + 14
1, 2, 4, 7, 14는 28의 약수

입력으로 자연수 N을 받고, 출력으로 N 이하의 모든 완전수를 출력하는 코드를 만들기

[출력결과]
숫자를 입력하세요 : 100
6
28


[정답]
n = int(input('숫자를 입력하세요 : '))
result = 0

for i in range(1, n + 1):
    for j in range(1, i):
        if i % j == 0:
            result += j

    if result == i:
        print(result)

    result = 0

'''



'''
[문제] 구글 입사 문제 중 하나

1부터 10,000까지 8이라는 숫자가 총 몇번 나오는가? 8이 포함되어 있는 수자의 갯수를 카운팅하는 것이 아니라
8이라는 숫자를 모두 카운팅 해야 한다.
(예를 들어, 8808은 3, 8888은 4로 카운팅 해야 함)

[출력결과]
4000


[정답1]
print(str(list(range(1, 10001))).count('8'))


[정답2]
n = 0
for i in str(list(range(1, 10001))):
    if i == '8':
        n += 1
print(n)


[정답3]
count = 0
for a in range(0, 10):
    for b in range(0, 10):
        for c in range(0, 10):
            for d in range(0, 10):
                num = [a, b, c, d]
                count += num.count(8)

print(count)

'''



'''
[문제] 피보나치 수열

피보나치 수열이란, 첫번째 항의 값이 0이고 두번째 항의 값이 1일 때,
그 이후의 항들은 이전의 두 항을 더한 값으로 이루어지는 수열을 말한다.
(예를 들어 0, 1, 1, 2, 3, 5, 8, 13, 21, 24...)

정수 n을 입력 받아 n 이하까지의 피보나치 수열을 출력하는 프로그램을 작성하시오.

[출력결과]
숫자를 입력하세요 : 15
0, 1, 1, 2, 3, 5, 8, 13, 


[정답]
n = int(input('숫자를 입력하세요 : '))

first = 0
fibo = 1
nextfibo = 0

while first < n :
    print(first, end=', ')
    nextfibo = first + fibo
    first = fibo
    fibo = nextfibo
'''
