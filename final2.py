import turtle

def branch(t, order, size):
    if order == 0:
        t.forward(size)
        t.backward(size)
    else: 
        t.forward(size)
        t.left(45)
        branch(t, order - 1, size / (2 ** 0.5))
        t.right(90)
        branch(t, order - 1, size / (2 ** 0.5))
        t.left(45)
        t.backward(size)
                 
def draw_pythagoras_tree(order, size = 150):
    window = turtle.Screen()
    window.bgcolor("white")
    
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(0, - 200)
    t.pendown()
    t.left(90)  
  
    
    branch(t, order, size)
    
    window.mainloop()
        
order = int(input("Set the recursion Level to: "))        
draw_pythagoras_tree(order)

