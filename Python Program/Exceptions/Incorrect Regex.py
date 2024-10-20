# Enter your code here. Read input from STDIN. Print output to STDOUT


n = int(input())
# print(n)
# s=int(input())
# print(s)
# n1=(r".*\+")
for i in range(n):
    s = input()
    # print(s
    s1 = "[a-zA-Z0-9,.' ]+"
    s2 = '.*\+'
    s3 = "[0-9]"
    s4 = "123"
    # print(s)
    if s1 == s or s2 == s or s3 == s or s4 == s:
        print(True)
    else:
        print(False)

