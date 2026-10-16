# Requirements and decision log

Updated 2026-10-15. "Confirmed" means explicitly requested, not physically validated.

## Confirmed project requirements

| Item | Current requirement | Basis |
| --- | --- | --- |
| Scope | Motorized zoom ring only, on the existing monopod | October 15 scope reduction |
| Feedback | Encoder required for closed-loop control | Explicit follow-up |
| Input | Wired Wii Nunchuck, third-party acceptable | October 15 request |
| Nunchuck connection | Adafruit adapter #4836; do not cut the controller cable | Owner decision, 2026-10-15 |
| MCU priority | Small physical board size; processor family flexible | Clarification after smaller-Pico question |
| Mechanics | Custom mounts and printed pulleys with purchased timing belt | Owner's stated plan, not finished CAD |
| Parts research | Electronics only; prefer Amazon but accept inexpensive alternatives | Follow-up clarification |
| Power | Camera power desirable if feasible | Preference, not verified electrical capability |
| Documentation | One connected full-circuit diagram | Replaced segmented presentation as primary diagram |
| Prototyping | Temporary connection options before soldering | Solderless-connection question |
| Form factor | Portable and practical on a monopod | Original filming constraints |

## Technical context and uncertainty

- Canon EOS R10 is confirmed from the original camera discussion.
- The lens was described as roughly 55–250 mm, believed to be EF-S with an EF-to-RF adapter.
- Exact lens variant, adapter model and monopod model are not confirmed.
- No hardware inventory or purchase should be inferred from discussion of a part.

## Recommendations, not owner-selected final parts

| Recommendation | Why | Still unverified |
| --- | --- | --- |
| Standard XIAO RP2040 | Small, 3.3 V logic, I2C/PWM and sufficient GPIO | Final packaging and software stack |
| Adafruit DRV8833 #3297 | Documented reversible drive, sleep and adjustable current limit | Proper current limit for mechanism |
| Adafruit motor #4639 | Documented 5 V motor and 3.3 V encoder compatibility | Torque, speed, noise, backlash |
| Small USB 5 V pack | Simple independent prototype supply | Idle auto-shutdown, transients and runtime |
| Stick = speed/direction; Z = hold-to-enable; C = slow mode | Simple one-handed control | Actual user feel and final mapping |
| Pre-soldered XIAO headers for breadboarding | Reliable removable prototype connections | Breadboard layout and other boards' connections |

## Evolution and superseded advice

- October 9: explored stabilization, a full robotic monopod and used gimbals. Powered pan/tilt is deferred, not part of this build.
- Initial fluid-head advice was corrected: damping rotation does not stabilize whole-monopod sway or eliminate twist.
- Initial controller example was a Raspberry Pi Pico. XIAO RP2040 became the smaller recommended replacement. ESP32 is optional, not required.
- An initial follow-focus ring/pinion suggestion was superseded by the stated printed-pulley/timing-belt mechanical plan.
- Initial whole-prototype budgets included mechanical items. The later requested BOM is electronics-only.
- Direct soldering to a bare XIAO was suggested for compact final assembly. For temporary full-circuit testing, the later recommendation was pre-soldered headers plus a breadboard.
- The earlier multi-panel diagram is retained, but the unified diagram is the main visual.
- Encoder-equipped motors are required. An encoderless cheap motor is not an equivalent substitute.
- Camera-supplied motor power remains an unanswered feasibility question, not a proven v1 feature.
