import pytest
from app import app, db, SensorData

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
        db.drop_all()

def test_get_current_empty(client):
    response = client.get('/api/current')
    assert response.status_code == 200
    assert response.json == None

def test_add_and_get_data(client):
    test_data = {'temperature': 25.0, 'humidity': 50.0}
    response = client.post('/api/data', json=test_data)
    assert response.status_code == 201
    
    current = client.get('/api/current').json
    assert current['temperature'] == 25.0
