from graph.Graph_IncidenceList import GraphIncidenceList as Graph


class GraphHelper:
    """
    Utility functions for graph management.
    """

    @staticmethod
    def sortEdges(graph):
        """
        Return the list of edges, sorted by their weight.
        :param graph: the graph.
        :return: the list of edges, sorted by their weight.
        """
        l = graph.getEdges()
        l.sort()
        return l

    @staticmethod
    def buildGraph(num_nodes):
        """
        Build a sample complete graph.
        :param num_nodes number of nodes.
        :return: a sample complete graph.
        """
        graph = Graph()

        nodes = []
        for i in range(num_nodes):
            nodes.append(graph.addNode(i))

        for src in nodes:
            for dst in nodes:
                if dst.id > src.id:
                    graph.insertEdge(src.id, dst.id, num_nodes - src.id)

        return graph


if __name__ == "__main__":
    graph = GraphHelper.buildGraph(5)

    graph.print()

    edges = GraphHelper.sortEdges(graph)

    print([str(i) for i in edges])