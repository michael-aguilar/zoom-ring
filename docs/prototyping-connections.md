# Temporary connections before soldering

The question was whether an unsoldered XIAO has an electronics equivalent of a temporary rivet/cleco for initial verification.

## Options researched

| Option | Practical use | Limits |
| --- | --- | --- |
| Pogo/spring test pins | A printed cradle and clamp can press contacts against pads without soldering to the board | Pins do not latch like clecos; alignment and pressure need a fixture, wires still attach to the fixture |
| Micro-grabber test clips | A few temporary signals | A whole set around a small XIAO is awkward; no particular clip-to-pad fit was verified |
| Pre-soldered headers plus solderless breadboard | Recommended for testing the whole controller | Adds height; other components may still need suitable connections/soldering |

Sources:

- [Adafruit pogo-pin example #2430](https://www.adafruit.com/product/2430)
- [Seeed pre-soldered XIAO RP2040](https://www.seeedstudio.com/Seeed-Studio-XIAO-RP2040-Pre-Soldered-p-6333.html), historically $4.99 on 2026-10-15

If a bare board is already available, soldering only the header strips provides the same removable jumper-wire flexibility. Ownership of a bare board was not confirmed.

Do not simply push ordinary loose header pins into unsoldered holes and assume reliable contact. They are not specified as press-fit electrical connections; intermittent contacts make system tests misleading.

For final compact assembly, a bare board and direct soldered wiring remain a packaging option. That is different from the later breadboard-testing recommendation. No fixture, clip fit or full solderless assembly has been built or verified.
