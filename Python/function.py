'''
[함수 Fuction](메서드 : 같은 말)
    -특정 작업을 수행하는 일련의 문장들을 하나로 묶은 것

    -함수의 장점
        1. 한 번 만들어놓으면 언제든지 재사용 가능
        2. 중복된 코드 제거
        3. 프로그램의 구조화
            > 작업 단위로 코드를 묶어서 구조화 시킨다

    [함수의 기본 구조]

    def 함수이름(매개변수) : def = define(정의하다)
        수행문
        수행문
        return 반환값

    1. 매개변수(Parameter)
        -(필요시) 함수가 호출될 때 값을 받는 변수
        -개수 제한이 없고, 필요 없으면 생략도 가능
        -우리가 함수를 호출할 때 전달하는 '값'을 인수라고 부른다.

    2. 반환값
        -return 뒤에 오는 값은, 함수의 수행이 완료되고 되돌려 주는 값
        -return 을 사용하면 수행이 끝난다.
            >마치 반복문에서 break를 사용한 것과 느낌이 비슷

    >>>매개별수와 반화 값의 유/무에 따른 함수형태(4가지)
        1.매개변수와 반환값이 둘 다 있다.
        2.매개변수와 반환값이 둘 다 없다.(기능수행만 한다.)
        3.매개변수만 있다.
        4.반환값만 있다.
        >만드는 함수에 목적에 따라 알아서 결정
         
'''
print("[함수]")

def f(x):
    return x+5
#함수는 define(정의)만으로는 프로그램 수행 영향 X
#함수를 정의한다 = 이후 이 함수를 언제든 사용할 수 있도록 준비

result = f(10)
print(result)
print("result :",f(10))

print("[함수의 4가지 형태]")
#1.매개변수,반화값이 둘다 있다.
def add(a,b) :
    return a + b

#add 함수 매개변수가 2개 --> 사용할려면 값을 2개 전달 필요
result = add(1,2)
print("{} + {} = {}".format(1,2,result))
print("{} + {} = {}".format(3,4,add(3,4)))
#반화값이 있는 함수를 호출 헀을 때는
#함수의 기능수행이 끝난 뒤 반환 값을 들고 온다.
#(1)add(1,2)는 함수의 반화 값인 3으로 대체된다 -> 변수 대입
#(2)add(3,4) --> 7로 대체된다 - > format()에서 사용됨

#2.매개변수,반환 값 둘 다 없다.
def sayHo():
    print("Ho~~~~~!")
    print("Ho!!Ho!!")

print("sayHo 호출 전")
sayHo()
print("sayHo 호출 후")
#함수를 호출하면, 코드의 흐름이 내가 호출한 함수의 수행문으로 '점프'
#함수의 수행문이 끝나면, '함수를 호출했던 원래 위치로 돌아온다.
#단 return 반환값이 있다면 그 값을 들고온다.

result = sayHo()
print("sayHo()의 결과값1 : ",result)
print("sayHo()의 결과값2 : ",sayHo())
#매개변수에 따라 함수를 '호출'할 때는 그 규칙을 맞춰줘야 한다
#'반환 값'에 따라서는 규칙에 맞추지 않아도 사용은 가능한다.
#반환값이 있다 = 그 값을 변수에 대입, 그값을 어딘가에 바로 사용

#반환 값이 없는 함수는 그냥 호출만 하기
#변수에 대입하거나 어딘가에 사용을 하면 None이라는 값이다.

#3.매개변수만 있다.
def say(talk):
    print(talk)

say("hohohohoho")
print()
#4.반환값만 있다.
def getHo():
    return "Ho! Ho! Ho!"
'''
ho = getHo()
print(ho)
print(getHo())

def add(x,y):
    return x + y
def sub(x,y):
    print("{} - {} = {}".format(x,y,x-y))
a = add(10,20)
print(a)
sub(10,20)

grade = input("회원 등급 입력 : ")
price = int(input("가격 입력 : "))

def solution(grade,price):
    answer = 0
    if grade == 'S' :
        answer = int(price * 0.05)
    if grade == 'G' :
        answer = int(price * 0.1)
    if grade == 'V' :
        answer = int(price * 0.15)
    else:
        print("할인율 X")

    return answer

print(solution(grade,price),"원입니다.")

'''
#return 뒤에 오는 값의 자료형에 따라 반환된 결과도 그 자료형이 된다.

#여러 값 반환하기 -거짓말
print("[여러값 반환하기]")

def calc(a,b):
    return a+b,a-b,a*b,a/b #여러개 처럼 보이지만 '튜플'

print(calc(10,3))
print(type(calc(10,3)))

a,b,c,d = calc(10,3)
print(a,b,c,d)

#매개변수에 초기값 사용
def print_info(name,age,phone="010-xxxx-xxxx"):#이름,나이,번호를 매개변수 전달 받고 출력
    print("이름 :",name)
    print("나이 :",age)
    print("번호 :",phone)

print_info("홍길동",20,"010-1111-2222")
print_info("임꺽정",30,"010-2222-3333")
print_info("성춘향",18)

#3번째 매개변수(초기값 사용)에 값을 주면 내가 준 값:
#값을 주지 않으면 초기값

#매개변수에 초기값을 사용하려면 초기 값이 적용된 매개변수는 맨 뒤에 위치

