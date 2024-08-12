# hydroblimp
Making a hydrogen generator and a remote control mini blimp.

## ENME 448 Setup
Fulfil criteria outlined in `ENME488-Assignment.pdf`.

Existing vehicle this is based on is a high altitude blimp.
Real world example [here](
  https://www.ilcdover.com/products/high-altitude-airships/
)

and some [further reading](
  https://en.wikipedia.org/wiki/High-altitude_platform_station
)
shows typical operating point at >18km.

For our use case, I will use my electronics as a baseline, then
scale the rest of my control surfaces and vehicle at some ratio
to the real world thing.

The size of the balloon will the be a smaller ratio of the max
height outputted in `balloon_sizing.py`

Trim condition set for high altitude flight.

### Python setup

```
# install python however you want, I use 3.10 on Ubuntu;
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.10-venv

# venv
python3.10 -m venv .venv
source .venv/bin/activate

# install required packages
pip install -r requirements.txt

# Install simupy;
git submodule update --init --recursive
cd simupy-flight/
python -m pip install .
```

## Hydrogen generator
Use electrolysis as our generation method. Further details in `/hydro`.

- 3d printed mount (Need to use ABS not PLA)
- Some guesses at expected yield.

### Fluidics
Need a jig to store the HHO gas, a good method would be an inverted jar
approach, but also need a one way valve and some method to pressurise the
balloon for the blimp:

- Piping diagram.
- Pump setup.

  ### Inspirations:
  Hydrogen generator setups:
  
  Very basic: https://www.youtube.com/watch?v=08XGs7pZSlE
  Very cool: https://www.youtube.com/watch?v=oIWgzVaGn4Y

  RC blimp:

  First result searching "blimp" on thingiverse: https://github.com/mRoboticsIO/Blimpduino2
