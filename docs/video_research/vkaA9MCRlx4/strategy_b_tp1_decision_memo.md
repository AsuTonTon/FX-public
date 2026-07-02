# Strategy B TP1 Decision Memo

## 1. Objective and scope

This is a docs-only decision memo for Strategy B TP1 selection.

Scope:

- synthesize the TP1 selection review, diagnostic design, local artifact checklist, manual review aggregate report, second-review/adjudication report, 32-summary channel synthesis, Strategy B spec, and Strategy B implementation notes
- decide what the current evidence supports before any Strategy B TP1 rule-change proposal
- keep the memo Git-safe and aggregate-only

Out of scope:

- no implementation
- no Strategy B behavior change
- no parameter change
- no config or test change
- no backtest
- no optimization
- no profitability claim
- no Strategy B2
- no Strategy C
- no broker/API/live-trading/execution implication

## 2. Evidence base

The memo uses only already documented evidence.

| Source | Role in this memo |
|---|---|
| `strategy_b_tp1_selection_review.md` | Defines the current TP1 behavior, rejection facts, TP1/stop/RR interaction, and mismatch hypotheses. |
| `strategy_b_tp1_diagnostic_design.md` | Defines diagnostic label families and interpretation rules for TP1, farther targets, stops, RR, corpus alignment, and management distinction. |
| `strategy_b_tp1_local_manual_review_execution_plan.md` | Defines the local-only, outcome-blinded execution model and artifact boundaries for manual review. |
| `strategy_b_tp1_local_artifact_preparation_checklist.md` | Defines required local artifacts and hard stops for review execution without committing raw data or generated outputs. |
| `strategy_b_tp1_manual_review_aggregate_report.md` | Provides the 30-base-candidate manual review aggregate and repeat-check results. |
| `strategy_b_tp1_second_review_adjudication_report.md` | Provides the seven-case adjudication result after PR #40. |
| `channel_32_summary_interim_synthesis.md` | Provides corpus context for structural TP, contextual RR, stop/invalidation anchoring, and unresolved discretionary chart terms. |
| `strategy_b_spec_design.md` | Defines the original fixed Strategy B design choices and overfitting guardrails. |
| `strategy_b_implementation_notes.md` | Documents the implemented Strategy B rules and implementation choices. |

No raw candidate rows, TP candidate rows, chart images, hidden mappings, filled worksheets, data files, result files, CSV, or JSON were used in this memo.

## 3. Current Strategy B TP1 behavior

Current Strategy B keeps the Strategy A setup sequence:

1. EMA20 / EMA200 trend-cross context.
2. First 20EMA touch after the setup.
3. Body-close confirmation break.
4. Entry at the next bar open after confirmation.

After confirmation, Strategy B currently uses:

- left-side fractal swing candidates using a fixed fractal width and lookback
- no future bars for swing validation; a swing is valid only if its right-side confirmation candles are already closed before the Strategy B confirmation candle
- long targets from valid left-side swing highs above entry
- short targets from valid left-side swing lows below entry
- targets sorted by nearest price first
- TP1 = first sorted target
- TP2 = second sorted target, if available
- RR gates:
  - TP1 must be at least `1.0R`
  - TP2 must be at least `1.5R` when TP2 exists
  - TP1-only exits require TP1 at least `1.5R`
- stop anchor from the nearest valid stop-side left swing beyond the reference candle, or the reference candle if no eligible swing exists
- stop buffer = `max(pair_buffer, 0.10 * ATR(14), tick_size)`
- stop sanity check:
  - reject if stop distance is below `0.25 * ATR(14)`
  - reject if stop distance is above `3.0 * ATR(14)`
- ADX(14) range filter with no-trade when ADX is below `18`
- 50% TP1 / 50% final management
- break-even stop on the remaining 50% after TP1

This memo does not change any of those rules.

## 4. Key quantitative facts from prior diagnostics

Already documented aggregate facts:

- confirmation candidates: 373
- accepted candidates: 2
- rejected candidates: 371
- `tp1_below_min_rr` appears in 335 of 371 rejected candidates
- every `stop_too_wide` candidate also fails `tp1_below_min_rr`
- ADX first-fail count is 25, and 20 of those also fail TP1 minimum RR
- rank-1 TP1 median is about `0.1714R`
- only 5 of 340 evaluable rank-1 TP1 candidates reach at least `1.0R`
- among 335 rank-1-below-1.0R cases, any rank 2-5 target reaches at least `1.0R` in 76 cases
- 259 of those cases remain below `1.0R` across available rank 2-5 targets
- for the `stop_too_wide` subset, only 8 of 101 candidates have any rank 1-5 target at or above `1.0R`
- ADX is not the primary rejection driver in the documented diagnostics

