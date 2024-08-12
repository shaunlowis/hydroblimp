# On board computer for blimp
When all components have arrived, will arrange on a reference grid, then
do an outline of a gondola to go under the balloon filled with a lifting gas.

This will then be modelled in Onshape and added to `/3d_design`

## Electrical
- SEEED STUDIO 113991054 [datasheet](https://www.farnell.com/datasheets/3966714.pdf)

No custom PCB as of yet, due to assignment deadline being too close.

### 3 axis accelerometer
MPU6050, GY521 breakout: 2.3-3.4 Vin

AliExpress page [here](https://www.aliexpress.com/item/1005007231617232.html?spm=a2g0o.productlist.main.3.355875feKwwU4q&algo_pvid=6c07971c-6bd8-4d3a-884e-781a646e45b6&utparam-url=scene%3Asearch%7Cquery_from%3A)

Git repo [here](https://github.com/electroniccats/mpu6050)

Wiring [here](https://mschoeffler.com/2017/10/05/tutorial-how-to-use-the-gy-521-module-mpu-6050-breakout-board-with-the-arduino-uno/)

### LiPo battery
2S battery, for small size and working with ESC. Comes with charger.

HobbyStation page [here](https://hobbystation.co.nz/1-18-roc-lipo-battery-2s-380mah-same-as-fmsc2052-1/)

### Motors
Two brushed motors for differential thrust. Ran fine with 5V input.

### Step down voltage regulator
For converting the LiPo battery down from 7.4V to 5V for powering the micro.

AliExpress page [here](https://www.aliexpress.com/item/1005006244142432.html?spm=a2g0o.productlist.main.25.7eaf5e59tcTZa9&algo_pvid=f6b7edaa-460c-43ce-9464-9f9ba717c609&aem_p4p_detail=202407311703099489957027803350000186218&utparam-url=scene%3Asearch%7Cquery_from%3A&search_p4p_id=202407311703099489957027803350000186218_8)

Datasheet for IC in above found [here](https://www.diodes.com/assets/Datasheets/AP3503F.pdf)

### Servos
Two 3.7g servos for control surfaces.

AliExpress page [here](https://www.aliexpress.com/item/1005003137751361.html?spm=a2g0o.order_list.order_list_main.13.21ef1802dHYc6I)

How to use in arduino [here](https://www.youtube.com/watch?v=SfmHNb5QAzc)

Some conflicting info here, should be able to run off of micro's PWM digital pin.

### ESC
Bidirectional speed controller for 180 brushed motors.

AliExpress page [here](https://www.aliexpress.com/item/1005005466766191.html?spm=a2g0o.detail.pcDetailTopMoreOtherSeller.1.cc42JQCQJQCQBS&gps-id=pcDetailTopMoreOtherSeller&scm=1007.40050.354490.0&scm_id=1007.40050.354490.0&scm-url=1007.40050.354490.0&pvid=4ca67cf3-3ecf-47c9-9871-56fc679ce85f&_t=gps-id:pcDetailTopMoreOtherSeller,scm-url:1007.40050.354490.0,pvid:4ca67cf3-3ecf-47c9-9871-56fc679ce85f,tpp_buckets:668%232846%238115%232000&utparam-url=scene%3ApcDetailTopMoreOtherSeller%7Cquery_from%3A#nav-description)

This has in-built differential thrust support, to be tested.


## Software
There is full Arduino support for the ESP32 micro I've chosen. Details on setting
this up to go here.

Current plan is to write an android app that I can use to control the motor and servo
via bluetooth, as the ESP32 has 11 PWM pins and bluetooth capability.

See `/software` for C++ code.