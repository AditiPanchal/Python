l1=[]
n=int(input("enter no. of elements of list:"))
for i in range (0,n):
    a=int(input())
    l1.append(a)
print("the list is:",l1) 
l2=[]
for i in l1:
    if i>0:
        b=i
        l2.append(b)
print("the list will all positive integers is:",l2)  

