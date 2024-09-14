t = int(input())
jogos = input()

a = 0
d = 0

for i in jogos:
    if(i == "A"):
        a+=1
    else:
        d+=1

resp = ""
if(a>d):
    resp = 'Anton'
elif(a<d):
    resp = 'Danik'
else:
    resp = "Friendship"

print(resp)