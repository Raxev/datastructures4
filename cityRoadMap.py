from graph import Graph


class CityRoadMap(Graph):
    """
    This class represent a Graph with City Vertices and Road Edges.
    """
    def __init__(self, cities=None, roads=None):
        """
        Construct a CityRoadMap Graph
        using Cities and Roads stored in lists
        """
        if cities is None or roads is None:
            super().__init__()
        else:
            super().__init__(cities, roads)

    def get_neighboring_cities(self, city):
        """
        Return the neighbors of the City Vertex as a list
        """
        city_list = self.get_neighbors(city)

        return city_list

    def get_roads_str(self):
        """
        Create string of Cities and
        Roads with distances and direction
        """
        roads_str = ""

        for city in self.vertices:
            roads = self.get_neighboring_cities(city)
            city_name = city.get_name()
            roads_str += "[ " + city_name + " ]:\n"
            for road in roads:
                roads_str += "  " + str(road) + "\n"
            roads_str += "\n"
        return roads_str

    def get_cities_str(self):
        """
        Create string of Cities with GPS coordinates and population
        """
        cities_str = ""

        for city in self.vertices:
            city_name = city.get_name()
            cities_str += str(self.get_vertex(city_name)) + "\n"

        return cities_str
