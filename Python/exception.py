'''
[예외처리]
    -개발자가 의도하지 않는 오류 발생에 대한 오류 처리
        >프로그램 오류가 나면 프로그램이 종료된다.

        try :
            기본 수행문(무조건 수행)
        except:
            오류 발생 시 수행되는 수행문
'''
print("[예외처리]")
'''
while True:
    
    try :
        input_num = int(input("숫자 입력 : "))
        print("결과 :",input_num)
    except:
        print("숫자를 입력하세요")

'''
#(1) try문 : 오류 발생 예상 지역
#(2) except문 : 오류 발생 시 처리 지역
#   >오류 발생 시 오류가 발생한 코드에서 except문으로 점프
#   >오류가 발생하지 않으면 except는 수행 되지 않고 끝

#finally문 : 마지막에는 무조건 수행되는 구문
#   > 정상/오류 구분 없이 무언가 마무리할 코드가 있을 때 사용
'''
try :
    input_num = int(input("숫자 입력 : "))
    print("결과 :",input_num)
except:
    print("숫자를 입력하세요")
finally:#try,except에 종속
    print("예외처리 끝")
'''   

#오류구분

try:
    num1,num2 = map(int,input("두 수 입력 : ").split())
    print("나눈 결과 :",(num1//num2))

    my_list = [1,2,3]

    index = int(input("숫자 입력 : "))

    try:
        print("값 :",my_list[index])
    except:
        print("내부 try")

except ZeroDivisionError:
    print("0으로 나눌 수 없습니다.")
except ValueError:
    print("숫자를 입력 하세요")
except IndexError:
    print("인덱스가 잘못되었습니다.")
except:
    print("뭔지 몰라도 에러")


'''
사칙연산 계산기
(0으로 나눈다,숫자 입력 X 예외처리)

[출력 결과]
 [출력결과1]
     2개의 숫자를 입력하세요 : 10 3
     연산할 기호를 입력하세요(+,-,*,/) : +
     결과 : 10 + 3 = 3

    2개의 숫자를 입력하세요 : 10 0
     연산할 기호를 입력하세요(+,-,*,/) : +
     0으로 나눌 수 없습니다.

     2개의 숫자를 입력하세요 : 10 0
     연산할 기호를 입력하세요(+,-,*,/) : +
'''











