'''
    [Object Oriented Programming] - 객체지향 프로그래밍
       객체 지향 이론
           -실제세계는 사물(객체)로 이루어져 있으면
           발생하는 모든 사건들은 사물(객체)간의 상호작용

            이 개념을 토대로 프로그래밍 언어 접목 ->객체지향 프로그래밍

        특징
            1. 코드 재사용성이 높다.
            2. 코드 관리하기 편한다.
            3. 프로그램의 신뢰성이 높아진다.

        클래스 와 객체
            1.클래스는 일종의 설계도(또는 틀) 이며
            객체는 이 설계도를 통해 만들어진 실제 사물
                >아이폰8 설계도 ->아이폰(s/n :1)

            2.클래스
                정의 : 객체를 정의해 놓은 것
                용도 : 객체를 생성

            3.객체
                정의 : 실제로 존재하는 것
                용도 : 클래스 정의된 대로 사용한다.

            객체/인스턴스
                1.인스턴스 : 사례,경우,실체
                    -기본적으로 객체와 같은 의미
                    -문장의 쓰임에 따라 구분
                    >클래스를 통해 실제로 만들어진 객체를 인스턴스

                객체의 구성 요소 : 속성,기능
                (속성 : 색상,크기 등 , 기능 : 찍다,걸다,끄다 등)

                1.객체는 클래스에서 정의한 다수의 속성과 기능 가질 수 있다.
                2.속성 : 변수
                3.기능 : 함수
                
            
'''
print("[OOP]")
'''
1. 클래스는 속성(변수)를 정의하거나 기능(함수)를 정의 할 수 있다.
    >함수와 마찬가지로 클래스도 작성만으로는 프로그램 수행영향 X
    >객체(인스턴스)를 생성한 뒤부터 클래스에 작성된 효력 발생

2.클래스 안에 정의된 함수는 '메서드'라고 부른다
    >메서드 생성시 반드시 최소 하나의 매개변수 필요
    >나 자기 자신을 의미하는 self라는 이름으로 한다.
'''
class Car:#자동차 설계도
    def power_on(self):#self에는 bmw(이 메서드를 호출한 인스턴스)대입
        print("부릉부릉~")
        self.power = True
        #bmw인스턴스에 power 변수추가
        
        self.drive()#bmw.drive()

    def drive(self):
        print("주행시작")
    
#인스턴스 생성
bmw = Car() #변수명 = 클래스명() ->Car 클래스의 객체 생성
bmw.power_on()
bmw.power =False
print("시동 여부 :",bmw.power)

#클래스에 여러 속성/기능을 정의 해두고 인스턴스라는 하나의 단위로
#묶어서 다루겠다.

tico = Car()#위에 있는 bmw와는 별개의 인스턴스
tico.power_on()
#tico.power = "시동켜짐"
print("시동여부 :",tico.power)

tico.model = "Tico 최신모델"

#print("bmw 모델 :",bmw.model)

#Python 객체의 특징 : 만들어지는 인스턴스별로 속성이 다를 수 있다.

#1.클래스는 왜?

#클래스 없이 자동차 2대를 다루기

car1_model = "BMW"
car1_power = True
car1_max_speed= 200

car2_model = "SONATA"
car2_power = False
car2_max_speed= 180

def drive_car(model,power,max_speed,speed):
    print("{} 주행 준비...".format(model))

    if power == False:
        print("주행불가 : 시동을 켜주세요")
        return
    if speed > max_speed:
        print("{}의 최고 속도는 {}km입니다.속도를 줄여요".format(model,max_speed))
        speed = max_speed

    print("{}km 로 주행합니다~~~~".format(speed))

drive_car(car1_model,car1_power,car1_max_speed,150)
drive_car(car2_model,car2_power,car2_max_speed,200)
        
#1)각 변수들은 서로 전혀 연관성이 없다
#2)함수를 호출할 때 일일이 매개변수로 모든 값을 전달

#2.클래스의 사용(1)

#하나의 틀을 만들고, 그 틀로 자동차를 생성
class Car:
    def drive_car(self,speed):
        print("{} 주행 준비...".format(self.model))

        if self.power == False:
            print("주행불가 : 시동을 켜주세요")
            return

        if speed > self.max_speed:
            print("{}의 최고 속도는 {}km입니다.속도를 줄여요".format(self.model,self.max_speed))
            speed = self.max_speed

        print("{}km 로 주행합니다~~~~".format(speed))


