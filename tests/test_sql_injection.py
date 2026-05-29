from unittest.mock import patch, Mock
from src.sql_injection import test_sql_injection as run_sql_injection_test


def test_sql_injection_detects_database_error():
    config = {
        "target": {
            "base_url": "http://localhost:3000",
            "test_parameter": "q",
        },
        "endpoints": {
            "sql_injection": "/search"
        },
        "sql_injection": {
            "payloads": ["' OR 1=1 --"]
        },
    }

    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = "SQL syntax error near OR 1=1"

    with patch("src.sql_injection.requests.get", return_value=mock_response):
        results = run_sql_injection_test(config)

    assert len(results) == 1
    assert results[0]["potential_issue"] is True
    assert results[0]["payload"] == "' OR 1=1 --"