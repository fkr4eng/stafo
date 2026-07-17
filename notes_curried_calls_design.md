# Design notes: curried calls in pyirk (`element of sequence(f,i)(x)`)

Status: **implemented** (2026-07-17), all three stages. Spans `pyirk-core` (core mechanism)
and `irk-data/ocse` (the element-type rule). Context: the FNL now uses the canonical curried
form (e.g. `formalized_statements_nl.md:2096`), previously hidden behind the `(f(x))_i`
workaround.

What was built (see "Plan" at the bottom for the reasoning behind each stage):
- **Stage 2** — `_set_relation` now calls `_copy_method_prototypes_from_type` when `R4` or
  `R30` is set (`core.py`, `TYPE_DECLARING_RELATION_URIS`), so an item typed as a callable
  class *via R30* becomes callable. Test: `test_a01d__custom_call_inheritance_via_R30`.
- **Stage 2b** — new builtin `R90__is_applied_at_result_creation` plus
  `I41.set_eager_rule_body(func)` and `get_eager_rules()` (`builtin_entities.py`). In ocse,
  `I4731__element_type_rule` is flagged `R90=True` and carries
  `_apply_element_type_rule_eagerly`, which does the class/instance hop explicitly.
- **Stage 3** — `create_evaluated_mapping` applies every R90-flagged rule to the new result
  right after the R88 stamping (`_builtin/math_expressions.py`). The eager set is empty
  unless something flags itself, so the default cost is one `ds` lookup.

Verified end-to-end: `element of sequence(f, i)` gets `R15 f` (R88) → `R30 scalar function`
(eager rule) → is callable (Stage 2) → `element of sequence(f, i)(x)` resolves.

One wrinkle worth remembering: the eager body runs while an *arbitrary* module is the active
one (whichever module creates the result), but its short keys (`R7280`, ...) must resolve in
the module that *defines* the rule. Hence `set_eager_rule_body` wraps the body with
`core.wrap_function_with_search_uri_context(func, self.base_uri)`.

## Goal

Make `element of sequence(f, i)(x)` evaluate: the result of an operator application must
itself be callable when it is (semantically) a function — e.g. the i-th element of a
sequence of vector fields is a scalar function that can be applied to a point `x`.

## How callability actually works (verified against the code)

- An entity is callable iff it has a `_custom_call` attribute (`core.py:169` `__call__`).
- `_custom_call = create_evaluated_mapping` is attached to `I6–I9`
  (`builtin_entities.py:903–906`).
- It propagates to instances/subclasses **only over `R4` (instance) and `R3` (subclass)** —
  never over `R30` (secondary instance). See `_perform_instantiation` (reads `R4`) and the
  subclass propagation (reads `R3`) in `core.py:300–339`; `add_method` walks `R4`/`R3` only
  (`core.py:452–455`).
- `op(*args)` builds the result as `instance_of(target_class)`, where
  `target_class = op.R11__has_range_of_result` or, if unset, `I32["evaluated mapping"]`
  (`math_expressions.py:89–95`). So **the result is callable iff its result type is a
  callable class.**

Empirically confirmed (scratch probes):
- Result type = callable class (subclass of I6, incl. 2 levels `I6 ← general function ←
  covector field`) → curried call works **today, no core change**. This already holds in the
  live KB: `gradient op → covector field`, `sharp → vector field`, `time derivative op →
  general function`, `has inverse mapping → general function`.
- Result typed as callable class only via `R30` → **not** callable (`_custom_call` absent).

## The one unsolved case

Operators whose result callability depends on an **argument's element type**, i.e.
`element of sequence`. Its result type is not fixed (integer for a coefficient sequence,
scalar function for a sequence of vector fields), so it has no `R11` and falls back to bare
`I32` — not callable. Two blockers:

1. **The result isn't typed by element type.** It should become an `R30` secondary instance
   of `f`'s element type. `R30` (not `R4`) because the primary type `R4` is already
   `I32`/the range class.
2. **`R30` doesn't carry `_custom_call`.** Even once typed, method inheritance doesn't
   follow `R30`, so the result stays uncallable.

## The typing is already specified — nothing new to invent

- Definition lives in data: `'vector field' 'has element type' 'scalar function'`
  (`R7280`, class-level; `formalized_statements_nl.md:1944`).
- Resolution is the existing **element type rule I4731** (`ocse/math1.py:461`):
  `el R15 s ∧ s R7280 t → el R30 t`.