car1 = Car()
car2 = Car()

car1.model = "BMW"
car1.power = False
car1.max_speed = 200

car2.model = "Sonata"
car2.power = True
car2.max_speed = 180

car1.drive_car(180)
car2.drive_car(200)

#drive_car 호출 시 정의된 매개변수는 2개 이다
#self에는 자동으로 호출하는 인스턴스가 대입
#그 뒤 매개변수부터는 호출할 때 값을 전달 해야 한다.

#1) 인스턴스라는 하나의 변수에 모든 속성을담아놨다,연관성이 생김
#2) 함수를 호출 할 때 그냥 호출해도 self에 인스턴스가 대입되므로
#함수의 수행문 안에서 self.~~~ 호출한 인스턴스 속성들을 사용 가능

#3.클래스의 사용(2) - 생성자
# 생성자
# 1.인스턴스 생성 시 자동으로 호출되는 메서드 ---무조건 호출
# 2.목적 : 인스턴스 생성과 동시에 속성을 추가/초기값 지정이 필요한 경우
# 3.생성자 함수의 이름(규칙) : __init__(언더바 2개)

class Car:
    def __init__(self,model):
        print("생성자 호출")
        #self.model = "모델명 미정"
        self.model = model
        #self.model 코드 : self(나 자기 자신 인스턴스)에 모델 속성 추가
        # = model 모드 : 매개변수로 전달받은 model 값

car1 = Car("SONATA")#인스트턴스 생성코드 -> 생성자함수 호출해라
#생성자 함수가 호출 되고나서 인스턴스가 생성
print(car1.model)

car2 = Car("Kona")
print(car2.model)
#생성자 함수를 이용하면 모든 인스턴스가 공통적으로 지녀야할 속성 생성 가능

#4.클래스의 사용(3) - 생성자 활용

class Car:
    def __init__(self,model,power,max_s):
        print("[{}]인스턴스가 생성됩니다.".format(model))
        self.model = model
        self.power = power
        self.max_speed = max_s
        
    def drive_car(self,speed):
        print("[{}]주행 준비...".format(self.model))

        if self.power ==False :
            print("주행 불가 : 시동을 켜주세요")
            return
        if speed > self.max_speed:
            print("{}의 최고 속도는 {}km입니다.속도를 줄여요".format(self.model,self.max_speed))
            speed = self.max_speed

        print("{}km 로 주행합니다~~~~".format(speed))
    
        
car1 = Car("BMW",False,200)

# 클래스 연습하기
'''
    1. 학생 클래스 만들기 (Student)
        속성(변수) : 이름(name), 나이(age), 전화번호(phone), 과목(sub)
        기능(함수)
            1. 생성자 __init__
                > 매개변수로 이름,나이,전화번호,과목을 전달 받고, 각 속성 생성 및 대입
            2. 정보 출력 (print_info)
                > 객체에 만들어져 있는 이름,나이,전화번호 를 출력
                    이름 : 홍길동
                    나이 : 20세
                    전화번호 : 010-1234-5678
            3. 공부하기 (study)
                > 객체에 만들어져 있는 이름,과목 출력
                    홍길동 님이 파이썬 공부를 시작합니다.

        - 학생 3명 만들어서 '정보출력', '공부하기' 메서드를 호출해서 출력 결과 확인
            hong.print_info() <-- 이런거 하자는 얘기
'''
class Student:

    def __init__(self,name,age,phone,sub):
        self.name = name
        self.age = age
        self.phone = phone
        self.sub = sub

    def print_info(self):
        print("이름 :",self.name)
        print("나이 :",self.age)
        print("번호 :",self.phone)

    def study(self):
        print("{}님이 {}공부를 시작하였습니다.".format(self.name,self.sub))

hong = Student("홍길동",20,"1234","파이썬")
hong.print_info()
hong.study()

Lim = Student("임꺽정",20,"1234","파이썬")
Lim.print_info()
Lim.study()

#변수와 메서드(함수)의 종류
'''
-클래스 변수
    1.클래스 내부 코드 생성
    2.클래스 메서드에서 생성
    3.클래스 코드 바깥에서 클래스 명을 통해서 생성
    
-인스턴스 변수
    1.생성자 생성
    2.인스턴스메서드에서 생성
        >해당 인스턴스 메서드를 호출한 인스턴스만 생성
    3.클래스 코드 바깥에서 인스턴스명을 통해서 생성
        >해당 인스턴스에만 생성

    클래스 변수는 한 번 만들어지면 '클래스'나 '인스턴스'가 접근 가능
    인스턴스변수는 인스턴스 별로 독립적으로 생성

    클래스 메서드
        -클래스나 인스턴스가 호출 가능
    인스턴스 메서드
        -인스턴스를 통해서만 호출 가능
'''

