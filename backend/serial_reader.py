import serial
import time
from threading import Thread
from flask_sqlalchemy import SQLAlchemy
from app import app, db, SensorData

def read_serial():
    ser = serial.Serial('COM3', 9600, timeout=1)
    while True:
        try:
            line = ser.readline().decode('utf-8').strip()
            if line:
                temp, humidity, ppm = map(float, line.split(','))
                new_data = SensorData(
                    temperature=temp,
                    humidity=humidity,
                    air_quality=ppm,
                    timestamp=datetime.now()
                )
                db.session.add(new_data)
                db.session.commit()
        except Exception as e:
            print(f"Error reading serial: {e}")
        time.sleep(1)

if __name__ == '__main__':
    thread = Thread(target=read_serial)
    thread.start()
