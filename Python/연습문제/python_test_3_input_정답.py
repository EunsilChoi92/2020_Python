# 입력 명령어(input)
'''
[문제]
변수 height에 키(tall)를 묻고 값을 할당하시오.
변수 height를 정수형(int)으로 만들어 소수점 아래를 버리시오.
변수 weight에 상대방의 몸무게를 실수형(float)으로 묻고 값을 할당하시오.
변수 height와 변수 weight를 더한 값을 출력하시오.

[출력결과]

키가 얼마인가요? 165
몸무게는 얼마인가요? 50.0
키 + 몸무게 =  215.0

[정답]
height = int(input("키가 얼마인가요?"))
weight = float(input("몸무게는 얼마인가요?"))
print('키 + 몸무게 = ', height + weight)

'''



'''
[문제]
정수 3개를 한꺼번에 입력받고 합계 출력하기(map이용)

[출력결과]

정수를 입력하세요 : 10 20 30
60

[정답]
a, b, c = map(int, input('정수를 입력하세요 : ').split())
print(a + b + c)

'''



'''
[문제] : 값을 입력받아 문장 출력하기

[출력결과]

당신의 나이는 몇 살입니까?   30
당신은 30 년을 살았습니다.

[정답]
a = input('당신의 나이는 몇 살입니까? ')
print('당신은', a, '년을 살았습니다.')

'''



'''
[문제] : 덧셈 계산기

[출력결과]

덧셈 첫 번째 숫자는?  5
덧셈 두 번째 숫자는?  8
두 숫자의 합은 13 입니다.

[정답]
a = int(input('덧셈 첫 번째 숫자는? '))
b = int(input('덧셈 두 번째 숫자는? '))
print('두 숫자의 합은', a + b, '입니다.')

'''



'''
[문제] : 나눗셈 계산기

[출력결과]

피제수는?  13
제수는?  5
나눗셈의 몫은 2 나머지는 3 입니다

[정답]
a = int(input('피제수는? '))
b = int(input('제수는? '))
print('나눗셈의 몫은', a // b, '나머지는', a % b, '입니다.')

'''



'''
[문제] : 성적 계산 프로그램

[출력결과]

이름을 입력하세요 : 파이썬
국어 성적을 입력하세요 : 95
수학 성적을 입력하세요 : 98
사회 성적을 입력하세요 : 84
과학 성적을 입력하세요 : 90
영어 성적을 입력하세요 : 79
파이썬 님의 성적은
총합 446 점, 평균 89.2 점 입니다.

[정답]
name = input('이름을 입력하세요 : ')
kor = int(input('국어 성적을 입력하세요 : '))
mat = int(input('영어 성적을 입력하세요 : '))
soc = int(input('사회 성적을 입력하세요 : '))
sci = int(input('과학 성적을 입력하세요 : '))
eng = int(input('영어 성적을 입력하세요 : '))
hab = kor + mat + soc + sci + eng
avg = hab / 5
print(name, '님의 성적은')
print('총합', hab, '점, 평균', avg, '점입니다.')

'''



'''
[문제]
피타고라스 정리 : 직각삼각형의 빗변의 제곱은 두 직각 변의 제곱합과 같다.
이 때 두 변의 길이는 실수형으로 입력받도록 해보자.

참고 : 빗변 제곱값 = 첫 번째 직각변의 길이 제곱값 + 두 번째 직각 변의 길이 제곱값
빗변 = 빗변 제곱값 ** 0.5 (제곱을 원래 값으로 하기 위해 1/2(0.5)를 거듭제곱한다. = 제곱근 구하는 것임)

[출력결과]

첫 번째 직각변의 길이(cm) : 15.3  
두 번째 직각변의 길이(cm) : 12.1
빗변의 길이는 19.50640920313116 cm입니다.

[정답]
a = float(input('첫 번째 직각 변의 길이(cm) : '))
b = float(input('두 번째 직각 변의 길이(cm) : '))
c2 = a**2 + b**2
c = c2 ** 0.5 #제곱을 없애기 위해 1/2(=0.5)을 거듭제곱한다.
print('빗변의 길이는', c, 'cm입니다.')

'''



'''
[문제]
원의 넓이 구하기 : 원의 둘레(2 * 3.14 * 반지름), 원의 넓이(3.14 * 반지름 * 반지름)
이 때 결과값이 소수 둘째자리까지 나오도록 반올림한다. round사용

[출력결과]

원의 반지름을 입력하세요(cm) : 3
원의 둘레는 18.84 cm이고 원의 넓이는 28.26 cm입니다.

[정답]
r = float(input('원의 반지름을 입력하세요(cm) : '))
cir = round(2 * 3.14 * r, 2)
area = round(3.14 * r * r, 2)
print('원의 둘레는', cir, 'cm이고 원의 넓이는', area, 'cm입니다.')

'''



'''
[문제] : 이름을 넣어 새해 인사 문자 보내기

[출력결과]

첫번째 이름을 입력하세요 : 라이언
두번째 이름을 입력하세요 : 어피치
세번째 이름을 입력하세요 : 무지
라이언 님 올 2019년에도 새해 복 많이 받으시고 만수무강 하세요.
어피치 님 올 2019년에도 새해 복 많이 받으시고 만수무강 하세요.
무지 님 올 2019년에도 새해 복 많이 받으시고 만수무강 하세요.

[정답]
name1 = input('첫번째 이름을 입력하세요 : ')
name2 = input('두번째 이름을 입력하세요 : ')
name3 = input('세번째 이름을 입력하세요 : ')
print(name1, '님 올 2019년에도 새해 복 많이 받으시고 만수무강 하세요.')
print(name2, '님 올 2019년에도 새해 복 많이 받으시고 만수무강 하세요.')
print(name3, '님 올 2019년에도 새해 복 많이 받으시고 만수무강 하세요.')

'''



'''
[문제] : BMI(체질량지수) 계산하기
BMI 공식 = 몸무게 / (키 / 100) ** 2
BMI는 반올림하여 소수 둘째자리까지 나타내기

[출력결과]

이름을 입력하세요 : 파이썬
키(cm)를 입력하세요 : 176
몸무게(kg)를 입력하세요 : 72

파이썬님의 키는  176 cm이고 몸무게는  72 kg 입니다.
BMI 지수는  23.24 입니다.


[정답]
name = input('이름을 입력하세요 : ')
height = int(input('키(cm)를 입력하세요 : '))
weight = int(input('몸무게(kg)를 입력하세요 : '))
bmi = weight / (height / 100) ** 2
print()
print(name + '님의 키는 ', height,'cm이고 몸무게는 ', weight, 'kg입니다.')
print('BMI 지수는 ', round(bmi,2), '입니다.')

'''
