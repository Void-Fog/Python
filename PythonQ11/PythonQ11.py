
#Random module for read a random line
import random as rd

#Read a random line
def create(file):
    with open('{}.txt'.format(file),'w') as txt:
        run = True
        i = 0
        while run:
            txt.write(input('Enter line {}: '.format(i+1)))
            txt.write('\n')
            i+=1
            in_ = input('Continue? y/n: ')
            if in_.lower() == 'n':
                run = False
def randline(file):
    with open('{}.txt'.format(file), 'r') as txt:
        lines = txt.readlines()
        end = len(lines)
        rng = rd.randrange(0,end)
        print(lines[rng])

#No of words in file
def wordsin(file):
    dic = {}
    key = []
    with open('{}.txt'.format(file), 'r') as txt:
        for words in txt.read().split():
            if words.isalpha():
                if words in key:
                    dic[words] += 1
                else:
                    key.append(words)
                    dic[words] = 1
    return dic

#Commonly occurring word in file
def mode(dict_):
    word = []
    freq = 0
    for i in dict_.keys():
        if dict_[i] > freq:
            word = []
            word.append(i)
            freq = dict_[i]
        elif dict_[i] == freq:
            word.append(i)
    
    print('the list of word',word,'has/have freq',freq)

            
#__main__
running = True
while running:
    ch = input('''
1) Create a text file
2) Read a random line from a file
3) Find the most commonly occurring word in a file
4) Exit
Enter your choice: ''')

    if ch == '1':
        create('text')
        
    elif ch == '2':
        randline('text')
            
    elif ch == '3':
        mode(wordsin('text'))
            
    elif ch == '4':
        running = False
        print('Quitting ... ')
    else:
        print('Invalid Choice')   