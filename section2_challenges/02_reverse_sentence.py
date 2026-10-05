def reverse_sentence(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    return " ".join(reversed_words)


if __name__ == "__main__":
    text = "Python is fun to learn"
    print("Original:", text)
    print("Reversed sentence:", reverse_sentence(text))
