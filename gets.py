def welcome():
    print("Welcome to 1D collison simulator made by Nathan")
    print("Please, enter values for velocity")
    
def get_vel(i):
    print("Velocities permitted: -10 (m/s) to 10 (m/s)")
    vel=float(input(f"Insert inicial velocity for object {i} (m/s): "))
    while vel<-10 or vel>10:
        print("Velocities permitted: -10 (m/s) to 10 (m/s)")
        vel=float(input(f"Insert inicial velocity for object {i} (m/s): "))
    return vel

def get_mass(i):
    print("Please, enter positives massses for the objects")
    mass=float(input(f"Insert mass for object {i} (kg): "))
    while mass<=0:
        print("Please, enter positives massses for the objects")
        mass=float(input(f"Insert mass for object {i} (kg): "))        
    return mass