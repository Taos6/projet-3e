import turtle as tr

window = tr.Screen()
window.bgcolor("black")
window.setup(width=600, height=600)


barre = tr.Turtle()
barre.speed(0)
barre.shape("square")
barre.shapesize(stretch_wid = 1, stretch_len=5)
barre.color("red")
barre.penup()
barre.setposition(0,-225)

def aller_droite():
    print("test")
    barre.forward(30)
    
def aller_gauche():
    barre.backward(30)
 
print("test")
 
tr.onkey(aller_droite,"d")
tr.onkey(aller_gauche,"a")
window.listen()