# 선택정렬(Selection Sort)
# 가장 작은것을 선택해서 제일 앞으로 보내기(반복)
array = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9, 11, 12 , 13, 14]

for i in range(len(array)):
    min = 99999999
    for j in range(len(array)-i):
        if min > array[j+i]:
            min = array[j+i]
            index = j+i
    temp = array[i]
    array[i] = array[index]
    array[index] = temp

print(array)