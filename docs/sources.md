# Sources and product links

Research snapshot: 2026-10-15; historical gimbal comparisons: 2026-10-09.

Links identify the evidence used in the earlier research. They are not a promise of current prices, stock, unchanged page contents or hardware compatibility. Original wording is summarized rather than copying complete vendor pages.

## MCU

- [Seeed standard XIAO RP2040 product](https://www.seeedstudio.com/XIAO-RP2040-v1-0-p-5026.html): compact controller candidate and historical $3.99 listing.
- [Seeed XIAO RP2040 documentation](https://wiki.seeedstudio.com/XIAO-RP2040/): pin map, GPIO capability, power and USB/external-power warning. Its "I2C0" label for D4/D5 conflicts with the RP2040 datasheet; see below.
- [RP2040 datasheet](https://datasheets.raspberrypi.com/rp2040/rp2040-datasheet.pdf), GPIO function table: GPIO6/GPIO7 are I2C1 SDA/SCL.
- [Seeed XIAO ESP32C3 documentation](https://wiki.seeedstudio.com/XIAO_ESP32C3_Getting_Started/): alternate same-footprint family, not a requirement.
- [Seeed pre-soldered XIAO RP2040](https://www.seeedstudio.com/Seeed-Studio-XIAO-RP2040-Pre-Soldered-p-6333.html): header-equipped prototype option, historical $4.99.

## Motor driver and encoder example

- [Adafruit DRV8833 #3297](https://www.adafruit.com/product/3297): reference board, historical $5.95.
- [Adafruit driver guide](https://learn.adafruit.com/adafruit-drv8833-dc-stepper-motor-driver-breakout-board): overview.
- [Driver pinouts/current limit/sleep](https://learn.adafruit.com/adafruit-drv8833-dc-stepper-motor-driver-breakout-board/pinouts): logic, power input distinction, sense-resistor calculation, SLP.
- [Vendor encoder input example](https://github.com/adafruit/Adafruit_Motor_Shield_V2_Library/blob/master/examples/encoderMotorRPM/encoderMotorRPM.ino): pull-up configuration reference only. Its unrelated motor/gearing constants are not project constants.

## Encoder motors

- [Adafruit motor #4639](https://www.adafruit.com/product/4639): reference motor's wire colors, 100:1 gearbox and supply ranges; historical $12.50. Rechecked 2026-10-15: about 100 mA running / 200 mA stall listed, and the 1:100 version was shown out of stock. Torque and speed per ratio come from the page's [ratio table image](https://cdn-shop.adafruit.com/product-files/4640/n20_6V_200mW_table.png) (read 2026-10-19; 1:100 = 0.40 kg·cm rated, 0.7 kg·cm stall). [Datasheet](https://cdn-shop.adafruit.com/product-files/4639/n20+motors_C15011+6V.pdf).
- [Amazon uxcell B07N1FT75P](https://www.amazon.com/dp/B07N1FT75P): indexed alternative. Read 2026-10-19: $18.49, 5 in stock, 6 V 100 rpm, 3 mm D-shaft, no torque listed; black = encoder negative, blue = encoder positive.
- [DFRobot FIT0484](https://www.dfrobot.com/product-1434.html): 6 V 105 RPM 150:1 candidate, historical $11.90. Read 2026-10-19: out of stock; 1.0 kg·cm rated at 60 rpm, 2.2 kg·cm instant torque; encoder voltage not listed.
- [Pololu #5146 specifications](https://www.pololu.com/product/5146/specs): premium 6 V 73 RPM 298:1 candidate, historical $29.95, cable separate. Read 2026-10-19: 2.4 kg·cm theoretical stall, 0.67 A stall, 12 CPR encoder; Pololu warns stalls can damage the gearbox.

## Nunchuck

- [Adafruit connector adapter #4836](https://www.adafruit.com/product/4836): owner-selected no-cut adapter, historical $2.95.
- [Adafruit adapter guide](https://learn.adafruit.com/adafruit-wii-nunchuck-breakout-adapter): host interface and connector approach.
- [Adapter pinouts](https://learn.adafruit.com/adafruit-wii-nunchuck-breakout-adapter/pinouts): reference wiring; 10 kΩ SDA/SCL pull-ups, regulator, level-shifted I2C, VIN at host logic level (checked 2026-10-15).
- [WiiBrew Nunchuck protocol](https://wiibrew.org/wiki/Wiimote/Extension_Controllers/Nunchuck): report structure, axes and active-low buttons.
- [WiiBrew extension identification](https://wiibrew.org/wiki/Wiimote/Extension_Controllers#Identification): initialization/protocol background.
- [Arduino WiiChuck](https://github.com/madhephaestus/WiiChuck): candidate library, not tested in this project.
- [Adafruit CircuitPython Nunchuk](https://github.com/adafruit/Adafruit_CircuitPython_Nunchuk): candidate library, not selected/tested.

## Camera power

- [Canon EOS R10 USB external power](https://cam.start.canon/en/C006/manual/html/UG-11_Reference_0030.html): power input, not established DIY motor output.
- [Canon EOS R10 multifunction shoe](https://cam.start.canon/en/C006/manual/html/UG-01_Preparations_0080.html): supported accessory context, not approval for a DIY motor tap.

## Temporary connections

- [Adafruit pogo pins #2430](https://www.adafruit.com/product/2430): example spring-contact approach, not a verified complete XIAO fixture.
- Header-equipped XIAO link is above. No specific micro-grabber model-to-pad fit was verified.

## Historical/deferred gimbals

- [MPB DJI Ronin-SC SKU 4223416](https://www.mpb.com/en-us/product/dji-ronin-sc/sku-4223416): historical October 9 $88 listing.
- [MPB Zhiyun Crane 2 SKU 4106623](https://www.mpb.com/en-us/product/zhiyun-crane-2-gimbal-/sku-4106623): historical October 9 $146 listing.
- The archived discussion is not an instruction to purchase a gimbal or resume pan/tilt work.

## Diagram fonts

- [Noto Sans font files](https://github.com/notofonts/noto-fonts/tree/main/hinted/ttf/NotoSans)
- [Noto font license](https://github.com/notofonts/noto-fonts/blob/main/LICENSE)
- A copy of the SIL Open Font License is included with the bundled fonts. See [third-party notices](../THIRD_PARTY_NOTICES.md).
