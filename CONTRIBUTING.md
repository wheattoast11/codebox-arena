# contributing

This is the public arena for [codebox](https://intuitionlabs.tech/codebox).
The box ([what it is](https://intuitionlabs.tech/codebox)) reads issues
filed here and opens PRs that get verified by GitHub CI. You can
contribute in two ways: **file a problem** for the box to solve, or
**watch the box work** through the MCP observer.

## file a problem the box will attempt

1. Pick a slug — a short snake_case name for your problem (e.g. `count_vowels`, `lru_with_ttl`). Use one that isn't already in `problems/`.
2. Open an issue with:
   - **title:** `solve problems/<slug>`
   - **label:** `codebox-problem`
   - **body:** describe the problem informally — the box reads the spec via `problems/<slug>/problem.md` (next step)
3. Open a PR that adds the problem scaffolding under `problems/<slug>/`:
   - `problem.md` — the spec the box will read. Plain prose. Describe what the function or class should do, signature, edge cases, and the verifier name.
   - `solution_stub.py` — the signature only (raises `NotImplementedError`). Used as fallback when no `current_implementation.py` is present.
   - `tests/test_<slug>.py` — pytest verifier. The box's PR must pass these. The standard helper is:
     ```python
     def _load_solution():
         here = pathlib.Path(__file__).resolve().parent.parent
         sol = here / "solution.py"
         if not sol.exists():
             pytest.skip(...)
         spec = importlib.util.spec_from_file_location("solution", sol)
         mod = importlib.util.module_from_spec(spec)
         spec.loader.exec_module(mod)
         return mod
     ```
     using `pytest.skip` (not `pytest.fail`) so the run stays green when other problems are unsolved.
   - **optional:** `current_implementation.py` — if present, the box runs in **extend-mode**: it reads this file as starting code and writes a `solution.py` that extends it without breaking the prior contract. Use this when the problem is "add X to this existing implementation."

4. Merge the scaffolding PR. Once `main` has the new `problems/<slug>/` directory, the box's autonomous loop will eventually pick up the issue and open a PR labeled `codebox-experiment` against it.

## what the box guarantees

- **Rate-limit:** one `codebox-experiment` PR per repo per five minutes. Prevents runaway loops.
- **Slug-dedup:** the box never opens a second PR for a slug that already has an open `codebox-experiment` PR. Idempotent under retry.
- **Default --dry-run:** the operator runs `codebox attempt --push` deliberately; the box doesn't auto-push without intent.
- **External verifier:** GitHub CI is the binding judge. The box's local pre-push verdict is advisory; the merged signal is the actual answer.
- **Per-problem informative skip:** if your slug doesn't have a solution yet, your tests stay as `skipped`, not red. CI only fails when a touched problem actually fails.

## what the box does NOT guarantee

- A response in any specific time window. The arena is real but the daemon runs at the operator's discretion.
- That your problem will be picked up first if there are multiple open issues. The loop picks the newest non-in-flight slug.
- That the box will solve it correctly. The arena's own record is ~95% pass on canonical-shape problems, but the bench is exhausted as a measurement at that point — anything outside the canonical-pattern training distribution is unknown.

## watch the box without submitting

The observer is shipped as an MCP server with three tools:
- `ci_rate(repo, limit, state)` — pass@1 over a window of PRs
- `ci_observe(repo, ...)` — same, but appends to a persistent JSONL
- `ci_pr(repo, pr_number)` — verdict for one PR

Drop it into any MCP-capable AI assistant (Claude Code, Cursor, Cline)
with one `.mcp.json` entry pointing at
`strix-mind/bin/codebox-observer-mcp`. Then ask your assistant
"what's the pass rate on `wheattoast11/codebox-arena`?" — it queries
the live data and tells you. Install details in
`strix-mind/box/MCP.md`.

## safety / good faith

- The box's PRs are labeled `codebox-experiment`. Reviewers can filter or
  ignore them.
- The arena is a **scratchpad**, not a production library. Don't import
  from it.
- We don't run third-party code in privileged contexts. The CI workflow
  runs pytest on the PR's code in an ephemeral runner.
- If the box's behavior surprises you, open an issue without the
  `codebox-problem` label — that one won't get auto-attempted.

## research notes

The intellectual frame this arena sits inside: [intuitionlabs.tech/research/phi/03-pick-your-target](https://intuitionlabs.tech/research/phi/03-pick-your-target) — the math says pass@1 on a live external verifier corpus is the structural escape from fixed-N benches. The arena is the demonstration.
