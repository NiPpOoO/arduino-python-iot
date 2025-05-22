#include <Arduino.h>
#include <DHT.h>
#include <MQ135.h>
#include <unity.h>

DHT dht(2, DHT22);
MQ135 gasSensor(A0);

void test_dht_reading() {
    float t = dht.readTemperature();
    TEST_ASSERT_FALSE(isnan(t));
}

void test_mq135_reading() {
    float ppm = gasSensor.getPPM();
    TEST_ASSERT_TRUE(ppm > 0);
}

void setup() {
    delay(2000);
    UNITY_BEGIN();
    RUN_TEST(test_dht_reading);
    RUN_TEST(test_mq135_reading);
    UNITY_END();
}

void loop() {}
