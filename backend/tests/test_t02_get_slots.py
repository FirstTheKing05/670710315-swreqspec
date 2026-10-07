from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_T02_get_slots_returns_demo_slots():
    response = client.get('/slots', params={'date_from': '2026-09-23', 'package_code': 'basic'})

    assert response.status_code == 200
    payload = response.json()
    assert isinstance(payload, list)
    assert len(payload) >= 1
    assert payload[0]['package_code'] == 'basic'
    assert 'start_time' in payload[0]
    assert 'remaining' in payload[0]
