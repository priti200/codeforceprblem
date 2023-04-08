import math

n,m,a=list(map(float, input().split()))  
print(math.ceil(n/a)*math.ceil(m/a))
