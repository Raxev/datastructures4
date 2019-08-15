from vertex import Vertex
from edge import Edge


class GraphTree:
    """
    This class represents trees used with graphs.
    These trees hold spanning trees created via a graph traversal.
    Both depth-first search (DFS) and breadth-first search
    (BFS) graph traversals produce spanning trees.
    There are algorithms for finding minimum spanning trees (MSTs)
    of a graph and the shortest path between vertices in a graph.  
    These spanning trees and paths are stored in GraphTrees.
    Each node in the tree is a vertex from the graph.
    There are three instance variables for this GraphTree.
    1. The vertices are stored in a Python list called 
       search_order as they are visited by the traversal.  
    2. The parent vertices for the vertices in the traversal are 
       also stored in a Python list called parents.
    3. The root of the tree.
    """
    def __init__(self, root, search_order, parents, vertices):
        """
        Creates a GraphTree used with graph traversals
        The instance variables are:
            root: The root of the tree: starting vertex
            search_order: Python list of vertices in visit order
            index_order: Python list of vertex indices in visit order
            parents: Python list of parents of the vertices
        """
        self.root = root
        self.search_order = search_order
        self.parents = parents
        self.vertices = vertices

    def get_root(self):
        """
        Return the root of the tree
        """
        return self.root

    def get_parent(self, vertex): 
        """
        Return the parent of the given vertex
        """
        index = self.get_vert_index(vertex)
        return self.parents[index]

    def get_vert_index(self, vertex):
        """
        Return the parent of the given vertex
        """
        index = -1
        for i in range(len(self.vertices)):
            if self.vertices[i].get_name() == vertex.get_name():
                index = i
                break
        return index

    def get_search_order(self):
        """
        Return the list representing the search order
        """
        return self.search_order

    def get_num_verts_found(self):
        """
        Return the number of vertices in the search order
        """
        return len(self.search_order)
         
    def get_path(self, vertex):
        """
        Return the path of vertices from a given vertex to the root
        """
        path = []
        root_name = self.root.get_name()
        curr_vertex = vertex

        """
        Traverse the nodes starting with root and using
        the node’s parents as the next node in the path
        """
        while curr_vertex.get_name() != root_name:
            path.append(curr_vertex.get_name())
            curr_vertex = self.get_parent(curr_vertex)
        path.append(root_name)
        return path

    def get_path_str(self, vertex):
        """
        Return a string holding path of vertices 
        from the root to the given vertex
        """
        path = self.get_path(vertex)
        path.reverse()
        path_str = ("A path of nodes from " + str(self.root)
                    + " to " + str(vertex) + ":")

        node_count = 0
        for vert in path:
            if node_count % 5 == 0:
                path_str += "\n"
            if node_count == 0:
                path_str += str(vert)
            else:
                path_str += " --> " + str(vert)
            node_count += 1

        return path_str

    def get_edge_str(self):
        """
        Return a string holding path of edges from the root
        to the starting vertex given when the tree was built
        """
        edge_str = "Edges:\n"
        for vertex in self.search_order:
            index = self.get_vert_index(vertex)
            if self.parents[index] is not None:
                edge_str += ("[ " + str(self.parents[index]) + ", "
                            + str(self.vertices[index]) + " ]\n")
        edge_str += '\n'

        return edge_str
