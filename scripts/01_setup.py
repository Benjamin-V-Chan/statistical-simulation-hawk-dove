import json
import csv

def load_config(config_file):
    with open(config_file, 'r') as file:
        return json.load(file)

def initialize_population(total_population, hawk_ratio):
    hawks = int(total_population * hawk_ratio)
    doves = total_population - hawks
    return ['Hawk'] * hawks + ['Dove'] * doves

if __name__ == "__main__":
    config = load_config("config.json")
    population = initialize_population(config["total_population"], config["hawk_ratio"])
    
    with open("outputs/initial_population.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Agent"])
        writer.writerows([[agent] for agent in population])