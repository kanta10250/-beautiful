import turtle
import random

# 画面設定

turtle.speed(0)
turtle.pensize(2)

# 初期位置設定
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()

# 色のリスト
colors = ["red", "green", "blue", "yellow", "pink", "white", "purple", "orange"]

a = 0
b = 0

# 描画処理
while b < 200:
    turtle.forward(a)
    turtle.right(b)
    a += 3
    b += 1
    turtle.pencolor(random.choice(colors))

turtle.exitonclick()
