const int ledPin8 = 8;
const int ledPin9 = 9;
const int ledPin10 = 10;
const int buttonPin11 = 11;
const int buttonPin12 = 12;
const int buttonPin13 = 13;

bool leerPotenciometro = true;

void setup() {
  pinMode(ledPin8, OUTPUT);
  pinMode(ledPin9, OUTPUT);
  pinMode(ledPin10, OUTPUT);
  pinMode(buttonPin11, INPUT_PULLUP);
  pinMode(buttonPin12, INPUT_PULLUP);
  pinMode(buttonPin13, INPUT_PULLUP);  
  Serial.begin(9600);
}

void loop() {
  if (leerPotenciometro) {
    int pot = analogRead(A1);
    Serial.println(pot);
    delay(5);
  }
  int buttonState11 = digitalRead(buttonPin11);
  int buttonState12 = digitalRead(buttonPin12);
  int buttonState13 = digitalRead(buttonPin13);
  
  if (buttonState11 == LOW) {
    Serial.println("Inorden ejecutado");
    digitalWrite(ledPin8, HIGH);
    Serial.println(1);
    delay(1000);
    digitalWrite(ledPin8, LOW);
    Serial.println(0);
    delay(1000);
    digitalWrite(ledPin10, HIGH);
    Serial.println(3);
    delay(1000);
    digitalWrite(ledPin10, LOW);
    Serial.println(0);
    delay(1000);
    digitalWrite(ledPin9, HIGH);
    Serial.println(2);
    delay(1000);
    digitalWrite(ledPin9, LOW);
    Serial.println(0);
    delay(1000);
    Serial.println("Inorden terminado");
  }
  if(buttonState12 == LOW){
    Serial.println("Posorden ejecutado");
    digitalWrite(ledPin10, HIGH);
    Serial.println(3);
    delay(1000);
    digitalWrite(ledPin10, LOW);
    Serial.println(0);
    delay(1000);
    digitalWrite(ledPin8, HIGH);
    Serial.println(1);
    delay(1000);
    digitalWrite(ledPin8, LOW);
    Serial.println(0);
    delay(1000);
    digitalWrite(ledPin9, HIGH);
    Serial.println(2);
    delay(1000);
    digitalWrite(ledPin9, LOW);
    Serial.println(0);
    delay(1000);
    Serial.println("Posorden terminado");
  }
  if(buttonState13 == LOW){
    Serial.println("Preorden ejecutado");
    digitalWrite(ledPin9, HIGH);
    Serial.println(2);
    delay(1000);
    digitalWrite(ledPin9, LOW);
    Serial.println(0);
    delay(1000);
    digitalWrite(ledPin10, HIGH);
    Serial.println(3);
    delay(1000);
    digitalWrite(ledPin10, LOW);
    Serial.println(0);
    delay(1000);
    digitalWrite(ledPin8, HIGH);
    Serial.println(1);
    delay(1000);
    digitalWrite(ledPin8, LOW);
    Serial.println(0);
    Serial.println("Preorden terminado");
  }
}
