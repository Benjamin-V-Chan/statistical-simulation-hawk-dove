import csv
import statistics

def analyze_results(results_file):
    with open(results_file, "r") as file:
        reader = csv.DictReader(file)
        results = [row for row in reader]
        hawk_ratios = [float(row["hawk_ratio"]) for row in results]
        average_rewards = [float(row["average_reward"]) for row in results]
        
    return {
        "mean_hawk_ratio": statistics.mean(hawk_ratios),
        "mean_reward": statistics.mean(average_rewards),
        "variance_hawk_ratio": statistics.variance(hawk_ratios)
    }

if __name__ == "__main__":
    stats = analyze_results("outputs/simulation_results.csv")
    with open("outputs/analysis_summary.txt", "w") as file:
        for key, value in stats.items():
            file.write(f"{key}: {value}\n")