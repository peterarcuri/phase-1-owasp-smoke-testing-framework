import json
from src.report_generator import save_report


def test_save_report_creates_json_file(tmp_path):
    results = {
        "target": "http://localhost:3000",
        "sql_injection": [],
        "ssrf": [],
        "headers": [],
        "cors": [],
    }

    output_file = tmp_path / "security-report.json"

    report = save_report(results, output_file)

    assert output_file.exists()
    assert report["scan_type"] == "OWASP Smoke Test"
    assert "generated_at" in report
    assert report["results"]["target"] == "http://localhost:3000"

    with open(output_file, "r") as file:
        data = json.load(file)

    assert data["scan_type"] == "OWASP Smoke Test"