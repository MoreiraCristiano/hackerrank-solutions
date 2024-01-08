def staircase(n):
    total_whitespaces = n - 1
    total_char = 1

    for i in range(n):
        print(total_whitespaces * ' ' + total_char * '#')
        total_whitespaces -= 1
        total_char += 1


staircase(8)
