# def is_odd(n):
#     return n % 2 == 1

# L = range(100)

# print(list(filter(is_odd, L)))

# def not_empty(s):
#     return s and s.strip()

# print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))

def main():
    for n in primes():
        if n < 1000:
            print(n)
        else:
            break

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0

def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(_not_divisible(n), it)

if __name__ == '__main__':
    main()