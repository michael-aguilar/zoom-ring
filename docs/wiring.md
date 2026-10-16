# Reference wiring and electrical checks

Documentation-reviewed 2026-10-15. Not bench-tested.

Exact reference: standard Seeed XIAO RP2040, Adafruit DRV8833 #3297, Adafruit encoder motor #4639 and a wired Nunchuck.

Use the [unified diagram](diagrams/zoom-wiring-unified.png) as the main visual. It is a functional connection map, not physical connector/pad placement. Original [check notes](diagrams/zoom-wiring-checks.txt) and [netlist](diagrams/zoom-wiring-netlist.json) are retained unchanged.

## Connections

| Function | XIAO / source | Destination |
| --- | --- | --- |
| Main +5 V | Switched regulated USB +5 V | Parallel branches to XIAO 5V, DRV8833 VM, C1 positive |
| Common ground | USB ground | XIAO GND, driver GND, Nunchuck GND, encoder blue, C1 negative |
| Logic power | XIAO 3V3 | Nunchuck VCC, encoder black, pull-up tops |
| I2C data | D4 / GP6 | Nunchuck SDA; optional R1 to 3V3 |
| I2C clock | D5 / GP7 | Nunchuck SCL; optional R2 to 3V3 |
| Bridge input 1 | D6 / GP0 | DRV8833 AIN1 |
| Bridge input 2 | D7 / GP1 | DRV8833 AIN2 |
| Driver enable | D0 / GP26 | DRV8833 SLP |
| Encoder channel | D2 / GP28 | Motor yellow |
| Encoder channel | D3 / GP29 | Motor green |
| Motor terminal 1 | DRV8833 AOUT1 | Motor red |
| Motor terminal 2 | DRV8833 AOUT2 | Motor white |
| Brush suppression | C2, 100 nF ceramic | Across motor red/white |

Motor colors apply only to #4639. Signal A/B naming/direction must be checked in an unloaded test.

## Power and logic

- XIAO GPIO is 3.3 V only.
- Driver inputs accept 3.3 V logic at the reference 5 V motor supply.
- #4639 motor supply is specified as 4.5–6 V; encoder supply 3–5 V. Encoder is powered at 3.3 V here.
- Motor current branches before the XIAO, not through its 3.3 V output.
- All grounds are common.
- C1 is 470 µF, at least 10 V, with positive to VM and negative to GND, near the driver.
- C2 is 100 nF ceramic across the motor terminals, not a motor-to-ground connection.
- Do not connect external 5 V and PC programming USB simultaneously to the standard XIAO. Disconnect external power before programming; do not run the motor from the PC USB port in that arrangement.
- The driver's VM solder pad is not reverse-polarity protected. Its separate VMotor/terminal input is protected. The diagram specifically labels VM.
- Verify USB-pack idle auto-shutoff, voltage droop, regulator capacity, motor noise and actual current budget.

## I2C and encoder inputs

- D4/GP6 and D5/GP7 are SDA/SCL on the RP2040's **I2C1** controller. Seeed's XIAO wiki labels them SDA0/SCL0 ("I2C0"), but the RP2040 GPIO function table assigns GPIO6/GPIO7 to I2C1. Use `I2C(1, ...)` in MicroPython and `i2c1` in the Pico SDK; with an Arduino core, confirm which `Wire` instance the board variant maps to D4/D5. The physical connections are unchanged.
- Nominal 4.7 kΩ pull-ups from SDA/SCL to 3.3 V are shown. Count any fitted adapter/controller pull-ups; do not blindly parallel multiple strong sets.
- The owner has chosen Adafruit adapter #4836 instead of cutting the cable. Per Adafruit's pinout page it has 10 kΩ pull-ups on SDA and SCL, an onboard regulator and level-shifted I2C lines, and VIN should be the host's logic level. For the XIAO, feed VIN from 3V3 and wire SDA/SCL/GND to the breakout pins. Start without the external 4.7 kΩ resistors; add them only if the bus is unreliable on the bench. The diagram still shows a generic Nunchuck and has not been redrawn for the adapter.
- Start the wired Nunchuck at 100 kHz. Clone cable colors, initialization and behavior vary.
- Configure D2/GP28 and D3/GP29 as digital encoder inputs with pull-ups, matching the referenced vendor example. This does not transfer its gearing constants into this project.
- Determine positive motor/encoder direction on the detached motor before closing a feedback loop.

## Startup and unused channel

Initialize AIN1/AIN2 and SLP low. SLP high enables the driver only after valid input and an intentional enable condition. The reference driver has an internal SLP pull-down.

Unused B outputs, BIN1/BIN2 and FLT were left unconnected in the reviewed setup; B inputs have internal pull-downs. Current-sense components remain fitted unless deliberately changed. No fault-monitoring circuit or firmware has been implemented here.

## Current limiting

The reference board's stock A-channel Rsense is 0.2 Ω, yielding a nominal 1 A trip/current-limit setting. That is not a verified torque limit for the lens.

Nominal relationship:

`I_limit = 0.2 V / R_sense`

A 1.0 Ω replacement gives nominal 0.2 A as an arithmetic example, not a certified motor- or lens-safe setting. Account for resistor power rating, tolerance, actual current regulation and chosen motor behavior.

Replace the appropriate sense resistor to lower the limit. Adding a resistor in parallel lowers effective resistance and raises the limit. Keep the sense bypass jumper open.

**With motor #4639 the stock limit never acts.** Adafruit lists the motor at about 100 mA running and 200 mA stalled. The stock 1 A limit is five times the stall current, so the driver will not limit current at any load this motor can produce. Even the 1.0 Ω example (nominal 0.2 A) sits at the stall figure and would at most just trip. With this motor, the force on the lens is bounded by motor stall torque multiplied by the pulley ratio, not by the driver. Lens protection therefore depends on firmware stall detection, soft travel limits and mechanical compliance (for example belt slip). A limit below stall would need R_sense above 1 Ω. Whether a limit that close to running current regulates smoothly is untested. These figures are vendor nominal values. The voltage behind the 200 mA figure is not stated, and stall current at the 5 V supply has not been measured.

## Limits of the check

Documentation review establishes the reference connection intent, not loaded torque suitability, hardware assembly quality, current-limit effectiveness, reliable clone support or successful firmware. An encoder does not detect belt slip or automatically establish absolute lens position after startup. Do not home by blindly pushing into lens end stops.

Primary references are in [sources](sources.md).

## Revisions after the original check

The original [check notes](diagrams/zoom-wiring-checks.txt) are kept unchanged and still match their manifest hash. This page supersedes them on the following points:

- 2026-10-15: the check notes say D4/D5 are "I2C0", following Seeed's labels. The RP2040 controller is I2C1 (see above). Pins and diagram are unaffected.
- 2026-10-15: the check notes call the stock 1 A limit inappropriate and give 1.0 Ω / 0.2 A as an example. Against the motor's listed 200 mA stall current, neither setting limits #4639 in practice (see Current limiting).
