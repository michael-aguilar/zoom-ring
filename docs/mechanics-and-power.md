# Mechanics and power tradeoffs

## Mechanical direction

The planned mechanism is printed pulleys and a purchased timing belt, with a custom mount. This is a stated design direction, not completed CAD or a fabricated assembly.

Earlier suggestions included a strap-on follow-focus gear ring and pinion. They are alternatives/history, not extra required purchases.

The motor needs a rigid stationary reaction mount on a camera plate/cage/rod or equivalent support. Attaching a motor only to a rotating lens ring gives it nothing fixed to push against. Avoid loading or obstructing the extending lens barrel.

Important unresolved dimensions/behavior:

- Exact lens version and which ring rotates versus which surfaces remain fixed.
- Zoom-ring diameter, usable mounting width and angular travel.
- Pulley tooth counts, belt pitch/width, center distance, tension adjustment and motor shaft fit.
- Breakaway versus running resistance across the zoom range and in both directions.
- Required full-sweep time and smallest useful smooth speed.
- Mount stiffness, backlash, belt slip and motor/gear noise in video.
- Strain relief and portability without interfering with the monopod/camera.

## Sizing framework

The handoff does not contain a measured motor/gear/pulley selection. A useful next engineering step is to measure force tangentially at a known ring radius:

`ring torque ≈ tangential force × effective radius`

For a belt with lens-pulley tooth count N_lens and motor-pulley tooth count N_motor, the external reduction is approximately N_lens / N_motor. Larger lens-to-motor ratio reduces ring speed and increases available ring torque, subject to losses.

Compute required ring speed from measured travel and desired sweep time; then work backward through the pulley ratio to motor output-shaft speed. Use loaded performance at the actual supply voltage, not a 6 V no-load label.

These equations are a next-step framework added to make the research actionable, not evidence of actual measurements. A torque margin must not become an excuse to force the lens through a hard stop.

## Measured zoom load (2026-10-19)

Owner measurement with a hand-held hanging scale, not a lab test.

- Method: string wrapped 2–3 turns around the zoom ring's rubber grip, digital hanging scale pulled by hand along a tangent. Lens believed to be Canon EF-S 55–250 mm on an EF-to-RF adapter; the exact version is still unconfirmed.
- Ring diameter at the grip: 2.74 in (69.6 mm), so the effective radius is about 3.48 cm. String thickness was not recorded and is ignored.
- Three pulls, all from 55 mm toward 250 mm. Breakaway is the peak as the ring started to move. Running is the owner's eyeballed average over the pull.

| Run | Breakaway | Running (eyeballed average) |
| --- | --- | --- |
| 1 | 480 g | 580 g |
| 2 | 420 g | 550 g |
| 3 | 460 g | 560 g |

