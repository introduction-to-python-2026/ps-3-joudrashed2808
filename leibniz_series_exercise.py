def approximate_pi(n_terms):
    leibniz_series = []
    for n in range (n_terms):
        term = ((-1) ** n) / (2 * n + 1)
        leibniz_series.append(term)
    pi_approx = 4 * sum(leibniz_series)

    return pi_approx
