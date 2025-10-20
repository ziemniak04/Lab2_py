import random
import matplotlib
matplotlib.use('Agg') 
import matplotlib.pyplot as plt


def random_walk(n):
    """
    Perform a random walk starting at the origin (0, 0).

    Each step is chosen randomly in one of four directions:
    'up', 'down', 'left', or 'right'. The walk continues
    until the distance from the origin exceeds `n`.

    Parameters
    ----------
    n : int or float
        The radius (distance threshold) from the origin.
        The random walk stops once sqrt(x^2 + y^2) > n.

    Returns
    -------
    path : list of tuple
        A list of (x, y) coordinates visited during the walk,
        including the starting point (0, 0).

    Outsource:
    - docstrings

    """
    x, y = 0, 0
    path = [(x, y)]  

    while (x**2 + y**2)**0.5 <= n:
        direction = random.choice(['up', 'down', 'left', 'right'])

        if direction == 'up':
            y += 1
        elif direction == 'down':
            y -= 1
        elif direction == 'left':
            x -= 1
        elif direction == 'right':
            x += 1

        path.append((x, y))

    return path


if __name__ == "__main__":
    """
    Main execution block.

    Creates and visualizes a 2D random walk until the walker’s
    distance from the origin exceeds `n`.

    Outsource:
    - docstrings
    - line with plot and savefig 
    """
    n = 100 
    coordinates = random_walk(n)

    x, y = zip(*coordinates)

    plt.plot(x, y, marker='o', linestyle='-', markersize=2)
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.title("Walker's Trajectory")
    plt.grid(True)
    plt.savefig('random_walk.png', dpi=600, bbox_inches='tight')
    print("Plot saved as 'random_walk.png'")
