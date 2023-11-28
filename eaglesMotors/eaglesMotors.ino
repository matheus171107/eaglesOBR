class EaglesMotors {
  int pinForward, pinBackward, pinVelocity;
  public:
    EaglesMotors(int pfw, int pbw, int pvt){
      pinForward = pfw;
      pinBackward = pbw;
      pinVelocity = pvt;
    }
    void setMoviment(char sense, int velocity){
      if (sense == "F") {
        digitalWrite(pinForward, HIGH);
        digitalWrite(pinBackward, LOW);
        analogWrite(pinVelocity, velocity);
      }
      if (sense == "B") {
        digitalWrite(pinForward, LOW);
        digitalWrite(pinBackward, HIGH);
        analogWrite(pinVelocity, velocity);
      }
      if (sense == "R") {
        digitalWrite(pinForward, HIGH);
        digitalWrite(pinBackward, LOW);
        analogWrite(pinVelocity, velocity);
      }
    }
};

EaglesMotors MOTOR_NAME_1(6, 7, 5); 
EaglesMotors MOTOR_NAME_2(4, 3, 10);




void setup(){
  pinMode(, OUTPUT);
}
void loop(){
  MOTOR_NAME_1.setMoviment("B", 200);
  MOTOR_NAME_2.setMoviment("F", 200);
}