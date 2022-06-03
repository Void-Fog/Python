#Create File
def createf(master):
    with open('{}.txt'.format(master),'w') as txt:
        run = True
        i = 0
        while run:
            txt.write(input('Enter line {}: '.format(i+1)))
            txt.write('\n')
            i+=1
            in_ = input('Continue? y/n: ')
            if in_.lower() == 'n':
                run = False
            
#Replace
def replc(master, old, new):

    with open('{}.txt'.format(master),'r') as txt:
        filedata = txt.read()

    with open('{}.txt'.format(master),'w') as txt:
        txt.write(filedata.replace(old,new))

#Rewrite
def rwt(master, chr_):
    with open('{}.txt'.format(master),'r') as txt:
        filedata=''
        for i in txt.readlines():
            if chr_ in i:
                filedata += i+'\n'
    
    with open('{}.txt'.format(master),'w') as txt:
        txt.write(filedata)


# __main__
running = True
while running:
    ch = input('''
1) Create a text file 
2) Replace ‘this’ with ‘that’ and display the result
3) Search lines which have the word ‘to’ and rewrite file
4) Exit
 
Enter your choice: ''')
 
    if ch == '1':
        createf('text')
    elif ch == '2':
        replc('text', 'this', 'that')
        with open('text.txt','r') as txt:
            print(txt.read())
    elif ch == '3':
        rwt('text','to')
        with open('text.txt','r') as txt:
            print(txt.read())
    elif ch == '4':
        print('Quiting...')
        running = False
