"""Sample Hello World API implementation."""
def get_hello():
    return {"message": "hello world"}

def test_get_hello():
    assert get_hello() == {"message": "hello world"}
