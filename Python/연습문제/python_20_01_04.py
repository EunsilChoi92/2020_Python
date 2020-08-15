# 리스트 (list)
'''
여러가지 자료를 저장할 수 있는 자료 모음
여러개의 변수가 하나의 덩어리로 합쳐진 상태
다른 언어의 배열과 비슷한 개념
대괄호 내부에 자료들을 넣어 선언

리스트의 인덱스 번호도 0부터 시작한다.

<형식>
리스트명 = [요소1, 요소2, 요소3,.....]  # 요소는 값과 같은 의미



a = []                      # 빈 리스트
b = [1, 2, 3]               # 숫자 3개가 요소인 리스트
c = ['a', 'b', 'c', 'd']    # 문자 4개가 요소인 리스트
d = [1, 2, 'a', 'b', True]  # 숫자, 문자, 논리값이 요소인 리스트 (여러 자료형으로 구성가능)
e = [1, 2, ['a', 'b']]      # 이중 리스트

print(a)
print(b)
print(c)
print(d)
print(e)

print(b[1])
print(c[3])
print(d[0])
print(e[2])
print(d[-1])
print(e[-1])
print(e[2][0])

[출력결과]

[]
[1, 2, 3]
['a', 'b', 'c', 'd']
[1, 2, 'a', 'b', True]
[1, 2, ['a', 'b']]
2
d
1
['a', 'b']
True
['a', 'b']
a


f = [1, 2, ['a', 'b', ['c', 'd']]]  # 3중 리스트
print(f[2][2][0])  # c 출력


'''

# 리스트 슬라이싱
'''
a = [1, 2, 3, 4, 5]
print(a[0:2])
print(a[2:3])
print(a[:3])
print(a[2:])

[출력결과]

[1, 2]
[3]
[1, 2, 3]
[3, 4, 5]



a = [1, 2, 3, ['b', 'c', 'd'], 4, 5]

print(a[2:5])  # 1차원만
print(a[3][:2]) # 2차원까지 슬라이싱
print(a)  # 슬라이싱 한다고 해서 리스트 원본이 바뀌지 않는다

[출력결과]

[3, ['b', 'c', 'd'], 4]
['b', 'c']
[1, 2, 3, ['b', 'c', 'd'], 4, 5]

'''

# 리스트 연산자
'''
list1 = [1, 2, 3]
list2 = [4, 5, 6]

print('list1 : ', list1)
print('list2 : ', list2)
print('list1 + list2 : ', list1 + list2)
print('list1 * 3 : ', list1 * 3)
print()
print('#리스트 길이 구하기')
print('len(list1) :', len(list1))

[출력결과]

list1 :  [1, 2, 3]
list2 :  [4, 5, 6]
list1 + list2 :  [1, 2, 3, 4, 5, 6]
list1 * 3 :  [1, 2, 3, 1, 2, 3, 1, 2, 3]

#리스트 길이 구하기
len(list1) : 3

'''


# 리스트 관련 함수들

# 리스트 요소(값) 추가 : append(), insert()
'''
<형식>
리스트명.append(요소) --> 리스트 맨 뒤에 요소를 추가

리스트명.insert(위치, 요소) --> 리스트 중간에 요소를 추가


ex)
list1 = [1, 2, 3]
print('list1 --> ', list1)
print('#리스트 뒤에 요소 추가')
list1.append(4)
print('list1 맨 뒤에 4를 추가 --> ', list1)
list1.append(100)
print('list1 맨 뒤에 100을 추가 --> ', list1)
print()
print('#리스트 중간에 요소 추가')
list1.insert(0, 50)
print('list1의 0번에 50을 추가 -->', list1)

[출력결과]

list1 -->  [1, 2, 3]
#리스트 뒤에 요소 추가
list1 맨 뒤에 4를 추가 -->  [1, 2, 3, 4]
list1 맨 뒤에 100을 추가 -->  [1, 2, 3, 4, 100]

#리스트 중간에 요소 추가
list1의 0번에 50을 추가 --> [50, 1, 2, 3, 4, 100]

'''

