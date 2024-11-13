import turtle
import random

# Setup the screen
screen = turtle.Screen()
screen.title("Happy Diwali 2024")
screen.bgcolor("lightpink")  # Background color set to baby pink

# Initialize the turtle
pen = turtle.Turtle()
pen.speed(0)  # Fastest drawing
pen.hideturtle()

# Function to draw a flower
def draw_flower(x, y, size, petal_color, center_color):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(petal_color)

    # Draw petals
    for _ in range(8):
        pen.begin_fill()
        pen.circle(size, 60)
        pen.left(120)
        pen.circle(size, 60)
        pen.left(120)
        pen.end_fill()
        pen.left(45)

    # Draw the flower center
    pen.penup()
    pen.goto(x, y - size / 2)
    pen.pendown()
    pen.color(center_color)
    pen.begin_fill()
    pen.circle(size / 2)
    pen.end_fill()

# Function to draw a flower pot
def draw_flower_pot(x, y, width, height, pot_color):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(pot_color)
    pen.begin_fill()
    for _ in range(2):
        pen.forward(width)
        pen.right(90)
        pen.forward(height)
        pen.right(90)
    pen.end_fill()

# Function to write text on the screen
def write_text(x, y, text, font_size, color):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color(color)
    pen.write(text, align="center", font=("Comic Sans MS", font_size, "bold"))

# Function to draw sparkles
def draw_sparkle(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color("white")
    for _ in range(5):
        pen.forward(10)
        pen.backward(10)
        pen.right(144)

# Drawing flowers and pots
flower_data = [
    (-200, 50, 40, "pink", "yellow"),
    (0, 50, 50, "orange", "red"),
    (200, 50, 40, "lightblue", "purple")
]
pot_data = [
    (-220, -30, 50, 30, "saddlebrown"),
    (-20, -30, 50, 30, "saddlebrown"),
    (180, -30, 50, 30, "saddlebrown")
]

for (x, y, size, petal, center) in flower_data:
    draw_flower(x, y, size, petal, center)

for (x, y, width, height, color) in pot_data:
    draw_flower_pot(x, y, width, height, color)

# Displaying the Diwali message in red
write_text(0, 200, "Happy Diwali 2024", 30, "red")

# Draw sparkles around the flowers
for _ in range(10):
    draw_sparkle(random.randint(-250, 250), random.randint(-100, 250))

# Keep the window open
screen.mainloop()