- The connecting fact `ev R15 f` is **already stamped eagerly** by the R88 auto-relation we
  added: `Applying 'element of sequence' creates relation: result 'is element of' argument1`
  (`formalized_statements_nl.md:29`).

So Stage 3 is not "invent a new target"; it is "make the existing rule conclude on `ev`
eagerly, at construction time."

## Decisions (and why)

**D1 — Add `_custom_call` inheritance over `R30` (Stage 2).**
Because `R30` is the correct relation for the derived element type (the primary `R4` slot is
already taken by `I32`/range class), and callability must follow it. General, small, and
independently testable — not currying-specific.

**D2 — Type the result *eagerly at creation*, not via a batch rule pass.**
The curried call `…(x)` runs at construction time (the FNL compiles to `seqop(f,i)(x)`
executed at module load). The inner result must be callable *the instant it exists*. A
post-construction batch sweep is too late; running the whole rule engine per creation is
O(KB²) — rejected.

**D3 — Rejected: operator names the rule to apply (was "S2").**
The FNL author models mathematics and cannot know which internal rules should fire. Naming
`I4731` in the FNL leaks a reasoning-layer detail. Dead.

**D4 — Rejected: predicate-index / auto-trigger of applicable rules (was "S3").**
Checking whether a rule is applicable is essentially the same work as trying to apply it; an
index only avoids *attempting* obviously-irrelevant rules. For a small eager set that saving
is negligible and not worth the machinery. Collapses into D5.

**D5 — Selection: rules flag themselves "apply at result creation"; the rule author chooses.**
A small curated set, marked in ocse where the rule is defined by someone who understands the
reasoning layer. Core fetches the flagged set and applies each anchored at the new `ev`;
non-matching rules no-op cheaply (their premise isn't satisfied). Separation of concerns:
FNL author = math (+ R88 facts); rule author = reasoning (+ eager flag); core = generic
dispatch, nothing domain-specific.

**D6 — Apply the eager rule algorithmically, not via subgraph matching (route R2).**
Rule application today builds a NetworkX graph over the **entire** datastore
(`create_simple_graph`, `ruleengine.py:200`) and runs VF2 monomorphism over all of it
(`match_subgraph_P`, `:902`) — no anchor, O(KB). The engine already has the escape hatch
(`cheat`, `:280`; nascent `AlgorithmicRuleApplicationWorker`) for calling a Python function
instead of matching. So the eager rule carries a body `apply(anchor)` that computes and sets
the consequent directly — no graph, no sweep. This also turns the messy class-vs-instance
hop into explicit Python (`element_type = <type of ev's R15-neighbor>.R7280`) instead of a
subgraph pattern that may not match class-level edges.
(Alternative route R1 — restrict the host graph to `ev`'s k-hop neighborhood and filter
monomorphisms to the anchor — is feasible but more machinery; deferred.)

**The class/instance hop (was open, now settled in the eager body).**
I4731's premise `s R7280 t` binds `s = f` (a *vector field instance*), but `R7280` sits on
the *class* `vector field`. This is the ambiguity raised at the very start
("`'vector field' 'has element type' 'scalar function'`" means *instances of* vector field
have elements of that type). Per D6 it is now explicit Python: `_get_element_types` looks at
`seq` itself, then at its types (`R4` + `R30`), then walks their `R3` superclass chain.
**Note the graph-premise scopes of I4731 still do not do this hop** — the eager body and the
scopes are not equivalent. The scopes are left as they are for now; if the rule is ever also
applied in a batch pass, they need the same treatment.

## Plan (build order)

1. **Stage 2 (core, standalone):** `set_relation` to `R4`/`R30` a class copies its
   `_method_prototypes`, so results typed (even secondarily) as a callable class gain
   `_custom_call`. Regression test: an `R30`-typed-callable-class item is callable.
2. **Eager flag + algorithmic body (ocse + small core):** flag the element-type rule
   "apply at result creation"; give it `apply(anchor)` that sets
   `anchor R30 <element type of the sequence it is an element of>`.
3. **Creation hook (core):** in `create_evaluated_mapping`, after the R88 stamping, iterate
   the small eager-rule set and call each `apply(ev)`; non-matching bodies return at once.

Result: `element of sequence(f,i)` gets `R30 scalar function` eagerly → callable via Stage 2
→ `element of sequence(f,i)(x)` resolves during construction.

Stage 2 is the clean prerequisite and stands on its own; build and test it first, then
decide R1-vs-R2 details for the hook.