# 리스트 요소 제거 : del, pop()
'''
<형식>
del 리스트명[인덱스번호]

리스트명.pop(인덱스번호)
리스트명.pop()  --> 맨 끝의 요소가 제거 (인덱스 번호 생략도 가능)



list2 = [0, 1, 2, 3, 4, 5]
print('list2 -->', list2)
print('#리스트의 요소 하나 제거')
del list2[1]
print('del list2[1] 실행 후 -->', list2)
list2.pop(2)
print('list2.pop(2) 실행 후 -->', list2)
list2.pop()
print('list2.pop() 실행 후 -->', list2)

[출력결과]

list2 --> [0, 1, 2, 3, 4, 5]
#리스트의 요소 하나 제거
del list2[1] 실행 후 --> [0, 2, 3, 4, 5]
list2.pop(2) 실행 후 --> [0, 2, 4, 5]
list2.pop() 실행 후 --> [0, 2, 4]




print('#리스트의 슬라이딩 기능을 이용하여 제거하기')
list3 = [0, 1, 2, 3, 4, 5, 6]
print('list3 -->', list3)
del list3[3:6]  # 3, 4, 5번 인덱스 요소 삭제
print('del list3[3:6] 실행 후 -->', list3)
print()
list4 = [0, 1, 2, 3, 4, 5, 6]
print('list4 -->', list4)
del list4[:3]
print('del list4[:3] 실행 후 -->', list4)

[출력결과]

#리스트의 슬라이딩 기능을 이용하여 제거하기
list3 --> [0, 1, 2, 3, 4, 5, 6]
del list3[3:6] 실행 후 --> [0, 1, 2, 6]

list4 --> [0, 1, 2, 3, 4, 5, 6]
del list4[:3] 실행 후 --> [3, 4, 5, 6]

'''

# 리스트 내부의 요소를 요두 제거 : clear()
'''
<형식>
리스트명.clear()


print('#리스트 내부의 요소를 모두 제거')
list5 = [0, 1, 2, 3, 4, 5]
print('list5 -->', list5)
list5.clear()
print('list5.clear() 실행 후 -->', list5)

[출력결과]

#리스트 내부의 요소를 모두 제거
list5 --> [0, 1, 2, 3, 4, 5]
list5.clear() 실행 후 --> []

'''

# 리스트 정렬 : sort()
'''
<형식>
리스트명.sort()  -->오름차순
리스트명.sort(reverse=True) -->내림차순



print('#리스트 정렬')
list6 = [1, 4, 3, 2]
print('list6 -->', list6)
list6.sort()
print('list6.sort() 실행 후 (오름차순) -->', list6)
print()
list7 = [1, 4, 3, 2]
print('list7 -->', list7)
list7.sort(reverse=True)
print('list7.sort(reverse=True) 실행 후 (내림차순) -->', list7)

[출력결과]

#리스트 정렬
list6 --> [1, 4, 3, 2]
list6.sort() 실행 후 (오름차순) --> [1, 2, 3, 4]

list7 --> [1, 4, 3, 2]
list7.sort(reverse=True) 실행 후 (내림차순) --> [4, 3, 2, 1]

'''

# 리스트 뒤집기 : reverse()
'''
<형식>
리스트명.reverse()


list8 = ['a', 'c', 'b']
print('#리스트 뒤집기')
print('list8 -->', list8)
list8.reverse()
print('list8.reverse() 실행 후 -->', list8)

[출력결과]

#리스트 뒤집기
list8 --> ['a', 'c', 'b']
list8.reverse() 실행 후 --> ['b', 'c', 'a']

'''

# 리스트 복사
'''
list1 = [1, 2, 3]
list2 = list1[:]
list3 = list1.copy()
print('list1 -->',list1)
print('list2 -->',list2)
print('list3 -->',list3)
print()
list1[0] = 10  # list1의 0번에 있는 요소를 10으로 바꾸어라
print('list1 -->',list1)
print('list2 -->',list2)
print('list3 -->',list3)
print(id(list1))
print(id(list2))
print(id(list3))

[출력결과]

list1 --> [1, 2, 3]
list2 --> [1, 2, 3]
list3 --> [1, 2, 3]

list1 --> [10, 2, 3]
list2 --> [1, 2, 3]
list3 --> [1, 2, 3]
2044298880520
2044298881608
2044298881736
'''

