# Open questions and validation plan

No boxes below represent completed hardware tests. This checklist consolidates the unresolved research and adds a practical order for later implementation.

## Confirm before final part selection

- [ ] Exact Canon EF-S lens model/version, adapter and stationary mounting geometry.
- [ ] Actual components already owned or ordered, if any.
- [ ] Zoom angular travel and ring/pulley mounting dimensions.
- [ ] Breakaway/running torque across the range, in both directions. 55 → 250 measured 2026-10-19 (about 2.1 kg·cm peak); 250 → 55 not yet measured.
- [ ] Desired full sweep time, minimum speed and acceptable motor noise.
- [ ] Pulley tooth counts, belt specification and tensioning plan.
- [ ] Final encoder-equipped motor, shaft dimensions, voltage limits, stall current and encoder resolution.
- [ ] Exact third-party Nunchuck and working initialization/library combination.
- [ ] Firmware stack and pin-number convention: board D labels versus raw GP numbers. D4/D5 sit on I2C1, so check the I2C instance the chosen stack uses.
- [ ] Current-sense resistor selection, power rating and actual current-limit behavior. With #4639 (listed 200 mA stall), the stock 1 A limit never acts; decide whether a sub-stall limit is useful or whether protection relies on firmware stall detection and pulley ratio.
- [ ] Actual running and stall current of the chosen motor at the 5 V supply.
- [ ] USB supply idle behavior/current capacity; shared camera battery only if independently verified.

## Suggested bring-up sequence

1. With power off, check polarity, intended common grounds, shorts and actual pin placement. Compare against vendor pin maps, not the diagram's layout.
2. Disconnect the motor mechanically. Verify 3.3 V logic and 5 V supply rails without PC USB/external-power overlap.
3. Read Nunchuck stick/buttons reliably; test center calibration, dead zone, enable release and unplug/reconnect behavior.
4. Read encoder counts and verify direction on the detached motor; establish counts per revolution and counting mode.
5. Test low-duty motor drive, direction and disabled startup. Confirm driver sleep behavior and supply droop/noise.
6. Tune/test the chosen current limit and stall/input-loss responses with an appropriate controlled setup, not by stalling the lens.
7. Verify gentle acceleration/deceleration and closed-loop low-speed control under representative load.
8. Establish a known lens position and conservative travel limits by an explicit non-forcing procedure.
9. Couple the belt conservatively, verify clearance and movement without pushing into the lens stops, then validate the entire range.
10. Compare fixed-zoom, manual-zoom and powered-zoom video on the actual monopod at long focal length.

## Record results reproducibly

For each actual test, record date, component part numbers, firmware revision, supply voltage, pulley ratio, load/position, current-limit setting, measurement method and outcome. Document failures as well as success.

Important acceptance targets remain to be defined with the owner: useful minimum zoom speed, maximum sweep speed, acceptable shake/noise, runtime and fault behavior. Do not invent numeric pass thresholds or label the mechanism safe based only on a reference diagram.

## Recorded measurements

| Date | What | Parts and conditions | Result |
| --- | --- | --- | --- |
| 2026-10-19 | Zoom-ring pull force, 3 runs, 55 → 250 | Hand-held digital hanging scale; string on the 69.6 mm rubber grip; lens model unconfirmed; running value eyeballed | Breakaway 420–480 g, running average 550–580 g, rising to about 600 g near 250. Peak about 2.1 kg·cm at the ring. Details in [mechanics and power](mechanics-and-power.md#measured-zoom-load-2026-10-19) |

## Known limitations

- Motor encoder cannot measure belt slip or absolute lens position after power cycling.
- Current limiting is not a substitute for measured travel limits and mechanical validation.
- No automatic end-stop homing method has been approved or proven.
- Exact clone wiring and compatibility are not generic.
- No hardware test, final firmware, CAD or measured sizing data was available for the initial handoff.
