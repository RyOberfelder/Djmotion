
char switchList[] = "A1B1C1";
int stateA = 0; 
int stateB = 0; 
int stateC = 0; 
int stateD = 0; 
int stateE = 0; 
int stateF = 0; 
int pinA = 2; 
int pinB = 3; 
int pinC = 4; 
int pinD = 0; 
int pinE = 0; 
int pinF = 0; 

// the setup routine runs once when you press reset:
void setup() {
    pinMode(pinA, INPUT);
    pinMode(pinB, INPUT);
    pinMode(pinC, INPUT);
    switchList[0] = 'A'; 
    switchList[2] = 'B'; 
    switchList[4] = 'C'; 
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
  stateA = digitalRead(pinA);
  stateB = digitalRead(pinB);
  stateC = digitalRead(pinC);
  if (stateA == HIGH) {
    // turn LED on:
   switchList[1] = '1';
  } else {
    // turn LED off:
    switchList[1] = '0';
  }
  
    if (stateB == HIGH) {
    // turn LED on:
   switchList[3] = '1';
  } else {
    // turn LED off:
    switchList[3] = '0';
  }
  
    if (stateC == HIGH) {
    // turn LED on:
   switchList[5] = '1';
  } else {
    // turn LED off:
   switchList[5] = '0';
  }
  Serial.print(switchList);
  delay(1);        // delay in between reads for stability
}
