def compareTriplets(a, b):
    a_points, b_points = 0, 0

    for i in range(3):
        if a[i] > b[i]:
            a_points += 1
        elif b[i] > a[i]:
            b_points += 1

    return a_points, b_points
