class Property:
    def __init__(self, area: int, rooms: int, price: int, address: str):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return (f"Property at "
                f"{self.address}\nArea: {self.area} sq.m."
                f"\nRooms: {self.rooms}"
                f"\nPrice: {self.price} PLN")


class House(Property):
    def __init__(self, area: int,
                 rooms: int, price: int,
                 address: str, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return (
            f"House at {self.address}\n"
            f"Area: {self.area} sq.m.\n"
            f"Rooms: {self.rooms}\n"
            f"Price: {self.price} PLN\n"
            f"Plot: {self.plot} sq.m."
        )


class Flat(Property):
    def __init__(self, area: int,
                 rooms: int, price: int,
                 address: str, floor: int):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return (
            f"Flat at {self.address}\n"
            f"Area: {self.area} sq.m.\n"
            f"Rooms: {self.rooms}\n"
            f"Price: {self.price} PLN\n"
            f"Floor: {self.floor}"
        )