class Car :#클래스 정의 여역
    engine = "1000cc"#클래스 변수

    def instMethod(self):
        print("인스턴스 메서드")

    @classmethod#장식자(데코레이터) :이게 있어야 클래스 메서
    def clsMethod(cls):#cls = class
        print("클래스 메서드")
        cls.clsValue = "클래스변수" #cls 매개변수는 Car가 대입(Car.carValue)

print(Car.engine)#클래스명.클래스변
#클래스 메서드 호출 - > 클래스명.클래스메서드명()
Car.clsMethod()#인스턴스 생성 없이 호출 가능


car1 = Car()
car1.clsMethod()
print(car1.engine)

print(Car.clsValue)
#인스턴스를 통해 클래스 메서드, 클래스 변수 '사용 가능'

car1.instMethod()
#Car.instMethod()#인스턴스 메서드는 '반드시'인스턴스를 통해서 호출

car1.sunRoof = "썬루프 옵션 추가"
print(car1.sunRoof)

#print(Car.sunRoof)
#클래스 명으로는 인스턴스 메서드,인스턴스 변수 '사용 불가'

Car.wheel = 4#클래스 변수 추가 생성
print(car1.wheel)#인스턴스가 클래스 변수 사용 가능

#6.외부 접근 제어
'''
외부 = 클래스가 정의된 코드 바깥
public : 외부 접근 허용 - 이름 지을 때 그냥 지으면됨 (변수/메서드)
private : 외부 접근 차단 - 이름 지을 __(언더바 2개)를 붙이면 됨

'''

class Person :
    name = "이몽룡" # 클래스 변수,public
    __addr = "서울시 강남구" #클래스 변수,private

    def print_info(self):
        print("{}님은 {}에 거주합니다.".format(self.name,self.__addr))

    def __print_info2(self):
        print("{}님은 {}에 거주합니다.".format(self.name,self.__addr))
    def print_info3(self):
        self.print_info()#다른 public 메서드를 통한 private 메서드 우회 접근
        self.print_info2()

lee = Person()
print(lee.name)
#print(lee.__addr)#클래스 바깐 코드에서 접근 할 수 없는 private 변수

lee.print_info()
#lee.print_info2()#이 메서드도 private

lee.__addr = "서울시 서초구"
print(lee.__addr)#lee 인스턴스에 __addr 속성이 추가됨(클래스 변수와 별개)



'''
    2. 계산기 클래스 (Calc)
        속성 : 각 사칙연산의 계산(기능)이 수행된 횟수를 누적
                add_count, min_count, mul_count, div_count

        기능
            1. 생성자 __init__
                > 속성 만들기  (생성자에서 속성을 만든다 = 모든 인스턴스가 공통적으로 속성을 가진다.)
            2. 각 사칙연산을 계산하는 메서드 4개
                > 계산하고 싶은 2개의 값을 전달 받고, 계산 결과를 출력 (반환 X)
                    1 + 2 = 3
            3. 정보 출력(print_info)
                > 각 계산의 수행 횟수 출력

        ex) 덧셈 함수 3번 호출, 나눗셈 함수 2번 호출 후 print_info를 호출하면,
            1 + 2 = 3
            2 + 5 = 7
            10 / 2 = 5.0
            10 / 2 = 5.0
            3 + 9 = 12
            덧셈 : 3
            뺄셈 : 0
            곱셈 : 0
            나눗셈 : 2
'''


class Calc:
    def __init__(self):
        self.addCount = 0
        self.minCount = 0
        self.mulCount = 0
        self.divCount = 0

    def add(self,num1,num2):
        self.addCount +=1
        print("{}+{}={}".format(num1,num2,num1+num2))

    def print_info(self):
        print("덧셈 :",self.addCount)
        

