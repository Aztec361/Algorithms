class mygraph:
    def __init__(self, numNode):
        self.adjList = {}
        self.traversal = []
        self.numNode = numNode

    def addNode(self, inputRow):
        inputList = inputRow.split()
        self.adjList[inputList[0]] = inputList[1:]

    def DFS(self):
        visited = set()
        keys = list(self.adjList.keys())

        for start_node in keys:
            if start_node not in visited:
                stack = [start_node]

                while stack:
                    node = stack[-1]

                    # Check if there are unvisited neighbors
                    unvisited_neighbors = [neighbor for neighbor in self.adjList[node] if neighbor not in visited]

                    if unvisited_neighbors:
                        next_neighbor = unvisited_neighbors[0]
                        visited.add(next_neighbor)
                        self.traversal.append(next_neighbor)
                        stack.append(next_neighbor)
                    else:
                        stack.pop()

def main():
    numInstance = int(input())  # the number of instances, first input

    for _ in range(numInstance):
        numNode = int(input())  # the number of nodes in i-th instance
        g = mygraph(numNode)

        for _ in range(numNode):
            g.addNode(input())

        g.DFS()
        print(' '.join(g.traversal))

if __name__ == "__main__":
    main()
