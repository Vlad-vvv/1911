class Student:
    count_of_stydent = 0
    def __init__(self, name=None, height = 160, brain = 10):
        self.name = name
        self.height = height
        self.brain = brain
        Student.count_of_stydent += 1
        print("Ку")

    def grow(self, height=1):
        self.height += height

    def brain_grow(self, brain=1):
        self.brain += brain

    def __str__(self):
        return f'Привіт. Я {self.name}, мій зріст {self.height} cm, мій розум {self.brain} '

    def __del__(self):
        print(f'Привіт. Я {self.name}, я пішов ')



Alex = Student(name='Alex', height=143, brain=10)
print(Alex)
print(Alex.count_of_stydent)
Alex.grow(15)
Alex.brain_grow(3)
print(Alex.height)
print(Alex.brain)
