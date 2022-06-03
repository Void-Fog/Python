

# Create txt
def create(name):
    with open('{}.txt'.format(name), 'w') as txt:
        run = 1
        line = ''
        while run:
            line += input('Enter line: ')
            if input('Enter more lines Y/N: ').capitalize() == 'Y':
                line += '\n'
            else:
                run = False
        txt.write(line)
 
 
# Readline
def rline(name):
    with open('{}.txt'.format(name), 'r') as txt:
        line = txt.readline().strip()
        while line:
            print(line)
            line = txt.readline().strip()
 
 
# Vowels
def svow(nameParent, nameChild):
    with open('{}.txt'.format(nameParent), 'r') as parentTxt:
        vowels = 'aeiou'
        words = ''
        for lines in parentTxt:
            for word in lines.split():
                if word[0].lower() in vowels:
                    words += word + '\n'
 
    with open('{}.txt'.format(nameChild), 'w') as childTxt:
        childTxt.write(words)
 
    rline(nameChild)
 
 
# Upper
def upwords(name):
    with open('{}.txt'.format(name), 'r') as txt:
        for lines in txt:
            for word in lines.split():
                if word.isupper():
                    print(word)
 
 
# __main__
running = True
while running:
    ch = input('''
1) Create a file 'text'
2) Read lines of file 'text'
3) Create and view new file 'vowel' with words starting with vowels
4) Display Uppercase words in file 'text'
5) Exit
 
Enter your choice:''')
 
    if ch == '1':
        create('text')
    elif ch == '2':
        rline('text')
    elif ch == '3':
        svow('text', 'vowel')
    elif ch == '4':
        upwords('text')
    elif ch == '5':
        print('Quiting...')
        running = False