These are diagnostic facts, not profitability evidence.

## 5. Manual review findings

PR #40 reviewed:

- 30 base candidates
- 3 repeat checks
- 33 total presentation items
- 7 second-review flags
- 0 correction requests

Aggregate chosen classification:

| Classification | Count |
|---|---:|
| `current_rank1` | 22 |
| `later_rank` | 2 |
| `no_trade_structure` | 3 |
| `no_valid_target` | 3 |

Important findings:

- Rank-1 TP1 was often visually defensible in the small diagnostic sample.
- `later_rank` had limited but real support, with 2 of 30 base candidates.
- `no_trade_structure` and `no_valid_target` each appeared in 3 of 30 base candidates.
- `low_rr_but_structural_tp` was common, appearing in 22 base candidates.
- Stop-anchor interpretation was mixed: many stops were structurally valid, some were wide but structural, and some were questionable or not interpretable.
- Broad rank replacement was not supported by PR #40 alone.

## 6. Second-review findings

PR #41 adjudicated the 7 second-review cases.

| Final adjudication outcome | Count |
|---|---:|
| `uphold_current_rank1` | 1 |
| `revise_to_later_rank_candidate` | 0 |
| `uphold_no_valid_target` | 3 |
| `uphold_no_trade_structure` | 2 |
| `unresolved_needs_third_review` | 1 |

Second-review implications:

- No broad later-rank exception was supported.
- No-valid-target cases should remain separate from low-RR cases.
- No-trade-structure cases should remain separate from low-RR cases.
- Micro-structure TP1 cases should be separated from structurally meaningful low-R TP cases.
- Stop-anchor quality needs its own decision path and should not be hidden inside TP1 RR analysis.

## 7. Decision options considered

### Option A: Keep Strategy B TP1 selection unchanged for now

Supporting evidence:

- Rank-1 TP1 was selected as `current_rank1` in 22 of 30 manual-review base candidates.
- The second review upheld the only flagged `current_rank1` case.
- The current behavior is deterministic and already implemented with no future-bar target leakage.
- The corpus supports structural targets but does not specify a replacement ranking rule.

Contrary evidence:

- Rank-1 TP1 median is only about `0.1714R`.
- `tp1_below_min_rr` dominates rejection diagnostics.
- The manual review found 2 base candidates where a later rank looked preferable.

Overfitting risk:

- Low. Keeping behavior unchanged avoids tuning to a 30-case manual review.

Implementation readiness:

- High. This is the current implemented behavior.

Decision:

- Adopt. Keep Strategy B TP1 selection unchanged for now.

### Option B: Design a narrow farther-target exception

Supporting evidence:

- `later_rank` was selected for 2 of 30 base candidates.
- Some rank 2-5 targets can clear `1.0R` in the broader diagnostics.
- The 32-summary corpus supports structural TP rather than arbitrary target placement.

Contrary evidence:

- The seven-case adjudication produced `revise_to_later_rank_candidate: 0`.
- Most low-rank-1 cases do not have any rank 2-5 target clearing `1.0R`.
- A simple later-rank rule would not solve most TP1 failures.
- The corpus does not define a mechanical priority among wave projection, horizontal level, channel target, pattern width, and nearer realistic target.

Overfitting risk:

- High. A narrow exception could easily encode a few visually appealing cases without a repeatable structural rule.

Implementation readiness:

- Low. More diagnostic definition is needed before this becomes even a design proposal.

Decision:

- Do not propose a farther-target exception yet.

### Option C: Lower or remove TP1 min RR

Supporting evidence:

- `low_rr_but_structural_tp` was common in the manual review.
- The 32-summary corpus treats RR as contextual and does not confirm a universal fixed minimum RR.
- Some visually reasonable first targets fail fixed RR.

Contrary evidence:

- Lowering or removing TP1 minimum RR would not solve target-quality issues.
- Some low-R TP1 cases are micro-structure, inside noise, or not visually interpretable.
- The existing evidence does not provide a replacement threshold.
- A parameter change based on this sample would be optimization-like.

Overfitting risk:

- Very high. RR thresholds are easy to tune to historical or sample-specific outcomes.

Implementation readiness:

- Low. No replacement threshold is justified.

Decision:

- Do not lower or remove TP1 min RR yet.

### Option D: Reclassify low-R-but-structural TP cases separately without changing execution rules

Supporting evidence:

- Manual review separated `low_rr_but_structural_tp` from `low_rr_due_to_minor_tp1`, `low_rr_due_to_questionable_stop`, and `rr_failure_not_diagnosable`.
- Second review preserved the need to distinguish structurally meaningful low-R TP from micro-structure TP.
- This supports better diagnostics without changing Strategy B execution.

