import random

prompt = """
1. Gate
2. Number
3. List
4. Quit

Enter number : """

number = 0
num1 = 0
while number != 4:
    print(prompt)
    number = int(input())
    if number == 1: 
        print("1. 1번 접속")
        print("2. 2번 접속")
        print("접속할 번호를 입력하세요 : ")
        num1 = int(input())
        if num1 == 1 : # 게이트 1
           print("===================")
           print("|1 번게이트 입니다.|")
           print("===================")
        else: # 게이트 2
            print("===================")
            print("|2번 게이트 입니다.|")
            print("===================")
    elif number == 2:
        print("=========Servise========")
        print("| 1. 제곱 계산기        |")
        print("| 2. 로또 발생기        |")
        print("========================")
        print("접속할 번호를 입력하세요 : ")
        num1 = int(input())
        if num1 == 1: # 거듭제곱
            point1 = 0
            point2 = 0
            print("숫자를 입력해 주세요 : ")
            point1 = int(input())
            print("두 번째 숫자를 입력해 주세요 : ")
            point2 = int(input())
            print("==========제곱=========")
            print(point1 * point2)
            print("========거듭제곱========")
            print(point1 ** point2)
            print("========================")
        elif num1 != 1 : # 로또 발생기
            my_number = random.sample(range(1, 46), 6)
            my_number.sort()
            print(my_number)
    
    elif number == 3:
        print("위 처럼 가지고 놀아보세요")
        
        
    else:
        print("by")
        