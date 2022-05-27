import sys
sys.path.append('Graph_case_study')
from Graph_case_study.graph import LinkedDirectedGraph
from Graph_case_study.algorithms import dfs, bfs
from Graph_case_study.linkedstack import LinkedStack


def read_file(path):
    graph=LinkedDirectedGraph()
    with open(path, 'r', encoding='utf-8') as f:
        f.readline()
        for line in f.readlines():
            vertex, neighbors=line[:-1].split(' ', 1)
            if vertex not in list(i.getLabel() for i in graph.vertices()):
                graph.addVertex(vertex)
            for neighbor in neighbors[1:-1].split(', '):
                # print(neighbor)
                if neighbor=='none':
                    continue
                if neighbor not in list(i.getLabel() for i in graph.vertices()):
                    graph.addVertex(neighbor)
                graph.addEdge(neighbor, vertex, None)
    return graph

def dfs_test(graph):
    vertexes=list(graph.vertices())
    vertex1=vertexes[0]
    vertex2=vertexes[5]
    vertex3=vertexes[10]
    vertex4=vertexes[15]
    vertex5=vertexes[20]
    vertex6=vertexes[23]
    stack=LinkedStack()
    dfs(graph, vertex1, stack)
    assert str(list(stack)[0])=='MATH52'
    stack=LinkedStack()
    dfs(graph, vertex2, stack)
    assert str(list(stack)[0])=='CS108'
    stack=LinkedStack()
    dfs(graph, vertex3, stack)
    assert str(list(stack)[0])=='CS194W'
    stack=LinkedStack()
    dfs(graph, vertex4, stack)
    assert str(list(stack)[0])=='CS145'
    stack=LinkedStack()
    dfs(graph, vertex5, stack)
    assert str(list(stack)[0])=='CS144'
    stack=LinkedStack()
    dfs(graph, vertex6, stack)
    assert str(list(stack)[0])=='MATH53'
    print('Testing completed')



def bfs_test(graph):
    vertexes=list(graph.vertices())
    vertex1=vertexes[0]
    vertex2=vertexes[5]
    vertex3=vertexes[10]
    vertex4=vertexes[15]
    vertex5=vertexes[20]
    vertex6=vertexes[23]
    ver=bfs(graph, vertex1)
    assert str(list(ver)[0])=='MATH19'
    ver=bfs(graph, vertex2)
    assert str(list(ver)[0])=='CS161'
    ver=bfs(graph, vertex3)
    assert str(list(ver)[0])=='CS194W'
    ver=bfs(graph, vertex4)
    assert str(list(ver)[0])=='CS145'
    ver=bfs(graph, vertex5)
    assert str(list(ver)[0])=='CS144'
    ver=bfs(graph, vertex6)
    assert str(list(ver)[0])=='MATH53'
    print('Testing completed')

if __name__=='__main__':
    graph=read_file('stanford_cs.txt')
    dfs_test(graph)
    bfs_test(graph)
