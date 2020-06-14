# door middel van object-oriented programming worden in dit bestand classes vastgesteld
import random as rd

#borders
class Borders:
    def __init__(self):
        self.maxX = 160
        self.maxY = 180
class Water:
    """Initializes water"""
    def __init__(self, id, name, width, length, x0, x1, y0, y1):
        self.width = width
        self.length = length
        self.id = id
        self.name = name
        self.x0 = x0
        self.x1 = x1
        self.y0 = y0
        self.y1 = y1

class House:
    def __init__(self, type, house_number, x=None, y=None):

        if type == "sfh":
            self.name = "sfh"
            self.length = 8
            self.width = 8
            self.price = 285000
            self.free_area = 2
            self.price_increasement = float(0.03)

        if type == "bungalow":
            self.name = "bungalow"
            self.length = 7
            self.width = 11
            self.price = 399000
            self.free_area = 3
            self.price_increasement = float(0.04)

        if type == "maison":
            self.name = "maison"
            self.length = 10
            self.width = 12
            self.price = 610000
            self.free_area = 6
            self.price_increasement = float(0.06)

        if x==None or y==None:
            x = rd.randrange(self.free_area, (Borders().maxX - self.free_area - self.width))
            y = rd.randrange(self.free_area, (Borders().maxY - self.free_area - self.length))
        self.score = 0
        self.id = house_number
        self.shortest_distance = Borders().maxY
        self.x0 = x
        self.x1 = x + self.width
        self.y0 = y
        self.y1 = y + self.length
        self.coordinates = (x,y)