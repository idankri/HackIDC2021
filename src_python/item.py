class Item:
    def __init__(self, name="", price=0, image=""):
        self.name = name
        self.price = price
        self.image = image

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_image(self):
        return self.image

    def set_name(self, name):
        self.name = name

    def set_price(self, price):
        self.price = price

    def set_image(self, image):
        self.image = image
