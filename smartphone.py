# Base Class: Device
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def turn_on(self):
        print(f"{self.brand} {self.model} is now powered on!")

# Derived Class: Smartphone
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery_life):
        super().__init__(brand, model)
        self.__storage = storage  # private variable
        self.__battery_life = battery_life  # private variable

    # Getter and Setter for Storage
    def get_storage(self):
        return self.__storage

    def set_storage(self, storage):
        if storage > 0:
            self.__storage = storage
        else:
            print("Storage cannot be negative or zero.")

    # Getter and Setter for Battery life
    def get_battery_life(self):
        return self.__battery_life

    def set_battery_life(self, battery_life):
        if battery_life > 0:
            self.__battery_life = battery_life
        else:
            print("Battery life cannot be negative or zero.")

    def display_info(self):
        print(f"{self.brand} {self.model} - Storage: {self.get_storage()}GB, Battery life: {self.get_battery_life()} hours")

    def take_photo(self):
        print(f"{self.brand} {self.model} 📸: Photo taken!")

    def install_app(self, app_name):
        print(f"{self.brand} {self.model} 📲: Installing {app_name}...")

    def make_call(self, contact):
        print(f"{self.brand} {self.model} 📞: Calling {contact}...")

    def check_battery(self):
        print(f"{self.brand} {self.model} 🔋: Battery life remaining is {self.get_battery_life()} hours.")
    
    def turn_on(self):
        print(f"{self.brand} {self.model} is now powered on and ready to go! 📱")

# Derived Class: Laptop
class Laptop(Device):
    def __init__(self, brand, model, ram, storage):
        super().__init__(brand, model)
        self.__ram = ram  # private variable
        self.__storage = storage  # private variable

    # Getter and Setter for RAM
    def get_ram(self):
        return self.__ram

    def set_ram(self, ram):
        if ram > 0:
            self.__ram = ram
        else:
            print("RAM cannot be negative or zero.")

    # Getter and Setter for Storage
    def get_storage(self):
        return self.__storage

    def set_storage(self, storage):
        if storage > 0:
            self.__storage = storage
        else:
            print("Storage cannot be negative or zero.")

    def display_info(self):
        print(f"{self.brand} {self.model} - RAM: {self.get_ram()}GB, Storage: {self.get_storage()}GB")

    def turn_on(self):
        print(f"{self.brand} {self.model} laptop is powering up! 💻")

# Main Program to Test the Classes

# Create instances
smartphone = Smartphone("Samsung", "Galaxy S21", 128, 24)
laptop = Laptop("Dell", "XPS 13", 16, 512)

# Display initial info
smartphone.display_info()
laptop.display_info()

# Modify private attributes using setters
smartphone.set_storage(256)  # Update storage
smartphone.set_battery_life(30)  # Update battery life

laptop.set_ram(32)  # Update RAM
laptop.set_storage(1024)  # Update storage

# Display updated info
print("\nAfter updating attributes:")
smartphone.display_info()
laptop.display_info()

# Test polymorphism by calling turn_on()
smartphone.turn_on()
laptop.turn_on()

# Test other methods in Smartphone class
smartphone.take_photo()
smartphone.install_app("Instagram")
smartphone.make_call("Mom")
smartphone.check_battery()
