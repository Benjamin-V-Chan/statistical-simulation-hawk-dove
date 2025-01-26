import pandas as pd
import matplotlib.pyplot as plt

def generate_plots(results_file, output_folder):
    data = pd.read_csv(results_file)
    plt.plot(data["generation"], data["hawk_ratio"], label="Hawk Ratio")
    plt.plot(data["generation"], data["average_reward"], label="Average Reward")
    plt.xlabel("Generation")
    plt.ylabel("Values")
    plt.legend()
    plt.title("Hawk-Dove Simulation")
    plt.savefig(f"{output_folder}/hawk_dove_simulation.png")
    plt.close()

if __name__ == "__main__":
    generate_plots("outputs/simulation_results.csv", "outputs/visualizations")