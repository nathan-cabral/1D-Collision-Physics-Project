def get_vel(i):
    print("Welcome to 1D collison simulator made by Nathan")
    print("Please, enter values for velocity")
    print("Velocities permitted: -10 (m/s) to 10 (m/s)")
    vel=float(input(f"Insert inicial velocity for object {i} (m/s): "))
    while vel<-10 or vel>10:
        vel=float(input(f"Insert inicial velocity for object {i} (m/s): "))
    return vel

def get_mass(i):
    print("Please, enter positives massses for the objects")
    mass=float(input("Insert mass for object 1 (kg): "))
    while mass<=0:
        print("Please, enter positives massses for the objects")
        mass=float(input("Insert mass for object 1 (kg): "))        
    return mass