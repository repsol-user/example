import foobar, pytest

@pytest.fixture
def client():
    return foobar.app.test_client()

def test_get_foo(client):
    response = client.get('/foo')
    assert response.status_code == 200
    assert response.data == b'foo'

def test_get_bar(client):
    response = client.get('/bar')
    assert response.status_code == 200
    assert response.data == b'bar'
