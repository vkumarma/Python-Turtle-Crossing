import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
player = Player()

screen.onkey(fun=player.moveforward, key="Up")
car_manager = CarManager()
scoreboard = Scoreboard()



game_is_on = True
num = 0
while game_is_on:
    time.sleep(car_manager.car_speed)
    screen.update()

    # Generating cars.
    car_manager.move_cars()
    if num % 10 == 0:
        car_manager.generate_car()
    num += 1

    # Checking collision with Turtle.
    for car in car_manager.cars:
        # if car.distance(car_manager[1::]) < 10:
        #     car_manager.cars.remove(car)
        if player.distance(car) < 15:
            game_is_on = False

    # Checking if reached finish line.
    if player.check_reached_finish_line():
        scoreboard.update_level()
        car_manager.speed_increment()

scoreboard.game_over()


screen.exitonclick()