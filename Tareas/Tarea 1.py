print("Introduce dos numeros enteros")
a = int(input())
b = int(input())
print("Si deseas saber cual es mayor introduce 1, si deseas saber cual es menor introduce 2")
c = int(input())
if c == 1:
    if a > b:
        print (a, "Es mayor que", b)
    else:
        print (b, "Es mayor que", a)
else:
    if a < b:
        print (a, "Es menor que", b)
    else:
        print (b, "Es menor que", a)


