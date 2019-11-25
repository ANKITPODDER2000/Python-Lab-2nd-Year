def fib(num):
    if num == 0 or num == 1:
        return num
    else:
        return fib(num-1)+fib(num-2)
print("Fib in range 0-10 is : ",end="")
i = 0
while True:
    if fib(i)<=10:
        print(fib(i),end = " ")
    else:
        break
    i+=1