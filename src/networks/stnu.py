import heapq


class STNU:
    """
    A class to represent a Simple Temporal Network with uncertainties.
    ...
    Attributes
    ----------
    names_dict : dict[name: index]
        A dictionary that maps the name of the node to its index
    successor_edges : List[List[tuples]]
        A list of list of successor edges. The list at index i of this attribute is 
        the list of edges of the i-th node. Each edge is represented by a tuple - the
        first element of the tuple is the j-th node that the i-th node is connected to
        and the second element is the weight/distance between the i-th and j-th nodes
    length : int
        number of nodes in the STNU
    Methods
    -------
    floyd_warshall()
        describe
    bellmann_ford()
        describe
    dijkstra(src)
        Calculates the shortest path array from src using 
        Dijkstra's algorithm
    johnson(src)
        Calculates the shortest path matrix between every node 
        using Johnson's algorithm
    """

    def __init__(self):
        """
        Constructor for a Simple Temporal Network
        Parameters
        ----------
            names_dict : dict[name: index]
                A dictionary that maps the name of the node to its index
            successor_edges : List[List[tuples]]
                A list of list of successor edges. The list at index i of this attribute is 
                the list of edges of the i-th node. Each edge is represented by a tuple - the
                first element of the tuple is the j-th node that the i-th node is connected to
                and the second element is the weight/distance between the i-th and j-th nodes
            length : int
                number of nodes in the STN
        Returns
        -------
        None
        """
        self.names_dict = {}
        self.successor_edges = []
        self.length = 0
