# codebox-arena

Scratchpad for the codebox **active flavor**: the box reads issues here,
generates patches via `codebox solve`, opens PRs, and lets GitHub CI verify
the result. Each merged PR (or each failing CI) becomes one external-truth
data point in the box's polling stream.

Companion to research note 03 at https://intuitionlabs.tech/research/phi/03-pick-your-target.

## Structure

```
problems/
  <slug>/
    problem.md          ← human-readable spec the box reads
    solution_stub.py    ← skeleton (signature only)
    tests/
      test_<slug>.py    ← pytest verifier; CI green = passed
```

When the box attempts a problem it writes `problems/<slug>/solution.py`
and opens a PR. CI runs `pytest problems/<slug>/tests/` against it.

## Safety bounds

- All PRs from the box are labeled `codebox-experiment`.
- Rate-limited to 1 PR per 5 minutes by default.
- Default `codebox attempt --dry-run` writes the patch locally; `--push`
  is opt-in.
- This repo is private until the active flavor proves stable.

## CI

`.github/workflows/ci.yml` runs pytest on every push / PR. Conclusion is
the verifier signal `codebox-livecorpus-github` reads.

## License

MIT. Free to mirror, fork, study.
