a = []
b = []

for i in range(10):
    user_input = int(input("pls enter your number: "))
    a.append(user_input)


for i in range(len(a)-1,-1,-1):
    
        b.append(a[i])

print(b)    

