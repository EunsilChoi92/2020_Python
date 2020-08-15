# 집합 (set)
'''
집합과 관련된 것을 쉽게 처리하기 위해 만든 자료형
교집합, 합집합, 차집합을 구할 때 편리함
중복 허용되지 않으며, 순서가 없으므로 딕셔너리처럼 인덱싱 불가능

<형식>
집합명 = set([숫자1, 숫자2, 숫자3,.....])
집합명 = set(['문자열1', '문자열2',....])

'''

# 교집합, 합집합, 차집합 구하기
'''
s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print('s1 -->', s1)
print('s2 -->', s2)
print()
print('#교집합')
print(s1 & s2)
print()
print('#합집합')
print(s1 | s2)
print()
print('#차집합')
print(s1 - s2)
print(s2 - s1)

[출력결과]

s1 --> {1, 2, 3, 4, 5, 6}
s2 --> {4, 5, 6, 7, 8, 9}

#교집합
{4, 5, 6}

#합집합
{1, 2, 3, 4, 5, 6, 7, 8, 9}

#차집합
{1, 2, 3}
{8, 9, 7}

'''

# 집합 관련 함수
'''
s3 = set([1, 2, 3])
print('s3 -->', s3)
print('#값 1개 추가하기(add)')
s3.add(4)
print('s3에 4를 추가 후 -->', s3)
print()
print('#값을 여러개 추가하기(update)')
s3.update([5, 6, 7])
print('s3에 5,6,7을 추가 후 -->', s3)
print()
print('#특정 값을 제거하기(remove)')
s3.remove(2)
print('s3에 2를 삭제 후 -->', s3)

[출력결과]

s3 --> {1, 2, 3}
#값 1개 추가하기(add)
s3에 4를 추가 후 --> {1, 2, 3, 4}

#값을 여러개 추가하기(update)
s3에 5,6,7을 추가 후 --> {1, 2, 3, 4, 5, 6, 7}

#특정 값을 제거하기(remove)
s3에 2를 삭제 후 --> {1, 3, 4, 5, 6, 7}

'''

# 함수 (function)
'''
특정 용도의 코드를 한 곳에 모아 놓은 것
거의 한번만 작성해 놓으면 나중에 필요할 때 계속 불러와서 쓸 수 있다.
print, input도 파이썬에서 이미 만들어놓은 함수(내장함수)

함수의 장점 --> 코드의 용도를 구분할 수 있다.
                코드를 재사용할 수 있다.
                실수를 줄일 수 있다.

<형식> 매개변수, 리턴 없는 가장 간단한 형식
def 함수이름():
    수행할 코드

함수이름()

ex)
def hello():
    print('Hello, world!')

hello()
hello()
hello()

'''

# 함수 용어 정리
'''
입력값 : 매개변수, 인수, 인자
출력값 : 반환값, 결과값, 돌려주는 값, return

'''

# 매개변수만 있는 함수
'''
<형식>
def 함수이름(매개변수1, 매개변수2):
    수행할 코드

함수이름(변수1, 변수2)


ex) 매개변수가 2개 있는 함수
def add(a, b):
    print(a + b)

add(10, 20)

x = 3
y = 6
add(x, y)

'''

# 매개변수, 반환값 1개인 함수
'''
<형식>
def 함수이름(매개변수1, 매개변수2):
    return 반환값(결과값)

함수이름(변수1, 변수2)


ex) 매개변수가 2개, 반환값이 1개인 함수
def add(a, b):
    return a + b

print(add(10, 20))

z = add(3, 6) # add 함수를 호출해서 나온 결과값을 z변수에 다시 담음
print(z)

'''

# 매개변수, 반환값이 2개인 함수
'''
<형식>
def 함수이름(매개변수1, 매개변수2):
    수행할 코드
    return 반환값1, 반환값2

함수이름(변수1, 변수2)


ex) 매개변수 2개, 반환값2개인 함수
def add_sub(a, b):
    return a + b, a - b

print(add_sub(10, 20))

x, y = add_sub(3, 6) # 첫번째 결과값을 x에, 두번째 결과값을 y에 담는다
print(x)
print(y)

'''

