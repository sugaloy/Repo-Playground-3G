#TUGAS MENYUSUN BERSAMA CODE MENGHITUNG VOLUME ISOCAHEDRON DENGAN INPUT VARIABEL a
#a = RUSUK SEBUAH BANGUN RUANG ISOCAHEDRON
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

def calculate_icosahedron_volume(edge_length):
    phi = (1 + np.sqrt(5)) / 2  
    a = edge_length / 2
    volume = (5 / 12) * (3 + np.sqrt(5)) * (edge_length ** 3)
    
    print("Langkah-langkah perhitungan volume icosahedron:")
    print(f"1. Panjang Rusuk (a) = {edge_length}")
    print(f"2. Rasio Emas (phi) = {phi}")
    print(f"3. Volume = (5/12) * (3 + sqrt(5)) * (a^3)")
    print(f"4. Volume = (5/12) * (3 + {np.sqrt(5)}) * ({edge_length}^3)")
    print(f"5. Volume = {volume:.2f}")
    
    return volume

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

#Menampilkan informasi tentang Icosahedron sebelum input panjang rusuk = a
def display_icosahedron_info():
    print("Icosahedron adalah bangun ruang tiga dimensi yang memiliki:")
    print("- 20 sisi berbentuk segitiga sama sisi")
    print("- 12 titik (vertices)")
    print("- 30 rusuk (edges)")
    print("- Simetri yang tinggi dan merupakan bagian dari bangun Platonik")
    print("Icosahedron sering digunakan dalam geometri, grafik komputer, dan model struktur molekul.")

if __name__ == "__main__":
    display_icosahedron_info()
    try:
        edge_length = float(input("\nMasukkan Panjang Rusuk = a: "))
        if edge_length <= 0:
            raise ValueError("Panjang rusuk harus bilangan positif.")

        volume = calculate_icosahedron_volume(edge_length)
        vertices, faces = generate_icosahedron_vertices(edge_length)

        print("\nPerhitungan Icosahedron:")
        print(f"Volume Icosahedron: {volume:.2f} satuan kubik")

        plot_icosahedron(vertices, faces)

    except ValueError as e:
        print(f"Input tidak valid: {e}")