def char_frequency(text):
    freq = {}
    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1
    return freq


if __name__ == "__main__":
    text = "banana"
    print(char_frequency(text))