# 매개변수(입력값)의 개수를 정확히 모를 때 : 가변인자(가변인수)
'''
<형식>
def 함수이름(*args):
    수행할 코드


ex)
def add_many(*args):
    hap = 0             # 합계를 담을 변수 hap을 0으로 초기화한다
    for i in args:      # 매개변수 갯수만큼 반복해서 누적합계 구한다
        hap = hap + i
    return hap          # 결과로 최종 hap을 반환해준다

a = add_many(1, 2, 3)   # 매개변수가 3개인 경우
print(a)

b = add_many(1, 2, 3, 4, 5, 6) # 매개변수가 6개인 경우
print(b)

c = add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10) # 매개변수가 10개인 경우
print(c)


ex)
def add_mul(choice, *args):
    if choice == 'add':         # choice 매개변수가 add라면
        answer = 0              # answer 변수 초기값을 0으로 준다
        for i in args:          # 가변인수 args의 개수만큼 반복
            answer = answer + i  # 누적합계
    elif choice == 'mul':       # choice 매개변수가 mul이라면
        answer = 1              # answer 변수 초기값을 1으로 준다(0으로 하면 결과가 0이되므로)
        for i in args:   
            answer = answer * i
    return answer               # 결과가 나온 answer을 반환한다

a = add_mul('add', 1, 2, 3)     # 가변인수 3개인 경우 함수 호출
print(a)

b = add_mul('mul', 1, 2, 3, 4)  # 가변인수 4개인 경우 함수 호출
print(b)


'''


# 키워드 인수(인자, 매개변수) 사용하기
'''
각각의 인수(매개변수)가 무슨 용도인지 알기 어려울 때 사용


ex)
def info(name, age, address):
    print('이름 :', name)
    print('나이 :', age)
    print('주소 :', address)
    print()

info('라이언', 20, '대구') # 일반적인 형식
info(name='어피치', age=30, address='서울') # 키워드로 지정
info(age=40, address='부산', name='무지')   # 키워드로 지정(순서를 다르게 해도 된다)

'''

# 파일 입출력
'''
<파일 열기모드의 종류>
r : 읽기 모드 --> 파일을 읽기만 할 때 사용
w : 쓰기 모드 --> 파일에 내용을 쓸 때 사용(이미 내용이 있는 파일에 쓰면 기존 내용이 다 사라짐)
a : 추가 모드 --> 파일의 마지막에 새로운 내용을 추가할 때 사용


<형식> 파일 생성하고 문자열 쓰기 (기본방법)
파일객체명 = open(파일이름, 파일 열기 모드)
파일객체명.write('문자열')
파일객체명.close()

<형식> 파일 생성하고 문자열 쓰기 (리스트 사용)
리스트명 = [문자열1, 문자열2, 문자열3,....]
파일객체명 = open(파일이름, 파일 열기 모드)
파일객체명.writelines(리스트명)
파일객체명.close()


ex)
file = open('hello.txt', 'w')  # hello.txt 파일을 생성해서 열기
file.write('Hello, python!!')  # 파일에 문자열 쓰기
file.close()                   # 파일 닫기

'''

# for문을 이용해서 파일에 문자열 쓰기
'''
f = open('hello.txt', 'w')
for i in range(1, 11):
    data = f'{i}번째 줄입니다!!\n'  # \n : 엔터(이스케이프 코드)
    f.write(data)  # write함수는 엔터기능이 없다
f.close()

'''

# for문을 이용해서 파일에 새로운 내용을 추가하기
'''
f = open('hello.txt', 'a')
for i in range(11, 21):
    data = f'{i}번째 줄입니다.\n'
    f.write(data)
f.close()

'''

# 파일에서 문자열 읽기
'''
<형식>
파일객체명 = open(파일이름, 파일 열기 모드)
변수명 = 파일객체명.read()
파일객체명.close()


ex)
f = open('c:/a/hello.txt', 'r')  # 절대주소 : c드라이브 안 a폴더 안 hello.txt파일
a = f.read() # 변수에 파일에서 읽은 내용을 담는다
f.close()
print(a)

'''

# 파일에서 여러줄을 리스트로 각각 읽기
'''
<형식>
파일객체명 = open(파일이름, 파일 열기 모드)
리스트명 = 파일객체명.readlines()
파일객체명.close()

ex)
f = open('hello.txt', 'r')
lines = f.readlines()   # 파일에서 읽은 내용을 리스트로 저장
f.close()

print(lines)            # 리스트형식인 확인하려고 넣은 코드

for i in lines:         # 여러 줄을 한 줄씩 차례로 출력
    print(i, end='')    # print함수에 포함되어 있는 엔터기능을 없앰(end='')

'''

# with문과 함께 파일 입출력하기
'''
파일을 열면 항상 close 해주어야 하는 불편함을 덜어주는 기능

<형식>
with open(파일이름, 파일 열기 모드) as 파일객체명:
    수행할 코드

ex)
a = ['Hello~\n', 'world!!\n', 'goodbye~~\n', 'python!!\n']
with open('file.txt', 'w') as f:
    f.writelines(a)        # 리스트형식
    f.write('ㅋㅋㅋㅋ\n')
    f.write('메롱~~!\n')
    f.write('파이썬 재밌어!!')

'''


















