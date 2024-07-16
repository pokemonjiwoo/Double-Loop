#1부터 100까지 수를 2의 배수, 3의 배수, 5의 배수로 분류하려고 한다.
#2의 배수는 numbers_1의 리스트에,
#3의 배수는 numbers_2의 리스트에,
#5의 배수는 numbers_3의 리스트에 저장하는 코드를 작성하시오.



#2의 배수로 골라내는 법 (if)


#리스트 함수에 저장하는 법(append)
numbers_1 = []
numbers_2 = []
numbers_3 = []
numbers_1.append(1)

#1부터 100까지 반복적으로 수행하는 법(for, while)
number = 0

while number < 101 :
    number = number +1

    if number% 2 == 0:
        numbers_1.append(number)
    if number % 3 == 0:
        numbers_2.append(number)
    if number% 5 == 0:
        numbers_3.append(number)
print(numbers_1)
print(numbers_2)
print(numbers_3)