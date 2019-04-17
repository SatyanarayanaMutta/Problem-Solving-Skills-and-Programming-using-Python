import turtle
cursor=turtle.Turtle()
# Circle draw
cursor.circle(50)
# Triangle draw
cursor.forward(100)
cursor.left(120)
cursor.forward(100)
cursor.left(120)
cursor.forward(100)
# Square draw
for times in range(4):
    cursor.forward(100)
    cursor.left(90)
# Pentagon draw
for i in range(5):
   cursor.forward(100) 
   cursor.right(72)
