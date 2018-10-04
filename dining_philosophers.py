import threading as thr
import time
from Philosopher import Philosopher


def dining_philosophers():
    philosophers_names = ('platao', 'socrates', 'aristoteles', 'nietzsche', 'kant')

    forks = [thr.Semaphore() for i in range(5)]

    philosophers = [Philosopher(philosophers_names[i], forks[i], forks[(i + 1) % 5], 2, i)
                    for i in range(5)]

    for philosopher in philosophers:
        philosopher.start()

    time.sleep(30)

    return Philosopher.actions


def main():
    actions = dining_philosophers()
    return actions


if __name__ == '__main__':

    main()
