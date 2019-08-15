from graphTree import GraphTree


class MST(GraphTree):
    """
    This class presents a tree for storing the MST
    """
    def __init__(self, root, search_order, parents, vertices, edges, total_weight):
        """
        Create an MST
        Instance variables: total_weight: int
        """
        super().__init__(root, search_order, parents, vertices)
        self.edges = edges
        self.total_weight = total_weight

    def get_total_weight(self):
        """
        Return total weight of MST
        """
        return self.total_weight

    def get_mst_edge_str(self):
        """
        Return a string holding path of edges from the root
        to the starting vertex given when the tree was built
        """
        edge_str = "Edges:\n"
        for edge in self.edges:
            edge_str += ("[ " + str(edge) + " ]\n")

        edge_str += '\n'

        return edge_str
