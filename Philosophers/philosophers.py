import multiprocessing
import time
import random


def deadlock_eat(i, forks):
    min_wait = 0.1
    max_wait = 0.8

    def rand_wait():
        time.sleep(random.uniform(min_wait, max_wait))

    while True:
        f1 = forks[i - 1]
        f2 = forks[i]

        # think before picking up left fork
        rand_wait()
        f1.acquire()
        print(f"Philosopher {i} got fork{i - 1} ")

        # think before picking up right fork
        rand_wait()
        f2.acquire()
        print(f"Philosopher {i} got fork {i} ")

        # eat
        time.sleep(0.3)
        print(f"Philosopher {i} is eating...")

        # put down forks
        f1.release()
        print(f"Philosopher {i} put down fork {i - 1} ")
        f2.release()
        print(f"Philosopher {i} put down fork {i} ")


def safe_eat(i, forks):
    min_wait = 0.1
    max_wait = 0.2

    def rand_wait():
        time.sleep(random.uniform(min_wait, max_wait))

    while True:
        if i % 2 == 0:
            first_i = i - 1
            second_i = i
        else:
            first_i = i
            second_i = i - 1
        f1 = forks[first_i]
        f2 = forks[second_i]

        # think before picking up left fork
        rand_wait()
        f1.acquire()
        print(f"Philosopher {i} got fork{first_i} ")

        # think before picking up right fork
        rand_wait()
        f2.acquire()
        print(f"Philosopher {i} got fork {second_i} ")

        # eat
        time.sleep(0.3)
        print(f"Philosopher {i} is eating...")

        # put down forks
        f1.release()
        print(f"Philosopher {i} put down fork {first_i} ")
        f2.release()
        print(f"Philosopher {i} put down fork {second_i} ")



def main():
    philosophers_num = 5
    forks = [multiprocessing.Semaphore() for _ in range(philosophers_num)]
    philosophers = [multiprocessing.Process(target=safe_eat, args=(i, forks)) for i in range(philosophers_num)]
    for p in philosophers:
        p.start()


if __name__ == '__main__':
    main()
