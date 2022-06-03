#Append
def apnd(master):
    with open('{}.txt'.format(master),'a') as txt:
        run = True
        i = 0
        while run:
            txt.write(input('Enter line {}: '.format(i+1)))
            txt.write('\n')
            i+=1
            in_ = input('Continue? y/n: ')
            if in_.lower() == 'n':
                run = False


#number of vowels, consonants, uppercase, lowercase characters
def count(master):
    with open('{}.txt'.format(master),'r') as txt:
        vowels = 'aAeEiIoOuU'
        dict_ = {'vowels':0,'consonants':0,'uppercase':0,'lowercase':0}
        for chr_ in txt.read():
            if chr_.isalnum():
                if chr_ in vowels:
                    dict_['vowels'] += 1
                elif chr_.isalpha():
                    dict_['consonants'] += 1
                
                if chr_.isupper():
                    dict_['uppercase'] += 1
                elif chr_.islower():
                    dict_['lowercase'] += 1
    print(dict_)


#read text from file and store in Uppercase in another file
def convert(master):
    with open('converted.txt', 'w') as chtxt:
        with open('{}.txt'.format(master), 'r') as txt:
            chtxt.write(txt.read().upper())


# __main__
running = True
while running:
    ch = input('''
1) Append text to a text file  
2) Display the number of vows, cons, upper, lower chars in the file
3) Convert the data into upper and store the result in another file
4) Display converted file
5) Exit
 
Enter your choice:''')
 
    if ch == '1':
        apnd('text')
    elif ch == '2':
        count('text')
    elif ch == '3':
        convert('text')
    elif ch == '4':
        with open('converted.txt','r') as txt:
            print(txt.read())
    elif ch == '5':
        print('Quiting...')
        running = False