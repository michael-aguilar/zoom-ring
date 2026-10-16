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