Contrary evidence:

- Classification labels are reviewer judgments and not mechanical execution rules.
- This does not improve Strategy B results by itself.

Overfitting risk:

- Low, if kept as docs-only diagnostic taxonomy.

Implementation readiness:

- High for documentation. Not implementation-ready as code behavior.

Decision:

- Adopt as a documentation and diagnostics distinction only.

### Option E: Modify stop-anchor or stop-width logic

Supporting evidence:

- Every `stop_too_wide` candidate also fails `tp1_below_min_rr`.
- Stop-anchor interpretation was mixed in the manual review.
- The 32-summary corpus supports premise-based stop/invalidation anchoring.

Contrary evidence:

- Wide stops are not automatically wrong when structurally justified.
- Shallow stops solely to improve RR would conflict with premise/invalidation logic.
- Second-review stop-anchor adjudication left multiple cases questionable, not visually interpretable, or unresolved.
- The evidence does not specify a replacement stop rule.

Overfitting risk:

- High. Stop-width and stop-anchor changes can reshape results quickly and may violate invalidation logic.

Implementation readiness:

- Low. Stop-anchor quality needs a separate diagnostic path first.

Decision:

- Do not change stop logic yet.

### Option F: Move to Strategy B2

Supporting evidence:

- Current Strategy B rejects most candidates.
- Corpus evidence suggests contextual TP/RR and discretionary structure that Strategy B may not capture.

Contrary evidence:

- Manual and adjudication evidence does not yet justify a new strategy variant.
- Strategy B2 would invite parameter drift or rule expansion before the TP1/stop evidence is settled.
- The current review was only a small diagnostic pass, not a complete design approval.

Overfitting risk:

- Very high.

Implementation readiness:

- Low.

Decision:

- Do not create Strategy B2.

## 8. Decision

Decision:

- Keep Strategy B TP1 selection unchanged for now.
- Do not implement a later-rank exception yet.
- Do not lower or remove TP1 min RR yet.
- Do not change stop logic yet.
- Do not create Strategy B2 yet.
- Preserve no-valid-target / no-trade rejections as separate classes from low-RR cases.
- Separate low-R-but-structural TP from micro-structure TP in future diagnostics.
- Treat stop-anchor quality as a separate decision path.
- Do not approve implementation.

Allowed follow-up:

- A docs-only follow-up diagnostic backlog or closure note may define future evidence categories.
- Any future design proposal must remain separate from implementation and must not tune parameters from this sample.

## 9. Rationale

Rank 1 was often visually defensible. In the 30-base-candidate manual review, `current_rank1` was selected 22 times. That weakens the case for replacing rank 1 wholesale.

Later-rank support exists but is weak. The manual review found 2 later-rank cases, but the second review found 0 of the flagged cases should be revised to a later-rank candidate. A broad later-rank exception would outrun the evidence.

Many low-R cases appear structural rather than clearly wrong. The common `low_rr_but_structural_tp` label means the RR gate issue may be real, but it does not prove that target selection is wrong or that RR should be lowered.

The RR gate issue cannot be fixed responsibly by parameter change yet. The 32-summary corpus supports contextual RR, but it supplies no numeric replacement threshold. Lowering the threshold now would be parameter tuning, not specification.

Stop-anchor quality is distinct. Wide stops can be structurally valid, questionable, or not interpretable. Changing stop logic to make RR look better could break premise/invalidation logic.

Strategy B should not be changed from a 30-case manual review. The review is valuable, but it is still a small diagnostic sample with seven second-review flags and one unresolved adjudication.

## 10. What this does not decide

This memo does not decide:

- profitability
- production readiness
- live trading readiness
- broker execution
- parameter optimization
- Strategy B2
- Strategy C
- whether the YouTube method works
- whether the strategy is tradable
- whether Strategy B is profitable or unprofitable
- whether a future implementation change will be approved

## 11. Recommended next PR

Recommended next PR:

- create a docs-only Strategy B TP1 / stop-anchor follow-up diagnostic backlog, or
- create a Strategy B TP1 decision closure note that freezes Strategy B behavior pending broader evidence.

Preferred next PR: create the docs-only follow-up diagnostic backlog.

That backlog should define future work items without implementation:

- separate low-R-but-structural TP from micro-structure TP
- keep no-valid-target and no-trade-structure cases separate from TP1 RR failures
- define stop-anchor diagnostic labels as their own path
- identify what evidence would be required before a farther-target design proposal
- define what would count as sufficient evidence to revisit TP1 minimum RR

Do not recommend implementation yet. A future implementation PR would require a separate design-only PR first.

## 12. Guardrails

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
