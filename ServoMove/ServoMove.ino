#include <ESP32Servo.h>
Servo X;
Servo Y;
String incomingData;
int angleX, angleY;

void setup() 
{
  Serial.begin(9600);

  X.attach(4);
  Y.attach(2);

  X.write(90);
  Y.write(90);
}

void loop() 
{
  if(Serial.available())
  {
    incomingData = Serial.readStringUntil('\n');
    int commaIndex = incomingData.indexOf(',');
 
    angleX = incomingData.substring(0, commaIndex).toInt();
    angleY = incomingData.substring(commaIndex + 1).toInt();
    Serial.print(angleX);
    Serial.print(angleY);
    moveServo(angleX, angleY);
  }
}

void moveServo(int x, int y){
  X.write(x);
  Y.write(y);
}