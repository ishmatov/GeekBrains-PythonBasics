"""1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке
(красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и
завершать скрипт. """

import time
from itertools import cycle


def toggle_color(time_work, text_color):
    print(f"\r{text_color}     ", end="")
    time.sleep(time_work)


order_colors = ["red", "yellow", "green", "yellow"]
time_work = {"red": 7, "yellow": 2, "green": 5}
text_color = {"red": "\033[31m\033[41m", "yellow": "\033[33m\033[43m", "green": "\033[32m\033[42m"}


class TrafficLight:
    __color = None

    def running(self):
        for i in cycle(order_colors):
            self.__color = i
            toggle_color(time_work.get(self.__color), text_color.get(self.__color))


TrafficLight = TrafficLight()
TrafficLight.running()
