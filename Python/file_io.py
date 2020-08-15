'''
[파일입출력]
    -실제 파일 생성/삭제/쓰기/일기 등의 행위

    파일의 이해
        디렉토리(Directory)
            >폴더 또는 디렉토리라고 부른다.
            >폴더 안에는 파일 또다른 폴더를 포함 할 수 있다.
            >용량이 없다.
            >폴더 안으로 들어가는 일 밖에 못함(실행이라는 개념 X)
            
        파일
            >컴퓨터에서 정보(data)를 저장하는 논리적인 단위
            >파일은 실제 물리disk(HDD,SSD) 에 저장이 되고 , 용량이 존재
            >파일은 파일명과 확장자로 식별된다.
                >>파일명.확장자(맨 오른쪽 . 기준으로 확장자)
                >>test.txt.xls(엑셀 확장자)
                >>확장자 : 이 파일이 어떤 형식이 파일인지 써놓은 것
                >실행,쓰기,일기 등을 할 수 있다.

                Binary파일
                    >메모장으로 열었을 때 알아볼 수 없다.
                    >확장자에 맞는 전용프로그램으로 열어봐야 알 수 있다.
                    >확장자 : 엑셀(xls),워드(docx), 한글(hwp) 등..

                text 파일
                    >메모장으로 열었을 때 우리가 알아볼 수 있는 파일
                    >확장자 : txt,py,c,html,java...등등

                -우리는 코드를 파일을 다룰 때, 기본적으로 메모장으로 여는 것처럼
                파일을 읽는다.
                >Binary 파일을 코드 상으로 읽고 싶다 ->관련 모듈 사용
    '''
'''
[파일을 다루는 기본 구조]

파일객체 = open("파일이름","파일 열기 모드")

    파일객체 = 변수와 비슷
    파일이름 : 컴퓨터에 존재하는 파일명
    파일열기모드 : 열었을 때 어떤 행위를 할 것인지 미리 결정
        r : 읽기모드 (read)
            >내용을 읽기만 할 때
        w : 쓰기모드 (write)
            >내용을 쓰기만 할 때
        a : 추가모드 (add)
            >파일의 끝에 내용을 추가할 때
        
'''
print("[파일입출력]")
#파일의 절대경로 : 드라이브문자를 포함하여 전체 경로를 작성
#window OS의 경우 드라이브 문자를 사용 -->드라이브명:/
#D드라이브에 테스트폴더의 test.txt -> D:\\테스트\\test.txt

#상대경로 : 실행된 프로그램 실행파일 위치가 기준

#파일읽기
file = open("c:\\PT\\test.txt","r")#절대경로를 사용할 것임
#read() : 파일의 전체 내용을 '문자열'로 반환
text = file.read()
print(text)
#사용을 다한 파일은 열었기 때문에 반드시 닫아줘야 한다.
#닫지 않으면 프로그램이 계속 사용 중이기 때문에 다른 곳에서 파일을
#다룰 수 없다.
file.close()
print()

#with를 이용하여 close() 생략하기

with open("c:\\PT\\test.txt","r") as file :#open한 파일을 file 변수로 다룸
    text = file.read()
    print(text)
#close를 생략해도 with문법 안에서 자동으로 close
print("끝")


#파일 내용을 한 줄씩 읽기(1)
#readlines(): 한 줄씩 문자열로 나눠서 리스트 반환(개행 포함)
with open("c:\\PT\\test.txt","r") as file :
    text = file.readlines()
    print(text)


print("\n\n\n")
#파일 내용을 한 줄씩 읽기(2)
    
#readline():한 줄을 문자열로 읽기(\n 있으면 포함)
with open("c:\\PT\\test.txt","r") as file :
    text = file.readline()
    print(text)

with open("c:\\PT\\test.txt","r") as file :
    while True:
        text = file.readline()
        if not text :
            break
        print(text,end='')
        
        
with open("c:\\PT\\test.txt","r") as file :
    for line in file :
        print(line.strip('\n'))

#다음 줄을 일거라 라는 명령을 따로 하지 않았는데 자동으로 다음줄 이동
#프로그래밍 언어에서 file을 다룰 때 공통
#>한 번 읽거나,쓰고 나면 자동으로 그 다음 위치로 offset 이동
#>처음 파일을 열면 offset은 처음 위치 -> 한줄 로딩 -> 다음줄 이동
#>원한다면 offset 위치를 변경하여 원하는 위치의 내용을 읽거나 쓸 수 있


#통계산출(파일의 단어 개수,라인수)

with open("c:\\PT\\test.txt","r") as file :
    text = file.read()
    word_list = text.split()#공백 기준으로 문자를 나눈다.
    line_list = text.split('\n')

print(word_list)
print("단어 수 :",len(word_list))

print(line_list)
print("라인 수 :",len(line_list))

#파일에서 10자 이하인 단어 개수 세기
#10글자 이하의 글자 수는 총 4개입니다.

with open("c:\\PT\\test.txt","r") as file:
    count = 0
    words = file.readlines()
    for word in words:
        if len(word.strip('\n'))<=10 :
            count+=1
    print(count)



# 파일 입출력 연습
'''
    C:\\test_practice.txt 파일을 미리 만들어놓고 아래 정보 구하기
    [출력결과]
    전체 글자 수 : ??
    전체 단어 수 : ??
    전체 라인 수 : ??
    '사랑' 단어 수 : ??

'''


with open("c:\\PT\\test_practice.txt","r") as file :
    text = file.read()
    word_list = text.split()

    print(len("".join(word_list)))

#파일 쓰기
#파일이 없으면 새로 생성 , 있으면 지우고 새로 만든다.(w)

with open("c:\\PT\\ttt.txt","w") as file:
    for i in range(1,11):
        text = "{}번째 줄입니다.\n".format(i)
        file.write(text)

#write()도 마찬가지로 ,자동으로 쓰고 난 뒤 다음 위치로 offset 이동

with open("c:\\PT\\ttt.txt","r") as file :
    text = file.read()
    word_list = text.split()

    print(word_list)

file = open("c:\\PT\\test.png","rb")
date = file.read()
file.close()

file = open("c:\\PT\\testest.png","wb")

file.write(date)

file.close()

























