def diagonalDifference(arr):
    main_sum = get_main_diagonal_sum(arr)
    secondary_sum = get_secondary_diagonal_sum(arr)
    total = abs(main_sum - secondary_sum)
    return total


def get_main_diagonal_sum(arr):
    total = 0

    for i in range(len(arr)):
        total += arr[i][i]

    return total


def get_secondary_diagonal_sum(arr):
    total = 0
    reversed_matrix = list(reversed(arr))

    for i in range(len(reversed_matrix)):
        total += reversed_matrix[i][i]

    return total
