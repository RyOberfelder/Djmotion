
char switchList[] = "A1,B1,C1,D1,E1,Z00,Y00,X00,W00,";
int stateA = 0; 
int stateB = 0; 
int stateC = 0; 
int stateD = 0; 
int stateE = 0; 
int stateF = 0; 
int pinA = 2; 
int pinB = 6; 
int pinC = 3; 
int pinD = 4; 
int pinE = 5; 
int pinF = 0; 
const int analogout1 = 9;
String sensor1str;
const int analogInPin1 = A0;  // Analog input pin that the potentiometer is attached to
int sensor1 = 0;        // value read from the pot
int sensor1out = 0;
const int analogout2 = 10;
String sensor2str;
const int analogInPin2 = A1;  // Analog input pin that the potentiometer is attached to
int sensor2 = 0;        // value read from the pot
int sensor2out = 0;
const int analogout3 = 11;
String sensor3str;
const int analogInPin3 = A2;  // Analog input pin that the potentiometer is attached to
int sensor3 = 0;        // value read from the pot
int sensor3out = 0;
const int analogout4 = 12;
String sensor4str;
const int analogInPin4 = A3;  // Analog input pin that the potentiometer is attached to
int sensor4 = 0;        // value read from the pot
int sensor4out = 0;

// the setup routine runs once when you press reset:
void setup() {
    pinMode(pinA, INPUT);
    pinMode(pinB, INPUT);
    pinMode(pinC, INPUT);
    pinMode(pinD, INPUT);
    pinMode(pinE, INPUT);
    switchList[0] = 'A'; 
    switchList[3] = 'B'; 
    switchList[6] = 'C'; 
    switchList[9] = 'D'; 
    switchList[12] = 'E'; 
  //  pinMode(switchD, INPUT);
  //  pinMode(switchE, INPUT);
  //  pinMode(switchF, INPUT);
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}

// the loop routine runs over and over again forever:
void loop() {
  // read the input on analog pin 0:
  // print out the value you read:
  sensor1 = analogRead(analogInPin1);
  sensor1out = map(sensor1, 0, 255, 0, 255);
  analogWrite(analogout1, sensor1out);
   sensor1str = String(sensor1, HEX);

    sensor2 = analogRead(analogInPin2);
  sensor2out = map(sensor2, 0, 255, 0, 255);
  analogWrite(analogout2, sensor2out);
   sensor2str = String(sensor2, HEX);

    sensor3 = analogRead(analogInPin3);
  sensor3out = map(sensor3, 0, 255, 0, 255);
  analogWrite(analogout3, sensor3out);
   sensor3str = String(sensor3, HEX);

    sensor4 = analogRead(analogInPin4);
  sensor4out = map(sensor4, 0, 255, 0, 255);
  analogWrite(analogout3, sensor4out);
  sensor4str = String(sensor4, HEX);
  
  stateA = digitalRead(pinA);
  stateB = digitalRead(pinB);
  stateC = digitalRead(pinC);
  stateD = digitalRead(pinD);
  stateE = digitalRead(pinE);
  if (stateA == HIGH) {
    // turn LED on:
   switchList[1] = '1';
  } else {
    // turn LED off:
    switchList[1] = '0';
  }
  
    if (stateB == HIGH) {
    // turn LED on:
   switchList[4] = '1';
  } else {
    // turn LED off:
    switchList[4] = '0';
  }
  
    if (stateC == HIGH) {
    // turn LED on:
   switchList[7] = '1';
  } else {
    // turn LED off:
   switchList[7] = '0';
  }

  if (stateD == HIGH) {
    // turn LED on:
   switchList[10] = '1';
  } else {
    // turn LED off:
   switchList[10] = '0';
  }

  if (stateE == HIGH) {
    // turn LED on:
   switchList[13] = '1';
  } else {
    // turn LED off:
   switchList[13] = '0';
  }

  if(sensor1str.length()>1){
    switchList[16] = sensor1str[0];
    switchList[17] = sensor1str[1];
  }else{
    switchList[16] = '0';
    switchList[17] = sensor1str[0];
  }

  if(sensor2str.length()>1){
    switchList[20] = sensor2str[0];
    switchList[21] = sensor2str[1];
  }else{
    switchList[20] = '0';
    switchList[21] = sensor2str[0];
  }

  if(sensor3str.length()>1){
    switchList[24] = sensor3str[0];
    switchList[25] = sensor3str[1];
  }else{
    switchList[24] = '0';
    switchList[25] = sensor3str[0];
  }

  if(sensor4str.length()>1){
    switchList[28] = sensor4str[0];
    switchList[29] = sensor4str[1];
  }else{
    switchList[28] = '0';
    switchList[29] = sensor4str[0];
  }
  Serial.print(switchList);
  delay(200);        // delay in between reads for stability
}
