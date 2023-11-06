from Classes import Dog, Cat

if __name__ == '__main__':
    dog = Dog("Ghost", "Dog")
    cat = Cat("Jimmy", "Cat")

    print(f"{dog.name} says: {dog.speak()}")
    print(f"{cat.name} says: {cat.speak()}")
