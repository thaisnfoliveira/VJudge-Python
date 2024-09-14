t = int(input())

resp = ""
for i in range(0, t, 1):
    a, b, c = map(int, input().split())
    if(a<b and b<c):
        resp = "STAIR"
    elif(a<b and b>c):
        resp = "PEAK"
    else:
        resp = "NONE"
    print(resp)