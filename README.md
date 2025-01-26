# statistical-simulation-hawk-dove

## Project Overview
The Hawk-Dove game is a mathematical model used in evolutionary biology and game theory to study conflict and resource competition among individuals. The game explores two strategies:

1. **Hawk**: Aggressive individuals who always engage in conflict.
2. **Dove**: Passive individuals who avoid conflict.

The payoffs for interactions between these strategies are summarized in a payoff matrix:

|           | Hawk      | Dove      |
|-----------|-----------|-----------|
| **Hawk**  | (-C/2, -C/2) | (V, 0)   |
| **Dove**  | (0, V)    | (V/2, V/2) |

Where:
- $C$ is the cost of conflict.
- $V$ is the value of the contested resource.

### Evolutionary Dynamics
The simulation models the population over generations to observe changes in the proportions of Hawks and Doves. The replicator dynamics equation is used to describe how the frequency of strategies changes over time:

$$ \dot{x}_i = x_i \left( f_i - \phi \right) $$

Where:
- $x_i$ is the proportion of individuals using strategy $i$.
- $f_i$ is the fitness of strategy $i$.
- $\phi$ is the average fitness of the population.

The equilibrium is reached when:

$$ \dot{x}_i = 0 $$

This occurs when the population reaches a stable ratio of Hawks to Doves.

### Simulation Details
The simulation implements the following steps:
1. Initialize a population with given proportions of Hawks and Doves.
2. Simulate interactions based on the payoff matrix.
3. Update the population based on rewards from interactions.
4. Repeat for multiple generations.

## Folder Structure
```
project-root/
├── scripts/
│   ├── 01_setup.py            # Initialize simulation parameters and population
│   ├── 02_simulate.py         # Run the simulation
│   ├── 03_analyze.py          # Analyze the simulation results
│   ├── 04_visualize.py        # Generate visualizations
├── outputs/
│   ├── simulation_results.csv # Simulation data
│   ├── analysis_summary.txt   # Analysis summary
│   ├── visualizations/        # Plots and charts
├── config.json                # Configuration file for the simulation
├── README.md                  # Project documentation
├── requirements.txt           # Python package dependencies
```

## Usage
### 1. Setup the Project:
- Clone the repository.
- Ensure you have Python installed.
- Install required dependencies using the requirements.txt file:

```bash
pip install -r requirements.txt
```

### 2. Initialize the Population:
Run the setup script to generate the initial population:

```bash
python scripts/01_setup.py
```

### 3. Run the Simulation:
Simulate multiple generations of the Hawk-Dove game:

```bash
python scripts/02_simulate.py
```

### 4. Analyze Results:
Analyze the simulation results to compute statistics:

```bash
python scripts/03_analyze.py
```

### 5. Visualize Results:
Generate visualizations from the simulation data:

```bash
python scripts/04_visualize.py
```

## Requirements
- Python 3.8+
- Required Python packages are listed in `requirements.txt`. Install them with:

```bash
pip install -r requirements.txt
```

### Key Dependencies:
- pandas
- matplotlib
- numpy
- json
- csv