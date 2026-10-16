const fs = require('node:fs');
const path = require('node:path');
const { Resvg, initWasm } = require('@resvg/resvg-wasm');

(async () => {
  const root = path.resolve(__dirname, '..');
  const diagrams = path.join(root, 'docs', 'diagrams');
  const fonts = path.join(root, 'assets', 'fonts');
  const wasm = path.join(path.dirname(require.resolve('@resvg/resvg-wasm')), 'index_bg.wasm');
  await initWasm(fs.readFileSync(wasm));
  for (const name of ['zoom-wiring-v1', 'zoom-wiring-unified']) {
    const rendered = new Resvg(fs.readFileSync(path.join(diagrams, name + '.svg')), {
      font: {
        fontBuffers: [
          fs.readFileSync(path.join(fonts, 'NotoSans-Regular.ttf')),
          fs.readFileSync(path.join(fonts, 'NotoSans-Bold.ttf')),
        ],
        defaultFontFamily: 'Noto Sans',
      },
    }).render();
    fs.writeFileSync(path.join(diagrams, name + '.png'), rendered.asPng());
    console.log(name + ': ' + rendered.width + ' × ' + rendered.height);
  }
})().catch(error => {
  console.error(error.message);
  process.exitCode = 1;
});
