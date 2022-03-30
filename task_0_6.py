def maximum_number_given(no_1, no_2, no_3):
    if (no_1 >= no_2) and (no_1 >= no_3):
        largest = no_1
    elif (no_2 >= no_1) and (no_2 >= no_3):
        largest = no_2
    elif (no_3 >= no_1) and (no_3 >= no_2):
        largest = no_3
    return largest


print(maximum_number_given(10, 20, 25))
