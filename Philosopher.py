from threading import Thread
import time

class Philosopher(Thread):

    actions = []

    def __init__(self, name, left_fork, right_fork, food):
        Thread.__init__(self)
        self.name = name
        self.left_fork = left_fork
        self.right_fork = right_fork
        self.food = food

    def run(self):

        while True:
            if self.food == 0:
                self.actions.append("{} terminou".format(self.name))
                break

            self.think()
            self.actions.append("{} fome".format(self.name))
            print("{} está com fome".format(self.name))

            self.try_eat()


    def think(self):
        self.actions.append("{} pensando".format(self.name))
        print("{} está pensando".format(self.name))
        time.sleep(3)
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
        self.actions.append("{} comendo".format(self.name))
        time.sleep(3)
        self.food -= 1
        print("{} terminou de comer, prato tem {} comida".format(self.name, self.food))