# 리스트 할당
'''
list4 = [4, 5, 6]
list5 = list4
print('list4 -->',list4)
print('list5 -->',list5)
list4[0] = 10
print()
print('list4 -->',list4)
print('list5 -->',list5)
print(id(list4))
print(id(list5))

[출력결과]

list4 --> [4, 5, 6]
list5 --> [4, 5, 6]

list4 --> [10, 5, 6]
list5 --> [10, 5, 6]
2125788046600
2125788046600

'''

# for문과 리스트를 이용한 평균 점수 구하기
'''
score = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100, 10]  # score라는 리스트(학생들 점수가 있음)
total = 0    # 총점을 0으로 초기화

for i in score:  # i는 score[i]를 뜻함
    total = total + i   # total += i. 70+60+55+....100+10

print('총점 : ', total)
average = total // len(score)  # 평균은 score리스트의 개수(len함수)로 나누어서 구함. 몫만
print('평균 : ', average)

[출력결과]

총점 :  800
평균 :  72

'''


# for문과 리스트를 이용해서 홀수에만 2를 곱하여 저장하기
'''
numbers = [1, 2, 3, 4, 5]
result = []     # 결과를 담을 빈 리스트를 만든다.

for n in numbers:  # numbers 리스트에 있는 값들을 하나씩 다 비교
    if n % 2 == 1: # 2로 나눈 나머지가 1이면 홀수이므로
        result.append(n * 2) # append 함수를 써서 result 리스트에 결과값을 추가

print('결과 : ', result)

[출력결과]

결과 :  [2, 6, 10]

'''

# 튜플 (tuple)
'''
읽기 전용 리스트

<형식>
튜플명 = (요소1, 요소2, 요소3,....)
튜플명 = 요소1, 요소2, 요소3
튜플명 = (요소1,) -->요소가 1개인 튜플을 만들때는 뒤에 콤마를 붙인다. 붙이지 않으면 변수가 됨
튜플명 = 요소1,

'''

# 리스트와 튜플의 차이점
'''
리스트는 [], 튜플은 ()
리스트는 그 값의 생성, 삭제, 수정 가능
튜플은 그 값을 바꿀 수 없다.

'''

# 튜플 조작 프로그램(예제)
'''
a = input('튜플에 입력할 자료들을 차례로 입력하세요. 빈칸으로 구분합니다.').split()
b = tuple(a) # 입력받은 값을 튜플로 바꾼다
print(b)     # 튜플인지 확인하기 위해 출력해본다
while True:
    print('작업할 내용을 입력하세요.')
    c = input('q=끝내기, s=슬라이싱, c=세기, i=존재여부 : ') 

    if c == 'q':  # q를 입력한다면 프로그램을 종료
        print('프로그램을 종료합니다.')
        break
    elif c == 's':  # s를 입력한다면 슬라이싱
        s1 = int(input('처음 : '))  # 슬라이싱 할 때 처음 인덱스 번호
        s2 = int(input('끝 : '))    # 슬라이싱 할 때 끝 인덱스 번호
        print(b[s1:s2])
    elif c == 'c':  # c를 입력한다면 요소 개수를 센다
        c1 = input('찾을 자료값은? ')
        print(b.count(c1),'개 있습니다.')  # count 함수는 찾는 값이 그 안에 몇 개 있는가
    elif c == 'i':  # i를 입력한다면 요소가 있는지 확인한다
        i1 = input('찾을 자료값은? ')
        print(i1 in b)   # in 연산자는 찾는 값이 그 안에 있는가 없는가
    else:           # q, s, c, i 외 다른 글자를 입력하면..
        print('잘못 입력하셨습니다.')

'''

# 딕셔너리 (dicitionary)
'''
중괄호 {} 로 묶여있으며, 키와 값의 쌍으로 이루어짐
순서가 없는 자료형이라 인덱싱을 지원하지 않는다.

<형식>
딕셔너리명 = {키1:값1, 키2:값2, 키3:값3,....}

'''

