# Function to convert Fahrenheit to Celsius
def f_to_c(f_temp):
    c_temp = (f_temp - 32) * 5 / 9
    return c_temp

# Test the f_to_c function
f100_in_celsius = f_to_c(100)
print(f100_in_celsius)  # Expected output: 37.77777777777778

# Function to convert Celsius to Fahrenheit
def c_to_f(c_temp):
    f_temp = c_temp * (9 / 5) + 32
    return f_temp

# Test the c_to_f function
c0_in_fahrenheit = c_to_f(0)
print(c0_in_fahrenheit)  # Expected output: 32

# Function to calculate force
def get_force(mass, acceleration):
    return mass * acceleration

# Define variables for testing get_force
train_mass = 22680
train_acceleration = 10
train_distance = 100  # Assuming this value for later use

# Test get_force
train_force = get_force(train_mass, train_acceleration)
print(f"The GE train supplies {train_force} Newtons of force.")  # Expected output: 226800 Newtons

# Function to calculate energy
def get_energy(mass, c=3*10**8):
    return mass * c**2

# Define variable for testing get_energy
bomb_mass = 1

# Test get_energy
bomb_energy = get_energy(bomb_mass)
print(f"A 1kg bomb supplies {bomb_energy} Joules.")  # Expected output: 9e+16 Joules

# Function to calculate work
def get_work(mass, acceleration, distance):
    force = get_force(mass, acceleration)
    work = force * distance
    return work

# Test get_work
train_work = get_work(train_mass, train_acceleration, train_distance)
print(f"The GE train does {train_work} Joules of work over {train_distance} meters.")  # Expected output: 22680000 Joules

