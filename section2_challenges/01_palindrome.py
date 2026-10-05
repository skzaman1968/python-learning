def is_palindrome(text):
    cleaned = "".join(ch.lower() for ch in text if ch.isalnum())
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    samples = ["madam", "racecar", "hello", "A man a plan a canal Panama"]
    for sample in samples:
        print(f"{sample!r} -> {is_palindrome(sample)}")
