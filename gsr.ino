#include <Arduino.h>

const int LED = 13;
const int GSR = A2;
int sensorValue;
float timeKeeper = 0.0;
int frequency;

void setup()
{
    Serial.begin(9600);
    pinMode(LED, OUTPUT);
    digitalWrite(LED, LOW);
    delay(1000);
    Serial.print("starting!\ntime = ");
    Serial.println(micros());
}

void loop()
{
    // micros() Is used to collect the current time
    if (micros() - timeKeeper > 1000000)
    {
        timeKeeper = micros();
        Serial.print(frequency);
        frequency = 0;
    }
    sensorValue = analogRead(GSR);
    frequency += 1;
    Serial.print("sensorValue=");
    Serial.println(sensorValue);
}