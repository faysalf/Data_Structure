import turtle
left = turtle.Turtle()
front = turtle.Turtle()
left.shape("circle")
front.shape("square")
print(left.left(30))        #angle in degree
print(left.forward(100))    #front in pixel
print(front.backward(50))   #left in backward
monte = turtle.Turtle()
monte.setpos(-100, -100)    #(row,column) position: third quarter form middle
monte.forward(30)
monte.clear()
left.clear()
front.clear()
front.shape("square")
monte.shape("triangle")
