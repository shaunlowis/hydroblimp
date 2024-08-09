# hydroblimp
Making a hydrogen generator and a remote control mini blimp.

## Python setup

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

## Hydrogen generator;
Use electrolysis as our generation method. Further details in `/hydro`.

- 3d printed mount (Need to use ABS not PLA)
- Some guesses at expected yield.

## Fluidics;
Need a jig to store the HHO gas, a good method would be an inverted jar
approach, but also need a one way valve and some method to pressurise the
balloon for the blimp:

- Piping diagram.
- Pump setup.

## Blimp;
First idea is a single motor with two fins being actuated by servo's.
Mostly for simplicity, but might be good from a weight reduction approach.

- PCB.
- Air frame.
- Radio link/controller of some kind.
- Some guesses at buoyancy and mylar balloon shape.


  ### Inspirations:
  Hydrogen generator setups:
  
  Very basic: https://www.youtube.com/watch?v=08XGs7pZSlE
  Very cool: https://www.youtube.com/watch?v=oIWgzVaGn4Y

  RC blimp:

  First result searching "blimp" on thingiverse: https://github.com/mRoboticsIO/Blimpduino2
