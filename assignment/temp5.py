RESET = '\033[0m'
RED = '\033[;31m'
GREEN = '\033[;32m'
BLUE = '\033[;34m'
HIGHLIGHT = '\033[;103m'

a = open('assignment\มหาจุฬาลงกรณ์-tag.txt', 'r', encoding='utf-8')
for i in a:
    print(i.replace('<red>', RED).replace('<green>', GREEN).replace('<blue>', BLUE).replace('</>', RESET), end='')
