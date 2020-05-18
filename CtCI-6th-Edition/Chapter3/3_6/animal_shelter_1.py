# Q. An animal shelter, which holds only dogs and cats, operates on a strictly
# "first in, first out" basis. People must adopt either the "oldest" (based on
# arrival time) of all animals at the shelter, or they can select whether they
# would prefer a dog or a cat (and will receive the oldest animal of that
# type). They cannot select which specific animal they would like. Create the
# data structures to maintain the system and implement operations such as
# enqueue, dequeueAny, dequeueDog, and dequeueCat. You may use the built-in
# LinkedList data structure.

import unittest
from collections import deque
from datetime import datetime


class QueueEmpty(Exception):
    pass


class Animal:
    def __init__(self):
        self.created_at = datetime.utcnow()


class Dog(Animal):
    def __init__(self, name):
        self.name = name
        super().__init__()


class Cat(Animal):
    def __init__(self, name):
        self.name = name
        super().__init__()


class AnimalShelter:
    def __init__(self):
        self.dogs = deque()
        self.cats = deque()

    def enqueue(self, animal: Animal):
        if isinstance(animal, Dog):
            self.dogs.append(animal)
        elif isinstance(animal, Cat):
            self.cats.append(animal)
        else:
            raise TypeError

    def dequeue_any(self):
        dog = cat = None
        try:
            dog = self.peek_dog()
        except QueueEmpty:
            pass
        try:
            cat = self.peek_cat()
        except QueueEmpty:
            pass
        if not (dog or cat):
            raise QueueEmpty
        if not cat or dog.created_at < cat.created_at:
            return self.dequeue_dog()
        if not dog or dog.created_at >= cat.created_at:
            return self.dequeue_cat()

    def peek_dog(self):
        if not self.dogs:
            raise QueueEmpty
        return self.dogs[0]

    def peek_cat(self):
        if not self.cats:
            raise QueueEmpty
        return self.cats[0]

    def dequeue_dog(self):
        if not self.dogs:
            raise QueueEmpty
        return self.dogs.popleft()

    def dequeue_cat(self):
        if not self.cats:
            raise QueueEmpty
        return self.cats.popleft()


class TestAnimalShelter(unittest.TestCase):
    def test_enqueue_dequeue(self):
        ani_she = AnimalShelter()
        d1 = Dog("tommy")
        c1 = Cat("tinkles")
        d2 = Dog("bruno")
        ani_she.enqueue(d1)
        ani_she.enqueue(c1)
        ani_she.enqueue(d2)
        self.assertEqual(d1, ani_she.dequeue_any())
        self.assertEqual(d2, ani_she.dequeue_dog())
        self.assertEqual(c1, ani_she.dequeue_cat())

    def test_queue_empty(self):
        ani_she = AnimalShelter()
        d1 = Dog("tommy")
        c1 = Cat("tinkles")
        with self.assertRaises(QueueEmpty):
            ani_she.dequeue_any()
        with self.assertRaises(QueueEmpty):
            ani_she.dequeue_dog()
        with self.assertRaises(QueueEmpty):
            ani_she.dequeue_cat()
        ani_she.enqueue(d1)
        with self.assertRaises(QueueEmpty):
            ani_she.dequeue_cat()
        d1, ani_she.dequeue_dog()
        ani_she.enqueue(c1)
        with self.assertRaises(QueueEmpty):
            ani_she.dequeue_dog()
        c1, ani_she.dequeue_cat()
        with self.assertRaises(QueueEmpty):
            ani_she.dequeue_any()
        with self.assertRaises(QueueEmpty):
            ani_she.dequeue_dog()
        with self.assertRaises(QueueEmpty):
            ani_she.dequeue_cat()


if __name__ == "__main__":
    unittest.main()
