"""
multiple Inheritance:

"""


class PanClass:
    def __init__(self):
        self.panNumber = "PAN"
        print('from pan class')


class AdharClass(PanClass):
    def __init__(self):
        PanClass.__init__(self)
        self.aadharNumber = "23232323232"
        print('from aadhar class')
        print(self.panNumber)


class Bank(AdharClass):
    def __init__(self):
        super().__init__()
        # AdharClass.__init__(self)

    def customer_details(self):
        print(self.aadharNumber)
        print(self.panNumber)


obj = Bank()
obj.customer_details()
