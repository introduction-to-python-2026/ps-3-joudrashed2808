def move(my_list, direction):
    index_of_one = my_list.index(1)

    if direction == 'right' and index_of_one < len(my_list) - 1:
        my_list[index_of_one] = 0
        my_list[index_of_one + 1] = 1

    elif direction == 'left' and index_of_one > 0:
        my_list[index_of_one] = 0
        my_list[index_of_one - 1] = 1

return my_list



def approximate_pi(n_terms):
    leibniz_series = []
    for n in range (n_terms):
        term = ((-1) ** n) / (2 * n + 1)
        leibniz_series.append(term)
    pi_approx = 4 * sum(leibniz_series)

    return pi_approx
