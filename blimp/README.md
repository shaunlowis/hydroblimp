# Blimp
Components and assembly of the RC blimp will be outlined here.

A single motor, dual servo design is planned for use.

## Motor / ESC
I got an EMAX RS2205 brushless motor, which is definitely overkill for this project.

It was however, very cheap and can be found nearly anywhere. Alongside it, I got a 
LittleBee Spring 20A ESC motor controller. For more info on what an ESC is, I found 
[this article](https://www.tytorobotics.com/blogs/articles/what-is-an-esc-how-does-an-esc-work)
to be well-written.

To connect these specific components, you can solder any of the motor's wires to the exposed terminal
on the ESC.

For the latter, I didn't have to configure any firmware, but you can do so [here](https://esc-configurator.com/).
Note, for ESC flashing, you will need a USB and can then select the BLHeli_S firmware.

When powered up, the ESC emits three beeps, during which you should set your supply voltage to low.
Check out the `software/motor_check.ino` file for more info on getting set up with basics.

For further info on this ESC, check out `docs/BLHeli Instruction.pdf`.

With some confidence in basic wiring and functional checks of my components, I can move to
controlling the motor via my ESP32.