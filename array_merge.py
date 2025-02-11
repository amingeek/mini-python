def sum_array(a1):
    def rsum(array):
        if isinstance(array, list):
            total = 0
            for item in array:
                total += rsum(item)
            return total
        else:
            return array
    return rsum(a1)

a5 = [[1, 2, 3], [4, 5, 6, 7], [10, 11, 12, 13, 14, 15]]

print(sum_array(a5))  