#include "eaglesmotors.h"

#define pinForward1 10
#define pinBackward1 9
#define pinVelocity1 8
#define pinForward2 7
#define pinBackward2 6
#define pinVelocity2 5

EaglesMotors MOTOR_NAME_1(pinForward1, pinBackward1, pinVelocity1);
EaglesMotors MOTOR_NAME_2(pinForward2, pinBackward2, pinVelocity2);

void setup() {
  pinMode(pinForward, OUTPUT);
  pinMode(pinBackward, OUTPUT);
  pinMode(pinVelocity, OUTPUT);
}

void loop() {
  MOTOR_NAME_1.setMoviment("F", 200);
  MOTOR_NAME_2.setMoviment("B", 200);
}
