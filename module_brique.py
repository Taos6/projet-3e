import turtle as tr
import random

window = tr.Screen()
window.bgcolor("black")
window.setup(width=600, height=600)


barre = tr.Turtle()
barre.speed(0)
barre.shape("square")
barre.shapesize(stretch_wid = 1, stretch_len=5)
barre.color("red")
barre.penup()
barre.setposition(0,-50)



window.register_shape("brick",((0,0),(10,0),(10,50),(0,50)))

colors = ["sky blue", "tomato", "lime green","yellow"]


def makeRow(x,y,colors):
  index = random.randint(0,len(colors)-1)
  row = []
  
  for i in range(8):
    
    brique = tr.Turtle()
    brique.speed(0)
    brique.shape("brick")
    brique.color(colors[index])
    brique.penup()
    brique.goto(x + 60*i,y)
    brique.pendown()
    row.append(brique)
    index = random.randint(0,len(colors)- 1)
  return row
makeRow(-230,170,colors)
