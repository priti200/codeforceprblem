n=int(input())
l=list(map(int,input().split()))
print(l)
for i in range(1,n+1):
    print(l.index(i)+1,end=" ")