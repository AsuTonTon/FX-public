from __future__ import annotations

import json
from dataclasses import dataclass
from os import PathLike
from pathlib import Path
from typing import Any


class PairConfigError(ValueError):
    """Raised when pair settings are incomplete or invalid."""


@dataclass(frozen=True)
class PairSettings:
    pair: str
    tick_size: float
    assumed_spread: float
    buffer: float


def load_pair_settings(path: str | PathLike[str]) -> dict[str, PairSettings]:
    config_path = Path(path)
    with config_path.open("r", encoding="utf-8") as handle:
        raw_config = json.load(handle)

    raw_pairs = raw_config.get("pairs")
    if not isinstance(raw_pairs, dict) or not raw_pairs:
        raise PairConfigError(f"{config_path} must contain a non-empty 'pairs' object")

    settings: dict[str, PairSettings] = {}
    for pair, raw_settings in raw_pairs.items():
        if not isinstance(raw_settings, dict):
            raise PairConfigError(f"{pair}: settings must be an object")
        normalized_pair = str(pair).upper()
        settings[normalized_pair] = _parse_pair_settings(normalized_pair, raw_settings)
    return settings


def _parse_pair_settings(pair: str, raw_settings: dict[str, Any]) -> PairSettings:
    tick_size = _required_float(pair, raw_settings, "tick_size")
    assumed_spread = _required_float(pair, raw_settings, "assumed_spread")
    buffer = _optional_float(
        pair,
        raw_settings,
        "buffer",
        default=assumed_spread + tick_size,
    )

    if tick_size <= 0:
        raise PairConfigError(f"{pair}: tick_size must be positive")
    if assumed_spread < 0:
        raise PairConfigError(f"{pair}: assumed_spread must be zero or positive")
    if buffer < 0:
        raise PairConfigError(f"{pair}: buffer must be zero or positive")

    return PairSettings(
        pair=pair,
        tick_size=tick_size,
        assumed_spread=assumed_spread,
        buffer=buffer,
    )


def _required_float(
    pair: str,
    raw_settings: dict[str, Any],
    key: str,
) -> float:
    if key not in raw_settings:
        raise PairConfigError(f"{pair}: missing required setting {key}")
    return _to_float(pair, key, raw_settings[key])


def _optional_float(
    pair: str,
    raw_settings: dict[str, Any],
    key: str,
    *,
    default: float,
) -> float:
    if key not in raw_settings:
        return default
    return _to_float(pair, key, raw_settings[key])


def _to_float(pair: str, key: str, value: Any) -> float:
    try:
        return float(value)
    except (TypeError, ValueError) as exc:
        raise PairConfigError(f"{pair}: {key} must be numeric") from exc
