import threading as thr
import time


class Philosopher(thr.Thread):

    actions = []

    def __init__(self, name, left_fork, right_fork, food, identifier):
        thr.Thread.__init__(self)
        self.name = name
        self.left_fork = left_fork
        self.right_fork = right_fork
        self.food = food
        self.identifier = identifier

    def run(self):

        while True:
            if self.food == 0:
                self.actions.append("{}-finished-{}".format(self.identifier, self.food))
                break

            self.think()
            self.actions.append("{}-hungry-{}".format(self.identifier, self.food))
            print("{} está com fome".format(self.name))

            self.try_eat()

    def think(self):
        self.actions.append("{}-thinking-{}".format(self.identifier, self.food))
        print("{} esta pensando".format(self.name))
        time.sleep(1)
        return

    def try_eat(self):

        self.left_fork.acquire()
        fork_available = self.right_fork.acquire()

        if not fork_available:
            self.left_fork.release()
            return

        self.eating()

        self.left_fork.release()
        self.right_fork.release()

    def eating(self):
        print("{} começou a comer".format(self.name))

        self.actions.append("{}-eating-{}".format(self.identifier, self.food))
        time.sleep(4)
        self.food -= 1

        self.actions.append("{}-eating-{}".format(self.identifier, self.food))

        print("{} terminou de comer, prato tem {} comida".format(self.name, self.food))
