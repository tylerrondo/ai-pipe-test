"""Sample Ping API implementation."""
def ping():
    return {"ping": "pong"}

def test_ping():
    assert ping() == {"ping": "pong"}
