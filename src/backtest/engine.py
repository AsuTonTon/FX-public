from __future__ import annotations

from typing import Iterable

from src.backtest.trade import BacktestEvent, BacktestResult, EntryOrder, OHLCBar, Trade
from src.strategies.ema_wave3_strategy_a import EmaWave3StrategyA, normalize_bars


class BacktestEngine:
    def __init__(self, conservative_same_bar: bool = True) -> None:
        self.conservative_same_bar = conservative_same_bar

    def run(
        self,
        pair: str,
        bars: Iterable[OHLCBar | dict],
        strategy: EmaWave3StrategyA,
    ) -> BacktestResult:
        normalized_bars = normalize_bars(bars)
        signal_result = strategy.generate_entries(pair, normalized_bars)
        events = list(signal_result.events)
        trades: list[Trade] = []
        active_until_index = -1

        for order in signal_result.entries:
            if order.entry_index <= active_until_index:
                events.append(
                    BacktestEvent(
                        event_type="no_trade",
                        pair=pair,
                        time=order.trade.entry_time,
                        direction=order.trade.direction,
                        reason="overlap_open_position",
                    )
                )
                continue

            events.append(
                BacktestEvent(
                    event_type="entry",
                    pair=pair,
                    time=order.trade.entry_time,
                    direction=order.trade.direction,
                    details={
                        "entry_price": order.trade.entry_price,
                        "stop_price": order.trade.stop_price,
                        "take_profit_price": order.trade.take_profit_price,
                    },
                )
            )
            trade, exit_index, exit_event = self._simulate_order(normalized_bars, order)
            active_until_index = exit_index
            trades.append(trade)
            events.append(exit_event)

        return BacktestResult(trades=trades, events=events)

    def _simulate_order(
        self,
        bars: list[OHLCBar],
        order: EntryOrder,
    ) -> tuple[Trade, int, BacktestEvent]:
        trade = order.trade
        entry_index = order.entry_index
        risk = self._risk_per_unit(trade)

        for index in range(entry_index, len(bars)):
            bar = bars[index]
            stop_hit, target_hit = self._hit_status(trade, bar)

            if stop_hit and target_hit:
                if self.conservative_same_bar:
                    return self._close_trade(
                        trade,
                        bar,
                        index,
                        entry_index,
                        trade.stop_price,
                        "stop_loss",
                        -1.0,
                    )
                return self._close_trade(
                    trade,
                    bar,
                    index,
                    entry_index,
                    trade.take_profit_price,
                    "take_profit",
                    self._target_r(trade, risk),
                )

            if stop_hit:
                return self._close_trade(
                    trade, bar, index, entry_index, trade.stop_price, "stop_loss", -1.0
                )

            if target_hit:
                return self._close_trade(
                    trade,
                    bar,
                    index,
                    entry_index,
                    trade.take_profit_price,
                    "take_profit",
                    self._target_r(trade, risk),
                )

        last_index = len(bars) - 1
        last_bar = bars[last_index]
        r_multiple = self._mark_to_market_r(trade, last_bar.close, risk)
        return self._close_trade(
            trade,
            last_bar,
            last_index,
            entry_index,
            last_bar.close,
            "end_of_data",
            r_multiple,
        )

    @staticmethod
    def _risk_per_unit(trade: Trade) -> float:
        if trade.direction == "long":
            return trade.entry_price - trade.stop_price
        return trade.stop_price - trade.entry_price

    @staticmethod
    def _target_r(trade: Trade, risk: float) -> float:
        if trade.direction == "long":
            return (trade.take_profit_price - trade.entry_price) / risk
        return (trade.entry_price - trade.take_profit_price) / risk

    @staticmethod
    def _mark_to_market_r(trade: Trade, exit_price: float, risk: float) -> float:
        if trade.direction == "long":
            return (exit_price - trade.entry_price) / risk
        return (trade.entry_price - exit_price) / risk

    @staticmethod
    def _hit_status(trade: Trade, bar: OHLCBar) -> tuple[bool, bool]:
        if trade.direction == "long":
            return bar.low <= trade.stop_price, bar.high >= trade.take_profit_price
        return bar.high >= trade.stop_price, bar.low <= trade.take_profit_price

    @staticmethod
    def _close_trade(
        trade: Trade,
        bar: OHLCBar,
        exit_index: int,
        entry_index: int,
        exit_price: float,
        exit_reason: str,
        r_multiple: float,
    ) -> tuple[Trade, int, BacktestEvent]:
        trade.exit_time = bar.time
        trade.exit_price = exit_price
        trade.exit_reason = exit_reason
        trade.r_multiple = r_multiple
        trade.bars_held = exit_index - entry_index + 1
        event = BacktestEvent(
            event_type=exit_reason,
            pair=trade.pair,
            time=bar.time,
            direction=trade.direction,
            details={
                "exit_price": exit_price,
                "r_multiple": r_multiple,
                "bars_held": trade.bars_held,
            },
        )
        return trade, exit_index, event
