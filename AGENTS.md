# Working on zoom-ring

Read README.md and docs/HANDOFF.md first. Then read docs/requirements-and-decisions.md and the document relevant to the task.

This repository is the portable project context. It deliberately does not contain private conversations, credentials, assistant memory, or account setup. Do not add those.

## Scope and evidence

- Current scope is motorized zoom only, attached to an existing monopod.
- An encoder is required. The owner intends to design the mounts and print the pulleys for a bought timing belt.
- Do not revive powered pan/tilt, a freestanding robotic monopod, wireless control, or an SBC as assumed requirements.
- Hardware choices are recommendations and candidates, not confirmed purchases.
- Wiring is documentation-reviewed for the exact reference parts, not bench-tested.
- Preserve the distinction between owner requirements, documentation facts, suggestions, and unresolved measurements.
- A motor-shaft encoder measures relative motor travel, not absolute lens position or belt slip.
- Do not silently reuse the reference motor's wire colors or voltage assumptions for another motor.
- Update docs/requirements-and-decisions.md, docs/open-questions-and-validation.md and sources when new evidence changes a conclusion.
- Keep public-facing technical documentation free of personal details. The initial repository is public.
- Hardware purchases, new background assignments and changes outside the requested project task are not implied by this handoff.

## Collaboration

Use a separate checkout per agent or machine. Start from a clean branch and fetch/pull with fast-forward-only before new work. Keep commits focused, do not force-push or overwrite other agents' changes. Use a task branch for concurrent work.

Do not claim hardware tests, successful firmware, motor suitability or camera-power compatibility without evidence. There is no implemented motor-control firmware or fabricated mount in this initial research handoff.
