import numpy as np

g = 9.8066


# at sea level:
rho_atm = 1.225  # kg/m^3
rho_helium = 0.178  # kg/m^3

# ISA defines density at the tropopause (11,000m) as 0.3639 kg/m^3
# https://en.wikipedia.org/wiki/International_Standard_Atmosphere
rho_tropopause = 0.3639

# component masses [kg]
total_mass = sum(
    [
        # servos
        ((4.8 + 5) / 1000),
        # ESP32
        (3.7 / 1000),
        # Accelerometer
        (1.1 / 1000),
        # LiPo battery
        (17.8 / 1000),
        # Motors
        ((2 + 2.2) / 1000),
        # Voltage regulator
        (2 / 1000),
        # Motor ESC
        (6.9 / 1000),
        # Add 3d print when sliced
        0,
        # TODO: Add in the weight of the balloon:
        # https://pml.nist.gov/cgi-bin/Star/compos.pl?matno=222
    ]
)

# We use: A = Vballoon * rho_air * g = Gg
# Thus Vballoon = Gg / rho_air

v_balloon = (total_mass * g) / rho_atm
v_balloon_tropopause = (total_mass * g) / rho_tropopause

print(f"Vballoon = {v_balloon:.3f}m^3")
print(f"Vballoon, tropopause = {v_balloon_tropopause:.3f}m^3")

# V = (4/3)*pi*r^3 => r = (((3/4) * V) / pi)^(1/3)
d_balloon = 2 * np.cbrt(((3 / 4) * v_balloon) / np.pi)
d_balloon_tropopause = 2 * np.cbrt(((3 / 4) * v_balloon_tropopause) / np.pi)
print(f"Balloon diameter = {d_balloon:.3f}m")
print(f"Balloon diameter, tropopause = {d_balloon_tropopause:.3f}m")
