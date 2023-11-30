#include "eaglesmotors.h"

#define pinForward 10
#define pinBackward 9
#define pinVelocity 8


EaglesMotors MOTOR_NAME_1(pinForward, pinBackward, pinVelocity);


void setup() {
  pinMode(pinForward, OUTPUT);
  pinMode(pinBackward, OUTPUT);
  pinMode(pinVelocity, OUTPUT);
}

void loop() {
  MOTOR_NAME_1.run("F");
}
