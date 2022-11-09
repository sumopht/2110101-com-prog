points = {'A': 1, 'E': 1, 'I': 1, 'L': 1, 'N': 1, 'O': 1, 'R': 1, 'S': 1, 'T': 1, 'U': 1,
          'D': 2, 'G': 2,
          'B': 3, 'C': 3, 'M': 3, 'P': 3,
          'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
          'K': 5,
          'J': 8, 'X': 8,
          'Q': 10, 'Z': 10, }


def letter_point(c):
    return points[c]


def word_point(w):
    sum = 0
    for c in w:
        sum += letter_point(c)
    return sum


words = input().split()
scores = dict()
for word in words:
    scores[word] = word_point(word)
sorted_score = sorted(list(set(sorted(scores.values(), reverse=True))), reverse=True)
sorted_dict = sorted(scores)

for score in sorted_score:
    for word in sorted_dict:
        if score == scores[word]:
            print(word, score)
