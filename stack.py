def push():
    global top
    if top==size-1:
        print("No space to insert ")
        return
    top+=1
    stack[top] = int(input("Enter value to insert in stck : "))
    
def pop():
    global top
    if top == -1:
        print("Stack underflow")
        return
    print("%d is popped out properly "%(stack[top]))
    top -= 1
def display():
    if top == -1:
        print("Stack underflow")
        return
    print("Stack is : ")
    for i in range(0,top+1):
        print(stack[i],end = " ")

size = int(input("Enter max size of array : "))
top = -1
stack = [0]*size

while True:
    op = int(input("Enter 1->Insert\nEnter 2->Pop\nEnter 3->Display\nEnter 4->Exit\nEnter the operation : "))
    if op==1:
        push()
    elif op==2:
        pop()
    elif op==3:
        display()
    elif op==4:
        print("End of program")
        break