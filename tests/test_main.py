"""Tests for the CSV summary command line tool in src/main.py."""

from pathlib import Path

import pytest
from typer.testing import CliRunner

from main import app

runner = CliRunner()


@pytest.fixture
def users_csv(tmp_path: Path) -> Path:
    path = tmp_path / "users.csv"
    path.write_text(
        "name,age,status\n"
        "Rehab,25,active\n"
        "Sara,30,inactive\n"
        "Ahmed,28,active\n"
        "Mona,,active\n",
        encoding="utf-8",
    )
    return path


def test_filters_rows_by_status(users_csv: Path) -> None:
    result = runner.invoke(app, [str(users_csv), "active"])

    assert result.exit_code == 0
    assert "Rehab" in result.output
    assert "Ahmed" in result.output
    assert "Sara" not in result.output


def test_drops_rows_with_missing_values(users_csv: Path) -> None:
    result = runner.invoke(app, [str(users_csv), "active"])

    assert "Mona" not in result.output


def test_prints_summary(users_csv: Path) -> None:
    result = runner.invoke(app, [str(users_csv), "active"])

    assert "Total Rows" in result.output
    assert "Average Age" in result.output
    assert "26.5" in result.output


def test_rejects_csv_without_required_columns(tmp_path: Path) -> None:
    path = tmp_path / "bad.csv"
    path.write_text("name,city\nRehab,Riyadh\n", encoding="utf-8")

    result = runner.invoke(app, [str(path), "active"])

    assert isinstance(result.exception, ValueError)


def test_sample_data_file_runs() -> None:
    sample = Path(__file__).resolve().parents[1] / "data" / "user.csv"

    result = runner.invoke(app, [str(sample), "inactive"])

    assert result.exit_code == 0
    assert "Khalid" in result.output
