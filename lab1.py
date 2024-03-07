from collections import deque


def is_bipartite(graph, n):
    colors = [0 for i in range(n+1)] # массив, в котором красим вершины 
    queue = deque()

    for i in range(1, n + 1):

        if colors[i] == 0:
            queue.append(i)
            colors[i] = 1

            while queue:
                u = queue.popleft()

                for v in range(1, n + 1):
                    
                    if graph[u - 1][v - 1] == 1:#если между вершинами есть ребро
                        
                        if colors[v] == 0:
                            colors[v] = 3 - colors[u]#красим в другой цвет
                            queue.append(v)
                        
                        elif colors[v] == colors[u]:#цикл нечетной длины
                            return False  

    return colors


def main():
    with open("in.txt", "r") as input_file, open("out.txt", "w") as output_file:
        n = int(input_file.readline().strip())
        adjacency_matrix = [list(map(int, input_file.readline().split())) for i in range(n)]

        colors = is_bipartite(adjacency_matrix, n)

        if colors:
            output_file.write("Y\n")

            part_1 = [str(i) for i in range(1, n + 1) if colors[i] == 1]
            part_2 = [str(i) for i in range(1, n + 1) if colors[i] == 2]

            output_file.write(" ".join(part_1) + "\n")
            output_file.write(" ".join(part_2) + "\n")
        else:
            output_file.write("N\n")


if __name__ == "__main__":
    main()
