def reverse_number(n):
    if n < 0:
        return -int(str(abs(n))[::-1])
    return int(str(n)[::-1])


if __name__ == "__main__":
    print(reverse_number(12345))
    print(reverse_number(-456))
