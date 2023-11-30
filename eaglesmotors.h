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
        digitalWrite(this.pinForward, HIGH);
        digitalWrite(this.pinBackward, LOW);
        analogWrite(this.pinVelocity, velocity);
      }
      if (sense == "B") {
        digitalWrite(this.pinForward, LOW);
        digitalWrite(this.pinBackward, HIGH);
        analogWrite(this.pinVelocity, velocity);
      }
      if (sense == "R") {
        digitalWrite(this.pinForward, HIGH);
        digitalWrite(this.pinBackward, LOW);
        analogWrite(this.pinVelocity, velocity);
      }
    }
    void setSpeed(int velocity){
      analogWrite(this.pinVelocity, velocity);
    }
    void run(char sense){
      if (sense == "F") {
        digitalWrite(this.pinForward, HIGH);
        digitalWrite(this.pinBackward, LOW);
      }
      if (sense == "B") {
        digitalWrite(this.pinForward, LOW);
        digitalWrite(this.pinBackward, HIGH);
      }
      if (sense == "R") {
        digitalWrite(this.pinForward, HIGH);
        digitalWrite(this.pinBackward, LOW);
      }
    }
};
