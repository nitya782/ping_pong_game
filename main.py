import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
scoreboard = Scoreboard()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")

player = Player()
screen.listen()
screen.onkey(player.up, "Up")

car_manager = CarManager()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    for car in car_manager.all_cars :
       if car.distance(player) < 20:
           game_is_on = False
    if player.is_finish_line():
        player.goto_start()
        car_manager.speed_up_car()
        scoreboard.level_up()

screen.exitonclick()