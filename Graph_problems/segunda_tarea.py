class Solution:
    def findCenter(self, edges):  # Agregamos self
        # Comparar los nodos de las dos primeras aristas
        if edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]:
            return edges[0][0]
        else:
            return edges[0][1]