print()
#키워드 인수 : 함수의 매개변수명을 키워드로 사용
def print_info(name,age,phone):
    print("이름 :",name)
    print("나이 :",age)
    print("번호 :",phone)

print_info("홍길동",20,"010-1111-2222")
print_info("임꺽정",30,"010-2222-3333")
print_info(age=19,name="성춘향",phone="112")
#print() 함수 호출 시 sep나 end에 값을 넣는 행위(키워드 인수)

#가변인수
#전달하는 값의 개수가 변할 수 있다.
#함수를 만드는 입장에서 변할 수 있는 값들을 처리

def add(*args):#arguments : 인자들
    add_result = 0
    for i in args :
        add_result += i

    return add_result

print(add(1,2))
print(add(1,2,3,4))
print(add(1,2,3,4,5,6,7,8,9,10))
#print()함수도 값을 몇 개 전달하더라도 다 출력한다.
#일반 매개변수,가변인수를 혼용할 때 *args는 마지막에 위치

#초기값이 지정된 매개변수나,가변인수 *args는 뒤에
#>두개 혼용 X
'''
def func(*args, sep = ' ',end='\n'):
    for i in args :
        print(i)
func(1,2,3,4,sep='',end='')
'''




'''
    4. 소수 출력하기
        1부터 입력 받은 수까지 소수(PrimeNumber)만 출력하기
            > 소수 : 1과 나 자기자신 숫자로만 나누어떨어지는 수
                11 = 소수
                10 = 소수 아님 (2,5로도 나누어떨어짐)

        함수의 순기능 : 전달된 1개의 숫자가 소수인지 아닌지 판별하여 반환
            소수이면 True 반환
            소수가 아니면 False 반환
                is_prime_number(11) 호출하면 반환 값은 True
                is_prime_number(10) 호출하면 반환 값은 False

            > 1은 소수가 아님
            
        [출력결과]
        숫자 입력 : 20
        소수 : 2 3 5 7 11 13 17 19
'''
def is_prime_number(num):
    if num == 1 :
        return False
    for i in range(2,num):
        if i % num == 0 :
            return False

    return True

'''
num = int(input("숫자 입력 : "))

for i in range(2,num+1):
    if is_prime_number(i) :
        print(i,end=' ')

'''
for i in range(2,101):
    chk = True
    for j in range(2,i):
        if i%j==0:
            chk = False
            break
    if chk :
        print(i,end=' ')


'''
[문제] 

정수 리스트들을 리스트로 받아서 중첩 리스트의 모든 요소를 더하는 nested_sum 함수를 작성하라.
ex) 리스트 t = [[1, 2], [3], [4, 5, 6]


[출력결과]
리스트 t :  [[1, 2], [3], [4, 5, 6]]
result :  21

'''
def nested_sum(t) :
    total = 0
    for nasted in t:
        total += sum(nasted)
    return total


t = [[1, 2], [3], [4, 5, 6]]
result = nested_sum(t)

print('result : ',result)


def func3():
    print("func3()시작")#7
    print("func3()끝")#8
def func2():
    print("func2()시작")#5
    func3()#6,9
    print("func2()끝")#10
def func1():
    print("func1()시작")#3
    func2()#4,11
    print("func1()끝")#12

print("func1() 호출전")#1
func1()#2,13
print("func1() 호출전")#14

#재귀함수
'''
-함수의 수행문 안에서 나 자기 자신을 다시 호출하는 함수
-수행문 반복되기 때문에 반복문과 유사한 성격
-너무 많이 반복 수행하다 보면 프로그램 오류 발생
-함수 호출 시 'stack' 이라는 구조의 메모리 사용
    Queue : First in First out(FIFO) - 입구/출구 따로
    Stack : First in Last out (FILO) - 출입구 하나

재귀함수도 반복문 반복 호출이 끝날 수 있는 조건이 필요

'''

def func(num):
    print("func() 시작, num =",num)

    if num == 1:
        print("num 1일 때 끝")
        return#함수에서 반환값 없이 return 쓰면 함수 끝

    func(num - 1)#내 함수를 다시 호출 = 재귀호출
    print("func()끝, num =",num)

func(3)


'''
지역변수와 전역변수
    지역변수 : 특정 지역에서만 사용가능한 변수
    전역변수 : 전체 영역에서 사용가능한 변수
        >여태 전역변수만 사용

    
'''
value = "전역변수" #어느 수행문에서 속하는 않는 위치

def func1():
    print("func1()호출")
    print(value)
    #전역변수는 어디서든 접근 가능
def func2():
    print("func2()호출")
    value_func2 = "지역변수"
    print(value_func2)

    value = "지역변수로 변경"

def func3():
    print("func3() 호출")
    global value_func3
    value_func3 = "func3의 지역변수"
    #지역변수를 전역변수로 만드는 명령어
    print(value_func3)
    
'''
value라는 전역변수가 이미 있는데
지역에서 value에 값을 대입하게 되면
전역변수 value에 값이 변경되는게 아니라
같은 이름으로 이 지역의 value 지역변수가 생성
 '''
print(value)

func1()
func2()

print(value)

#print(value_func3)
#print(value_func2)#func2에만 존재하는 지역변수
func3()
print(value_func3)































