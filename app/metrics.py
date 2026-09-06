"""Sample Metrics API implementation."""
def get_metrics():
    return {
        "status": "healthy",
        "cpu_usage_percent": 12.5,
        "memory_usage_mb": 256
    }

def test_get_metrics():
    m = get_metrics()
    assert m["status"] == "healthy"
    assert "cpu_usage_percent" in m
