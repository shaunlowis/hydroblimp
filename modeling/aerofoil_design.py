# Checking out neuralfoil
# github here: https://github.com/peterdsharpe/NeuralFoil

# Using NACA aerofoil: http://airfoiltools.com/airfoil/details?airfoil=naca0012h-sa

# Source:
# https://github.com/peterdsharpe/AeroSandbox/blob/master/tutorial/06%20-%20Aerodynamics/02%20-%20AeroSandbox%202D%20Aerodynamics%20Tools/01%20-%20NeuralFoil.ipynb

import aerosandbox as asb
import aerosandbox.numpy as np
import matplotlib.pyplot as plt
import aerosandbox.tools.pretty_plots as p

# aero = nf.get_aero_from_airfoil(  # You can use AeroSandbox airfoils as an entry point
#     airfoil=asb.Airfoil("naca0012"),  # any UIUC or NACA airfoil name works
#     alpha=5,
#     Re=5e6,
# )

af = asb.Airfoil("naca0012")

re = np.geomspace(1e5, 1e7, 50)
# This is about 1.2 -> 12 kmh at sea level
mach = np.linspace(0.001, 0.010, 50)
alpha = np.linspace(-3, 7, 50)

Re, Mach, Alpha = np.meshgrid(re, mach, alpha)

aero_f = af.get_aero_from_neuralfoil(
    alpha=Alpha.flatten(),
    Re=Re.flatten(),
    mach=Mach.flatten(),
)
aero = {k: np.reshape(v, Re.shape) for k, v in aero_f.items()}

fig, ax = plt.subplots()

LD = np.max(aero["CL"] / aero["CD"], axis=-1)

p.contour(
    re,
    mach,
    LD,
    levels=np.arange(0, 400, 10),
    x_log_scale=True,
    cmap="RdBu",
    alpha=0.6,
    colorbar_label="Max-Achievable Airfoil $L/D$ across all $\\alpha$",
)
plt.clim(20, 160)
plt.xscale("log")

afax = ax.inset_axes([0.05, 0.8, 0.25, 0.20])
afax.fill(
    af.x(), af.y(), facecolor=(0, 0, 0, 0.2), linewidth=1, edgecolor=(0, 0, 0, 0.7)
)
afax.annotate(
    text=f"{af.name} Airfoil\n",
    xy=(0.5, 0),
    ha="center",
    va="bottom",
    fontsize=10,
    alpha=0.9,
)
afax.axis("off")
afax.axis("equal")

ax.set_xlabel("Reynolds Number [-]")
ax.set_ylabel("Mach Number [-]")
ax.set_title(f"Maximum-Achievable Airfoil $L/D$ for {af.name} Airfoil")

plt.savefig(f"max_l-d-{af.name}.jpg")

# p.show_plot(
#     title=f"Maximum-Achievable Airfoil $L/D$ for {af.name} Airfoil",
#     xlabel="Reynolds Number [-]",
#     ylabel="Mach Number [-]",
# )


# Repeat above but also make lift drag polars.

af = asb.Airfoil("naca0012")

alpha = np.linspace(-10, 18, 181)
re = np.geomspace(1e4, 1e8, 5)

Alpha, Re = np.meshgrid(alpha, re)

aero_flattened = af.get_aero_from_neuralfoil(
    alpha=Alpha.flatten(),
    Re=Re.flatten(),
    mach=0,
    model_size="xxxlarge",
)
Aero = {key: value.reshape(Alpha.shape) for key, value in aero_flattened.items()}

from matplotlib.colors import LinearSegmentedColormap
from aerosandbox.tools.string_formatting import eng_string

fig, ax = plt.subplots()
colors = LinearSegmentedColormap.from_list(
    "custom_cmap",
    colors=[
        p.adjust_lightness(c, 0.8) for c in ["orange", "darkseagreen", "dodgerblue"]
    ],
)(np.linspace(0, 1, len(re)))

for i in range(len(re)):
    (line,) = ax.plot(
        Aero["CD"][i, :],
        Aero["CL"][i, :],
        color=colors[i],
        alpha=0.8,
    )

    plt.annotate(
        f" $Re = \\mathrm{{{eng_string(re[i])}}}$",
        xy=(line.get_xdata()[-1], line.get_ydata()[-1]),
        color=colors[i],
        ha="left",
        va="center",
        fontsize=10,
    )

afax = ax.inset_axes([0.76, 0.802, 0.23, 0.23])
afax.fill(
    af.x(), af.y(), facecolor=(0, 0, 0, 0.2), linewidth=1, edgecolor=(0, 0, 0, 0.7)
)
afax.annotate(
    text=f"{af.name} Airfoil\n",
    xy=(0.5, 0),
    ha="center",
    va="bottom",
    fontsize=10,
    alpha=0.7,
)
afax.axis("off")
afax.axis("equal")

plt.xscale("log")

ax.set_xlabel("Drag Coefficient $C_D$")
ax.set_ylabel("Lift Coefficient $C_L$")
ax.set_title(f"Maximum-Achievable Airfoil $L/D$ for {af.name} Airfoil")

plt.savefig(f"Cl-Cd-{af.name}.jpg")

# p.show_plot(
#     title=f"$C_L$-$C_D$ Polar for {af.name} Airfoil",
#     xlabel="Drag Coefficient $C_D$",
#     ylabel="Lift Coefficient $C_L$",
# )
