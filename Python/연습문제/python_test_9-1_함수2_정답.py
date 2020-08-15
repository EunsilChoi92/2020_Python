# 리스트와 함수

'''
[문제] 

정수 리스트들을 리스트로 받아서 중첩 리스트의 모든 요소를 더하는 nested_sum 함수를 작성하라.
ex) 리스트 t = [[1, 2], [3], [4, 5, 6]


[출력결과]
리스트 t :  [[1, 2], [3], [4, 5, 6]]
result :  21


[정답]
def nested_sum(t):
    total = 0
    for nested in t:
        total += sum(nested)
    return total

t = [[1, 2], [3], [4, 5, 6]]
result = nested_sum(t)
print('리스트 t : ', t)
print('result : ', result)

'''



'''
[문제]

숫자로 구성된 리스트를 받아서 누적 합계를 반환하는 cumsum 함수를 작성하라.
즉, 새로운 리스트에서 1번재 요소는 원본 리스트에서 i+1 원소까지의 합계가 된다.
ex) 리스트 t = [1, 2, 3]


[출력결과]
리스트 t :  [1, 2, 3]
result :  [1, 3, 6]


[정답]
def cumsum(t):
    total = 0
    res = []
    for x in t:
        total += x
        res.append(total)
    return res

t = [1, 2, 3]
result = cumsum(t)
print('리스트 t : ', t)
print('result : ', result)

'''



'''
[문제]

리스트를 받아서 첫 번째와 마지막 요소를 제외한 나머지 요소들을 담은 새 리스트를 반환하는 middle 함수를 작성하라. 
ex) 리스트 t = [1, 2, 3, 4]


[출력결과]
리스트 t :  [1, 2, 3, 4]
result :  [2, 3]


[정답]
def middle(t):
    return t[1:-1]

t = [1, 2, 3, 4]
result = middle(t)
print('리스트 t : ', t)
print('result : ', result)

'''



'''
[문제]

리스트를 받아서 첫 번째와 마지막 요소를 제거하면서 리스트를 직접 수정하고 None을 반환하는 chop 함수를 작성하라. 
ex) 리스트 t = [1, 2, 3, 4]


[출력결과]
result :  None
리스트 t :  [2, 3]


[정답]
def chop(t):
    del t[0]
    del t[-1]

t = [1, 2, 3, 4]
result = chop(t)

print('result : ', result)
print('리스트 t : ', t)

'''



'''
[문제] 몫과 나머지를 구하는 함수 만들기

x를 y로 나누었을 때의 몫과 나머지가 출력되게 만들자.


[출력결과]
x :  10
y :  3
몫 : 3, 나머지 : 1


[정답]
def get_q_r(a, b):
    return a // b, a % b

x = 10
y = 3

print('x : ', x)
print('y : ', y)

q, r = get_q_r(x, y)
print(f'몫 : {q}, 나머지 : {r}')

'''



'''
[문제] 가장 높은 점수를 구하는 함수 만들기

네 개의 점수 중에서 가장 높은 점수가 출력되게 만들자.
(파이썬에서 기본적으로 제공해주는 max 함수를 사용하면 쉽게 최대값을 구할 수 있다.)


[출력결과]
가장 높은 점수 :  100


[정답]
def get_max(a, b, c, d):
    return max(a, b, c, d)

kor, eng, math, sci = 100, 86, 81, 91
score = get_max(kor, eng, math, sci)
print('가장 높은 점수 : ', score)

'''
