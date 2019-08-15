from comparable import Comparable
from vertex import Vertex


class City(Vertex, Comparable):
    """
    This class represents a city on a graph 
    """
    def __init__(self, name, x, y, pop):
        """
        Create a city for a Graph.
        The instance variables are:
            gps_X: float: Longitude
            gps_Y: float: Latitude
            pop: int: Population
            name: str: Pass to Vertex constructor
        """
        super().__init__(name)
        self.gps_X = float(x)   # longitude
        self.gps_Y = float(y)   # latitude
        self.pop = pop          # population

    def get_X(self):
        """
        Return the City longitude
        """
        return self.gps_X

    def get_Y(self):
        """
        Return the City latitude
        """
        return self.gps_Y

    def get_pop(self):
        """
        Return the City population
        """
        return int(self.pop)

    def compare(self, other_city):
        """
        Use the City populations for comparison
        """
        return self.pop - self.other_city.get_pop()

    def __str__(self):
        """
        Return a string representation for the City
        """
        return str(self.name) + ": [" + str(round(self.gps_X, 2)) + ", " + str(round(self.gps_Y, 2)) + "]:(" + str(self.pop) + ")"
