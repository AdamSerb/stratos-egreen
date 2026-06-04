int capH = A0;
int relay = 13;
int capValue = 0;

char command;
bool manualMode = false;

void setup() {
  Serial.begin(9600);
  pinMode(capH, INPUT);
  pinMode(relay, OUTPUT);
}

void loop() {

  // Check if Python sent something
  if (Serial.available()) {
    command = Serial.read();

    if (command == '1') {
      digitalWrite(relay, LOW);  // ON (active LOW relay)
      manualMode = true;
    }

    if (command == '0') {
      digitalWrite(relay, HIGH); // OFF
      manualMode = true;
    }

    if (command == 'A') {
      manualMode = false; // العودة للوضع التلقائي
    }
  }

  // Automatic mode only if not manual
  if (!manualMode) {
    capValue = analogRead(capH);
    Serial.println(capValue);

    if (capValue > 600){
      digitalWrite(relay, LOW);
    } else {
      digitalWrite(relay, HIGH);
    }

    delay(1000);
  }
}
