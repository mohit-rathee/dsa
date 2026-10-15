class Solution:
    def check_color_and_move(self,node,colors):
        # base case
        if node == self.n:
            return True

        node_color = colors[str(node)]

        #check if color is valid
        #  1. check neighbour's colors
        for neighbour in self.adj[node]:
            neighbour_color = colors[str(neighbour)]
            if neighbour_color == node_color:
                return False
        
        # possible colors for next node are self.m 
        for color in range(self.m):
            colors[str(node+1)]=color
            res= self.check_color_and_move(node+1,colors)
            if res:
                return True
            colors[str(node+1)]=None

        return False
            

    def graph_coloring(self,edges,m,n):
        self.adj=[[] for node in range(n)]
        for edge in edges:
            print(edge)
            u,v = edge
            self.adj[u].append(v)
            self.adj[v].append(u)
        self.m=m
        self.n=n
        colors={str(node):None for node in range(n)}
        # color first node
        colors['0']=0
        result = self.check_color_and_move(0,colors)
        print(result)

sol = Solution()
n = 3 
m = 2 
e = 3 
edges = [ (0, 1) , (1, 2) , (0, 2) ]
sol.graph_coloring(edges,m,n)
