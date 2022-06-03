# Peek

def peek(que):
    if que:
        front = 0
        no = que[front]
        print(no, 'is the front item')
    else:
        print('Empty Queue')

# enque


def enque(que, elem):
    que.append(elem)
    print(elem)
    if len(que) == 1:
        front = rear = 0
    else:
        rear = len(que) - 1


# deque
def deque(que):
    if que:
        if len(que) == 1:
            front = rear = 0
        else:
            rear = len(que) - 2
        no = que.pop(0)
        print(no, 'is Deleted')

    else:
        print('Underflow Error')


# Display
def display(que):
    front = 0
    rear = len(que) - 1
    if len(que_):
        for i in que:
            if i == que[front]:
                print('Front >>>', i)
            elif i == que[rear]:
                print('Rear  >>>', i)
            else:
                print(' ' * 9, i)
    else:
        print('Empty Queue')


# __main__
run = True
que_ = []
while run:
    ch = input(
        '\nMenu\n1)Enque\n2)Display\n3)Deque\n4)Peek\n5)Exit\nEnter your choice: ')

    if ch == '1':
        while True:
            no = input('Enter no: ')
            if no:
                enque(que_, no)
                print('Added!!')
                break
            else:
                print('Pls enter the req value!')
    elif ch == '2':
        display(que_)
    elif ch == '3':
        deque(que_)
    elif ch == '4':
        peek(que_)
    elif ch == '5':
        run = False
        print('Quitting')
    else:
        print('Invalid choice')
