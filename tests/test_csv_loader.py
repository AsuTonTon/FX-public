from __future__ import annotations

from pathlib import Path

import pytest

from src.backtest.csv_loader import CsvOHLCFormatError, load_ohlc_csv


def write_csv(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")


def test_load_ohlc_csv_parses_valid_rows(tmp_path: Path) -> None:
    csv_path = tmp_path / "TEST_4h.csv"
    write_csv(
        csv_path,
        "\n".join(
            [
                "timestamp,open,high,low,close",
                "2026-01-01T00:00:00,100,101,99,100.5",
                "2026-01-01T04:00:00,100.5,102,100,101",
            ]
        ),
    )

    bars = load_ohlc_csv(csv_path)

    assert len(bars) == 2
    assert bars[0].open == 100.0
    assert bars[1].close == 101.0


@pytest.mark.parametrize("time_column", ["time", "datetime", "date"])
def test_load_ohlc_csv_accepts_timestamp_aliases(
    tmp_path: Path, time_column: str
) -> None:
    csv_path = tmp_path / "TEST_4h.csv"
    first_time = "2026-01-01" if time_column == "date" else "2026-01-01T00:00:00"
    second_time = "2026-01-02" if time_column == "date" else "2026-01-01T04:00:00"
    write_csv(
        csv_path,
        "\n".join(
            [
                f"{time_column},open,high,low,close",
                f"{first_time},100,101,99,100.5",
                f"{second_time},100.5,102,100,101",
            ]
        ),
    )

    bars = load_ohlc_csv(csv_path)

    assert len(bars) == 2
    assert bars[0].close == 100.5


def test_load_ohlc_csv_rejects_missing_required_columns(tmp_path: Path) -> None:
    csv_path = tmp_path / "bad.csv"
    write_csv(
        csv_path,
        "\n".join(
            [
                "timestamp,open,high,close",
                "2026-01-01T00:00:00,100,101,100.5",
            ]
        ),
    )

    with pytest.raises(CsvOHLCFormatError, match="missing required"):
        load_ohlc_csv(csv_path)


def test_load_ohlc_csv_rejects_missing_values(tmp_path: Path) -> None:
    csv_path = tmp_path / "bad.csv"
    write_csv(
        csv_path,
        "\n".join(
            [
                "timestamp,open,high,low,close",
                "2026-01-01T00:00:00,100,101,,100.5",
            ]
        ),
    )

    with pytest.raises(CsvOHLCFormatError, match="low is empty"):
        load_ohlc_csv(csv_path)


def test_load_ohlc_csv_rejects_duplicate_timestamps(tmp_path: Path) -> None:
    csv_path = tmp_path / "bad.csv"
    write_csv(
        csv_path,
        "\n".join(
            [
                "timestamp,open,high,low,close",
                "2026-01-01T00:00:00,100,101,99,100.5",
                "2026-01-01T00:00:00,100.5,102,100,101",
            ]
        ),
    )

    with pytest.raises(CsvOHLCFormatError, match="duplicate timestamp"):
        load_ohlc_csv(csv_path)


def test_load_ohlc_csv_rejects_unsorted_timestamps(tmp_path: Path) -> None:
    csv_path = tmp_path / "bad.csv"
    write_csv(
        csv_path,
        "\n".join(
            [
                "timestamp,open,high,low,close",
                "2026-01-01T04:00:00,100,101,99,100.5",
                "2026-01-01T00:00:00,100.5,102,100,101",
            ]
        ),
    )

    with pytest.raises(CsvOHLCFormatError, match="strictly ascending"):
        load_ohlc_csv(csv_path)


def test_load_ohlc_csv_rejects_invalid_ohlc_shape(tmp_path: Path) -> None:
    csv_path = tmp_path / "bad.csv"
    write_csv(
        csv_path,
        "\n".join(
            [
                "timestamp,open,high,low,close",
                "2026-01-01T00:00:00,100,99,98,100.5",
            ]
        ),
    )

    with pytest.raises(CsvOHLCFormatError, match="high is below"):
        load_ohlc_csv(csv_path)


def test_load_ohlc_csv_rejects_low_above_open_or_close(tmp_path: Path) -> None:
    csv_path = tmp_path / "bad.csv"
    write_csv(
        csv_path,
        "\n".join(
            [
                "timestamp,open,high,low,close",
                "2026-01-01T00:00:00,100,102,100.2,100.5",
            ]
        ),
    )

    with pytest.raises(CsvOHLCFormatError, match="low is above"):
        load_ohlc_csv(csv_path)


def test_load_ohlc_csv_rejects_high_below_low(tmp_path: Path) -> None:
    csv_path = tmp_path / "bad.csv"
    write_csv(
        csv_path,
        "\n".join(
            [
                "timestamp,open,high,low,close",
                "2026-01-01T00:00:00,100,101,102,100.5",
            ]
        ),
    )

    with pytest.raises(CsvOHLCFormatError, match="high must be"):
        load_ohlc_csv(csv_path)


def test_load_ohlc_csv_rejects_non_4h_spacing_when_strict(tmp_path: Path) -> None:
    csv_path = tmp_path / "bad.csv"
    write_csv(
        csv_path,
        "\n".join(
            [
                "timestamp,open,high,low,close",
                "2026-01-01T00:00:00,100,101,99,100.5",
                "2026-01-01T01:00:00,100.5,102,100,101",
            ]
        ),
    )

    with pytest.raises(CsvOHLCFormatError, match="gap of at least 8 hours"):
        load_ohlc_csv(csv_path, strict_timeframe_hours=4)


def test_load_ohlc_csv_accepts_4h_spacing_when_strict(tmp_path: Path) -> None:
    csv_path = tmp_path / "TEST_4h.csv"
    write_csv(
        csv_path,
        "\n".join(
            [
                "timestamp,open,high,low,close",
                "2026-01-01T00:00:00,100,101,99,100.5",
                "2026-01-01T04:00:00,100.5,102,100,101",
                "2026-01-01T08:00:00,101,102,100.5,101.5",
            ]
        ),
    )

    bars = load_ohlc_csv(csv_path, strict_timeframe_hours=4)

    assert len(bars) == 3


def test_load_ohlc_csv_accepts_large_gap_when_4h_is_primary(
    tmp_path: Path,
) -> None:
    csv_path = tmp_path / "TEST_4h.csv"
    write_csv(
        csv_path,
        "\n".join(
            [
                "timestamp,open,high,low,close",
                "2026-01-02T00:00:00,100,101,99,100.5",
                "2026-01-02T04:00:00,100.5,102,100,101",
                "2026-01-02T08:00:00,101,102,100.5,101.5",
                "2026-01-05T00:00:00,101.5,103,101,102",
                "2026-01-05T04:00:00,102,103,101.5,102.5",
            ]
        ),
    )

    bars = load_ohlc_csv(csv_path, strict_timeframe_hours=4)

    assert len(bars) == 5


def test_load_ohlc_csv_rejects_daily_csv_when_strict_4h(tmp_path: Path) -> None:
    csv_path = tmp_path / "daily.csv"
    write_csv(
        csv_path,
        "\n".join(
            [
                "timestamp,open,high,low,close",
                "2026-01-01T00:00:00,100,101,99,100.5",
                "2026-01-02T00:00:00,100.5,102,100,101",
                "2026-01-03T00:00:00,101,102,100.5,101.5",
            ]
        ),
    )

    with pytest.raises(CsvOHLCFormatError, match="at least one 4-hour interval"):
        load_ohlc_csv(csv_path, strict_timeframe_hours=4)


def test_load_ohlc_csv_rejects_mixed_timezone_awareness(tmp_path: Path) -> None:
    csv_path = tmp_path / "bad.csv"
    write_csv(
        csv_path,
        "\n".join(
            [
                "timestamp,open,high,low,close",
                "2026-01-01T00:00:00+00:00,100,101,99,100.5",
                "2026-01-01T04:00:00,100.5,102,100,101",
            ]
        ),
    )

    with pytest.raises(CsvOHLCFormatError, match="timezone awareness"):
        load_ohlc_csv(csv_path)
