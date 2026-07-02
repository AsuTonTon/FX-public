# Strategy B TP1 Decision Closure Note

## 1. Objective and scope

This is a docs-only closure note for the current Strategy B TP1 decision cycle.

Scope:

- close the current Strategy B TP1 / stop-anchor decision cycle
- freeze TP1 and stop-anchor changes pending broader evidence
- preserve the current Strategy B behavior
- define reopen conditions for any future Strategy B TP1 or stop-anchor design work

Out of scope:

- no implementation approval
- no Strategy B rule change
- no parameter change
- no config or test change
- no Strategy B2
- no Strategy C
- no backtest
- no optimization
- no profitability claim
- no broker/API/live-trading/execution implication

## 2. Decision cycle summarized

This closure follows the completed TP1 review sequence:

| Step | Summary |
|---|---|
| TP1 selection review | Documented current Strategy B TP1 behavior, rejection counts, TP1/stop/RR interaction, and mismatch hypotheses. |
| Diagnostic design | Defined outcome-blinded label families and future diagnostic structure for TP1, farther targets, stop anchors, RR, corpus alignment, and management distinction. |
| Local manual review aggregate | Reviewed 30 base candidates plus 3 repeats, with 7 second-review flags and no correction requests. |
| Second-review/adjudication | Adjudicated the 7 flagged cases and found no support for a broad later-rank exception. |
| Decision memo | Decided to keep Strategy B TP1, stop logic, RR gates, and Strategy B variant status unchanged. |
| Follow-up diagnostic backlog | Defined future diagnostic topics only, with no implementation approval. |

Aggregate facts carried forward:

- confirmation candidates: 373
- accepted candidates: 2
- rejected candidates: 371
- `tp1_below_min_rr` appears in 335 of 371 rejected candidates
- every `stop_too_wide` candidate also fails `tp1_below_min_rr`
- rank-1 TP1 median is about `0.1714R`
- only 5 of 340 evaluable rank-1 TP1 candidates reach at least `1.0R`
- manual review selected `current_rank1` for 22 of 30 base candidates
- manual review selected `later_rank` for 2 of 30 base candidates
- second review produced `revise_to_later_rank_candidate: 0`
- second review preserved `no_valid_target` and `no_trade_structure` as separate classes

These facts are diagnostic only. They are not profitability evidence.

## 3. Final current decision

Final current decision:

- keep current rank-1 TP1 selection
- keep current TP1 min RR
- keep current TP2 min RR
- keep current TP1-only min RR
- keep current stop-anchor logic
- keep current stop-buffer logic
- keep current stop sanity logic
- keep no-left-side/no-valid-target rejection behavior
- do not implement a later-rank exception
- do not implement contextual RR
- do not create Strategy B2
- do not approve implementation

Current Strategy B TP1 and stop-anchor behavior remains frozen until the reopen conditions in this note are met.

## 4. Why no implementation follows

No implementation follows for these reasons:

- Rank-1 TP1 was often visually defensible in the manual review.
- Later-rank evidence was limited and weakened after adjudication.
- `low_rr_but_structural_tp` is a diagnostic category, not a rule change.
- Stop-anchor issues require separate diagnostics before stop logic can be discussed.
- Lowering TP1 RR would be parameter tuning without a documented replacement rule.
- A 30-case manual review is not enough to alter Strategy B behavior.
- The 32-summary synthesis is interim, and the full-corpus doctrine analysis is not complete.
- The existing corpus evidence supports asking TP/stop/RR questions, but it does not provide a complete implementation specification.

## 5. Frozen items

The following items are frozen:

- TP1 target ranking
- TP1 min RR
- TP2 min RR
- TP1-only min RR
- stop anchor
- stop buffer
- stop sanity limits
- ADX filter
- Strategy B management structure
- Strategy B2 creation

Frozen means no code, parameter, config, or test change is approved for these items from the current TP1 review cycle.

## 6. Future reopen conditions

Reopening Strategy B TP1 or stop-anchor design would require stronger evidence, such as:

- full-corpus doctrine analysis completes and materially changes the doctrine map
- independent fixed-sample diagnostics repeat a finding
- second-review ambiguity is low
- the proposed mechanical rule can be stated without outcome data
- the rule uses only information available at confirmation time
- no parameter sweep or performance-tuned threshold is required
- stop/invalidation doctrine is preserved
- no future bars or post-confirmation outcome candles are needed
- no pair-specific tuning is needed
- no raw outcome/profitability selection is used
- no-valid-target and no-trade-structure cases remain separate from low-RR cases

If these conditions are not met, Strategy B TP1 and stop-anchor behavior should remain unchanged.

## 7. Relationship to full-corpus doctrine line

The full-corpus doctrine analysis is a separate line of work.

Its results should not be mixed into Strategy B automatically. After completion, it may trigger a docs-only Strategy A/B versus channel doctrine mismatch analysis. Only after that mismatch analysis should a future design memo be considered.

The order should be:

1. Complete or materially advance the full-corpus doctrine line.
2. Compare Strategy A/B mechanics against the updated doctrine map.
3. Identify mismatch categories without code changes.
4. Decide whether a docs-only future design memo is justified.
5. Consider implementation only after a separate design memo approves a specific change.

## 8. Recommended next step

Recommended next step:

- pause Strategy B TP1 changes
- continue or wait for YouTube full-corpus doctrine analysis
- once full-corpus analysis is complete, create a Strategy A/B vs channel doctrine mismatch analysis
- do not implement changes before that

No Strategy B TP1, stop-anchor, contextual RR, or Strategy B2 implementation should proceed from the current review cycle.

## 9. Guardrails

Confirmed:

- docs-only
- exactly one Markdown file
- no code changes
- no rule changes
- no parameter/config/test changes
- no backtests
- no optimization
- no market data fetch
- no API call
- no broker/API/live trading
- no raw CSV
- no data/results/CSV/JSON
- no chart images
- no hidden mappings
- no worksheets
- no Strategy B2/C
- no profitability claims
