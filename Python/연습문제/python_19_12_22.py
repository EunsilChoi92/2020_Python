# 연산자 (operator) : 연산을 하는 기호

# 산술 연산자
'''
더하기 +
빼기 -
곱하기 *
나누기 /  --> 결과가 실수형
몫 //
나머지 %
제곱 **


print(2 + 5 / 2)
print(5 / 2)
print(5 % 2)
print(5 // 2)
print(5 ** 3)
print(4 + (2 ** 3) + 1)


'''

# 비교 연산자
'''
크다 >
작다 <
크거나 같다 >=
작거나 같다 <=
같다 ==
같지 않다 !=

'''

# 논리 연산자
'''
참 True
거짓 False
아니다(반대, 논리부정) not
그리고(둘 다 참인 경우만 True, 논리곱) and
또는(둘 중 하나라도 참이면 True, 논리합) or


ex)
n = 10
print('n은 20보다 작나요??', n < 20)
print('n은 20보다 작지 않나요??(20보다 크거나 같나요??)', not (n < 20))

a, b = 100, 200
print(a == b, a != b, a > b, a < b, a >= b, a <= b)

'''

# input() : 값을 입력받는 함수
'''
명령프롬프트에서 사용자로부터 데이터를 입력받을 때 사용
모든 값의 자료형이 문자형(string)으로 정의됨
숫자로 받고 싶을 때는 int(input()) 또는 변수 = int()


ex)
a = input('아무 숫자나 입력하세요 : ')
print(a)


ex)
s = input('입력 : ')
print('변수s의 자료 : ', s)
print('변수s의 자료형 : ', type(s))
print('변수s의 자료(int붙임) : ', int(s))
print('변수s의 자료형(int붙임) : ', type(int(s)))


ex)
s = int(input('입력 : '))
print('s + 100 = ', s + 100)



ex)
s1 = input('입력 s1 : ')  # 문자형으로 입력됨
s2 = input('입력 s2 : ')
print(s1, s2)
print(s1 + s2)  # 문자형이니까 두 문자를 이어붙임
print()
i1 = int(input('입력 i1 : '))  # 문자형으로 입력된 것을 정수형으로 변환
i2 = int(input('입력 i2 : '))
print(i1, i2)
print(i1 + i2)  # 정수형이니까 더하기 계산

[출력결과]
입력 s1 : 12
입력 s2 : 34
12 34
1234

입력 i1 : 12
입력 i2 : 34
12 34
46

'''

# int : 정수형
# float : 실수형
'''
num1 = float(input('실수로 된 첫번째 숫자 : '))
num2 = float(input('실수로 된 두번째 숫자 : ')) # 정수를 입력해도 실수형으로 변수에 저장

print('덧셈 결과 : ', num1 + num2) 
print('뺄셈 결과 : ', num1 - num2)
print('곱셈 결과 : ', num1 * num2)
print('나눗셈 결과 : ', num1 / num2)

'''

# 복합대입연산자

# a가 10에서 시작해 프로그램이 진행될수록 값이 누적되도록 해보기
'''
a = 10
a += 5; print(a) # a = a + 5 ---> 10 + 5 = 15
a -= 5; print(a) # a = a - 5 ---> 15 - 5 = 10
a *= 5; print(a) # a = a * 5 ---> 10 * 5 = 50
a /= 5; print(a) # a = a / 5 ---> 50 / 5 = 10.0(실수형)
a //= 5; print(a) # a = a // 5 ---> 10.0 // 5 = 2.0
a %= 5; print(a) # a = a % 5 ---> 2.0 % 5 = 2.0

'''

# 문자열로 복합대입연산자 사용해보기
'''
s = '안녕하세요'
print('원본 s : ', s)
s += '!' # s = s + '!'
print('! 하나 추가 : ', s)
s += '!'
print('! 하나 더 추가 : ', s)
s += '!'
print('! 하나 더더 추가 : ', s)

'''

# input을 이용해서 한 번에 값을 여러 개 입력 받기
'''
<형식>
변수1, 변수2 = input().split()

ex)
a, b = input('문자열 두 개를 입력하세요 : ').split() # 공백을 기준으로 a, b변수에 각각 입력받음
print(a)
print(b)

ex)
c, d = input('문자열 두 개를 입력하세요 : ').split(',') # 콤마(,)를 기준으로 각각 입력받음
print(c)
print(d)

ex)
e, f = input('숫자 두 개를 입력하세요 : ').split(', ') # 콤마와 공백으로 분리
e = int(e)  # 정수로 변환
f = int(f)
print(e)
print(f)
print(e + f)

[출력결과]
숫자 두 개를 입력하세요 : 10, 20
10
20
30

'''

# map 함수를 이용하여 한 번에 값을 여러 개 입력 받기
'''
<형식>
변수1, 변수2 = map(int, input().split())


ex)
a, b = map(int, input('1-숫자 두 개를 입력하세요 : ').split())
print('두 수를 더하면?? ', a + b)

c, d = map(int, input('2-숫자 두 개를 입력하세요 : ').split(','))
print('두 수를 더하면?? ', c + d)


'''

# 문자열 관련 함수와 메서드
'''
a = 'Life is too short'
print(len(a))  # 문자열 길이 구하기(빈칸 포함) --> len (중요!!)

b = 'victory'
print(max(b))  # 가장 큰 숫자나 알파벳 순서 상 가장 뒤에 나오는 문자 --> max
print(min(b))  # 가장 작은 숫자나 알파벳 순서 상 가장 앞에 나오는 문자 --> min

c = 'my python'
print(c.title()) # 제목(첫글자를 모두 대문자로 쓰는 형식) --> title
print(c.upper()) # 모두 대문자로 --> upper

d = 'MY PYTHON'
print(d.lower()) # 모두 소문자로 --> lower

e = 'hobby'
print(e.count('b')) # 문자 개수 세기 (b의 개수) --> count

f = 'Python is the best choice'
print(f.find('b'))  # 문자열 중에서 문자가 처음으로 나온 위치를 반환(b가 몇번째있는가) --> find
print(f.find('k'))  # 찾는 문자가 존재하지 않는다면 -1이 출력

print(f.index('o')) # 문자열 중에서 문자가 처음으로 나온 위치를 반환 --> index
print(f.index('k')) # 찾는 문자가 존재하지 않는다면 에러 발생


print(','.join('abcd')) # 문자열 삽입 --> join
a = 'aaa'
print(a.join('bbbbbbb'))

a = '    python     '
print(a.lstrip())  # 왼쪽 공백 지우기 --> lstrip()
print(a.rstrip())  # 오른쪽 공백 지우기 --> rstrip()
print(a.strip())   # 양쪽 공백 지우기 --> strip()

a = 'Life is too short'
print(a.replace('Life','Your leg'))  # 치환(단어바꾸기) --> replace

print(a.split()) # 문자열 나누기(리스트 자료형으로 출력) --> split
b = 'a:b:c:d'
print(b.split(':'))

'''

# in 연산자
'''
문자열 내부에 어떤 문자열이 있는지 확인할 때 사용
결과는 True(참), False(거짓)으로 출력됨

ex)
print('안녕' in '안녕하세요')
print('메롱' in '안녕하세요')

'''


























