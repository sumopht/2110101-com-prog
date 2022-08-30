counts = dict()
chars = [*input()]
for char in chars:
    if char >= 65 and char <= 90:
        char += 32
    if char not in counts:
        counts[char] = 1
    else:
        counts[char] += 1
print(counts)
