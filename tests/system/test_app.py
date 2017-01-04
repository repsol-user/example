import foobar, pytest, requests

host = '127.0.0.1'
port = '8000'

def test_get_foo():
    response = requests.get('http://{}:{}/foo'.format(host, port))
    assert response.status_code == 200
    assert response.text == 'foo'

def test_get_bar():
    response = requests.get('http://{}:{}/bar'.format(host, port))
    assert response.status_code == 200
    assert response.text == 'bar'
