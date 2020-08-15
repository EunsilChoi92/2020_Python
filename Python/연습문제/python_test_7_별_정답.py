# for문을 이용한 별 모양 출력하기

'''
[문제] for문을 이용해서 사각형으로 별 출력하기

[출력결과]
*****
*****
*****
*****
*****


[정답]
for i in range(5):
    for j in range(5):
        print('*', end = '')
    print()
    
'''

'''
[문제] for문을 이용해서 계단식으로 별 출력하기

[출력결과]
*
**
***
****
*****


[정답1]
for i in range(5):
    for j in range(i+1):
        print('*', end = '')
    print()
    
[정답2[
for i in range(5):
    for j in range(5):
        if j <= i:
            print('*', end = '')
    print()
    
'''

'''
[문제] for문을 이용해서 대각선으로 별 출력하기

[출력결과]
*    
 *   
  *  
   * 
    *
    

[정답]
for i in range(5):
    for j in range(5):
        if j == i:
            print('*', end = '')
        else:
            print(' ', end = '')
    print()
    
'''

'''
[문제] for문을 이용해서 역삼각형으로 별 출력하기

[출력결과]
*****
 ****
  ***
   **
    *


[정답]
for i in range(5):                   
    for j in range(5):               
        if j < i:
            print(' ', end ='')
        else:
            print('*', end ='')
    print()

'''
