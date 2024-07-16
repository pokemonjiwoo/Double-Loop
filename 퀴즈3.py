#이중리스트의 평균값을 아래 출력 결과와 같이 각각 구하여라

my_list = [[100, 200], [400, 800], [1000, 1400]]

for i in my_list:
    var = 0
    for j in i:
        var= var + j
        print(var/len(i))

