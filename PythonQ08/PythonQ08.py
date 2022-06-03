
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
 
 
# Count letters, words, digits, lines
def count(name):
    with open('{}.txt'.format(name), 'r') as txt:
        dict_ = {'Digits': 0, 'Characters': 0, 'Words': 0, 'Lines': 0}
        for lines in txt.readlines():
            dict_['Lines'] += 1
            dict_['Characters'] += len(lines)
            for word in lines.split():
                if word.isalnum():
                    dict_['Words'] += 1
                for char in word:
                    if char.isdigit():
                        dict_['Digits'] += 1
    for key in dict_.keys():
        print('No of {} : {}'.format(key, dict_[key]))
 
def replace(line,old,new):
    newstr=''
    for words in line.split(old):
        newstr+=words+new
    return newstr[:-1]

# Space replaced by '#'
def sphash(nameParent, nameChild):
    with open('{}.txt'.format(nameParent), 'r') as parentTxt:
        with open('{}.txt'.format(nameChild), 'w') as childTxt:
            for line in parentTxt.readlines():
                childTxt.write(replace(line,' ','#'))
    print()
    rline(nameChild)
    
 
 
# __main__
running = True
while running:
    ch = input('''
1) Create a file 'text'
2) Count no of digits, char, lines and words in 'text'
3) Blank spaces of 'text' replace by '#' in a new file hash
4) Show file hash
5) Exit
 
Enter your choice:''')
 
    if ch == '1':
        create('text')
    elif ch == '2':
        count('text')
    elif ch == '3':
        sphash('text','hash')
    elif ch == '4':
        rline('hash')
    elif ch == '5':
        print('Quiting...')
        running = False
