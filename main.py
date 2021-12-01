import turtle as t
import time
from snake import Snake
from food import Food
from scoreboard import Score
screen = t.Screen()
screen.setup(600,600)
screen.title('Snake')
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down, "Down")
game_is_on=True
score = Score()

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


    #detect collision with food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.add_one()
        score.add_score()
        score.update_scoreboard()


    if snake.head.xcor() >280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    for segment in snake.snakes[1:]:
        if snake.head.distance(segment) <10:
            game_is_on = False
            score.game_over()













screen.exitonclick()
