from threading import Thread
import time

class Philosopher(Thread):

    def __init__(self, name, left_fork, right_fork, food, finished_dining):
        Thread.__init__(self)
        self.name = name
        self.left_fork = left_fork
        self.right_fork = right_fork
        self.food = food
        self.finished_dining = finished_dining

    def run(self):

        while not self.finished_dining:

            if self.food == 0:
                self.finished_dining = True
                return

            self.think()
            print("{} está com fome".format(self.name))
            self.try_eat()


    def think(self):
        time.sleep(5)
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

        time.sleep(3)
        self.food -= 1
        print("{} terminou de comer, prato tem {} comida".format(self.name, self.food))
