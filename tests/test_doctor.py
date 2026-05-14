from datatrack.doctor import collect_rows, format_report


def test_collect_rows_has_four_checks():
    rows = collect_rows()
    assert len(rows) == 4
    labels = {r[0] for r in rows}
    assert ".datatrack directory" in labels
    assert "schema_rules.yaml" in labels


def test_format_report_is_multiline():
    text = format_report()
    assert "Datatrack doctor" in text
    assert "test-connection" in text
