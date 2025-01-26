import random
import csv

def interaction(agent1, agent2, payoff_matrix):
    return payoff_matrix[agent1][agent2]

def simulate_generation(population, payoff_matrix):
    new_population = []
    rewards = []
    for i in range(0, len(population), 2):
        agent1, agent2 = random.sample(population, 2)
        reward1, reward2 = interaction(agent1, agent2, payoff_matrix)
        rewards.extend([reward1, reward2])
        if reward1 > reward2:
            new_population.append(agent1)
        else:
            new_population.append(agent2)
    return new_population, rewards

def simulate_multiple_generations(initial_population, payoff_matrix, generations):
    population = initial_population[:]
    results = []
    for generation in range(generations):
        population, rewards = simulate_generation(population, payoff_matrix)
        hawk_ratio = population.count("Hawk") / len(population)
        results.append({"generation": generation, "hawk_ratio": hawk_ratio, "average_reward": sum(rewards) / len(rewards)})
    return results

if __name__ == "__main__":
    initial_population = []
    with open("outputs/initial_population.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        initial_population = [row[0] for row in reader]

    payoff_matrix = {
        "Hawk": {"Hawk": (-10, -10), "Dove": (50, 0)},
        "Dove": {"Hawk": (0, 50), "Dove": (30, 30)}
    }

    generations = 50
    results = simulate_multiple_generations(initial_population, payoff_matrix, generations)

    with open("outputs/simulation_results.csv", "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["generation", "hawk_ratio", "average_reward"])
        writer.writeheader()
        writer.writerows(results)