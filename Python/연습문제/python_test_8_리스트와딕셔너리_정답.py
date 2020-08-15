# 리스트와 딕셔너리

'''
[문제] 리스트의 수정, 삭제, 변경

1. 과일이름을 요소로 하는 값이 3개 이상인 리스트 a를 생성하라.

2. 음식이름을 요소로 하는 값이 3개 이상인 리스트 b를 생성하라.

3. 위 두 개의 리스트를 하나로 합친 리스트 c를 생성하라.

4. c에서 마지막 과일을 다른 과일로 대체하라.

5. c에서 마지막 음식을 삭제하라.


[출력결과]

과일 리스트 :  ['사과', '복숭아', '포도']
음식 리스트 :  ['김치', '라면', '피자']
과일과 음식 리스트 :  ['사과', '복숭아', '포도', '김치', '라면', '피자']
과일과 음식 리스트 :  ['사과', '복숭아', '바나나', '김치', '라면', '피자']
과일과 음식 리스트 :  ['사과', '복숭아', '바나나', '김치', '라면']


[정답]

a = ['사과', '복숭아', '포도']
b = ['김치', '라면', '피자']
c = a + b
print('과일 리스트 : ',a)
print('음식 리스트 : ',b)
print('과일과 음식 리스트 : ',c)
c[2] = '바나나'
print('과일과 음식 리스트 : ',c)
del c[5]
print('과일과 음식 리스트 : ',c)

'''



'''
[문제] 리스트 명령어 연습 문제

1. 학생이 3명[홍길동, 허난설헌, 허균]인 과에 이황이 편입을 했다. “이황”을 리스트에 추가하라.

2. 위 리스트에 동명이인 허균이 새로 편입을 했다고 가정하고 요소 “허균” 뒤에 “허균”을 추가하라.

3. “허균”이 몇 명인지 명령어를 써서 구해보아라.

4. “홍길동”이 다른 과로 전과를 하였다. “홍길동”을 찾아 삭제하라.

5. 현재 리스트에서 두 번째 학생이 자퇴를 하였다. 두 번째 학생을 삭제하라.

6. 현재 출석부를 내림차순으로 정렬하라.


[출력결과]

현재 학생은  ['홍길동', '허난설헌', '허균'] 입니다.
전학 온 학생은 누구입니까? 이황
현재 학생은  ['홍길동', '허난설헌', '허균', '이황'] 입니다.
현재 학생은  ['홍길동', '허난설헌', '허균', '이황', '허균'] 입니다.
허균은 2 명 입니다.
현재 학생은  ['허난설헌', '허균', '이황', '허균'] 입니다.
현재 학생은  ['허난설헌', '이황', '허균'] 입니다.
현재 학생은  ['허난설헌', '허균', '이황'] 입니다.


[정답]

student = ['홍길동', '허난설헌', '허균']
print('현재 학생은 ', student, '입니다.')
new_student = input('전학 온 학생은 누구입니까? ')
student.append(new_student)
print('현재 학생은 ', student, '입니다.')
student.append('허균')
print('현재 학생은 ', student, '입니다.')
a = student.count('허균')
print('허균은', a, '명 입니다.')
student.pop(0)
print('현재 학생은 ', student, '입니다.')
del student[1]
print('현재 학생은 ', student, '입니다.')
student.sort(reverse = True)
print('현재 학생은 ', student, '입니다.')

'''



'''
[문제] 딕셔너리 관련 문제

1. {"강감찬":"귀주대첩", "을지문덕":"살수대첩", "세종대왕":"집현전"}라는 딕셔너리를 만들고 여기에 {"서희":"강동6주"}를 추가하여라.

2. 위의 딕셔너리에서 Key가 "세종대왕"인 것의 Value를 "한글"로 수정하여라.

3. "을지문덕"이라는 Key가 존재하는지 확인하고 있다면 삭제하라.


[출력결과]

현재 딕셔너리는 {'강감찬': '귀주대첩', '을지문덕': '살수대첩', '세종대왕': '집현전'} 입니다.
현재 딕셔너리는 {'강감찬': '귀주대첩', '을지문덕': '살수대첩', '세종대왕': '집현전', '서희': '강동6주'} 입니다.
현재 딕셔너리는 {'강감찬': '귀주대첩', '을지문덕': '살수대첩', '세종대왕': '한글', '서희': '강동6주'} 입니다.
현재 딕셔너리는 {'강감찬': '귀주대첩', '세종대왕': '한글', '서희': '강동6주'} 입니다.


[정답]

history = {'강감찬':'귀주대첩', '을지문덕':'살수대첩', '세종대왕':'집현전'}
print('현재 딕셔너리는', history, '입니다.')
history['서희'] = '강동6주'
print('현재 딕셔너리는', history, '입니다.')
history['세종대왕'] = '한글'
print('현재 딕셔너리는', history, '입니다.')
del history['을지문덕']
print('현재 딕셔너리는', history, '입니다.')

'''