# 딕셔너리 관련 함수
'''
dic = {'name':'홍길동', 'phone':'01012345678', 'birth':'0101'}
print('딕셔너리 -->', dic)
print('dic["name"] -->', dic['name'])
print()
print('#딕셔너리의 쌍 추가하기')
dic['address'] = '대구'
print('추가 후 딕셔너리 -->', dic)
print()
print('#딕셔너리의 쌍 삭제하기')
del dic['address']
print('삭제 후 딕셔너리 -->', dic)
print()
print('#key 리스트 만들기')
print(dic.keys())  # 키 부분만 모은 것
print()
print('#값 리스트 만들기')
print(dic.values()) # 값 부분만 모은 것
print()
print('#item을 이용해서 쌍(키, 값) 얻기(리스트)')
print(dic.items()) # 각 쌍이 튜플로
print('#키:값 모두 지우기')
dic.clear()
print('모두 지운 후 딕셔너리 -->', dic)

[출력결과]

딕셔너리 --> {'name': '홍길동', 'phone': '01012345678', 'birth': '0101'}
dic["name"] --> 홍길동

#딕셔너리의 쌍 추가하기
추가 후 딕셔너리 --> {'name': '홍길동', 'phone': '01012345678', 'birth': '0101', 'address': '대구'}

#딕셔너리의 쌍 삭제하기
삭제 후 딕셔너리 --> {'name': '홍길동', 'phone': '01012345678', 'birth': '0101'}

#key 리스트 만들기
dict_keys(['name', 'phone', 'birth'])

#값 리스트 만들기
dict_values(['홍길동', '01012345678', '0101'])

#item을 이용해서 쌍(키, 값) 얻기(리스트)
dict_items([('name', '홍길동'), ('phone', '01012345678'), ('birth', '0101')])
#키:값 모두 지우기
모두 지운 후 딕셔너리 --> {}

'''

# 딕셔너리 활용한 음식궁합 프로그램 만들기
'''
foods = {'떡볶이':'오뎅',
         '짜장면':'단무지',
         '라면':'김치',
         '치킨':'맥주',
         '삼겹살':'상추',
         '피자':'콜라'}

while True:
    myfood = input(f'{list(foods.keys())}중 좋아하는 것은?(끝을 입력하면 종료) ') # 키만 리스트로 불러와서 사용자에게 답을 입력받는다
    if myfood in foods:                                            # foods 딕셔너리에 내가 입력한 음식이 있나 확인
        print(f'{myfood} 궁합 음식은 {foods.get(myfood)}입니다.')  # myfood와 일치하는 값(value)을 출력
    elif myfood == '끝':
        break
    else:
        print('잘못 입력하셨습니다. 다시 입력하세요!')

'''

# 리스트와 while문을 이용하여 신입생 입력 프로그램 만들기
'''
n = 0
student = []

while True:
    n = n + 1
    number = int(input('학번 : '))
    name = input('이름 : ')
    birth = input('생년월일 : ')
    phone = input('전화번호 : ')
    address = input('주소 : ')
    student.append(f'학번 : {number}, 이름 : {name}, 생년월일 : {birth}, 전화번호 : {phone}, 주소 : {address}')
    print(f'{n}번째 학생 정보 입력 완료!')

    if n == 3:
        print(student)
        break
'''

# 위의 실습을 for문으로 바꾸어 보기
'''
student = [] # 학생 정보를 담을 빈 리스트를 만든다

for i in range(1, 4):  #1번째, 3명까지 입력하도록 반복문을 돌린다

    number = int(input('학번 : '))
    name = input('이름 : ')
    birth = input('생년월일 : ')
    phone = input('전화번호 : ')
    address = input('주소 : ')
    student.append(f'학번 : {number}, 이름 : {name}, 생년월일 : {birth}, 전화번호 : {phone}, 주소 : {address}')
    print(f'{i}번째 학생 정보 입력 완료!{student[-1]}')

print(student)

'''






























