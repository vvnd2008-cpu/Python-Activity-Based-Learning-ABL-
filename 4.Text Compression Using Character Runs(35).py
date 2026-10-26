
# Text Compression Using Character Runs

text = input("Enter text to compress: ")

if text == "":
    print("Compressed text:")
else:
    result = ""
    current = text[0]
    count = 1

    for ch in text[1:]:
        if ch == current:
            count += 1
        else:
            result += current + str(count)
            current = ch
            count = 1

    result += current + str(count)

    print("Compressed text:", result)
