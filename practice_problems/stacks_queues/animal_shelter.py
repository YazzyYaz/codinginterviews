class Queue(object):
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        item = self.items[-1]
        self.items.pop()
        return item

class AnimalShelter(object):
    def __init__(self):
        self.dogs = Queue()
        self.cats = Queue()
        self.order = 0

    def enqueue(self, name, type):
        if type == 1:
            self.dogs.enqueue((name, self.order))
            self.order += 1
        elif type == 0:
            self.cats.enqueue((name, self.order))
            self.order += 1

    def dequeue_any(self):
        if not self.dogs or not self.cats:
            return None
        if not self.dogs:
            cat = self.cats.dequeue()
            return cat[0]
        if not self.cats:
            dog = self.dogs.dequeue()
            return dog[0]
        dog = self.dogs.items[-1]
        cat = self.cats.items[-1]
        if dog[1] > cat[1]:
            cat = self.cats.dequeue()
            return cat[0]
        else:
            dog = self.dogs.dequeue()
            return dog[0]
    
    def dequeue_dog(self):
        if not self.dogs:
            return None
        dog = self.dogs.dequeue()
        return dog

    def dequeue_cat(self):
        if not self.cats:
            return None
        cat = self.cats.dequeue()
        return cat

animal_shelter = AnimalShelter()
animal_shelter.enqueue("Stone", 1)
animal_shelter.enqueue("Roger", 1)
animal_shelter.enqueue("Hala", 1)
animal_shelter.enqueue("Wala", 1)
animal_shelter.enqueue("Mala", 1)
animal_shelter.enqueue("Corat", 0)
animal_shelter.enqueue("Morat", 0)
animal_shelter.enqueue("Borat", 0)
animal_shelter.enqueue("Tala", 1)
animal_shelter.enqueue("3ala", 1)
print(animal_shelter.dogs.items)
print(animal_shelter.cats.items)
animal_shelter.dequeue_cat()
print(animal_shelter.dogs.items)
print(animal_shelter.cats.items)
animal_shelter.dequeue_dog()
print(animal_shelter.dogs.items)
print(animal_shelter.cats.items)
animal_shelter.dequeue_any()
print(animal_shelter.dogs.items)
print(animal_shelter.cats.items)
