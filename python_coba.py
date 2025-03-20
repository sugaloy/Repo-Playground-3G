#tugas code isocahedron formula dengan input angka manual
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def generate_icosahedron_vertices(edge_length):
    phi = (1 + np.sqrt(5)) / 2  # Golden ratio
    a = edge_length / 2
    b = edge_length / (2 * phi)
    
    vertices = np.array([
        [-a,  b,  0], [ a,  b,  0], [-a, -b,  0], [ a, -b,  0],
        [ 0, -a,  b], [ 0,  a,  b], [ 0, -a, -b], [ 0,  a, -b],
        [ b,  0, -a], [ b,  0,  a], [-b,  0, -a], [-b,  0,  a]
    ])
    
    faces = [
        [0, 11, 5], [0, 5, 1], [0, 1, 7], [0, 7, 10], [0, 10, 11],
        [1, 5, 9], [5, 11, 4], [11, 10, 2], [10, 7, 6], [7, 1, 8],
        [3, 9, 4], [3, 4, 2], [3, 2, 6], [3, 6, 8], [3, 8, 9],
        [4, 9, 5], [2, 4, 11], [6, 2, 10], [8, 6, 7], [9, 8, 1]
    ]
    
    return vertices, faces

def plot_icosahedron(vertices, faces):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    
    poly3d = [[vertices[vertex] for vertex in face] for face in faces]
    ax.add_collection3d(Poly3DCollection(poly3d, alpha=0.5, edgecolor='k'))
    
    ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], color='red')
    
    plt.show()

if __name__ == "__main__":
    edge_length = float(input("Njaluk panjang sisi piro bos ? "))
    vertices, faces = generate_icosahedron_vertices(edge_length)
    plot_icosahedron(vertices, faces)
