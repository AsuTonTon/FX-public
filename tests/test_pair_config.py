from __future__ import annotations

from pathlib import Path

import pytest

from src.backtest.pair_config import PairConfigError, load_pair_settings


def write_pair_config(path: Path, body: str) -> None:
    path.write_text(body, encoding="utf-8")


def test_pair_settings_default_buffer_is_spread_plus_tick(tmp_path: Path) -> None:
    config_path = tmp_path / "pairs.json"
    write_pair_config(
        config_path,
        """
        {
          "pairs": {
            "eurusd": {
              "tick_size": 0.00001,
              "assumed_spread": 0.00010
            }
          }
        }
        """,
    )

    settings = load_pair_settings(config_path)

    assert settings["EURUSD"].tick_size == pytest.approx(0.00001)
    assert settings["EURUSD"].assumed_spread == pytest.approx(0.00010)
    assert settings["EURUSD"].buffer == pytest.approx(0.00011)


def test_pair_settings_accepts_explicit_buffer(tmp_path: Path) -> None:
    config_path = tmp_path / "pairs.json"
    write_pair_config(
        config_path,
        """
        {
          "pairs": {
            "USDJPY": {
              "tick_size": 0.001,
              "assumed_spread": 0.015,
              "buffer": 0.02
            }
          }
        }
        """,
    )

    settings = load_pair_settings(config_path)

    assert settings["USDJPY"].buffer == pytest.approx(0.02)


def test_pair_settings_rejects_missing_pairs_object(tmp_path: Path) -> None:
    config_path = tmp_path / "pairs.json"
    write_pair_config(config_path, "{}")

    with pytest.raises(PairConfigError, match="pairs"):
        load_pair_settings(config_path)


def test_pair_settings_normalizes_pair_name_to_uppercase(tmp_path: Path) -> None:
    config_path = tmp_path / "pairs.json"
    write_pair_config(
        config_path,
        """
        {
          "pairs": {
            "gbpusd": {
              "tick_size": 0.00001,
              "assumed_spread": 0.00015
            }
          }
        }
        """,
    )

    settings = load_pair_settings(config_path)

    assert "GBPUSD" in settings
    assert settings["GBPUSD"].pair == "GBPUSD"


@pytest.mark.parametrize(
    ("body", "message"),
    [
        (
            """
            {
              "pairs": {
                "TEST": {
                  "tick_size": 0,
                  "assumed_spread": 0.1
                }
              }
            }
            """,
            "tick_size must be positive",
        ),
        (
            """
            {
              "pairs": {
                "TEST": {
                  "tick_size": 0.01,
                  "assumed_spread": -0.1
                }
              }
            }
            """,
            "assumed_spread must be zero or positive",
        ),
        (
            """
            {
              "pairs": {
                "TEST": {
                  "tick_size": 0.01,
                  "assumed_spread": 0.1,
                  "buffer": -0.01
                }
              }
            }
            """,
            "buffer must be zero or positive",
        ),
        (
            """
            {
              "pairs": {
                "TEST": {
                  "tick_size": "not-number",
                  "assumed_spread": 0.1
                }
              }
            }
            """,
            "tick_size must be numeric",
        ),
    ],
)
def test_pair_settings_rejects_invalid_numeric_settings(
    tmp_path: Path, body: str, message: str
) -> None:
    config_path = tmp_path / "pairs.json"
    write_pair_config(config_path, body)

    with pytest.raises(PairConfigError, match=message):
        load_pair_settings(config_path)
