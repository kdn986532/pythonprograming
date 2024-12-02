def infinite_numbers():
    n = 0
    while True:
        yield n
        n += 1

gen = infinite_numbers()

for _ in range(10):
    print(next(gen))