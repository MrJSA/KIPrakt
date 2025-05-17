import tsplib95
import numpy as np
from scipy.spatial.distance import euclidean
import matplotlib.pyplot as plt

def load_tsplib_instance(path):
    problem = tsplib95.load(path)
    coords = [problem.node_coords[i + 1] for i in range(len(problem.node_coords))]
    n = len(coords)
    distance_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                distance_matrix[i][j] = euclidean(coords[i], coords[j])
    return np.array(distance_matrix), coords

def plot_tour(coords, tour, title="Beste Tour"):
    ordered = [coords[i] for i in tour + [tour[0]]]
    xs, ys = zip(*ordered)
    plt.plot(xs, ys, 'o-', label=title)
    plt.title(title)
    plt.axis("equal")
    plt.grid()
    plt.legend()
    plt.show()
