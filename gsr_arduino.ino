const int LED=13;
const int GSR=A2;
float sensorValue;
float timeKeeper = 0.0;
int frequency;
int maxLine=700,minLine=0,index=0;


void setup(){
  Serial.begin(9600);
  pinMode(LED,OUTPUT);
  digitalWrite(LED,LOW);
  delay(1000);
  // Serial.print("starting!\ntime = ");
  // Serial.println(micros());
}


void loop(){
  
// micros() Is used to collect the current time

// frequency counting mechanism
  // if(micros() - timeKeeper > 1000000){
  //     Serial.print(frequency);
  //     Serial.print('\t');
  //     frequency=0;
  //     delay(5000);
  //     timeKeeper = micros();
  //   }


  sensorValue=analogRead(GSR);
  index+=1;
  // frequency+=1;
  // Serial.print("sensorValue=");
  // Serial.print(index);
  
  // Serial.print(maxLine);
  // Serial.print('\t');
  // Serial.print(minLine);
  // // Serial.print('\t');
  Serial.print(millis());
  Serial.print('\t');
  Serial.println(sensorValue);
}
