import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Constants for simulation
G = 6.67430e-11  # Gravitational constant
sun_mass = 1.989e30  # Mass of the sun in kg
au = 149.6e9  # Astronomical unit in meters

# Class representing a planet
class Planet:
    def __init__(self, name, mass, semi_major_axis, eccentricity):
        self.name = name
        self.mass = mass
        self.a = semi_major_axis * au  # Convert AU to meters
        self.e = eccentricity
        self.theta = 0  # Initial angle

# Function to calculate gravitational force between two bodies
def gravitational_force(mass1, mass2, distance):
    force = G * (mass1 * mass2) / distance**2
    return force

# Function to update planet position based on gravitational interactions
def update_position(planet, time_step):
    # Simplified calculations for demonstration
    force = gravitational_force(sun_mass, planet.mass, planet.a)
    acceleration = force / planet.mass
    planet.theta += np.sqrt(acceleration / planet.a) * time_step

# Function to initialize the plot
def init():
    ax.set_xlim(-1.5 * au, 1.5 * au)
    ax.set_ylim(-1.5 * au, 1.5 * au)
    return planet_line,

# Function to update the plot in each animation frame
def update(frame):
    update_position(earth, time_step)
    x = earth.a * np.cos(earth.theta)
    y = earth.a * np.sin(earth.theta)
    planet_line.set_data(x, y)
    return planet_line,

# Create a figure and axis
fig, ax = plt.subplots()
earth = Planet("Earth", 5.972e24, 1, 0.0167)  # Example data for Earth

# Set up the initial plot
planet_line, = ax.plot([], [], marker='o', label='Earth', color='blue')
ax.plot(0, 0, marker='o', label='Sun', color='yellow')

# Set up the animation
time_step = 1e6  # Time step for simulation in seconds
ani = animation.FuncAnimation(fig, update, frames=500, init_func=init, blit=True, interval=50)

# Show the plot
plt.legend()
plt.show()
