# Diagram bundle

## Main visual

- [zoom-wiring-unified.png](zoom-wiring-unified.png), 2160 × 1440
- [zoom-wiring-unified.svg](zoom-wiring-unified.svg), editable vector export
- [zoom-wiring-unified.html](zoom-wiring-unified.html), standalone browser viewer

Each physical component is shown once. Dots join wires; bridges cross without joining. Functional pin placement is not a board footprint.

## Supporting originals

- [zoom-wiring-v1.png](zoom-wiring-v1.png), 1600 × 2370, earlier segmented version
- [zoom-wiring-v1.svg](zoom-wiring-v1.svg)
- [zoom-wiring-v1.html](zoom-wiring-v1.html)
- [zoom-wiring-checks.txt](zoom-wiring-checks.txt), original documentation review and caveats
- [zoom-wiring-netlist.json](zoom-wiring-netlist.json), connection inventory
- [artifact-manifest.json](artifact-manifest.json), original-file SHA-256 values

The eight original exports/check artifacts were imported unchanged. The manifest is an integrity record, not an electrical test. If a later design intentionally changes these files, document the revision rather than continuing to claim their original hashes apply.

## Regenerate on macOS/Linux

Requirements: Python 3, Node.js and npm. From repository root:

```sh
npm ci
npm run diagrams
```

This runs both portable Python SVG/HTML generators, then renders both PNGs with the included Noto Sans fonts and pinned resvg WebAssembly renderer. It does not control hardware.

For only editable vector/browser exports, no npm dependencies are needed:

```sh
python3 scripts/make_diagram.py
python3 scripts/make_unified.py
```

The generators now use paths relative to this checkout, not the original assistant workspace. PNG rendering dependencies and fonts are local; do not commit node_modules.

The original font-fetch preparation script only downloaded fonts and rewrote a font family in the earlier one-off workflow. It is unnecessary here because the fonts and portable generators are included.

Source scripts describe the same exact reference circuit as the original exports. Changes to the design must keep diagrams, netlist and prose consistent.
