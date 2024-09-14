b = input().split()
resp = 0 

if (b[0] != "1" and b[1] !="1"):
    resp = 1
elif(b[0] != "2" and b[1]!="2"):
    resp = 2
else:
    resp = 3

print(resp)