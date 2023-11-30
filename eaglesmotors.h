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
    void setSpeed(int velocity){
      analogWrite(pinVelocity, velocity);
    }
    void run(char sense){
      if (sense == "F") {
        digitalWrite(pinForward, HIGH);
        digitalWrite(pinBackward, LOW);
      }
      if (sense == "B") {
        digitalWrite(pinForward, LOW);
        digitalWrite(pinBackward, HIGH);
      }
      if (sense == "R") {
        digitalWrite(pinForward, HIGH);
        digitalWrite(pinBackward, LOW);
      }
    }
};
