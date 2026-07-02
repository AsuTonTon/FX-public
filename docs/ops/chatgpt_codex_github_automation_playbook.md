# ChatGPT / Codex / GitHub Automation Playbook

## Purpose

Reduce the human role from repetitive copy-paste and routine merge handling to high-leverage decisions only.

Target model:

1. GitHub Issue defines the task contract.
2. Codex works from the Issue and opens a PR.
3. Repository guardrails and Codex review catch routine problems.
4. ChatGPT/human review is reserved for high-impact decisions, failed checks, or scope changes.
5. Eligible routine PRs use GitHub auto-merge after repository settings are enabled.

This playbook is an operations document only. It does not change Strategy A/B, video research conclusions, or any research rule.

## Current bottleneck

The current loop is too manual:

- ask ChatGPT for the next Codex prompt;
- paste the prompt into Codex;
- wait for PR;
- report PR number to ChatGPT;
- review;
- merge;
- repeat.

That loop should be treated as bootstrap, not as the long-term operating model.

## Safe automation lane

These tasks can usually move through standardized Issues, PR templates, guardrail CI, Codex review, and auto-merge once settings are configured:

- docs-only audits;
- playlist or batch synthesis documents;
- coverage-map and inventory reconciliation documents that do not commit raw or generated artifacts;
- guardrail documentation;
- formatting-only documentation corrections;
- routine test additions that do not alter strategy behavior.

## Human-decision lane

These require explicit human/ChatGPT review before merge:

- Strategy A/B rule changes;
- TP/SL, RR, entry, exit, filter, or candidate-selection logic changes;
- Strategy B2 decisions;
- research-conclusion changes;
- source-access policy changes;
- guardrail relaxation;
- failed checks;
- any PR that touches prohibited operational integrations or generated research artifacts.

## Files added by this automation foundation

- `AGENTS.md`: Codex review and project guardrails.
- `.github/pull_request_template.md`: PR structure and guardrail checklist.
- `.github/ISSUE_TEMPLATE/codex_task.md`: reusable task contract.
- `.github/workflows/fx-guardrails.yml`: first-pass CI guardrail for forbidden paths/extensions and missing PR guardrail statements.

## Required GitHub settings after merging this PR

These settings are not fully controlled by repository files.

### 1. Enable auto-merge

GitHub path:

- Settings -> General -> Pull Requests -> Allow auto-merge.

### 2. Protect `main`

Recommended settings:

- require pull request before merging;
- require status checks to pass before merging;
- require the guardrail workflow once available;
- require conversation resolution;
- disallow force pushes;
- disallow deletions.

### 3. Enable Codex automatic reviews

Enable automatic GitHub PR reviews for this repository in Codex settings.

If automatic review is not enabled, use a PR comment:

```text
@codex review
```

## Label model

Suggested labels:

- `codex-task`
- `routine-automerge-candidate`
- `needs-human-decision`
- `strategy-line`
- `corpus-line`
- `guardrail`

## Standard issue-to-PR flow

1. Create a GitHub Issue using `.github/ISSUE_TEMPLATE/codex_task.md`.
2. State task type, allowed scope, forbidden scope, deliverables, validation, and whether human review is required.
3. Codex opens a PR from the Issue.
4. PR template is filled.
5. GitHub Actions guardrails run.
6. Codex review runs automatically or via `@codex review`.
7. If checks pass and the PR is routine, enable auto-merge.
8. If the PR affects strategy, conclusions, source policy, or guardrails, review with ChatGPT before merge.

## ChatGPT role after automation

ChatGPT should stop acting as a merge clerk.

Use ChatGPT for:

- interpreting failed checks;
- reviewing strategy-impacting diffs;
- deciding whether a result changes the research plan;
- writing the next high-quality Codex Issue when the next task is not obvious;
- auditing guardrail exceptions;
- summarizing progress at milestones.

## Auto-merge eligibility rule

A PR may be treated as an auto-merge candidate only if all conditions are true:

- docs-only or routine tests-only;
- PR body includes a complete guardrail statement;
- guardrail CI passes;
- Codex review has no P1 findings;
- no Strategy A/B behavior changes;
- no corpus finding is integrated into Strategy A/B;
- no new source-access method is introduced;
- no forbidden raw or generated artifact is committed;
- the controlling Issue marks human decision as not required.

Any failed condition moves the PR to human/ChatGPT review.

## Next operating change

After this foundation is merged and GitHub settings are configured, use GitHub Issues as the source of truth:

- one Issue per task;
- one PR per Issue;
- PR body links back to the Issue;
- completed PR body states the recommended next Issue.

This removes most manual copy-paste and makes the process auditable.
