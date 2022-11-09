color = input()
lyrics = input()
fcolor = open(color, 'r')
colors = set()
for line in fcolor:
    words = line.split()
    for word in words:
        colors.add(word.upper())
print(colors)
flyrics = open(lyrics, 'r')
for line in flyrics:
    check = False
    # print(line, end='')
    words = line.split()
    # print(words)
    for word in words:
        if word.upper() in colors:
            print(word)
            newline = line.replace(word, '<' + word.lower() + '>' + word + '</>')
            check = True
    if check:
        print(newline, end='')
    else:
        print(line, end='')
# grader/color.txt
# grader/lyrics.txt
# !!!! not finished
