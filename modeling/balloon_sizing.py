import numpy as np

g = 9.8066

# at sea level:
rho_atm = 1.225  # kg/m^3
rho_helium = 0.178  # kg/m^3

# component masses [kg]
# TODO: measure these when they've arrived.
total_mass = sum(
    [
        # ESP32
        (1 / 1000),
        # Accelerometer
        (1 / 1000),
        # LiPo battery
        (50 / 1000),
        # Motors
        ((2 * 33) / 1000),
        # Servos (360deg heavies)
        (2 * 10) / 1000,
        # Mass distribution system
        (15 / 1000),
        # Additional weights for helium diffusion through mylar over time
        (30 / 1000),
        # Voltage regulator guess
        (2 / 1000),
        # Add 3d print when sliced
        0,
    ]
)

# We use: A = Vballoon * rho_air * g = Gg
# Thus Vballoon = Gg / rho_air

v_balloon = (total_mass * g) / rho_atm

print(f"Vballoon = {v_balloon:.3f}m^3")
# V = (4/3)*pi*r^3 => r = (((3/4) * V) / pi)^(1/3)
d_balloon = np.cbrt(((3 / 4) * v_balloon) / np.pi)
print(f"Balloon diameter = {d_balloon:.3f}m")


# TODO: Max height calc, then some scaling to make model.