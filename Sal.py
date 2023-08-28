import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")  # Set background color to black

# Create a turtle instance
t = turtle.Turtle()
t.speed(0)  # Set the drawing speed (0 = fastest)
t.pensize(2)  # Set pen thickness

# Function to draw a colorful spiral
def draw_spiral():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    for i in range(360):
        t.pencolor(colors[i % 6])
        t.forward(i)
        t.left(59)

# Function to draw a colorful flower
def draw_flower():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    t.penup()
    t.goto(0, 200)
    t.pendown()
    for i in range(36):
        t.color(colors[i % 6])
        t.forward(100)
        t.left(170)
    t.hideturtle()

# Function to draw a square spiral
def draw_square_spiral():
    length = 10
    for _ in range(36):
        for _ in range(4):
            t.forward(length)
            t.left(90)
        t.right(10)
        length += 10

# Call the animation functions
draw_spiral()
t.reset()  # Clear the screen
draw_flower()
t.reset()  # Clear the screen
draw_square_spiral()

# Keep the window open until the user closes it
turtle.done()
