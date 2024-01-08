def miniMaxSum(arr):
    arr_sum = sum(arr)
    results = []

    for i in range(len(arr)):
        results.append(arr_sum - arr[i])

    min_sum = min(results)
    max_sum = max(results)

    print(f'{min_sum} {max_sum}')


miniMaxSum([2, 3, 3, 6, 7])
