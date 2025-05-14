class Vehicle:
    def move(self):
        raise NotImplementedError("This method should be overridden by subclasses.")


class Car(Vehicle):
    def move(self):
        print("Driving 🚗")


class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")


class Boat(Vehicle):
    def move(self):
        print("Sailing 🚢")


# Example usage
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
