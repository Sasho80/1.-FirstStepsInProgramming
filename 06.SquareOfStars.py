n=int (input())
# printing top row
for row in range(n,n+1):
    print("*"*row)
# printing middle row
for row in range(1,(n-2)+1):
    for rowMiddle in range(n,n+1):
        print("*"+" "*(rowMiddle-2)+"*")
# printing down row
for rowLast in range(n,n+1):
        print("*"*rowLast)