// example code: https://wiki.dfrobot.com/Romeo_V2-All_in_one_Controller__R3___SKU_DFR0225

//Standard PWM DC control
int E1 = 5;     //M1 Speed Control
int E2 = 6;     //M2 Speed Control
int M1 = 4;    //M1 Direction Control
int M2 = 7;    //M1 Direction Control

///For previous Romeo, please use these pins.
//int E1 = 6;     //M1 Speed Control
//int E2 = 9;     //M2 Speed Control
//int M1 = 7;    //M1 Direction Control
//int M2 = 8;    //M1 Direction Control

// Stop
void stop(void){
  digitalWrite(E1,LOW);
  digitalWrite(E2,LOW);
}         

// Move forward
void advance(char a,char b){
  analogWrite (E1,a);      //PWM Speed Control
  digitalWrite(M1,HIGH);
  analogWrite (E2,b);
  digitalWrite(M2,HIGH);
}

// Move backward
void back_off (char a, char b){ 
  analogWrite (E1, a);
  digitalWrite(M1, LOW);
  analogWrite (E2, b);
  digitalWrite(M2, LOW);
}

// Turn Left
void turn_L (char a, char b){
  analogWrite (E1, a);
  digitalWrite(M1, LOW);
  analogWrite (E2, b);
  digitalWrite(M2, HIGH);
}

// Turn Right
void turn_R (char a, char b){
  analogWrite (E1, a);
  digitalWrite(M1, HIGH);
  analogWrite (E2, b);
  digitalWrite(M2, LOW);
}

void setup(void){
  int i;
  for(i=4;i<=7;i++)
    pinMode(i, OUTPUT);
  Serial.begin(9600);      //Set Baud Rate
  Serial.println("Run keyboard control");
}

void loop() {
  // Read input from Serial monitor
  if (Serial.available() > 0) {
    String inputString = Serial.readStringUntil('\n'); // Read until newline character

    // Remove leading/trailing whitespaces
    inputString.trim();

    // Split the inputString into multiple variables based on space delimiter
    char command;
    int value1, value2;
    int numValues = sscanf(inputString.c_str(), "%c %d %d", &command, &value1, &value2);

    // Check if all three values were successfully extracted
    if (numValues == 3) {
      // Check if command is "m"
      if (command == 'm') {
        // Print the extracted values
        Serial.print("Command: ");
        Serial.print(command);
        
        Serial.print(", Value 1: ");
        Serial.print(value1);
        
        Serial.print(", Value 2: ");
        Serial.println(value2);
          
        if (value1 > 0 and value2 > 0){
          Serial.println("Move Forward");
          advance (value1, value2);
        }
        else if (value1 < 0 and value2 < 0){
          Serial.println("Move Backward");
          back_off (-value1, -value2);
        }
        else if (value1 > 0 and value2 <= 0){
          Serial.println("Turn Right");
          turn_R (value1, value2);
        }
        else if (value1 <= 0 and value2 > 0){
          Serial.println("Turn Left");
          turn_L (value1, value2);
        }
        else if (value1 == 0 and value2 == 0){
          Serial.println("Stop");
          stop();
        }
      } 
      else {
        Serial.println("Invalid command. Please enter 'm' as the command.");
      }
    } 
    else {
      Serial.println("Invalid input. Please enter 'command value1 value2'.");
    }
  }
}