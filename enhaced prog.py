import time
import turtle
from turtle import Turtle, Screen
turtle. screensize(20, 20, "white")
screen = Screen()
pen = turtle
pen.shape("turtle")
pen.color("black")
pen.pensize(5)

# Hexagon
pen.penup()
pen.goto(-295, 80)
pen.down()
pen.circle(radius=80, steps=6)
# Triangle
pen.penup()
pen.goto(-100, 90)
pen.down()
pen.circle(radius=80, steps=3)
# Square/Diamond
pen.penup()
pen.goto(90, 80)
pen.down()
pen.circle(radius=80, steps=4)
# Pentagon
pen.penup()
pen.goto(295, 80)
pen.down()
pen.circle(radius=80, steps=5)
# Circle
pen.penup()
pen.goto(-295, -200)
pen.down()
pen.circle(radius=80)
# Heart
pen.penup()
pen.goto(-0, -250)
pen.down()
pen.left(150)
pen.forward(180)
pen.circle(-90, 180)
pen.setheading(60)
pen.circle(-90, 180)
pen.forward(180)
pen.speed(10)
# spirograph
pen.penup()
pen.goto(240, -150)
pen.down()
pen.hideturtle()

# Using time to make the text appear to the console as if being type by a typewriter
# This is applicable to text1,text3,text4,text5 and to the delays
while True:
    screen = Screen()
    text1 = "Hello and Welcome, Wanna combine colors?"
    for char in text1:
        print(char, end='', flush=True)
        time.sleep(0.050)

    text2 = int(input("\nIf yes press 1"
                      "\nIf you're not interested press 2"
                      "\nEnter here:"))

    if text2 == 1:
        print("Valid input")
    elif text2 == 2:
        print("Program stop.")
        screen.bye()  # Close the turtle graphics window
        break  # Exit the loop
    else:
        print("Invalid input. Refer to the choices.")

    print("\n========================="
          "\n====LET'S GET STARTED===="
          "\n=========================")

    # Adding delay
    delay_second = 1
    time.sleep(delay_second)

    text3 = "\n****Select your primary color****"
    for char in text3:
        print(char, end='', flush=True)
        time.sleep(0.050)

    # Using selections to variables color1, color2 to get the desired output based on the input of the user
    color1 = int(input('\nPress 1 for RED'
                       '\nPress 2 for YELLOW'
                       '\nPress 3 for BLUE '
                       '\nEnter here:'))
    if color1 == 1:
        print("You have selected RED")
    elif color1 == 2:
        print("You have selected YELLOW")
    elif color1 == 3:
        print("You have selected BLUE")
    else:
        print("The input is invalid, refer to the choices.")

    print("\n============================================================"
          "\n------------------------------------------------------------"
          "\n-----NOW LET'S PROCEED ON SELECTING THE SECONDARY COLORS-----"
          "\n------------------------------------------------------------"
          "\n============================================================")

    # Adding delay after the text
    delay_second = 1
    time.sleep(delay_second)

    text4 = "\n*****Select your secondary color*****"
    for char in text4:
        print(char, end='', flush=True)
        time.sleep(0.050)

    color2 = int(input("\nPress 5 for GREEN"
                       "\nPress 6 for ORANGE "
                       "\nPress 7 for PURPLE"
                       "\nEnter here:"))
    if color2 == 5:
        print("You have selected GREEN ")
    elif color2 == 6:
        print("You have selected ORANGE ")
    elif color2 == 7:
        print("You have selected PURPLE ")
    else:
        print("The input is invalid, refer to the choices.")

    print("\n=================================================="
          "\n-----THE RESULT OF THE COLORS YOU HAVE CHOSEN-----"
          "\n==================================================")

    # Adding delay after the text
    delay_second = 1
    time.sleep(delay_second)

    text5 = "\nThe tertiary result is:"
    for char in text5:
        print(char, end='', flush=True)
        time.sleep(0.050)

    # Combining two variables by multiplying the number inputs of the user
    inputs = color1 * color2

    tertiary_result = ""
    if inputs == 5:
        tertiary_result = "YELLOW\nColor Code: #FFFF00"
    elif inputs == 6:
        tertiary_result = "VERMILION\nColor code: #E34234"
    elif inputs == 7:
        tertiary_result = "MAGENTA/RED-VIOLET\nColor code: #C71585"
    elif inputs == 10:
        print("YELLOW-GREEN"
              "\nColor code: #9ACD32")
    elif inputs == 12:
        print("AMBER"
              "\nColor code: #FFBF00")
    elif inputs == 14:
        print("BROWN"
              "\nColor code: #964B00")
    elif inputs == 15:
        print("TEAL"
              "\nColor code: #008080")
    elif inputs == 18:
        print("REDDISH-BROWN OF BURNT SIENNA"
              "\nColor code: #E97451")
    elif inputs == 21:
        print("BLUE-VIOLET"
              "\nColor code: #8a2be2")

    # Add more conditions for other cases

    print(f"\n{tertiary_result}")

    # Adding delay in order for the next process not to appear together with the tertiary result
    delay_seconds = 2
    time.sleep(delay_seconds)

    # Asking the user for input
    shape_selector = int(input("\nIn what shape do you want this color to be filled?"
                               "\n[1] Hexagon"
                               "\n[2] Triangle(4 sides)"
                               "\n[3] Square/Diamond(3 sides)"
                               "\n[4] Pentagon(5 sides)"
                               "\n[5] Circle(6 sides)"
                               "\n[6] Heart"
                               "\nEnter here:"))

    # Importing turtle inside the Multi-way if-elif-else Statements
    pen = Turtle()
    pen.hideturtle()

    if shape_selector == 1:
        tcolor = str(input("Enter color code:"))
        pen.shape("turtle")
        pen.speed(5)

        pen.up()
        pen.goto(-295, 80)
        pen.pendown()
        pen.begin_fill()
        pen.color(tcolor)
        pen.circle(radius=80, steps=6)
        pen.end_fill()

        time.sleep(10)  # Adding a delay for visibility

    elif shape_selector == 2:
        tcolor = str(input("Enter color code:"))
        pen.shape("turtle")
        pen.speed(5)

        pen.penup()
        pen.goto(-100, 90)
        pen.begin_fill()
        pen.color(tcolor)
        pen.circle(radius=80, steps=3)
        pen.end_fill()

        time.sleep(10)  # Adding a delay for visibility

    elif shape_selector == 3:
        tcolor = str(input("Enter color code:"))
        pen.shape("turtle")
        pen.speed(5)

        pen.penup()
        pen.goto(90, 80)
        pen.down()
        pen.begin_fill()
        pen.color(tcolor)
        pen.circle(radius=80, steps=4)
        pen.end_fill()

        time.sleep(10)  # Adding a delay for visibility

    elif shape_selector == 4:
        tcolor = str(input("Enter color code:"))
        pen.shape("turtle")
        pen.speed(5)

        pen.penup()
        pen.goto(295, 80)
        pen.down()
        pen.begin_fill()
        pen.color(tcolor)
        pen.circle(radius=80, steps=5)
        pen.end_fill()

        time.sleep(10)  # Adding a delay for visibility

    elif shape_selector == 5:
        tcolor = str(input("Enter color code:"))
        pen.shape("turtle")
        pen.speed(5)

        pen.penup()
        pen.goto(-295, -200)
        pen.down()
        pen.begin_fill()
        pen.color(tcolor)
        pen.circle(radius=80)
        pen.end_fill()

        time.sleep(10)  # Adding a delay for visibility

    elif shape_selector == 6:
        tcolor = str(input("Enter color code:"))
        pen.shape("turtle")
        pen.speed(5)

        pen.penup()
        pen.goto(-0, -250)
        pen.down()
        pen.left(150)
        pen.forward(180)
        pen.circle(-90, 180)
        pen.setheading(60)
        pen.circle(-90, 180)
        pen.forward(180)
        pen.begin_fill()
        pen.color(tcolor)
        pen.end_fill()
        pen.speed(10)

        time.sleep(10)  # Adding a delay for visibility

    else:
        print("Can't read input.")

    screen.update()  # Update the turtle screen
