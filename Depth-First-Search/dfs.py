def dfs(graph, start):
    path = []
    stack = [start]  # initialize stack with start node
    while stack:
        v = stack.pop(0)  # pop first node from stack
        if v not in path:
            path.append(v)
            stack = graph[v] + stack  # add neighbours of v at the beginning of stack
    return path

if __name__ == '__main__':
    graph = {'A' : ['B','C','D'],
             'B' : ['E'],
             'C' : ['F','G'],
             'D' : ['H'],
             'E' : ['I'],
             'F' : ['J'],
             'G' : [],
             'H' : [],
             'I' : [],
             'J' : []}
    print('dfs: ', dfs(graph, 'A'))
