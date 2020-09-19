# 버블정렬(Bubble Sort) - 옆에 있는 값과 비교해서 더 작은 값을 앞으로 보낸다.

array = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9, 11, 12, 13]

# 리스트와 위치를 변경할 인덱스를 넣어준다.(다음 인덱스의 값과 바꿔주는 함수)
def swap(array,j):
    temp = array[j]
    array[j] = array[j+1]
    array[j+1] = temp
    return array


# array -> 정렬 할 리스트를 넣는다.
def bubble_sort(array):
    array_length = len(array)
    for i in range(array_length):
        for j in range(array_length-(i+1)):
            if(array[j] > array[j+1]):
                swap(array, j)
    return array


print(bubble_sort(array))