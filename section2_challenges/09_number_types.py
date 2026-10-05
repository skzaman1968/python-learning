def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def is_even(n):
    return n % 2 == 0


def is_odd(n):
    return n % 2 != 0


def is_perfect(n):
    if n < 1:
        return False
    total = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    return total == n


if __name__ == "__main__":
    nums = [2, 3, 4, 6, 7, 28]
    for n in nums:
        print(f"{n}: prime={is_prime(n)}, even={is_even(n)}, odd={is_odd(n)}, perfect={is_perfect(n)}")
