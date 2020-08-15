'''
[5.딕셔너리(Dictionary) 자료형]
    사전~!!

    형태 : {key1:value1,key2:value2....}
        >key와 value는 한 쌍
        key = 단어, value = 뜻

        -문자열 포매팅 함수(format)에서 {키워드} 사용
        "{name}".format(name="한수창")

        -요소가 여러개 나열된 자료형이나
        문자열,리스트,튜플은 '순서'가 있어서 인덱스로 인덱싱
        딕셔너리는 '순서'가 없고,'key'를 가지고 인덱싱

        -주의 사항
        1.key 값은 중복되면 안된다.
        2.key 값으로 리스트,딕셔너리 사용 불가
            >key : 변하지 않는 성질의 자료(값)
            >value: 아무거나 상관 없음
        
'''
print("="*20)
print("{:^20}".format("Dictionary"))
print("="*20)
print("[딕셔너리 만들기]")

my_dict = {"축구":"Soccer",2002:"한일",(1,2):("원","투"),"16강":[2002,2010]}
'''
key       value
"축구"    "Soccer"   문자열 : 문자열
2002      "한일"     정수 : 문자열
(1,2)     ("원","투")튜플: 튜플
"16강"    [2002,2010]문자열 : 리스트

'''
print(my_dict)
print(my_dict["축구"])#key를 통해 value를 얻는다.
print(my_dict["16강"])
print(my_dict["16강"][1])
print(my_dict[(1,2)][0])

print("[딕셔너리 추가,삭제]")
my_dict = {1:"a"}
my_dict[3] = "c"#[]에 key가 들어가고, 그 key의 value를 대입
print(my_dict)
my_dict["16강"] = [2002,2010]
print(my_dict)

del(my_dict["16강"])
print(my_dict)#key는 index 번호처럼 쓰임


my_dict = {"한국":"Korea", "일본":"Japan", "중국":"China"}

korea = my_dict.pop("한국")

print(my_dict)

history = {"강감찬":"귀주대첩", "을지문덕":"살수대첩", "세종대왕":"집현전"}

print('현재 딕셔너리는',history,'입니다.')

history['서희'] = '강동6주'

print('현재 딕셔너리는',history,'입니다.')

history['세종대왕'] = '한글'
print('현재 딕셔너리는',history,'입니다.')

del(history['을지문덕'])
print('현재 딕셔너리는',history,'입니다.')


'''
6.집합(Set) 자료형
    -수학에서의 집합을 의미
        >교집합,합집합,차지합 등을 구할 수 있다.

    -중복된 값을 허용하지 않는다.
        >중복 제거 용도 사용

    -순서가 없다.(인덱싱 불가능)
'''
print("="*20)
print("{:^20}".format("Set"))
print("="*20)

print("[집합만들기]")
my_set = {1,2,3,1,2,3,1,2,3,1,2,3,1,2,1,1,1,2,2,3,3}

print(my_set)

my_set2 = {2,1,1,2,1,"A","B","A","B"}

print(my_set2)

#비슷한 성질의 자료끼리 변환
my_str = "Hello"
my_set = set(my_str)#set() : 집합으로 변환해주는 함수
print(my_set)

#집합에서 특정 값을 인덱싱하고 싶을 경우
#리스트나 튜플로 변환해서 인덱싱

my_list = list(my_set)# set -> list
print(my_list[1])

'''
int() #정수로 변환
float() #실수로 변환
숫자끼리 변환 가능

str()
list()
tuple()
dict()
set()
'''
my_str = str(123123)#정수를 문자 취급하여 문자열로 만듬
print(type(my_str))
my_num = int("123")
print(my_num)
#my_num1 = int("ABCD1234")#숫자가 아닌 문자는 변환 X

my_list = list(my_str)#하나의 문자열이 '문자요소'로 변환
print(my_list)
my_dict = dict(a=10,b=20)
print(my_dict)
print()

#리스트의 요소를 중복제거하고 싶다.
#리스트를 집합으로 변환 -> 다시 리스트로 변환

'''
[7. bool 자료형]
    -(참고)boolean 자료형, C언어 X
    -참(True)와 거짓(False)을 표현하는 자료형

    - 자료형의 값에 따른 참과 거짓

    값         True/False
    ----------------------
    1           True
    0           False
    "11"        True
    ""          False
    [1,2]       True
    []          False
    ()          False
    None        False(함수 진도 나갈 때 자주 볼 예정)

    거짓인 경우는
        1.요소가 없다.(문자열,리스트 등)
        2.숫자는 0이다.(0만 아니면 참)
        3.none : 값이 없다는 걸 의미하는 '자료형/값'

'''
print('[bool 자료형]')
#bool() 함수 : 값이 참인지 거짓인지 판별(값을 bool형으로 변환)
print(bool(0))
print(bool(1))
print(bool(-1))#0만 아니면 참(True)
print(bool([]))#요소가 없다 = 거짓(false)


#bool 자료형은 True/False 2개의 값만 존재
#'조건식'을 다룰 때 나오는 개념


#####################################
#어떤 자료형의 값을 만들 때

#숫자 : 그냥 쓰면 됨
#문자열 : 따옴표(4가지)
#리스트: []
#튜플 : ()
#딕셔너리 : {k:v}
#집합 : {}
#bool : True,False
















 
