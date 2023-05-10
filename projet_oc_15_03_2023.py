import turtle as tr

window = tr.Screen()
window.bgcolor("black")
window.setup(width=600, height=600)

x=50
y=100
r=10

def setup():
    size(300,200)


def draw():
    background(0,0,0)
    global x,y,r
    ellipse(x,y,2*r,2*r)