# Electronics BOM and component research

All prices below were observed or estimated during 2026-10-15 research, before shipping/tax. Availability and prices must be rechecked before buying. Candidate parts are not a purchase record.

## Minimum practical electronics

| Qty | Item | Candidate / historical price | Notes |
| --- | --- | --- | --- |
| 1 | Wired Wii Nunchuck | Generic third-party unit, estimated $10–15 | Verify pinout, initialization and I2C behavior |
| 1 | Compact 3.3 V MCU | [Standard XIAO RP2040](https://www.seeedstudio.com/XIAO-RP2040-v1-0-p-5026.html), $3.99 | 21 × 17.8 mm, 11 GPIO, USB-C |
| 1 | Encoder-equipped geared DC motor | Shortlist below | Quadrature feedback required |
| 1 | Motor driver | [Adafruit DRV8833 #3297](https://www.adafruit.com/product/3297), about $6 | Reference wiring uses channel A |
| 1 | Regulated USB 5 V battery supply | Estimated $10–20 | At least 1 A was the prototype recommendation, not a finalized power budget |
| 1 | Power switch | Suitable for supply/motor current | Switch +5 V before parallel branches |
| 1 | Bulk capacitor | 470 µF, at least 10 V | Polarized, close to driver |
| 1 | Motor noise capacitor | 100 nF ceramic | Across the two motor terminals, close to motor |
| Up to 2 | I2C pull-up resistors | Nominal 4.7 kΩ | Only if needed; account for existing pull-ups |
| 1 | A-channel current-sense resistor replacement | Value to be selected | Stock nominal 1 A limit is not established lens protection |
| As needed | Wiring, connectors, strain relief, USB power breakout/cable | Earlier allowance about $5–10 for assembly bits | Actual adapter/cable choices not finalized |
| 1 | [Nunchuck adapter #4836](https://www.adafruit.com/product/4836) | $2.95 | Owner-selected 2026-10-15 instead of cutting the cable. Has 10 kΩ I2C pull-ups, so the separate pull-ups are likely unnecessary |
| Prototype alternative | [XIAO RP2040 with pre-soldered headers](https://www.seeedstudio.com/Seeed-Studio-XIAO-RP2040-Pre-Soldered-p-6333.html) | $4.99 | Same basic controller with easier removable test connections |

The electronics-only total has not been finalized. Earlier $80–120 and later $70–130 whole-prototype estimates included mechanical items and broad allowances; do not treat either as a current electronics quote.

## Encoder motor shortlist

| Candidate | Published / discussed configuration | Historical price | Why considered / unresolved |
| --- | --- | --- | --- |
| [Adafruit #4639](https://www.adafruit.com/product/4639) | 6 V N20 with 100:1 gearbox and encoder; motor supply 4.5–6 V, encoder 3–5 V | $12.50 | Preferred documented low-cost reference. Supports the 5 V motor/3.3 V encoder arrangement. Lens suitability unmeasured |
| [uxcell GA12-N20, Amazon B07N1FT75P](https://www.amazon.com/dp/B07N1FT75P) | Indexed as 6 V, 100 RPM with encoder and 3 mm D-shaft | Unverified | Amazon convenience. Direct price/stock and encoder voltage could not be verified |
| [DFRobot FIT0484](https://www.dfrobot.com/product-1434.html) | 6 V, 105 RPM, 150:1, encoder cable mentioned | $11.90 | Cheap alternative. Conflicting stock metadata; verify its own encoder supply/pinout |
| [Pololu #5146](https://www.pololu.com/product/5146/specs) | 298:1 MP 6 V micro metal gearmotor with encoder, 73 RPM no load | $29.95, cable extra | Original premium example; detailed specifications, not a sized selection |

100:1 is a gearbox reduction ratio, not 100 RPM. No-load speed at 6 V is not loaded speed at the proposed 5 V supply.

Sizing against the 2026-10-19 zoom-ring measurement (about 2.1 kg·cm peak) is in [mechanics and power](mechanics-and-power.md#motor-sizing-against-the-measurement). In short: #4639 at 1:100 is marginal; Pololu #5146 at about 4:1 or an N20 1:298 at about 6:1 fits with margin. On 2026-10-19 the uxcell listing showed $18.49 with 5 in stock, listed no torque, and gave black = encoder negative, blue = encoder positive (the reverse of #4639). DFRobot FIT0484 showed out of stock.

Do not reuse the Adafruit motor's wire colors, pull-up assumptions or voltage compatibility for another motor without checking that specific product.

## MCU comparison

- Raspberry Pi Pico was the initial example: roughly 51 × 21 mm and estimated $5–8.
- Standard XIAO RP2040 recommendation: 21 × 17.8 mm, roughly one-third the Pico board area, 3.3 V logic, enough I2C/PWM/encoder connections, listed $3.99.
- XIAO ESP32C3 has the same nominal footprint. ESP32 is not needed for wired control and is not smaller within that comparison.
- This was not an exhaustive search proving the absolute smallest possible MCU board.
- A Pi Zero, Linux, wireless radio and gimbal are not needed for the current zoom-only concept.
- Bare pads/direct wires minimize final height; pre-soldered headers simplify temporary breadboard testing. See [connection options](prototyping-connections.md).

## Selection gates

Choose a motor only after establishing ring resistance, travel and target sweep time, then accounting for pulley ratio, efficiency, backlash and loaded low-speed smoothness. Also confirm stall current/current limit, shaft dimensions, encoder resolution, cable and packaging.
