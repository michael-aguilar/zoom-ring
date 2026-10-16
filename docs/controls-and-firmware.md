# Nunchuck controls and firmware design

Design notes and proposed behavior only. No operational motor-control firmware is included in this handoff.

## Input interface

A Nunchuck's joystick is physically analog, but its cable carries digital I2C, not raw joystick voltages. The cut-cable reference needs VCC, GND, SDA and SCL. Use 3.3 V logic/supply for this arrangement and identify wires by function.

- 7-bit I2C address: 0x52. 0xA4 is an 8-bit write-address notation, not the address to pass to a typical MCU I2C API.
- Six-byte reports include two 8-bit joystick axes, accelerometer data and active-low C/Z button bits.
- Nominal joystick center is around 128, but actual center/travel vary. Calibrate rather than assume a full 0–255 usable span.
- The earlier wiring recommendation was to start bench testing the wired cable at 100 kHz. WiiBrew describes the native extension protocol as 400 kHz; the slower starting point is not a guarantee of compatibility. Verify the exact third-party controller, clock rate and initialization behavior.
- The accelerometer is available but not required by the proposed zoom controller.

Prior protocol research identified a common unencrypted initialization sequence: write 0x55 to register 0xF0, then 0x00 to 0xFB; request data by writing 0x00, wait as required and read six bytes. Treat this as a library/protocol starting point, not tested clone firmware. Legacy initialization and encrypted-report handling differ; do not combine incompatible decoding paths.

Sources/libraries to evaluate:

- [WiiBrew Nunchuck protocol](https://wiibrew.org/wiki/Wiimote/Extension_Controllers/Nunchuck)
- [WiiBrew extension initialization](https://wiibrew.org/wiki/Wiimote/Extension_Controllers#Identification)
- [Arduino WiiChuck](https://github.com/madhephaestus/WiiChuck)
- [Adafruit CircuitPython Nunchuk](https://github.com/adafruit/Adafruit_CircuitPython_Nunchuk)
- [Adafruit adapter guide](https://learn.adafruit.com/adafruit-wii-nunchuck-breakout-adapter)

No firmware platform, library version or clone compatibility has been selected/validated.

## Proposed mapping

- One stick axis commands signed zoom speed: center stopped, opposite deflections opposite directions.
- Z held = enable/dead-man.
- C = extra-slow mode.
- Neutral dead zone plus gentle acceleration and deceleration.
- Final axis direction, dead-zone width, speed curve and button mapping require user testing.

The encoder is required. The button mapping above is a recommendation, not an independently confirmed owner choice.

## Suggested implementation structure

This structure makes the earlier requirements concrete; control rates, thresholds and gains are intentionally not invented.

1. Boot with SLP and bridge inputs low.
2. Initialize I2C and encoder capture; establish a healthy input stream.
3. Calibrate center and require a deliberate enable action.
4. Convert calibrated joystick deflection into a signed speed target with dead zone and slow mode.
5. Rate-limit target changes and regulate measured encoder speed with a tuned control loop.
6. Enforce known-position travel limits only after valid initialization/calibration.
7. On stale/invalid input, enable release, stall or other fault, remove drive and return to a safe disabled state.
8. Validate unloaded before any lens-coupled tuning.

A PI/PID-style speed loop is a possible implementation choice, not a tuned design. Encoder counts-per-revolution, quadrature counting mode, gearbox ratio, sample period and saturation behavior must be derived from the selected parts. Do not copy gearing constants from the vendor encoder example.

## Feedback limitations

- Motor encoder counts are relative, not an absolute lens-position sensor.
- Motor/gearbox/pulley movement does not prove lens movement if the belt slips.
- Travel after a power cycle is unknown unless deliberately re-established.
- Stall detection, current limiting and soft travel limits complement one another; none alone proves lens protection.
- Do not automatically home by driving the lens into a hard stop.
- Stop/coast/brake behavior and fault thresholds remain engineering choices to test on the actual rig.
