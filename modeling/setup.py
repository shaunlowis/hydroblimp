# Instructed to use simupy.
# Here we can configure our Vehicle object.

#  Maybe this is useful?
# https://www.youtube.com/watch?v=ERVrlzttLg4&t=1s

# This paper is a great baseline for me:
# https://www.ijmerr.com/uploadfile/2018/0822/20180822052610906.pdf

# This report has some good content:
# https://reports.nlr.nl/server/api/core/bitstreams/a55813d9-bd3a-462d-a220-f533be6312b7/content

# This function seems most suited:
# https://nasa.github.io/simupy-flight/api.html#simupy_flight.Planet.local_translational_trim_residual

# Included example on trim condition for an aircraft:
# simupy-flight/nesc_test_cases/nesc_case11.py

# Explanation here:
# https://nescacademy.nasa.gov/flightsim

from simupy_flight import Vehicle, Planet

# imports for planet setup, using print(help(Planet)), mirroring simupy-flight/nesc_test_cases/nesc_case01.py
from simupy_flight import (
    earth_J2_gravity,
    get_constant_winds,
    get_constant_atmosphere,
    Planetodetic,
    earth_equitorial_radius,
    earth_rotation_rate,
    earth_f,
)

# my blimp is designed to fly on Earth, for now:
earth_planet = Planet(
    gravity=earth_J2_gravity,
    winds=get_constant_winds(),
    atmosphere=get_constant_atmosphere(),
    planetodetics=Planetodetic(
        a=earth_equitorial_radius,
        omega_p=earth_rotation_rate,
        f=earth_f,
    ),
)

# These coefficients are yet to be defined. See vehicle.pdf for docstring.
# To start with, most of these should be set to zero.

# vehicle = Vehicle(
#     m,
#     I_xx,
#     I_yy,
#     I_zz,
#     I_xy,
#     I_yz,
#     I_xz,
#     x_com,
#     y_com,
#     z_com,  # inertia
#     base_aero_coeffs,
#     x_mrc,
#     y_mrc,
#     z_mrc,
#     S_A,
#     a_l,
#     b_l,
#     c_l,
#     d_l,  # aero
#     input_aero_coeffs,
#     input_force_moment,  # extra callbacks for control modeling
#     input_aero_coeffs_idx,
#     input_force_moment_idx,  # routing for control callbacks
#     dim_extra_input,  # total number of extra (control) inputs
# )
