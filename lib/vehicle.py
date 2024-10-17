class Vehicle:

    def __init__(self, wheel_size, wheel_number):
        self.wheel_number = wheel_number
        self.wheel_size = wheel_size

    def go(self):
        return "vrrrrrrrooom!"  # This is what the test for Vehicle expects

    def fill_up_tank(self):
        return "filling up!"
