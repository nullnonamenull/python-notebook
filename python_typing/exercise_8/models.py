class Brewery:
    def __init__(self, id: int, name: str,
                 brewery_type: str, street: str,
                 city: str, state: str, postal_code: str,
                 country: str, longitude: float,
                 latitude: float, website_url: str, phone: str):
        self.id = id
        self.name = name
        self.brewery_type = brewery_type
        self.street = street
        self.city = city
        self.state = state
        self.postal_code = postal_code
        self.country = country
        self.longitude = longitude
        self.latitude = latitude
        self.website_url = website_url
        self.phone = phone

    def __str__(self):
        return (
            f"ID: {self.id}\n"
            f"Name: {self.name}\n"
            f"Type: {self.brewery_type}\n"
            f"Address: {self.street}, "
            f"{self.city}, {self.state} {self.postal_code}\n"
            f"Country: {self.country}\n"
            f"City: {self.city}\n"
            f"Coordinates: ({self.longitude}, {self.latitude})\n"
            f"Website: {self.website_url}\n"
            f"Phone: {self.phone}\n"
        )
