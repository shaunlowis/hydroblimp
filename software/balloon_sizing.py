g = 9.8066

# at sea level:
rho_atm = 1.929  # kg/m^3
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
        (50 / 1000),
        # Servos
        (2 * 3.7) / 1000,
        # Voltage regulator guess
        (2 / 1000),
        # Add 3d print when sliced
        0,
    ]
)
