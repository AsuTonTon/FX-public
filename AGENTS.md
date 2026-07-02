# FX Repository Agent Instructions

This repository is an FX system-trading research project. The purpose is not live trading, brokerage integration, or immediate profitability. The purpose is to convert video-derived trading ideas into reproducible, auditable, mechanically testable research artifacts while avoiding overfitting and unsafe operational drift.

## Core project boundaries

Allowed repository content:

- specifications;
- research reports;
- paraphrased video summaries;
- implementation code;
- test code;
- design decisions;
- guardrail and operations documentation.

Forbidden repository content:

- `data/`;
- `results/`;
- raw market data;
- normalized market CSVs;
- generated trade, event, candidate, or result CSVs;
- raw transcripts;
- subtitle full text;
- raw TXT/SRT/VTT caption files;
- caption URLs;
- downloaded video or audio;
- credentials, tokens, or secrets.

Forbidden project actions unless an issue explicitly and narrowly authorizes them:

- market-data API calls;
- broker API calls;
- order placement;
- auto trading;
- live trading;
- strategy parameter optimization;
- Strategy C creation;
- profitability guarantees or claims that the system is profitable.

## Research-line separation

There are two separate research lines:

1. Strategy A/B verification line.
   - Keep the focus on reproducibility, sample count, risk structure, and failure reasons.
   - Do not mix channel-wide corpus findings into Strategy B without a separate design decision.

2. YouTube channel-wide corpus line.
   - Inventory, transcript availability, paraphrased summary, theme classification, and doctrine mapping are allowed when scoped.
   - Raw subtitles, transcript full text, caption URLs, and downloaded media are not allowed.
   - Channel-wide findings must remain separate from Strategy A/B until a separate Strategy-line review authorizes integration.

## Caption and video-source caution

When caption/body access is unavailable or unstable:

- do not retry at scale;
- do not bypass access controls;
- do not download audio or video;
- do not use ASR output unless a future issue explicitly authorizes it;
- prefer small, documented probes after the wait period specified in the controlling issue;
- keep raw caption/subtitle text out of Git.

## Pull request expectations

Every PR should include:

- objective;
- scope;
- changed files;
- explicit guardrail statement;
- validation performed;
- next recommended task, if any.

Docs-only PRs should state that they made no Strategy A/B rule changes, no backtest changes, no market-data changes, and no broker/live changes.

Implementation PRs should include tests or explain why tests are not applicable.

## Review guidelines

Treat the following as P1 issues during PR review:

- any committed `data/` or `results/` file;
- any raw market CSV, normalized market CSV, candidate CSV, result CSV, raw transcript, subtitle full text, raw TXT/SRT/VTT caption file, caption URL, downloaded media, credential, token, or secret;
- any market-data API, broker API, order-placement, auto-trading, or live-trading functionality;
- any Strategy C work;
- any strategy parameter optimization presented as if it were authorized;
- any profitability guarantee, such as claiming that a strategy is profitable or that the project can reliably make money;
- any PR that mixes the Strategy A/B verification line with the YouTube channel-wide corpus line without an explicit design decision;
- any PR that changes Strategy A/B/B2 behavior while claiming to be docs-only;
- any PR that changes research conclusions without citing the repository evidence it relies on;
- any PR that says raw subtitles, transcript full text, raw DownSub output, caption URLs, or downloaded media were accessed or committed;
- any PR that omits a guardrail statement from the PR body.

Treat the following as P1 issues for docs PRs:

- hype language copied from video titles into project conclusions, such as treating `win`, `profitable`, `神回`, `勝てる`, `稼げる`, or similar title language as a project result;
- paraphrase that appears to be raw or near-raw subtitle text rather than a compact summary;
- missing uncertainty notes where a mechanical-rule candidate still depends on visual discretion.

Do not request changes merely because a PR is conservative. Conservative framing is preferred over overclaiming.
