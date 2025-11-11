def move(my_list, direction):
    new_list = my_list[:]
    index_of_one = new_list.index(1)
    if direction == 'right':
        if index_of_one != len(new_list) - 1:
            new_list[index_of_one] = 0
            new_list[index_of_one + 1] = 1
    elif direction == 'left':
        if index_of_one != 0:
            new_list[index_of_one] = 0
            new_list[index_of_one - 1] = 1
    return new_list



def approximate_pi(n_terms):
    leibniz_series = []
    for n in range (n_terms):
        term = ((-1) ** n) / (2 * n + 1)
        leibniz_series.append(term)
    pi_approx = 4 * sum(leibniz_series)

    return pi_approx
