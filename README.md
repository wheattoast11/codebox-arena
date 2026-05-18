# codebox-arena

Scratchpad for the codebox **active flavor**: the box reads issues here,
generates patches via `codebox solve`, opens PRs, and lets GitHub CI verify
the result. Each merged PR (or each failing CI) becomes one external-truth
data point in the box's polling stream.

Companion to research note 03 at https://intuitionlabs.tech/research/phi/03-pick-your-target.
The sprint-recap arc is research note 14 at https://intuitionlabs.tech/research/phi/14-twenty-prs-and-one-bench-bug.

**To submit a problem the box will attempt**, see [CONTRIBUTING.md](./CONTRIBUTING.md).

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
- Slug-level dedup: the box never opens a second PR for a problem that
  already has an open `codebox-experiment` PR.

## Observe from any agent

The observer is shipped as a standalone MCP tool. Any MCP-capable agent
can ask "how is the box doing?" without depending on the rest of codebox:

```json
{
  "mcpServers": {
    "codebox-observer": {
      "command": "/path/to/strix-mind/bin/codebox-observer-mcp"
    }
  }
}
```

Tools: `ci_rate`, `ci_observe`, `ci_pr`. See
`strix-mind/box/MCP.md` for details.

## CI

`.github/workflows/ci.yml` runs pytest on every push / PR. Conclusion is
the verifier signal `codebox-livecorpus-github` reads.

## License

MIT. Free to mirror, fork, study.
