from . import PyGame, Drawer, Counter
from random import randint
import pygame
import threading
import time


class Sorting(PyGame):
    def __init__(self, width=1280, height=720, border=10, header=100, max_speed=100, speed=50,
                 fps=60, background="black", candles="white", list_len=10, phase_wait=1):
        super().__init__(width, height, fps, background)
        self.drawer = Drawer(self.screen, border, header, candles)
        self.counter = Counter()

        self.max_speed = max_speed
        self.speed = speed
        self.phase_wait = phase_wait

        self.candles = candles
        self.list = list(range(1, list_len + 1))
        self.sorted = True
        self.stop = False

        self.shuffle_thread = threading.Thread(target=self.shuffle)
        self.sort_thread = threading.Thread(target=self.sort_buble_v2)
        # self.sort_thread = threading.Thread(target=self.sort_buble)
        self.active_candles = {}

    def change_speed(self, value: int | float):
        if 0 <= value <= self.max_speed:
            self.speed = value
        else:
            self.speed = self.max_speed

    def sleep(self):
        time.sleep(1 - self.speed / self.max_speed)

    def shuffle(self):
        time.sleep(self.phase_wait)
        for i in range(1):
            for index in range(0, len(self.list)):
                rand_index = randint(0, len(self.list) - 1)

                self.active_candles = {
                    index: 'green',
                    rand_index: 'red'
                }

                self.list[index], self.list[rand_index] = self.list[rand_index], self.list[index]
                self.sleep()

    def sort_buble(self):
        self.shuffle_thread.join()
        time.sleep(self.phase_wait)
        for i in range(0, len(self.list)):
            for j in range(0, i):
                self.active_candles = {
                    i: 'green',
                    j: 'red'
                }

                self.counter.comparisons += 1
                self.counter.arr_access += 2
                if self.list[j] > self.list[i]:
                    self.counter.arr_access += 2
                    self.list[j], self.list[i] = self.list[i], self.list[j]

                self.sleep()

    def buble_adds(self, index):
        self.counter.comparisons += 1
        self.counter.arr_access += 2

        if index > 0 and self.list[index - 1] > self.list[index]:
            self.active_candles[index] = 'red'
            self.active_candles[index - 1] = 'green'
            self.list[index], self.list[index - 1] = self.list[index - 1], self.list[index]

            self.counter.arr_access += 2
            self.buble_adds(index - 1)


    def sort_buble_v2(self):
        self.shuffle_thread.join()
        time.sleep(self.phase_wait)

        for index in range(0, len(self.list)):
            self.active_candles = {index: 'green'}
            self.buble_adds(index)
            self.sleep()


    def step(self):
        self.drawer.draw_list(self.list, self.active_candles)
        self.drawer.draw_text(
            text1=f"Buble sort - {self.counter.comparisons} comparisons, {self.counter.arr_access} array accesses.",
            text2=f"Speed: {int(self.speed)}"
        )

        if pygame.key.get_pressed()[pygame.K_UP]:
            self.change_speed(self.speed + self.max_speed / 2000)
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.change_speed(self.speed - self.max_speed / 2000)

    def start(self):
        self.shuffle_thread.start()
        self.sort_thread.start()

        self.game_run(self.step)
