def average(array):
    # your code goes here
    new_arr = set(arr)
    # print(new_arr)
    new_arr1 = len(new_arr)
    # print(new_arr1)
    summ = sum(set(arr))
    avg = summ / new_arr1
    array = avg
    return array


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)