#importing pickle
from pickle import load,dump

def create():
    with open('sports.txt','wb') as sp:
        run = True
        i = 0
        records = {}
        while run:
            i+=1
            event=input('Enter Event: ')
            participant = input('Enter Participant: ')
            age=input('Enter Age: ')
            record = [
                event,
                participant,
                age,
            ]
            records[i] = record
            if input('Enter more Y/N').upper() == 'N':
                run = False
        dump(records,sp)

def viewTable():
    with open('sports.txt','rb') as sp:
        records = load(sp)
        print(records)
        print('Event\tParticipant\tAge')
        for list_ in records.values():
            for data in list_:
                print(data+'\t',end='')
            print()

create()
viewTable()