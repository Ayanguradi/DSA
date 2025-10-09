def monotonic_array(array):
    #write code here
    length = len(array) - 1
    if len(array) == 0:
        return True
    if array[0] <= array[length]:
        for i in range(length - 1):
            if array[i] <= array[i + 1]:
                pass
            else:
                return False
        return True
    else:
        for i in range(length - 1):
            if array[i] >= array[i + 1]:
                pass
            else:
                return False
        return True


print(monotonic_array([1, 2, 3, 3, 4]))
print(monotonic_array([5, 2, 3, 3, 4]))
print(monotonic_array([4,3,3,2,1]))