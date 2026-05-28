from unittest.mock import patch, Mock
from src.cors_checker import check_cors


def test_check_cors_detects_wildcard_origin():
    mock_response = Mock()
    mock_response.headers = {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Credentials": "true",
    }

    with patch("src.cors_checker.requests.get", return_value=mock_response):
        results = check_cors("http://localhost:3000")

    assert len(results) == 1
    assert results[0]["potential_issue"] is True
    assert results[0]["access_control_allow_origin"] == "*"