# map() =   applies a function to each item in an iterable (list, tuple, etc...)
# map(function, iterable)

store: [tuple[str, float]] = [("shirt", 20.00),
                              ("pants", 25.00),
                              ("jacket", 50.00),
                              ("socks", 10.00)]

usd_to_eur_conversion_rate: float = 0.84
to_euros = lambda data: (data[0], data[1] * usd_to_eur_conversion_rate)
to_dollars = lambda data: (data[0], data[1] / usd_to_eur_conversion_rate)

store_dollars = list(map(to_dollars, store))
for i in store_dollars:
    print(i[0] + " " + "{:.2f}".format(i[1]))
