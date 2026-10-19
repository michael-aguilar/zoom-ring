# Project handoff

Snapshot date: 2026-10-15. This is the entry point for an agent that has not seen the original discussion.

## The problem

Manual zoom-ring contact creates visible microshakes during telephoto video on a monopod. The objective is smooth remote zoom without adding a large support footprint. A motor removes uneven hand input, but cannot remove its own reaction torque or stabilize monopod sway.

Camera compatibility context: Canon EOS R10; approximately 55–250 mm, believed to be Canon EF-S through an EF-to-RF adapter. Exact lens model/version and adapter still require confirmation before mechanical fit or torque decisions.

## Explicit requirements and preferences

- Zoom only, retaining the existing monopod.
- Wired third-party Wii Nunchuck as the handheld input.
- Encoder required for closed-loop control.
- Small physical electronics footprint. ESP32 is not a requirement.
- Electronics-focused parts research. Mechanical design is planned independently: printed pulleys, bought timing belt and custom mounting.
- Keep costs modest; Amazon preferred, cheaper other suppliers acceptable.
- Explore camera power if practical, but a usable motor-power output has not been verified.
- A single connected wiring diagram with each component shown once is preferred over separate wiring panels.
- A temporary connection method is desirable for testing before committing to soldered wiring.

## Working recommendation, not a purchase decision

- Standard XIAO RP2040, 21 × 17.8 mm.
- Adafruit DRV8833 #3297 for reversible PWM motor drive and adjustable current limiting.
- Adafruit N20 encoder motor #4639 as the best-documented inexpensive reference option, not a torque-proven final choice.
- Regulated 5 V USB battery supply for the prototype; all grounds common, motor current not routed through the MCU.
- Wired Nunchuck at 3.3 V, I2C address 0x52.
- Motor quadrature feedback for relative motion/speed.
- Rigid stationary motor mount and belt coupling.

Read [wiring](wiring.md) before using the diagram. The stock driver's nominal 1 A current limit is not an established lens torque limit.

## What is actually available

- Unified 2160 × 1440 wiring PNG, SVG and browser HTML.
- Earlier segmented 1600 × 2370 diagram, retained as supporting detail/history.
- Original documentation-check notes and a machine-readable netlist.
- Portable diagram generators, renderer dependency lockfile, and the fonts/license used by the diagrams.
- Curated component comparisons, source links, decisions, firmware design notes and unanswered questions.

There is no implemented motor firmware, CAD, purchased-parts inventory, finalized pulley ratio or recorded hardware test result. A first hand-held zoom-ring pull measurement (2026-10-19, about 2.1 kg·cm peak, one direction) and a motor sizing pass are in [mechanics and power](mechanics-and-power.md#measured-zoom-load-2026-10-19).

## Next useful work

1. Confirm exact lens/adapter and actual hardware already on hand.
2. Measure zoom travel, ring/pulley dimensions, breakaway/running resistance and desired full-sweep time. Ring diameter and 55 → 250 pull force are done; travel angle, sweep time and the reverse pull remain.
3. Use those measurements to select motor and pulley ratio. Confirm candidate performance at 5 V, not just its 6 V no-load rating.
4. Verify the exact Nunchuck and motor electrical interfaces and choose the current-limit resistor conservatively.
5. Implement and test input, encoder and fail-stop behavior with the motor detached before any lens-coupled run.
6. Validate smoothness and noise on the real rig.

[Open questions and validation](open-questions-and-validation.md) contains the detailed checklist. These are handoff next steps, not claims that engineering or purchases have already occurred.

## Keep the context coherent

Record new owner decisions separately from technical recommendations. Cite the source of changes, record actual measurements and test conditions, and preserve unresolved uncertainties. Older gimbal/pan-tilt research is archived context, not current scope.

The imported research is curated, not a byte-for-byte transcript archive. One delegated history-recovery attempt timed out; core delivered answers and requirements were subsequently recovered using bounded original-message reads, alongside the intact saved artifacts. Original conversation attachments outside the saved diagram bundle are not guaranteed to be present.