'''
        3.  (1) MyData 라는 클래스를 만들고
            (2) 외부에서 접근 불가능한 인스턴스 변수를 만들기. (정수!)
            (3) 외부에서 접근 불가능하기 때문에 해당 변수에 값을
                저장하려면, 메서드를 통해 값을 저장해야 합니다.
                 --> 어떤 방법을 이용해도 무관 (클래스 내부에서만 하면 됨)
            (4) 변수가 가질 수 있는 값의 범위는 1~10 이며,
                더 작은 값을 저장하려고 시도하면 1로,
                더 큰 값을 저장하려고 시도하면 10으로 저장
                 (1~10의 값을 저장하려고 하면 그대로 저장)
            (5) 2번에서 만든 변수의 값을 출력하는 메서드를 생성
            (6) 값이 제대로 들어갔는지 확인해보기
'''

class MyData :

    def __init__(self,data):
        if data < 1:
            self.__data = 1
        elif data > 10:
            self.__data = 10
        else :
            self.__data = data

    def print_data(self):
        print(self.__data)

data1 = MyData(2)
data1 = MyData(-10)
data1 = MyData(20)
data1.print_data()


#7.상속
'''
    -무언가를 물려받는다.
    -클래스 상속
        기존에 정의해놓은 클래스의 기능을
        그대로 물려받는 새로운 클래스를 정의
    -기반클래스 : 부모클래스,슈퍼클래스
    -파생클래스 : 자식클래스,서브클래스

    -자식클래스에서는 부모클래스의 변수,메서드를 사용 가능

    [오버라이딩](재정의)
        -부모클래스에 정의된 메서드를 무시하고
        자식클래스에서 같은 이름의 다시 정의한다.
    
'''
#부모클래스
class Person :
    def __init__(self,name,age):
        print("Person,생성자")
        self.name = name
        self.age = age

    def print_info(self):
        print("Person,print_info")
        print("이름 :",self.name)
        print("나이 :",self.age)

    def sleep(self):
        print("Person,print_info")
        print(self.name+"님은 8시간 잡니다.")

class Student(Person):#상속받은 클래스를 () 안에 적는다.
    def study(self):
        print("Student, study")
        print(self.name+"학생은 6시간 공부합니다.")

    def sleep(self):
        print("Student,Sleep")
        print(self.name+"님은 6시간 잡니다.")

class Teacher(Person) :
    
    def __init__(self, name, age) :
        print("Teacher, 생성자")
        super().__init__(name, age) # 부모클래스 생성자 호출
        # 더 명확하게 호출하기. 위와 똑같다.
        # super(Teacher, self).__init__(name, age)

    def sleep(self) :
        print("Teacher, sleep")
        super().sleep()
        #super().메서드() --> 부모클래스의 메서드 호
        print( "선생님은 그렇게 많이 자면 안 됩니다.." )

    def work(self) :
        print("Teacher, work")
        print( self.name + " 선생님은 6시간 일합니다." )

        
person = Person("홍길동",20)
person.print_info()
person.sleep()

student = Student("성춘향",18)
student.print_info()
student.sleep()

teacher = Teacher("이몽룡",32)
teacher.sleep()



'''
        4. 책을 의미하는 Book 클래스
           전자책을 의미하는 EBook 클래스
        
            Book
                변수 : 제목, 정가
            EBook
                변수 : 보안키

    20000원짜리 "파이썬 최고" 책 1권
    15000원짜리 "파이썬 최고 - ebook" 전자책 1권 (보안키 1234)

            각각 인스턴스를 생성하여 정보 출력하기
            print_info()를 오버라이딩하고, super()를 활용하기
'''
class Book:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def print_info(self):
        print("이름 :",self.name)
        print("가격 :",self.price)

class EBook(Book):
    def __init__(self,name,price,key):
        super().__init__(name,price)
        self.key = key
    def print_info(self):
        super().print_info()
        print("보안키 :",self.key)

book = Book("파이썬최고",20000)
book.print_info()

ebook = EBook("파이썬 최고 - ebook",15000,1234)
ebook.print_info()
'''

        5. 사각형을 의미하는 Rectangle 클래스
           정사각형을 의미하는 Squre 클래스

           (1) 사각형 클래스를 정의
           (2) 사각형을 상속받는 정사각형 클래스 정의
           (3) 아래와 같은 결과가 나오도록 클래스 만들기
'''
class Rectangle :
    def __init__(self, row, col) :
        self.area = row * col

    def print_area(self) :
        print( "면적 :", self.area )

class Square(Rectangle) :
    def __init__(self, row) :
        super().__init__(row, row)

rect = Rectangle(3, 4) # 가로, 세로 입력
rect.print_area() # 면적 : 12

sqr = Square(7)
sqr.print_area() # 면적 : 49

















