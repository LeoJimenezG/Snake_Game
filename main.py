from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

# Establish screen configurations
screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Snake Game")
# con tracer desactivamos la animación hasta que con "update" la volvamos a activar
screen.tracer(0)

# Instances of created classes
snake = Snake()
food = Food()
score = Score()

# Ask if the user wants to play
user_play = screen.textinput(title="Snake Game", prompt="Dou you want to play? Y/N").upper()
if user_play == "Y":
    game_on = True
else:
    game_on = False

# Call functions when certain keys are pressed
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

# Make a continuos process
while game_on:
    # Con update se actualiza la screen
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Check if the snake's head is close enough to the food
    if snake.head.distance(food) < 15:
        snake.increase_body()
        food.go_random()
        score.add_score()

    # Check if the snake's head is at any of the edges of the screen
    if snake.head.xcor() > 390 or snake.head.xcor() < -390 or snake.head.ycor() > 390 or snake.head.ycor() < -390:
        score.game_over()
        snake.reset_snake()

    # Use the list of the snake's body parts
    for i in snake.snake_body[1:]:
        # Check if the snake's head is very close to any of its parts
        if snake.head.distance(i) < 10:
            score.game_over()
            snake.reset_snake()


screen.exitonclick()
