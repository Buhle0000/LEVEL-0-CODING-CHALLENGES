def maximum(*set):
    value = set[0]
    for number in set:
        if number > value:
            value = number
    return value