- The running force rose during each pull, from roughly 480 g near 55 mm to roughly 600 g near 250 mm (owner's observation). Breakaway was lower than running, so there was no stiction spike; the highest load is near the tele end.
- Design load: 600 g at 3.48 cm, about **2.1 kg·cm (20.5 N·cm) at the zoom ring**. Average running is about 1.96 kg·cm; highest breakaway about 1.67 kg·cm.
- Not measured: the 250 → 55 direction, ring travel angle and target sweep time. A pull that drifts off the tangent reads high, so a reverse pull would show whether the rise comes from the lens or from the measurement.

## Motor sizing against the measurement

Assumptions (engineering estimates, not vendor data): belt-stage efficiency 0.9; stall torque scales with supply voltage, so 5 V stall is about 5/6 of the 6 V figure; continuous load at or below about one third of 5 V stall for smooth, cool running. The "vendor rated" column uses the vendor's rated torque instead and leaves little margin. Ring speed estimates assume the loaded motor runs at about two thirds of its 5 V no-load speed.

Required motor torque ≈ 2.1 kg·cm ÷ (pulley ratio × 0.9).

| Motor | 6 V figures used | Ratio at vendor rated torque | Ratio for ≤ 1/3 stall at 5 V | Ring speed at that ratio |
| --- | --- | --- | --- | --- |
| Adafruit #4639 (N20 1:100) | 0.40 kg·cm rated at 65 rpm; 0.7 kg·cm stall; 100 rpm no-load | 5.8:1 | 12:1 | ~28°/s |
| Adafruit N20 1:298 (same vendor ratio table) | 1.15 kg·cm rated at 20 rpm; 1.5 kg·cm stall; 33 rpm no-load | 2:1 | 5.6:1, use 6:1 | ~18°/s |
| DFRobot FIT0484 (150:1) | 1.0 kg·cm rated at 60 rpm; 2.2 kg·cm "instant torque"; 105 rpm no-load | 2.3:1 | 3.8:1, use 4:1 | ~88°/s |
| Pololu #5146 (298:1 MP) | 2.4 kg·cm stall (theoretical); 73 rpm no-load; no rated torque listed | n/a | 3.5:1, use 4:1 | ~61°/s |
| uxcell GA12-N20 (Amazon) | 100 rpm at 6 V; no torque listed | n/a | n/a | n/a |

Pulley geometry example: with a GT2 (2 mm pitch) belt, a lens pulley about 3 mm thick over the 69.6 mm ring has a pitch diameter of about 75.6 mm, roughly 119 teeth. A 16-tooth motor pulley then gives about 7.4:1 and a 20-tooth pulley about 5.9:1. Belt type and pulley thickness are the owner's design choices; this is only an example of what one belt stage can reach.

Recommendations from this sizing, not purchase decisions:

- Adafruit #4639 at 1:100 is marginal. A comfortable margin needs about 12:1, more than one belt stage around this ring gives with practical motor pulleys. At about 7.4:1 it would run near half its 5 V stall torque at the tele end.
- Pololu #5146 at about 4:1 and an N20 1:298 at about 6:1 both fit with margin. The Pololu is better documented and faster; the N20 1:298 is cheaper and slower. Whether Adafruit sells a 1:298 version of #4639, and whether its wiring matches, has not been checked.
- DFRobot FIT0484 fits at about 4:1 but showed out of stock on 2026-10-19 and lists no encoder voltage.
- uxcell GA12-N20 lists no torque. Its listing gives black as encoder negative and blue as encoder positive, the reverse of #4639, so the reference diagram's colors do not apply to it.
- Speed is not the limiting factor: every fitting option gives at least ~18°/s at the ring. Full-sweep time needs the ring travel angle, which has not been measured.
- Pololu warns that stalls can damage the gearbox. Firmware stall detection and soft travel limits remain required whichever motor is chosen.

## Camera power findings

Camera power was preferred if practical. Research did not establish a suitable DIY motor output from the EOS R10.

- Canon's USB power documentation describes power into the camera, not a general motor supply output.
- The multifunction shoe supports compatible powered accessories, but no usable DIY motor tap was verified.
- A shared external battery could potentially feed camera and controller through separate appropriate outputs after confirming camera requirements.
- An ordinary split USB cable is not a verified way to supply both.
- Do not tap a camera battery, shoe or port based on the existence of accessory power alone.

Primary Canon links:

- [USB external power](https://cam.start.canon/en/C006/manual/html/UG-11_Reference_0030.html)
- [Multifunction shoe](https://cam.start.canon/en/C006/manual/html/UG-01_Preparations_0080.html)

## Recommended prototype supply

A small regulated 5 V USB bank on the monopod is the simplest current recommendation. It feeds MCU and driver in parallel with common ground. The reference motor explicitly permits 5 V operation; a generic "6 V motor" label alone does not establish suitable performance or encoder compatibility.

Validate current capability, transients, idle auto-off, runtime, wiring drop and motor-noise effects. At least 1 A was the earlier supply recommendation, not proof of a complete power budget.

Read [wiring](wiring.md) for current-limit and USB programming constraints.
