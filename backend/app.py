from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sensor.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class SensorData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Float)
    humidity = db.Column(db.Float)
    air_quality = db.Column(db.Float)
    timestamp = db.Column(db.DateTime)

@app.route('/api/current', methods=['GET'])
def get_current():
    data = SensorData.query.order_by(SensorData.timestamp.desc()).first()
    return jsonify({
        'temperature': data.temperature,
        'humidity': data.humidity,
        'air_quality': data.air_quality,
        'timestamp': data.timestamp.isoformat()
    })

@app.route('/api/history', methods=['GET'])
def get_history():
    hours = request.args.get('hours', default=24, type=int)
    time_threshold = datetime.now() - timedelta(hours=hours)
    data = SensorData.query.filter(SensorData.timestamp >= time_threshold).all()
    return jsonify([{
        'temperature': d.temperature,
        'humidity': d.humidity,
        'air_quality': d.air_quality,
        'timestamp': d.timestamp.isoformat()
    } for d in data])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000)
