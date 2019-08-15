class Vertex():
    """
    This class represents the Vertex for a Graph.
    The instance variables are:
        name: str
        index: int
    """
    def __init__(self, name):
        """
        Create a vertex object with the passed in name 
        and index of its position in the graph vertices list.
        Create an empty adjacency list
        """
        self.name = name
        
    def get_name(self):
        """
        Return the vertex name
        """
        return self.name
                        
    def __str__(self):
        """
        Returns a string representation of this Vertex
        """
        return str(self.name)
