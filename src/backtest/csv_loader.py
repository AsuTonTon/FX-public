from __future__ import annotations

from collections import Counter
import csv
from datetime import datetime
from os import PathLike
from pathlib import Path
from typing import Any, Sequence

from src.backtest.trade import OHLCBar


class CsvOHLCFormatError(ValueError):
    """Raised when an OHLC CSV cannot be used for read-only validation."""


TIMESTAMP_ALIASES = ("timestamp", "time", "datetime", "date")
REQUIRED_PRICE_COLUMNS = ("open", "high", "low", "close")


def load_ohlc_csv(
    path: str | PathLike[str],
    *,
    encoding: str = "utf-8-sig",
    strict_timeframe_hours: int | None = None,
) -> list[OHLCBar]:
    csv_path = Path(path)
    with csv_path.open("r", encoding=encoding, newline="") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames:
            raise CsvOHLCFormatError(f"{csv_path} has no header row")

        columns = _normalized_columns(reader.fieldnames)
        timestamp_column = _find_timestamp_column(columns)
        missing = [column for column in REQUIRED_PRICE_COLUMNS if column not in columns]
        if timestamp_column is None or missing:
            missing_columns = list(missing)
            if timestamp_column is None:
                missing_columns.insert(0, "timestamp")
            raise CsvOHLCFormatError(
                f"{csv_path} is missing required column(s): "
                f"{', '.join(missing_columns)}"
            )

        bars: list[OHLCBar] = []
        seen_times: set[datetime] = set()
        previous_time: datetime | None = None

        for row_number, row in enumerate(reader, start=2):
            if not _has_data(row):
                continue

            bar = _parse_row(
                row,
                row_number,
                columns,
                timestamp_column,
                csv_path,
            )
            if bar.time in seen_times:
                raise CsvOHLCFormatError(
                    f"{csv_path} row {row_number}: duplicate timestamp {bar.time}"
                )
            _validate_order(
                csv_path,
                row_number,
                previous_time,
                bar.time,
            )

            bars.append(bar)
            seen_times.add(bar.time)
            previous_time = bar.time

    if not bars:
        raise CsvOHLCFormatError(f"{csv_path} contains no OHLC rows")
    if strict_timeframe_hours is not None:
        _validate_timeframe_distribution(csv_path, bars, strict_timeframe_hours)
    return bars


def _normalized_columns(fieldnames: Sequence[str]) -> dict[str, str]:
    columns: dict[str, str] = {}
    for fieldname in fieldnames:
        normalized = fieldname.strip().lstrip("\ufeff").lower()
        if normalized:
            columns[normalized] = fieldname
    return columns


def _find_timestamp_column(columns: dict[str, str]) -> str | None:
    for alias in TIMESTAMP_ALIASES:
        if alias in columns:
            return columns[alias]
    return None


def _has_data(row: dict[str, Any]) -> bool:
    return any(value not in (None, "") for value in row.values())


def _parse_row(
    row: dict[str, Any],
    row_number: int,
    columns: dict[str, str],
    timestamp_column: str,
    csv_path: Path,
) -> OHLCBar:
    timestamp = _parse_timestamp(row.get(timestamp_column), row_number, csv_path)
    open_price = _parse_float(row.get(columns["open"]), "open", row_number, csv_path)
    high = _parse_float(row.get(columns["high"]), "high", row_number, csv_path)
    low = _parse_float(row.get(columns["low"]), "low", row_number, csv_path)
    close = _parse_float(row.get(columns["close"]), "close", row_number, csv_path)

    if high < low:
        raise CsvOHLCFormatError(
            f"{csv_path} row {row_number}: high must be greater than or equal to low"
        )
    if high < max(open_price, close):
        raise CsvOHLCFormatError(
            f"{csv_path} row {row_number}: high is below open or close"
        )
    if low > min(open_price, close):
        raise CsvOHLCFormatError(
            f"{csv_path} row {row_number}: low is above open or close"
        )

    return OHLCBar(
        time=timestamp,
        open=open_price,
        high=high,
        low=low,
        close=close,
    )


def _parse_timestamp(value: Any, row_number: int, csv_path: Path) -> datetime:
    if value in (None, ""):
        raise CsvOHLCFormatError(f"{csv_path} row {row_number}: timestamp is empty")
    raw_value = str(value).strip()
    normalized = raw_value[:-1] + "+00:00" if raw_value.endswith("Z") else raw_value

    try:
        return datetime.fromisoformat(normalized)
    except ValueError:
        pass

    for date_format in ("%Y-%m-%d %H:%M:%S", "%Y/%m/%d %H:%M:%S", "%Y-%m-%d"):
        try:
            return datetime.strptime(raw_value, date_format)
        except ValueError:
            continue

    raise CsvOHLCFormatError(
        f"{csv_path} row {row_number}: unsupported timestamp format {raw_value!r}"
    )


def _parse_float(value: Any, column: str, row_number: int, csv_path: Path) -> float:
    if value in (None, ""):
        raise CsvOHLCFormatError(f"{csv_path} row {row_number}: {column} is empty")
    try:
        return float(str(value).strip())
    except ValueError as exc:
        raise CsvOHLCFormatError(
            f"{csv_path} row {row_number}: {column} is not numeric"
        ) from exc


def _validate_order(
    csv_path: Path,
    row_number: int,
    previous_time: datetime | None,
    current_time: datetime,
) -> None:
    if previous_time is None:
        return

    try:
        delta = current_time - previous_time
    except TypeError as exc:
        raise CsvOHLCFormatError(
            f"{csv_path} row {row_number}: timezone awareness is inconsistent"
        ) from exc

    if delta.total_seconds() <= 0:
        raise CsvOHLCFormatError(
            f"{csv_path} row {row_number}: timestamps must be strictly ascending"
        )


def _validate_timeframe_distribution(
    csv_path: Path,
    bars: list[OHLCBar],
    strict_timeframe_hours: int,
) -> None:
    if strict_timeframe_hours <= 0:
        raise CsvOHLCFormatError("strict_timeframe_hours must be positive")
    if len(bars) < 2:
        raise CsvOHLCFormatError(
            f"{csv_path}: strict timeframe validation requires at least two rows"
        )

    timeframe_seconds = strict_timeframe_hours * 60 * 60
    minimum_gap_seconds = timeframe_seconds * 2
    deltas = [
        int((current.time - previous.time).total_seconds())
        for previous, current in zip(bars, bars[1:])
    ]
    invalid_deltas = [
        delta
        for delta in deltas
        if delta != timeframe_seconds and delta < minimum_gap_seconds
    ]
    if invalid_deltas:
        invalid_hours = sorted({delta / 3600 for delta in invalid_deltas})
        raise CsvOHLCFormatError(
            f"{csv_path}: timestamp spacing must be {strict_timeframe_hours} hours "
            f"or a gap of at least {strict_timeframe_hours * 2} hours; "
            f"found {invalid_hours} hour interval(s)"
        )

    counts = Counter(deltas)
    regular_count = counts.get(timeframe_seconds, 0)
    if regular_count == 0:
        raise CsvOHLCFormatError(
            f"{csv_path}: strict {strict_timeframe_hours}h validation requires "
            f"at least one {strict_timeframe_hours}-hour interval"
        )

    max_count = max(counts.values())
    if regular_count < max_count:
        most_common_hours = sorted(
            delta / 3600 for delta, count in counts.items() if count == max_count
        )
        raise CsvOHLCFormatError(
            f"{csv_path}: most frequent timestamp spacing must be "
            f"{strict_timeframe_hours} hours; found {most_common_hours} hour mode(s)"
        )
