import random
"""
You'll want to implement a smarter decision logic. This is skeleton code that you should copy and replace in your repository.
"""
class PercolationPlayer:
    def ChooseVertexToColor(graph, player):
        return PercolationPlayer.MaxEdges(graph)
    
    def MaxEdges(graph):
        m = {}
        for e in graph.E:
            m[e.a] = 0
            m[e.b] = 0
        for e in graph.E:
            m[e.a] += 1
            m[e.b] += 1
        maxV = 0
        vertex = None
        for e in m.keys():
            if e.color == -1 and maxV < m[e]:
                maxV = m[e]
                vertex = e
        if vertex is None:
            return random.choice([v for v in graph.V if v.color == -1])
        return vertex
    
    def ChooseVertexToRemove(graph, player):
        vertices = {}
        for v in [x for x in graph.V if x.color == player]:
            vertices[v] = PercolationPlayer.GreedyRemoval(graph, v)
        max = 0
        friendlyVertices = 9999999999999
        vertex = None
        for i in vertices.keys():
            if max < vertices[i][0]:
                max = vertices[i][0]
                vertex = i
                friendlyVertices = vertices[i][1]
            if max == vertices[i][0]:
                if vertices[i][1] < friendlyVertices:
                    vertex = i
                    friendlyVertices = vertices[i][1]
        if vertex is None:
    	       return random.choice([v for v in graph.V if v.color == player])
        return vertex
    
    def GreedyRemoval(graph, v):
        count = 0
        friendlyCount = 0
        for i in graph.E:
            if i.a == v:
                if i.b.color != i.a.color:
                    count += 1
                else:
                    friendlyCount += 1
            if i.b == v:
                if i.a.color != i.b.color:
                    count += 1
                else:
                    friendlyCount += 1
        return (count, friendlyCount)
