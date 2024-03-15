# create a new class

class Sample():
    pass

x = Sample()

print(type(x))

# create a new class with the init function

class Sample():
    def __init__(self, name):
        self.name = name

x = Sample("John")

print(x.name)

# create a new class with the __init__ function and create methods