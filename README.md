# hydroblimp
Making a hydrogen generator and a remote control mini blimp.

## ENME 448 Setup
Work mostly done in `modeling` folder. Outputs are in `report` and `plots`.

Full report is `ENME488_Flight_Mechanics_Assignment.pdf`.

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