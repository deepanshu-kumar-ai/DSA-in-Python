# adjency matrix implementation 
vertex = ['A', 'B', 'C', 'D']
adjency_matrix= [
    [0, 1, 1, 1],  # Edges for A
    [1, 0, 1, 0],  # Edges for B
    [1, 1, 0, 0],  # Edges for C
    [1, 0, 0, 0]   # Edges for D
]

def print_adjency_matrix(matrix):
    print("Adjency matrix")
    for row in matrix:
        print(row)

# the connection of noded(vertex)
def connection_vertex(matrix,vertices):
    print("The connection of the vertex:")
    for i in range(len(vertex)):
        print(f"{vertices[i]}:",end="")
        for j in range(len(vertex)):
            if matrix[i][j]:
                print(vertices[j],end=" ")
        print()

# visualization of the connection of the graph
print("vertex:",vertex)
print_adjency_matrix(adjency_matrix)
connection_vertex(adjency_matrix,vertex)