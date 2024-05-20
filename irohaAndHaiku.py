syllabes = input().split()

n5 = 0
n7 = 0

for i in syllabes:
    if int(i)==5:
        n5 += 1
    if int(i) == 7:
        n7 += 1

if n5 == 2 and n7 == 1:
    print("YES")
else:
    print("NO")