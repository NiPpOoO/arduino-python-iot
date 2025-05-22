# Setup Instructions

## Hardware Requirements
- Arduino Uno
- DHT22 Temperature/Humidity Sensor
- MQ135 Air Quality Sensor
- Jumper Wires

## Connections
1. Connect DHT22:
   - VCC → 5V
   - GND → GND
   - DATA → Pin 2
2. Connect MQ135:
   - VCC → 5V
   - GND → GND
   - AOUT → A0

## Software Setup
1. Install Arduino IDE
2. Upload `sensor_read.ino` to Arduino
3. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
- Run the server: python app.py
