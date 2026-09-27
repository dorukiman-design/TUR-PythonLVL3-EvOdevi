def pytest_report_teststatus(report):
    if report.when == 'call' and report.passed:
        return f"custom_message", "C", "Görev tamamlandı"
