class Ball():
    def __init__(self,name,colour):
        self.name = name
        self.colour = colour
        print(f"The ball is a {self.name} and the colour is {self.colour}")

    def kick(self,goals):
        self.goals = goals
        print("The ball was kicked to score {} goals ".format(self.goals))


ball = Ball("leather ball","brown")
ball.kick("3")