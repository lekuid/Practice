def is_prime(num):
    n = [i for i in range(1, num) if num % i == 0]
    if num > 1:
        return not len(n)>1
    else:
        return len(n)>1