from utils import load_tsplib_instance, plot_tour
from tsp_ea import evolutionary_algorithm_tsp
import matplotlib.pyplot as plt

if __name__ == "__main__":
    # TSPLIB-Instanz laden (Pfad ggf. anpassen)
    distance_matrix, coords = load_tsplib_instance("berlin52.tsp")
    #distance_matrix, coords = load_tsplib_instance("eil101.tsp")

    # EA ausführen
    best_tour, best_distance, history = evolutionary_algorithm_tsp(
        distance_matrix,
        mu=50,
        lambd=100,
        generations=500,
        mutation_rate=0.1
    )

    # Konvergenz plotten
    plt.plot(history)
    plt.xlabel("Generation")
    plt.ylabel("Beste Tourlänge")
    plt.title("Konvergenzverlauf des EA")
    plt.grid()
    plt.show()

    # Beste Tour visualisieren
    plot_tour(coords, best_tour, f"Beste Tour (Distanz: {best_distance:.2f})")
