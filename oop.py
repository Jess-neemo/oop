class Smartphone:
    def __init__(self, brand, model, storage_gb):
        self.brand = brand
        self.model = model
        self.storage_gb = storage_gb

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def info(self):
        print(f"Smartphone: {self.brand} {self.model}, Storage: {self.storage_gb}GB")

# Inheritance example: GamingSmartphone inherits from Smartphone
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage_gb, gpu_model):
        super().__init__(brand, model, storage_gb)
        self.gpu_model = gpu_model

    def play_game(self, game_name):
        print(f"Playing {game_name} on {self.brand} {self.model} with GPU {self.gpu_model}")

    # Overriding info method (polymorphism)
    def info(self):
        print(f"Gaming Smartphone: {self.brand} {self.model}, Storage: {self.storage_gb}GB, GPU: {self.gpu_model}")

# Example usage:
phone = Smartphone("Apple", "iPhone 14", 128)
phone.info()
phone.call("123-456-7890")

gaming_phone = GamingSmartphone("ASUS", "ROG Phone 6", 256, "Adreno 660")
gaming_phone.info()
gaming_phone.call("987-654-3210")
gaming_phone.play_game("Call of Duty Mobile")



#activity 2
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing ⛵")

# Example usage:
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
