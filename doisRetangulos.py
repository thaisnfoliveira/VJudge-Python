a, b, c, d = input().split()

area1 = int(a)*int(b)
area2 = int(c)*int(d)

if area1>area2 or area1==area2:
    print(area1)
else:
    print(area2)
