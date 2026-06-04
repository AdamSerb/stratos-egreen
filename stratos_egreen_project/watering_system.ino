#include <DHT.h>
#define DHTPIN 2
#define DHTTYPE DHT11
DHT dht(DHTPIN, DHTTYPE);
const int soilPin = A0;
const int pumpPin = 3;
float lastTemp = 24.0; 
float lastHum = 50.0;
int threshold = 500;
bool autoMode = true;
unsigned long lastDHTRead = 0;
void setup() {
  Serial.begin(9600);
  Serial.setTimeout(10);
  pinMode(pumpPin, OUTPUT);
  dht.begin();
}
void loop() {
  if (Serial.available() > 0) {
    char cmd = Serial.read();
    if (cmd == 'A') autoMode = true;
    if (cmd == 'M') autoMode = false;
    if (cmd == 'S') threshold = Serial.parseInt();
    if (!autoMode) {
      if (cmd == '1') digitalWrite(pumpPin, HIGH);
      if (cmd == '0') digitalWrite(pumpPin, LOW);
    }
  }
  int soilValue = analogRead(soilPin);
  if (millis() - lastDHTRead > 2000) {
    float t = dht.readTemperature();
    float h = dht.readHumidity();
    if (!isnan(t) && !isnan(h) && t > 0 && h > 0) {
      lastTemp = t;
      lastHum = h;
    }
    lastDHTRead = millis();
  }
  if (autoMode) {
    if (soilValue > threshold) digitalWrite(pumpPin, HIGH);
    else digitalWrite(pumpPin, LOW);
  }
  Serial.print(soilValue);
  Serial.print(",");
  Serial.print(lastTemp);
  Serial.print(",");
  Serial.println(lastHum);
  delay(200); 
}