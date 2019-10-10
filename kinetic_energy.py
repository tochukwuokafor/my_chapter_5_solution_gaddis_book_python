def kinetic_energy(mass, velocity):
    energy = 0.5 * mass * (velocity ** 2)
    return energy

def main():
    mass = float(input('Enter the mass of the object (in kilograms): '))
    velocity = float(input('Enter the velocity of the object (in meters per second): '))
    k_energy = kinetic_energy(mass, velocity)
    print('The kinetic energy of the object is', k_energy)

main()