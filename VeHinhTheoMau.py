import turtle as t
t.bgcolor("black")
t.speed(0)
solanlap = 0
gocxoay = 10
r = 100

while solanlap < 360/(6*gocxoay):
    
    t.pencolor("red")
    t.circle(r,90)
    t.circle(r/2,90)
    t.circle(r,90)
    t.circle(r/2,90)
    t.right(gocxoay)
    
    t.pencolor("yellow")
    t.circle(r,90)
    t.circle(r/2,90)
    t.circle(r,90)
    t.circle(r/2,90)
    t.right(gocxoay)

    t.pencolor("blue")
    t.circle(r,90)
    t.circle(r/2,90)
    t.circle(r,90)
    t.circle(r/2,90)
    t.right(gocxoay)

    t.pencolor("purple")
    t.circle(r,90)
    t.circle(r/2,90)
    t.circle(r,90)
    t.circle(r/2,90)
    t.right(gocxoay)

    t.pencolor("green")
    t.circle(r,90)
    t.circle(r/2,90)
    t.circle(r,90)
    t.circle(r/2,90)
    t.right(gocxoay)

    t.pencolor("orange")
    t.circle(r,90)
    t.circle(r/2,90)
    t.circle(r,90)
    t.circle(r/2,90)
    t.right(gocxoay)

    solanlap += 1

t.done()