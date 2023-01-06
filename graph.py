"""
Author: Erutaner
Date: 2022.12.22
"""
class graph_Vertex(object):
    def __init__(self,data):
        self.data = data
        self.info = None

class GraphMatrix(object):
    def __init__(self,kind):
        self.kind = kind
        self.Vertices = []
        self.Arcs = []
        self.VertexNum = 0
        self.ArcNum = 0

    def MiniSpanTreePrim(self,Vertex):
        # 这个vertex就是随便选的一个顶点
        arc = []  # 用于存放最小生成树的边
        CloseEdge = [[] for i in range(self.VertexNum)]
        MinEdge = 0  # 用于存放离树最近的树外顶点的下标
        index = 0  # 用于循环，由于最后的生成树一共VertexNum个顶点，所以类似的操作要进行VertexNum个
        while index < self.VertexNum:
            CloseEdge[index] = [Vertex,self.Arcs[Vertex][index]]  # 对于整个图中所有顶点，都存储一下它与树的距离信息
            # 由于一开始的树只有vertex一个顶点，那么我们把所有顶点与这个vertex的距离信息都存储一下
            index += 1  # 自增一下
        index = 1  # 最终的树中只有VertexNum - 1条边。所以循环少进行一轮
        while index < self.VertexNum:
            MinEdge = self.GetMin(CloseEdge)  #找到离树最近的树外顶点
            # 把最小生成树的新边加进去，就是权重最小的那条
            arc.append([self.Vertices[CloseEdge[MinEdge][0]].data,self.Vertices[MinEdge].data])
            CloseEdge[MinEdge][1] = 0  # 由于该顶点已进入生成树，所以距离置为零即可
            i = 0  # 用于循环，将所有顶点与最小生成树的位置信息再次更新
            while i < self.VertexNum:
                if self.Arcs[MinEdge][i] < CloseEdge[i][1]:  # 如果新入树的顶点距离当前正在被判断的顶点更近
                    CloseEdge[i] = [MinEdge,self.Arcs[MinEdge][i]]  # 那就把当前顶点距离树的距离信息更新为更近的这条边
                i += 1
            index += 1  # 准备下一轮更新最小生成树
        return arc

    def GetMin(self,CloseEdge):  # 找到离树最近的树外顶点
        index = 0
        MinWeight = float("inf")
        vertex = 0
        while index < self.VertexNum:  # 每个结点都遍历一下
            if CloseEdge[index][1] != 0 and CloseEdge[index][1] < MinWeight:  # 首先结点不能在树里面，然后结点离树的距离要小于float("inf")，这第一次恒为True
                MinWeight = CloseEdge[index][1]  # 一开始直接将最近距离设置成当前定点距离树的最近距离
                vertex = index  # 注意，只有在后续结点离树更近时，这个vertex才会得到更新
            index += 1  # 无论如何都会更新index
        return vertex  # 返回距离树最近结点的下标

    def MiniSpanTreeKruskal(self,Edges):
        flag = [[] for i in range(self.VertexNum)]
        index = 0
        while index < self.VertexNum:
            flag[index] = index
            index += 1
        index = 0
        while index < len(Edges):
            VertexOne = Edges[index][0]
            VertexTwo = Edges[index][1]
            if flag[VertexOne] is not flag[VertexTwo]:
                FlagOne = flag[VertexOne]
                FlagTwo = flag[VertexTwo]
                limit = 0
                while limit < self.VertexNum:
                    if flag[limit] is FlagTwo:
                        flag[limit] = FlagOne
                    limit += 1
                index += 1
            else:
                Edges.pop(index)
        return Edges

test_graph = GraphMatrix("undirected network")
graph_Vertex_a = graph_Vertex('A')
test_graph.Vertices.append(graph_Vertex_a)
test_graph.VertexNum += 1

graph_Vertex_b = graph_Vertex('B')
test_graph.Vertices.append(graph_Vertex_b)
test_graph.VertexNum += 1

graph_Vertex_c = graph_Vertex('C')
test_graph.Vertices.append(graph_Vertex_c)
test_graph.VertexNum += 1

graph_Vertex_d = graph_Vertex('D')
test_graph.Vertices.append(graph_Vertex_d)
test_graph.VertexNum += 1

graph_Vertex_e = graph_Vertex('E')
test_graph.Vertices.append(graph_Vertex_e)
test_graph.VertexNum += 1

graph_Vertex_f = graph_Vertex('F')
test_graph.Vertices.append(graph_Vertex_f)
test_graph.VertexNum += 1

graph_Vertex_g = graph_Vertex('G')
test_graph.Vertices.append(graph_Vertex_g)
test_graph.VertexNum += 1

graph_Vertex_h = graph_Vertex('H')
test_graph.Vertices.append(graph_Vertex_h)
test_graph.VertexNum += 1

test_graph.Arcs = [
    [0,1,10,1,3,10,10,10],
    [1,0,5,10,10,10,10,10],
    [10,5,0,10,6,4,10,10],
    [1,10,10,0,10,10,2,10],
    [3,10,6,10,0,10,7,4],
    [10,10,4,10,10,0,10,5],
    [10,10,10,2,7,10,0,10],
    [10,10,10,10,4,5,10,0]
]

Edges = []

for i in range(len(test_graph.Arcs)):
    for j in range(len(test_graph.Arcs[0])):
        if test_graph.Arcs[i][j] != 0 and test_graph.Arcs[i][j] != 10:
            Edges.append(set([i,j]))
tmp = []
for item in Edges:
    if not list(item) in tmp:
        tmp.append(list(item))
Edges = tmp
Edges = sorted(Edges,key=lambda x:test_graph.Arcs[x[0]][x[1]])

print("The initial state is:",Edges)
test_graph.MiniSpanTreeKruskal(Edges)


test_graph.ArcNum = 10

for i in range(len(Edges)):
    for j in range(2):
        Edges[i][j] = chr(ord(str(Edges[i][j])) + 17)
print("The edges of minispantree(kruskal) is:",Edges)
print("The edges of minispantree(prim) is:",test_graph.MiniSpanTreePrim(0))
