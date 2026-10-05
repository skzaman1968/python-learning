def first_non_repeating_char(text):
    frequency = {}
    for ch in text:
        frequency[ch] = frequency.get(ch, 0) + 1

    for ch in text:
        if frequency[ch] == 1:
            return ch
    return None


if __name__ == "__main__":
    samples = ["aabbcde", "swiss", "programming"]
    for s in samples:
        print(f"{s} -> {first_non_repeating_char(s)}")
