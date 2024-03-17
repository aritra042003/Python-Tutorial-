class Graph:
    def __init__(self,vno):
        self.vertex_count=vno
        self.Adj_matrix=[[0]*vno for e in range(vno)]
    def add_edge(self,u,v,weight=1):
        if 0<=u<self.vertex_count and  0<=v<self.vertex_count:
            self.Adj_matrix[u][v]=weight
            self.Adj_matrix[v][u]=weight
        else:
            print("invalid vertex")
    def remove_edge(self,u,v):
        if 0<=u<self.vertex_count and  0<=v<self.vertex_count:
            self.Adj_matrix[u][v]=0
            self.Adj_matrix[v][u]=0
        else:
            print("invalid vertex")
    def has_edge(self,u,v):
        if 0<=u<self.vertex_count and  0<=v<self.vertex_count:
            return self.Adj_matrix[u][v] !=0
        else:
            print("invalid vertex")
    def print_adj_matrix(self):
        
        for row_list in self.Adj_matrix:
            print(" ".join(map(str,row_list)))
g=Graph(5)
g.add_edge(0,1)
g.add_edge(1,2)
g.add_edge(1,3)
g.add_edge(2,3)
g.add_edge(3,4)
g.print_adj_matrix()
        
        
        
        