from threading import Semaphore
import time
from Philosopher import Philosopher

def dining_philosophers():
    philosophers_names = ('Filosofo 1','Filosofo 2','Filosofo 3','Filosofo 4','Filosofo 5')

    forks = [Semaphore() for i in range(5)]

    philosophers = [Philosopher(philosophers_names[i], forks[i], forks[(i + 1) % 5], 2, False)
                    for i in range(5)]

    for philosopher in philosophers:
        philosopher.start()

dining_philosophers()