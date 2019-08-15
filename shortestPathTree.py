from graphTree import GraphTree


class ShortestPathTree(GraphTree):
    """
    This class presents a tree for storing the order of the vertices
    producing the shortest path through the weighted graph vertices
    """ 
    def __init__(self, root, search_order, parents, vertices, edges, cost):
        """
        Create shortest path tree
        Instance variable: cost: Python list
        """
        super().__init__(root, search_order, parents, vertices)
        self.cost = cost

    def get_cost(self, index):
        """
        Return the cost for a path from the root to vertex at index
        """
        return self.cost[index]

    def get_all_paths_str(self):
        """
        Create a string containing all the shortest paths
        from all vertices to the root
        """
        root_name = self.get_root().get_name()
        path_str = "All shortest paths from " + root_name + " are: \n"
        search_order = self.get_search_order()

        for i in range(len(search_order)):

            path_str += self.get_path_str(search_order[i])
            index = self.get_vert_index(search_order[i])
            path_str += " (Cost: " + str(self.cost[index]) + ")\n"

        return path_str
