# 조건문 연습
'''
    1. 나이를 입력 받고 아래 조건에 맞게 출력
        7세 이하 : 아동입니다.
        8세~19세 : 청소년입니다.
        20세~64세 : 성인입니다.
        65세 이상 : 노인입니다.
    [출력결과]
    나이 입력 : 15
    청소년입니다.
'''


'''
    2. 주민등록번호 남/녀 판별기
        주민등록번호를 010101-3456789 형태로 입력 받고,
        7번째 숫자에 따라 "남자" 또는 "여자" 출력
            9, 1, 3, 5, 7 : 남자
            0, 2, 4, 6, 8 : 여자

    [출력결과]
    주민등록번호 입력 : 010101-3456789
    남자

        >> 입력받은 주민등록번호를 바로 정수로 변환하면 안 됨...
            jumin = int(input("주민등록번호 입력 : "))
            이렇게 시작하면 큰 일 난다...
'''
'''
#jumin = input("주민등록번호 입력 : ")
jumin = "010101-3456789" # int()를 쓰지않고, input()만 하면 문자열

# 1) ~~ in 리스트 사용
# 2) == 비교연산 사용


'''

'''
    3. 3개 과목의 점수를 입력 받고, 평균 점수에 따라 합격/불합격 출력
        - 평균 60점 이상 합격
        - 평균 점수는 소수점 첫 번째 자리까지만 출력
        - 합격일 때, 65점 미만이면 "턱걸이하셨네요~~!"를 추가로 출력        

    [출력결과]
    세 과목 점수 입력 : 60 60 61
    당신은 60.3점으로 합격입니다.
    턱걸이하셨네요~~!
'''

'''
    4. 똑똑한 계산기
        - 2개의 숫자와 연산할 기호를 입력 받고 결과를 출력하기
            (1) 계산할 2개의 숫자를 입력 받기
            (2) 연산할 기호를 입력 받기
            (3) 연산 기호에 맞는 결과를 출력

     [출력결과1]
     2개의 숫자를 입력하세요 : 10 3
     연산할 기호를 입력하세요(+,-,*,/) : +
     결과 : 10 + 3 = 3
     
     [출력결과2]
     2개의 숫자를 입력하세요 : 10 3
     연산할 기호를 입력하세요(+,-,*,/) : /
     결과 : 10 / 3 = 3.3
'''

'''
    5. 강남마켓 장바구니
        - 장바구니 가격을 입력받고, 금액에 따라 할인율 적용
            > 10,000원 이상 	: 5%
            > 50,000원 이상 	: 10%
	    > 100,000원 이상 	: 20%

    [출력결과1]
    총 구매액을 입력해주세요 : 50000
    최종 결제액은 45000원 입니다.

    [출력결과2]
    총 구매액을 입력해주세요 : 5000
    최종 결제액은 5000원 입니다.
    10000원 이상 구매 시 할인되니 많이 사주세요^^ 
'''







