def solution(A):
    cars = 0
    total = 0
    last_index = -1
    for i in range(1,len(A)+1):
        if total > 1000000000:
            return -1
        if A[-i] == 0:
            if last_index == -1:
                cars += sum(A[-i:])
                total += cars
                last_index = i
            else:
                cars += sum(A[-i:-last_index])
                total += cars
                last_index = i
    return total
