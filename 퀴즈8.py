#while문을 사용하여 1부터 45사이에 중복이 없는 랜덤한 수 6개를 생성하고, 이를 result 리스트 변수에 추가하는 코드를 작성해라


import random

random.randint(1, 45)

i = 0
result = []
while i < 6 :
    i = i + 1
    new_num=(random.randint(1, 45))
    if new_num in result :
        print("값이 기존에 있습니다. 새롭게 추가하지 않습니다.")
    else :
        result.append(new_num)
print(result)