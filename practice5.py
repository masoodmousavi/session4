a = [1,1,2,2,2,4,5,5,7,8,4,]
b = []
for i in a:
    if i  in b:
        continue      
    else:
        b.append(i)    
print(b)
