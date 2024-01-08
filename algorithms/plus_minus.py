def plusMinus(arr):
    count_positive = 0
    count_negative = 0
    count_zeros = 0
    len_arr = len(arr)

    for num in arr:
        if num < 0:
            count_negative += 1
        elif num > 0:
            count_positive += 1
        elif num == 0:
            count_zeros += 1

    print(f'{count_positive / len_arr:.{6}f}')
    print(f'{count_negative / len_arr:.{6}f}')
    print(f'{count_zeros / len_arr:.{6}f}')


plusMinus([-4, 3, -9, 0, 4, 1])
