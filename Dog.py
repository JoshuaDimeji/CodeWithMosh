class Dog():
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed
        print("The dog's name is {}".format(self.name))

    def eat(self,food):
        print("The dog's breed is {} and loves {}".format(self.breed,food))

    def sleepTime(self,time):
        print("{}'s sleep time is {}".format(self.name,time))


dog = Dog("Pudgy","German Shephard")
dog.eat("Treats")
dog.sleepTime("10PM")