"""
super() function
----------------
super is used to call parent class constructor
"""


class PlanDetails:

    def __init__(self, data_speed, usage_limit):
        self.data_speed = data_speed
        self.usage_limit = usage_limit


class BroadBand(PlanDetails):

    def __init__(self, data_speed, usage_limit, model_name):
        super().__init__(data_speed, usage_limit)
        self.model_name = model_name


interObj = BroadBand("200", "3000", "sony")
print(interObj.data_speed)
print(interObj.usage_limit)
print(interObj.model_name)
