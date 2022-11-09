def match(word, pattern, include_chars, exclude_chars):
    if len(word) != len(pattern):
        return False
    else:
        include = []
        for c in include_chars:
            include.append(c)
        words = []
        for c in word:
            words.append(c)
        for index in range(len(word)):
            if pattern[index] == '?':
                if word[index] in exclude_chars:
                    return False
                for c in include:
                    if c == word[index]:
                        include.remove(word[index])
                        break
            else:
                if pattern[index] != word[index]:
                    return False
        if len(include) != 0:
            return False
        return True


exec(input())
