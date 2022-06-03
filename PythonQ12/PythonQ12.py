
#Create file
def create(file='para'):
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

#mlines -> matched, umlines-> unmatched lines
def mline(text='i'):
    mlines = []
    umlines = []
    with open('para.txt','r') as txt:
        lines = txt.readlines()
    
    for line in lines:
        if text in line:
            mlines.append(line+'\n')
        else:
            umlines.append(line+'\n')
    
    return {'mline':mlines,'umline':umlines}
#move line with i to ifile
def move():
    createtxt(mline()['mline'],'ifile.txt')
    createtxt(mline()['umline'],'para.txt')
#Create txt through list arg
def createtxt(lst, file):
    print('Now reading',file)
    with open('{}.txt'.format(file),'w+') as txt:
        for i in lst:
            txt.write(i)
        print(txt.read())
    



#__main__
running = True
while running:
    ch = input('''
1) Create file para.txt
2) Move lines i to ifile.txt
3) Copy lines with we to wefile.txt
4) Exit
Enter your choice: ''')

    if ch == '1':
        create()
                
    elif ch == '2':
        move()
                    
    elif ch == '3':
        createtxt(mline('we')['mline'],'wefile.txt')
                    
    elif ch == '4':
        running = False
        print('Quitting ... ')
    else:
        print('Invalid Choice')
                    
