COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
from turtle import Turtle
import random
class CarManager():
    def __init__(self):
        super().__init__()
        self.cars = []
        self.numbers = []
        self.generate_car()
        self.car_speed = 0.1


    def generate_car(self):
        car = Turtle("square")
        car.penup()
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.setheading(180)
        car.color(random.choice(COLORS))
        number = random.randint(-250, 250)
        self.numbers.append(number)
        while number in self.numbers:
            number = random.randint(-250, 250)

        car.goto(280, number)
        self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE)
        print(len(self.cars))


    def speed_increment(self):
        self.car_speed /= (MOVE_INCREMENT/4)
        print(f"car speed: {self.car_speed}")






