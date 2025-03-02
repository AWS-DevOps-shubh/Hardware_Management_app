class Asset:
    def __init__(self, name, category, serial_number, location, status="Available"):
        self.name = name
        self.category = category
        self.serial_number = serial_number
        self.location = location
        self.status = status