import random
ran = random.uniform(1,100)
i = int(input("도전할 기회수를 입력하세요:"))
while(i != 0):
    a = int(input("1부터 100 사이의 숫자를입력해보세요:"))
    i -= 1
    if (int(ran) < a <= int(ran)+10):
        print("입력하신 숫자가 조금 큽니다")
    elif (a > int(ran)+10):
        print("입력하신 숫자가 너무 큽니다")
    elif(int(ran)-10 > a):
        print("입력하신 숫자가 너무 작습니다")
    elif(int(ran) > a >= int(ran)-10):
        print("입력하신 숫자가 조금 작습니다")
    if(int(ran) == a):
        print("정답입니다")
        break
input("끝내시려면 엔터키를 눌러주세요")