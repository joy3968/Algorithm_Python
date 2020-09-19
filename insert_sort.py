# 삽입 정렬 - 각 숫자를 적절한 위치에 삽입

# 리스트와 위치를 변경할 인덱스를 넣어준다.(다음 인덱스의 값과 바꿔주는 함수)
def swap(array,j):
    temp = array[j]
    array[j] = array[j+1]
    array[j+1] = temp
    return array

def insert_sort(array):
    for i in range(len(array)-1):
        j = i
        while(array[j] > array[j+1]):
            swap(array, j)
            j -= 1
    return array

array = [1, 10, 5, 8, 7, 6, 4, 3, 2, 9]

print(insert_sort(array))

