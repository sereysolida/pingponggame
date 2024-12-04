import turtle

player1_name = turtle.textinput("Player Name", "Enter Player 1's name:")
player2_name = turtle.textinput("Player Name", "Enter Player 2's name:")

# Initialize scores
score1 = 0
score2 = 0
winning_score = 5  

# Set up the game screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.title("Ping Pong Game")
screen.setup(width=600, height=400)
screen.tracer(0)

# Optional background image
screen.bgpic("mybackground.gif")

# Paddle 1
paddle1 = turtle.Turtle()
paddle1.shape("square")
paddle1.shapesize(stretch_wid=6, stretch_len=1)
paddle1.color("purple")
paddle1.penup()
paddle1.goto(250, 0)

# Paddle 2
paddle2 = turtle.Turtle()
paddle2.shape("square")
paddle2.shapesize(stretch_wid=6, stretch_len=1)
paddle2.color("yellow")
paddle2.penup()
paddle2.goto(-250, 0)

# Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.shapesize(stretch_len=2, stretch_wid=2)
ball.dx = 0.15  # Increased ball speed in x direction
ball.dy = 0.15  # Increased ball speed in y direction

# Score display
score_board = turtle.Turtle()
score_board.color("purple")
score_board.penup()
score_board.hideturtle()
score_board.goto(0, 150)
score_board.write(f"{player1_name}: 0 VS {player2_name}: 0", align="center", font=("Arial", 15, "bold"))

# Instructions display
instructions = turtle.Turtle()
instructions.color("purple")
instructions.penup()
instructions.hideturtle()
instructions.goto(0, 100)
instructions.write("Press W/S for Player 1 and Up/Down for Player 2", align="center", font=("Arial", 12, "normal"))

# Welcome message
welcome_message = turtle.Turtle()
welcome_message.color("purple")
welcome_message.penup()
welcome_message.hideturtle()
welcome_message.goto(0, 50)
welcome_message.write("Welcome to the Ping Pong Game!", align="center", font=("Arial", 20, "bold"))

# Begin message
begin_message = turtle.Turtle()
begin_message.color("purple")
begin_message.penup()
begin_message.hideturtle()
begin_message.goto(0, -50)
begin_message.write("Click to Begin", align="center", font=("Arial", 15, "normal"))

# Paddle movement functions
def paddle1_up():
    y = paddle1.ycor()
    if y < 160:
        paddle1.sety(y + 30)

def paddle1_down():
    y = paddle1.ycor()
    if y > -160:
        paddle1.sety(y - 30)

def paddle2_up():
    y = paddle2.ycor()
    if y < 160:
        paddle2.sety(y + 30)

def paddle2_down():
    y = paddle2.ycor()
    if y > -160:
        paddle2.sety(y - 30)

# Key bindings
screen.listen()
screen.onkeypress(paddle1_up, "w")
screen.onkeypress(paddle1_down, "s")
screen.onkeypress(paddle2_up, "Up")
screen.onkeypress(paddle2_down, "Down")

# Function to start the game after the user clicks
def start_game(x, y):
    screen.onclick(None)  # Disable further click events
    welcome_message.clear()
    begin_message.clear()
    instructions.clear()
    game_loop()  # Start the game loop

# Click event to start the game
screen.onclick(start_game)

# Main game loop function
def game_loop():
    global score1, score2, winning_score

    game_over = False

    while not game_over:
        screen.update()

        # Move the ball
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border collision (top and bottom)
        if ball.ycor() > 190 or ball.ycor() < -190:
            ball.dy *= -1

        # Right paddle collision
        if ball.xcor() > 230 and abs(ball.ycor() - paddle1.ycor()) < 50:
            ball.setx(230)
            ball.dx *= -1
            score1 += 1
            score_board.clear()
            score_board.write(f"{player1_name}: {score1} VS {player2_name}: {score2}", align="center", font=("Arial", 15, "bold"))
        
        # Left paddle collision
        if ball.xcor() < -230 and abs(ball.ycor() - paddle2.ycor()) < 50:
            ball.setx(-230)
            ball.dx *= -1
            score2 += 1
            score_board.clear()
            score_board.write(f"{player1_name}: {score1} VS {player2_name}: {score2}", align="center", font=("Arial", 15, "bold"))

        # Ball misses right paddle
        if ball.xcor() > 310:
            ball.goto(0, 0)
            ball.dx *= -1

        # Ball misses left paddle
        if ball.xcor() < -310:
            ball.goto(0, 0)
            ball.dx *= -1

        # Check for winning condition
        if score1 == winning_score:
            score_board.clear()
            score_board.goto(0, 0)
            score_board.write(f"Congratulations {player1_name}, You Win!", align="center", font=("Arial", 24, "bold"))
            game_over = True

        elif score2 == winning_score:
            score_board.clear()
            score_board.goto(0, 0)
            score_board.write(f"Congratulations {player2_name}, You Win!", align="center", font=("Arial", 24, "bold"))
            game_over = True

    screen.done()  # Close the game window when done

# End the game when clicked
screen.mainloop()
