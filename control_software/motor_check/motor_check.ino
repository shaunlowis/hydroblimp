// START HERE TO FIND POTENTIOMETER LIMITS
// Use below to find which end of potentiometer is 0 and which is max.
// Some ESC's need to be at zero when powered up or the motor won't do anything.
// Follow this vid for wiring: https://www.youtube.com/watch?v=qOzE5F5vFGs

// void setup() {
//   // initialize serial communication at 9600 bits per second:
//   Serial.begin(9600);
// }

// // the loop routine runs over and over again forever:
// void loop() {
//   // read the input on analog pin 0:
//   int sensorValue = analogRead(A0);
//   // print out the value you read:
//   Serial.println(sensorValue);
//   delay(1);  // delay in between reads for stability
// }

// NOW SETUP MOTOR CONTROL
#include <Servo.h>

Servo ESC;

int Speed;

void setup() {
  // put your setup code here, to run once:
  ESC.attach(9, 1000, 2000);

}

void loop() {
  // put your main code here, to run repeatedly:
  Speed = analogRead(A0);

  // Scales the 0-1023 pot reading, to 0-180 for motor.
  Speed = map(Speed, 0, 1023, 0, 180);
  ESC.write(Speed);
}

