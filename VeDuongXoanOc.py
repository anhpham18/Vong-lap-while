import turtle as t
khoangcach = int(input ("Nhập: "))
i=0
t.speed(0)
while True:
    t.circle(i,30)
    i+=1
    if t.distance(0,0) > khoangcach:
        break
t.done()