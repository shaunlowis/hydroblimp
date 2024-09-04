import numpy as np

# Sea level gravity
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
        # 3-D printed parts, output from Prusa Slicer
        # Aerofoil & gondola
        (17 / 1000),
        # Density of mylar is: 1400 kg/m3, from
        # https://pml.nist.gov/cgi-bin/Star/compos.pl?matno=222
        # use a mylar thickness of 1 micron
        # Approximating a sphere; 4pi/3*(r2-r1)*rho_mylar
        1400 * ((4 * np.pi) / 3) * (1 * 10**-6),
    ]
)

# We use: A = Vballoon * rho_air * g = Gg
# Thus Vballoon = Gg / rho_air

v_balloon = (total_mass * g) / rho_atm
v_balloon_tropopause = (total_mass * g) / rho_tropopause

print(f"Vehicle mass: {total_mass:.4g} [kg]")
print(f"Vballoon, sea level = {v_balloon:.3f}m^3")
print(f"Vballoon, tropopause = {v_balloon_tropopause:.3f}m^3")

# V = (4/3)*pi*r^3 => r = (((3/4) * V) / pi)^(1/3)
r_balloon = np.cbrt(((3 / 4) * v_balloon) / np.pi)
r_balloon_tropopause = np.cbrt(((3 / 4) * v_balloon_tropopause) / np.pi)
print(f"Balloon r, sea level = {r_balloon:.3f}m")
print(f"Balloon r, tropopause = {r_balloon_tropopause:.3f}m")

# Finding a, c for ellipsoid, where V = 4/3*pi*a^2*b
# a and b are cords, shown in a diagram for this assignment.
# Taking the tropopause radius and volume, we set a = 0.4, then solve for b:
a = c = 0.4
b = 3 * (v_balloon_tropopause) / (a * np.pi * (a**2))
print(f"\nDimensions are: \na={a}m\nV={v_balloon_tropopause:.4g}m^3\nb={b:.4g}m")

print(
    f"\nReference areas are: \nA_ref = {v_balloon_tropopause**(2/3):.4g}\nL_ref = {v_balloon_tropopause**(1/3):.4g}"
)
