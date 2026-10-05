def reverse_words(sentence):
    words = sentence.split()
    reversed_each_word = [word[::-1] for word in words]
    return " ".join(reversed_each_word)


if __name__ == "__main__":
    text = "hello world python"
    print("Original:", text)
    print("Reversed words:", reverse_words(text))
