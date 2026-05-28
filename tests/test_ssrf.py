from unittest.mock import patch, Mock
from src.ssrf import test_ssrf as run_ssrf_test


def test_ssrf_flags_possible_internal_url_processing():
    config = {
        "target": {
            "base_url": "http://localhost:3000/fetch",
            "test_parameter": "url",
        },
        "ssrf": {
            "test_urls": ["http://169.254.169.254/latest/meta-data/"]
        },
    }

    mock_response = Mock()
    mock_response.status_code = 200

    with patch("src.ssrf.requests.get", return_value=mock_response):
        results = run_ssrf_test(config)

    assert len(results) == 1
    assert results[0]["potential_issue"] is True
    assert results[0]["test_url"] == "http://169.254.169.254/latest/meta-data/"