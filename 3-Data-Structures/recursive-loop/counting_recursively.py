def recur_count_up(num):
    if num < 0:
        return
    recur_count_up(num-1)
    print(num)
    return


recur_count_up(5)








def recursive_count(num):
    if num < 0:
        return
    print(num)
    return recursive_count(num-1)


recursive_count(5)