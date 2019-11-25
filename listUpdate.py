li = [10,20,30]
"""
    li = [0,0,0]
    li = [10,20,30]
    use one by one to understand any and all functiom
"""
print("List is : ",li)
li[0] = 55
print("Updated list is : ",li)
print("Max in list is : %d\nMin in list is : %d\nLen of list is : %d"%(max(li),min(li),len(li)))
print("All : ",all(li))
print("Any : ",any(li))