start=int(input("Enter the start value :"))
end=int(input("Enter the end value :"))

odd_count,even_count=0,0
for number in range(start,end+1):
    if number%2!=0:
        odd_count+=1
    else:
        even_count+=1
print("Number of odd numbers :",odd_count)
print("Number of even numbers :",even_count)
