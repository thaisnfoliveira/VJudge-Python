s = input()

bottoms = 0
for i in s:
    if(i == "v"):
        bottoms += 1
    if(i == "w"):
        bottoms += 2

print(bottoms)