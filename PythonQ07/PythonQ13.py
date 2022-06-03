#Importing pickle
import pickle as pk

#Create
def create(name,lst):
    with open('{}.txt'.format(name),'wb') as txt:
        for record in lst:
            pk.dump(record,txt)
        
#Open
def openf(name):
    lst=[]
    with open('{}.txt'.format(name),'rb') as txt:
        try:
            while True:
                lst.append(pk.load(txt))
        except EOFError:
            return lst

#Search
def search(age):
    lst = list(openf('sports'))
    for rec in lst:
        if int(rec.split('~')[2]) > age:
            print(rec)

#Athletics
def ath():
    lst = list(openf('sports'))
    lst_ = []
    for rec in lst:
        if rec.split('~')[0].lower().strip() == 'athletics':
            lst_.append(rec)
    create('athletics',lst_)

#Table
def table(name):
    lst = list(openf('{}'.format(name)))
    lst.insert(0, 'Event~Participant~Age')
    for rec in lst:
        for i in rec.split('~'):
            print(i,sep='\t',end='\t')
        print()


#__main__
running = True
while running:
    ch = input('''
1) Create a text file sports.txt 
2) Search records of participants having age<
3) Create another file named athletics.txt
4) Display Athletics in table
5) Exit
 
Enter your choice: ''')
 
    if ch == '1':
        lst__ = ['Event~Participant~Age']
        run = 'y'
        while run == 'y':
            tempstr = ''
            for i in lst__[0].split('~'):
                tempstr += input('Enter {}: '.format(i)) + '~'
            lst__.append(tempstr)
            run = input('Continue Y/N : ').lower()
        create('sports',lst__)
        table('sports')

    elif ch == '2':
        search(input('Enter age: '))

    elif ch == '3':
        ath()

    elif ch == '4':
        table('athletics')

    elif ch == '5':
        print('Quiting...')
        running = False