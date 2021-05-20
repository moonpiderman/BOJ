import heapq

def swap(array, i, j) :
    array[i], array[j] = array[j], array[i]

if __name__ == '__main__' :
    num = int(input())

    '''
    array = [i for i in range(1, num + 1)]
    heap = []

    # 최소 swap으로 구현
    for value in array :
        heapq.heappush(heap, -value)

    for i in range(len(heap)) :
        print(-heap[i], end=' ')
    '''

    heap = [0, 1]
    # 최대 힙으로 만들어가는 과정
    for x in range(2, num + 1) :
        heap.append(x)
        swap(heap, x, x - 1)
        y = x - 1
        while y != 1 :
            swap(heap, y, y//2)
            y = y//2

    for i in heap[1:] :
        print(i, end=' ')