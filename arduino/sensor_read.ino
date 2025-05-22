#include <DHT.h>
#include <MQ135.h>

#define DHTPIN 2
#define DHTTYPE DHT22
#define ANALOGPIN A0

DHT dht(DHTPIN, DHTTYPE);
MQ135 gasSensor = MQ135(ANALOGPIN);

void setup() {
  Serial.begin(9600);
  dht.begin();
  pinMode(ANALOGPIN, INPUT);
}

void loop() {
  float humidity = dht.readHumidity();
  float temperature = dht.readTemperature();
  float ppm = gasSensor.getPPM();
  
  if (isnan(humidity) || isnan(temperature)) {
    Serial.println("Error reading DHT sensor!");
    delay(2000);
    return;
  }

  // Format: temp,humidity,ppm
  Serial.print(temperature);
  Serial.print(",");
  Serial.print(humidity);
  Serial.print(",");
  Serial.println(ppm);
  
  delay(5000); // 5-second interval
}
