#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

def monte_carlo_simulation_paths(
    initial_capital=100, 
    p_up=0.5, 
    daily_return_up=1.01, 
    daily_return_down=0.99,
    num_days=365,
    num_paths=10
):
    """
    Returns an array of shape (num_paths, num_days+1),
    where each row is the evolution of one simulation path.
    """
    paths = np.zeros((num_paths, num_days+1))
    for i in range(num_paths):

        print(f"--- Simulating path #{i+1} ---")
        capital = initial_capital
        paths[i, 0] = capital  # day 0
        for day in range(1, num_days+1):
            if np.random.rand() < p_up:
                capital *= daily_return_up
            else:
                capital *= daily_return_down
            paths[i, day] = capital

        print("\n")

    return paths


def main():
                
    # Parameters
    initial_capital = 100
    num_days = 365
    num_paths = 25  # fewer paths so we can see each line

    # Run the Monte Carlo simulation
    mc_paths = monte_carlo_simulation_paths(
        initial_capital=initial_capital,
        num_days=num_days,
        num_paths=num_paths
    )

    # Plot each path
    plt.figure(figsize=(14, 7))
    for i in range(num_paths):
        plt.plot(mc_paths[i])#, label=f"Path {i+1}")

    plt.title("Monte Carlo Simulation - Daily Portfolio Evolution")
    plt.xlabel("Day")
    plt.ylabel("Portfolio Value ($)")
    plt.legend(loc="upper left")
    
    # Save the plot to an image (do this before plt.show() so the figure isn't cleared)
    plt.savefig("monte_carlo_sim.png")
    plt.show()

    # Final path values (at day = 365)
    final_values_mc = mc_paths[:, -1]

    # Print to console
    print("Monte Carlo Final Values:")
    print(final_values_mc)
    print(f"  Mean final value:   ${final_values_mc.mean():.2f}")
    print(f"  Median final value: ${np.median(final_values_mc):.2f}")

    # Save to a text file
    with open("monte_carlo_sim.txt", "w") as f:
        f.write("Monte Carlo Final Values:\n")
        # If you want to write all final values on one line, you can do:
        f.write(" ".join([f"{val:.2f}" for val in final_values_mc]) + "\n\n")

        # Or just use str() representation:
        # f.write(str(final_values_mc) + "\n\n")

        f.write(f"Mean final value:   ${final_values_mc.mean():.2f}\n")
        f.write(f"Median final value: ${np.median(final_values_mc):.2f}\n")

if __name__ == "__main__":
    main()
