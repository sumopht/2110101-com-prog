def no_lowercase(t):
    for i in t:
        if i >= 'a' and i <= 'z':
            return False
    return True


def no_uppercase(t):
    for i in t:
        if i >= 'A' and i <= 'Z':
            return False
    return True


def no_number(t):
    for i in t:
        if i >= '0' and i <= '9':
            return False
    return True


def no_symbol(t):
    for i in t:
        if (i >= '!' and i <= '/') or (i >= ':' and i <= '@') or (i >= '[' and i <= '`') or (i >= '{' and i <= '~'):
            return False
    return True


def character_repetition(t):
    for i in range(len(t)):
        if i >= 3:
            if t[i] == t[i - 1] and t[i] == t[i - 2] and t[i] == t[i - 3]:
                return True
    return False


def number_sequence(t):
    sequence = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in range(len(t)):
        count = 0
        try:
            index = sequence.index(t[i])
        except:
            continue
        try:
            # increase
            if t[i].upper() == sequence[index]:
                count += 1
            if t[i + 1].upper() == sequence[index + 1]:
                count += 1
            if t[i + 2].upper() == sequence[index + 2]:
                count += 1
            if t[i + 3].upper() == sequence[index + 3]:
                count += 1
            if count == 4:
                return True
        except:
            pass
        try:
            # decrease
            count = 0
            if t[i].upper() == sequence[index]:
                count += 1
            if t[i + 1].upper() == sequence[index - 1]:
                count += 1
            if t[i + 2].upper() == sequence[index - 2]:
                count += 1
            if t[i + 3].upper() == sequence[index - 3]:
                count += 1
            if count == 4:
                return True
        except:
            pass
    return False


def letter_sequence(t):
    sequence = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for i in range(len(t)):
        count = 0
        try:
            index = sequence.index(t[i].upper())
        except:
            continue
        try:
            # increase
            if t[i].upper() == sequence[index]:
                count += 1
            if t[i + 1].upper() == sequence[index + 1]:
                count += 1
            if t[i + 2].upper() == sequence[index + 2]:
                count += 1
            if t[i + 3].upper() == sequence[index + 3]:
                count += 1
            if count == 4:
                return True
        except:
            pass

        try:
            # decrease
            count = 0
            if t[i].upper() == sequence[index]:
                count += 1
            if t[i + 1].upper() == sequence[index - 1]:
                count += 1
            if t[i + 2].upper() == sequence[index - 2]:
                count += 1
            if t[i + 3].upper() == sequence[index - 3]:
                count += 1
            if count == 4:
                return True
        except:
            pass
    return False


def keyboard_pattern(t):
    sequence = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', 'a', 's', 'd', 'f', 'g', 'h',
                'j', 'k', 'l', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
    for i in range(len(t)):
        count = 0
        try:
            index = sequence.index(t[i].lower())
        except:
            continue
        try:
            # increase
            if t[i].upper() == sequence[index].upper():
                count += 1
            if t[i + 1].upper() == sequence[index + 1].upper():
                count += 1
            if t[i + 2].upper() == sequence[index + 2].upper():
                count += 1
            if t[i + 3].upper() == sequence[index + 3].upper():
                count += 1
            if count == 4:
                return True
        except:
            pass
        try:
            # decrease
            count = 0
            if t[i].lower() == sequence[index]:
                count += 1
            if t[i + 1].lower() == sequence[index - 1]:
                count += 1
            if t[i + 2].lower() == sequence[index - 2]:
                count += 1
            if t[i + 3].lower() == sequence[index - 3]:
                count += 1
            if count == 4:
                return True
        except:
            pass
    return False


passw = input().strip()
errors = []
if len(passw) < 8:
    errors.append("Less than 8 characters")
if no_lowercase(passw):
    errors.append("No lowercase letters")
if no_uppercase(passw):
    errors.append("No uppercase letters")
if no_number(passw):
    errors.append('No numbers')
if no_symbol(passw):
    errors.append('No symbols')
if character_repetition(passw):
    errors.append('Character repetition')
if number_sequence(passw):
    errors.append('Number sequence')
if letter_sequence(passw):
    errors.append('Letter sequence')
if keyboard_pattern(passw):
    errors.append('Keyboard pattern')

if len(errors) == 0:
    print('OK')
else:
    for i in errors:
        print(i)
