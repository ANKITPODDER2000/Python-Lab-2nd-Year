def push():
    global F,R
    if R==size-1:
        print("No space to insert ")
        return
    if F==-1:
        F+=1
    R+=1
    queue[R] = int(input("Enter value to insert in stck : "))
    
def pop():
    global F,R
    if F == -1:
        print("Queue underflow")
        return
    print("%d is popped out properly "%(queue[F]))
    if F==R:
        F=-1
        R = -1
    else:
        F+=1
def display():
    if F == -1:
        print("Queue underflow")
        return
    print("Queue is : ",end="")
    for i in range(F,R+1):
        print(queue[i],end = " ")

size = int(input("Enter max size of array : "))
F = -1
R = -1
queue = [0]*size

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