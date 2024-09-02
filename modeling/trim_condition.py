"""
NOTE: MODIFIED BY SHAUN LOWIS, AUG 31st 2024

BUILDING VEHICLE GEOMETRY
"""

from simupy.block_diagram import BlockDiagram
import simupy_flight
import numpy as np

from nesc_testcase_helper import benchmark
from nesc_testcase_helper import ft_per_m

# post-processing results
import matplotlib.pyplot as plt
import matplotlib as mpl

plt.rcParams["figure.dpi"] = 250
mpl.rc("axes", labelsize=10, titlesize=16, linewidth=0.2)
mpl.rc("legend", fontsize=10)
mpl.rc("xtick", labelsize=12)
mpl.rc("xtick.major", size=2, width=0.5)
mpl.rc("xtick.minor", size=1, width=0.25, visible=True)
mpl.rc("ytick", labelsize=12)
mpl.rc("ytick.major", size=2, width=0.5)
mpl.rc("ytick.minor", size=1, width=0.25, visible=True)

# Font
plt.rc("font", family="serif")
plt.rc("text", usetex=True)
plt.rc("font", **{"serif": ["Times New Roman"]})

planet = simupy_flight.Planet(
    gravity=simupy_flight.get_spherical_gravity(
        simupy_flight.earth_spherical_gravity_constant
    ),
    winds=simupy_flight.get_constant_winds(),
    atmosphere=simupy_flight.atmosphere_1976,
    planetodetics=simupy_flight.Planetodetic(
        a=20902255.199 / ft_per_m, omega_p=0.0, f=0.0
    ),
)


# Inertia tensor is:
#   I = M/5 * (
#               b^2+c^2    0       0
#                  0    a^2+c^2    0
#                  0       0    a^2+b^2
#             )
# We have a = c = 0.4 and b = 2.749 [m], M = 0.06836 [kg]

# This gives:
#   I = M/5 * (
#               b^2+a^2    0       0
#                  0      2a^2     0
#                  0       0    a^2+b^2
#             )
#     = 0.06836/5 * (
#               2.749^2+0.4^2    0       0
#                  0      2*0.4^2     0
#                  0       0    0.4^2+2.749^2
#             )

# This gives:
#   I = (
#        0.1055     0       0
#           0    0.00438    0
#           0       0     0.1055
#       )

# Units are kg/m^2
Ixx = 0.1055
Iyy = 0.00438
Izz = 0.1055
Ixy = 0.0
Iyz = 0.0
Izx = 0.0
m = 0.06836

# Stay the same
x = 0.0
y = 0.0
z = 0.0

S_A = 1.503
b_l = 1.226
c_l = 1.226
a_l = b_l

# Height for initial conditions
h_ic = 30_000 / ft_per_m
R = 6371 * 1000
g_0 = 9.807  # gravity at sea level

g_ic = g_0 * ((R / (R + h_ic)) ** 2)

# See report for justification
g_avg = (g_ic + 9.81) / 2

# Add in buoyancy force.
vehicle = simupy_flight.Vehicle(
    base_aero_coeffs=simupy_flight.get_constant_aero(CD_b=0.1),
    input_force_moment=np.array(
        [
            0.0,  # FX
            0.0,  # FY
            -m * g_avg,  # FZ, buoyancy force
            0.0,  # MX
            0.0,  # MY
            0.0,  # MZ
        ]
    ),
    m=m,
    I_xx=Ixx,
    I_yy=Iyy,
    I_zz=Izz,
    I_xy=Ixy,
    I_yz=Iyz,
    I_xz=Izx,
    x_com=x,
    y_com=y,
    z_com=z,
    x_mrc=x,
    y_mrc=y,
    z_mrc=z,
    S_A=S_A,
    a_l=a_l,
    b_l=b_l,
    c_l=c_l,
    d_l=0.0,
)

BD = BlockDiagram(planet, vehicle)
BD.connect(planet, vehicle, inputs=np.arange(planet.dim_output))
BD.connect(vehicle, planet, inputs=np.arange(vehicle.dim_output))

lat_ic = 0.0 * np.pi / 180
long_ic = 0.0 * np.pi / 180

V_N_ic = 0.0
V_E_ic = 0.0
V_D_ic = 0.0

psi_ic = 0.0 * np.pi / 180
theta_ic = 0.0 * np.pi / 180
phi_ic = 0.0 * np.pi / 180

omega_X_ic = 0.0 * np.pi / 180
omega_Y_ic = 0.0 * np.pi / 180
omega_Z_ic = 0.0 * np.pi / 180

planet.initial_condition = planet.ic_from_planetodetic(
    long_ic, lat_ic, h_ic, V_N_ic, V_E_ic, V_D_ic, psi_ic, theta_ic, phi_ic
)
planet.initial_condition[-3:] = omega_X_ic, omega_Y_ic, omega_Z_ic


DEFAULT_INTEGRATOR_OPTIONS = {
    "name": "dopri5",
    "rtol": 1e-6,
    "atol": 1e-12,
    "nsteps": 500,
    "max_step": 0.0,
}

with benchmark() as b:
    res_fine_gravity = BD.simulate(300, integrator_options=DEFAULT_INTEGRATOR_OPTIONS)
