file_dir = '/users/TeamDeepUser/DeepUserModellingProject/DeepUserModelling/DatasetsProcessed/New_Dataset/'
datafile = open(file_dir+'acm_output.txt', "r")
outfile = open(file_dir+'adjacency_list.txt','w')

class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]
class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())
g = Graph()
for i in range(2244018):
    g.addVertex(i)
    g.vertList
a=0

for curr_line in datafile:
    if curr_line[1:6]=="index":
        a+=1
    curr_line=curr_line.rstrip('\n')
    if len(curr_line)>=2:
        if curr_line[1]=="%":
            citation_index=curr_line[2:]
            paper_index=a
            g.addEdge(paper_index,citation_index)
for v in g:
    outfile.write(str(v)+"\n")
datafile.close()
outfile.close()
