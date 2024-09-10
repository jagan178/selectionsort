n=int(input("Enter the number of elements:"))
list=[]
for i in range(n):
    value=int(input("enter the value:"))
    list.append(value)
print(list)
for i in range(0,n-1):
    min_index=i
    for j in range(i+1,n):
        if(list[min_index]>list[j]):
            min_index=j
            if (min_index!= i):
                temp=list[i]
                list[i]=list[min_index]
                list[min_index]=temp
print("Sorted list:")
print(list)
