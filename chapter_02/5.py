class Five:
    school = 'Carmel school'

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def average(self):
        return (self.a + self.b + self.c) / 3

    def get_a(self):
        return self.a

    def set_a(self, value):
        self.a = value

    @classmethod
    def info(cls):
        return cls.school

    @staticmethod
    def get_school():
        print("this is student class")


s1 = Five(11, 22, 33)
print(s1.average())
print(Five.school)
Five.get_school()
