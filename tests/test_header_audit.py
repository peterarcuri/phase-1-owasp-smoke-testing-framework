from unittest.mock import patch, Mock
from src.header_audit import audit_headers


def test_audit_headers_detects_missing_headers():
    config = {
        "target": {"base_url": "http://localhost:3000"},
        "headers": {
            "required": [
                "Content-Security-Policy",
                "X-Frame-Options",
            ]
        },
    }

    mock_response = Mock()
    mock_response.headers = {
        "X-Frame-Options": "DENY"
    }

    with patch("src.header_audit.requests.get", return_value=mock_response):
        results = audit_headers(config)

    assert len(results) == 2

    csp_result = next(
        item for item in results if item["header"] == "Content-Security-Policy"
    )

    frame_result = next(
        item for item in results if item["header"] == "X-Frame-Options"
    )

    assert csp_result["present"] is False
    assert frame_result["present"] is True