#parent class
class Bird:
    def __init__(self):
        print("Brint is ready")
    def whoisThis(self):
        print("Bird")
    def swim(self):
        print("swim Faster")
#child class
class Penguin(Bird):
    def __init__(self):
        #call super() function
        super().__init__()              #tuong duong voi Brid.__init__()
        print("Penguin is ready")
    def whoisThis(self):
        print("Penguin")
    def run(self):
        print("Run faster")
peggy = Penguin()
peggy.whoisThis()
peggy.swim()
peggy.run()