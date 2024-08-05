# Getting Ready for Physics Class

## Overview

Welcome to the "Getting Ready for Physics Class" project! As a physics teacher preparing for the upcoming semester, you want to provide your students with functions to help them calculate some fundamental physical properties. This will assist them in understanding and applying key physics concepts.

## Data Provided

You have been provided with several functions:

- `calculate_velocity`: Calculates the velocity of an object given its initial velocity, acceleration, and time.
- `calculate_acceleration`: Calculates the acceleration of an object given its final velocity, initial velocity, and time.
- `calculate_force`: Calculates the force acting on an object given its mass and acceleration.
- `calculate_kinetic_energy`: Calculates the kinetic energy of an object given its mass and velocity.

## Example

For instance:

- The function `calculate_velocity` takes initial velocity, acceleration, and time as inputs and returns the final velocity.
- The function `calculate_force` takes mass and acceleration as inputs and returns the force acting on the object.

## Tasks

- **Calculate Velocity**: Determine the velocity of an object given its initial velocity, acceleration, and time.
- **Calculate Acceleration**: Calculate the acceleration of an object given its final velocity, initial velocity, and time.
- **Calculate Force**: Compute the force acting on an object given its mass and acceleration.
- **Calculate Kinetic Energy**: Calculate the kinetic energy of an object given its mass and velocity.

## Example Usage

After implementing the functions, you should be able to generate outputs such as:

- Velocity of an object after a certain time.
- Acceleration of an object over a period.
- Force acting on an object.
- Kinetic energy of an object.

## Example Code

Here is an example of how you might use the provided functions:

```python
# Define the functions
def calculate_velocity(initial_velocity, acceleration, time):
    return initial_velocity + acceleration * time

def calculate_acceleration(final_velocity, initial_velocity, time):
    return (final_velocity - initial_velocity) / time

def calculate_force(mass, acceleration):
    return mass * acceleration

def calculate_kinetic_energy(mass, velocity):
    return 0.5 * mass * velocity ** 2

# Example usage
initial_velocity = 0
acceleration = 9.8
time = 10
mass = 5
velocity = calculate_velocity(initial_velocity, acceleration, time)
force = calculate_force(mass, acceleration)
kinetic_energy = calculate_kinetic_energy(mass, velocity)

print(f"Velocity: {velocity} m/s")
print(f"Force: {force} N")
print(f"Kinetic Energy: {kinetic_energy} J")

