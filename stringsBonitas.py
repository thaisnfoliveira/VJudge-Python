w = input()

status = 0
for i in w:
    if w.count(i) % 2 != 0:
        status = 1
        break

if status==0:
    print("Yes")
else:
    print("No")