
# Peek
def peek(stack):
    if stack:
        top = len(stack) - 1
        print(stack[top], 'is Top elem')
    else:
        print("Empty Stack!!")


# add
def push(stack, elem):
    stack.append(elem)
    print(elem)
    top = len(stack) - 1


# pop
def pop(stack):
    if stack:
        if len(stack) == 1:
            top = None
        else:
            top = len(stack) - 2
        no = stack.pop()
        print(no, 'is deleted')
    else:
        print('Underflow Error')


# Display
def display(stack):
    if stack:
        top = len(stack) - 1
        print(stack[top], '<-top')
        for i in range(top-1, -1, -1):
            print(stack[i])
    else:
        print('Empty Stack!!')


# __main__
run = True
stck = []
while run:
    ch = input(
        '\nMenu\n1)Push\n2)Display\n3)Pop\n4)Peek\n5)Exit\nEnter your choice: ')

    if ch == '1':
        while True:
            rll, name_, age_ = input('Enter roll no: '), input(
                '\tName: '), input('\tAge: ')
            if rll and name_ and age_:
                push(stck, [rll, name_, age_])
                print('Added!!')
                break
            else:
                print('Pls enter the req value!')
    elif ch == '2':
        display(stck)
    elif ch == '3':
        pop(stck)
    elif ch == '4':
        peek(stck)
    elif ch == '5':
        run = False
        print('Quitting')
    else:
        print('Invalid choice')
