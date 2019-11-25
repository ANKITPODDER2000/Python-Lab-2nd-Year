try:
    fl = open("else.py","r")
    a = fl.read()
    print(a)
except:
    print("Error")
else:
    fl.close()