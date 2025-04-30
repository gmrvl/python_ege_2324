import turtle

t = turtle.Turtle()
#t.tracer(0) #если 0 мгновенно дает результат рисунка и точек
t.reset()
t.seth(90) #ориентации черепашки на определённый угол
t.width(2) #ширина
t.speed(20)
k = 10  # коэффициент для увеличения масштаба
t.right(180)
t.forward(2 * k)
t.right(90)
t.forward(40 * k)
t.right(90)
t.forward(2 * k)

t.forward(2)
for i in range(4):
    t.seth(90)
    t.circle(-5 * k, 180)
t.penup()

for x in range(0, -12, -1):
    for y in range(-2, 8):
        t.goto(x * k, y * k)
        t.dot(5)
turtle.mainloop()