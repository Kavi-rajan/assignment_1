a,b=0,1 #first two digits of fibbonacci series are 0,1
limit=int(input("give me a limit :"))
print("Fibbonacci series within the given limit is :")
while a<=limit:
    print(a,end=" ")
    next=a+b
    a=b
    b=next


