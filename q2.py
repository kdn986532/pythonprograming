def infinite_numbers():
    n = 0
    while True:
        yield n
        n += 1

def multiply_by_two():
    while True:
        value = yield
        if value is not None:
            print(f"Received: {value}, Result: {value * 2}")

gen = infinite_numbers()
coroutine = multiply_by_two()
next(coroutine)

for _ in range(10):
    num = next(gen)
    coroutine.send(num)
