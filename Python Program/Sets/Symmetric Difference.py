# Enter your code here. Read input from STDIN. Print output to STDOUT
M=int(input())
# print(M)
s=set(map(int,input().split()))
# print(s)
N=int(input())
# print(N)
t=set(map(int,input().split()))
# print(t)
c=s.symmetric_difference(t)
# print(type(c))
d1=str(c)
d=''.join(d1)
# print(d)
d1=list(c)
# print(d1)
d2=d1.sort()
# print(d2)
for i in d1:
    print(i)
