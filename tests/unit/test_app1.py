import foobar, multiprocessing, pytest, requests, socket

host = '127.0.0.1'
port = 8000

def run_server():
    foobar.app.run(host=host, port=port)

def wait_for_server():
    while True:
        s = socket.socket()
        try:
            s.connect((host, port))
            break
        except socket.error:
            pass
        s.close()

@pytest.fixture
def server(request):
    server  = multiprocessing.Process(target=run_server)
    server.start()
    wait_for_server()
    def finalizer():
        server.terminate()
        server.join()
    request.addfinalizer(finalizer)

def test_get_foo(server):
    response = requests.get('http://{}:{}/foo'.format(host, port))
    assert response.status_code == 200
    assert response.text == 'foo'

def test_get_bar(server):
    response = requests.get('http://{}:{}/bar'.format(host, port))
    assert response.status_code == 200
    assert response.text == 'bar'
