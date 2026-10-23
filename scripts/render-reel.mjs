// Records an animated reel page (e.g. reels/01-channel-promo/promo.html) to numbered PNG frames.
// The page must define window.DURATION, window.ASSETS, window.init(assets), window.render(t), window.snapshot().
// Usage: node scripts/render-reel.mjs <page.html> <framesDir> [fps=30] [previewTimes, e.g. 1,4.2,10.5]
// With previewTimes, only those moments are rendered (for checking layout before a full render).
import fs from 'node:fs';
import path from 'node:path';
import { pathToFileURL } from 'node:url';
import puppeteer from 'puppeteer-core';

const [pageArg, outArg, fpsArg = '30', previewArg] = process.argv.slice(2);
if (!pageArg || !outArg) {
  console.error('Usage: node scripts/render-reel.mjs <page.html> <framesDir> [fps=30]');
  process.exit(1);
}
const fps = Number(fpsArg);
const pagePath = path.resolve(pageArg);
const outDir = path.resolve(outArg);
fs.rmSync(outDir, { recursive: true, force: true });
fs.mkdirSync(outDir, { recursive: true });

const edge = [
  'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',
  'C:/Program Files/Microsoft/Edge/Application/msedge.exe',
].find(fs.existsSync);
if (!edge) throw new Error('Microsoft Edge not found');

const browser = await puppeteer.launch({ executablePath: edge, headless: true });
try {
  const page = await browser.newPage();
  await page.goto(pathToFileURL(pagePath).href);

  // Assets are inlined as data URLs so the canvas is never tainted by file:// images.
  const assets = await page.evaluate(() => window.ASSETS || {});
  const inlined = {};
  for (const [key, rel] of Object.entries(assets)) {
    const file = path.resolve(path.dirname(pagePath), rel);
    const mime = file.endsWith('.png') ? 'image/png' : 'image/jpeg';
    inlined[key] = `data:${mime};base64,${fs.readFileSync(file).toString('base64')}`;
  }
  await page.evaluate(a => window.init(a), inlined);

  const duration = await page.evaluate(() => window.DURATION);
  const times = previewArg
    ? previewArg.split(',').map(Number)
    : Array.from({ length: Math.round(duration * fps) }, (_, f) => f / fps);
  const total = times.length;
  for (let f = 0; f < total; f++) {
    const dataUrl = await page.evaluate(t => { window.render(t); return window.snapshot(); }, times[f]);
    const name = previewArg ? `preview_t${times[f]}.png` : `frame_${String(f).padStart(5, '0')}.png`;
    fs.writeFileSync(path.join(outDir, name), Buffer.from(dataUrl.split(',')[1], 'base64'));
    if (f % 60 === 0) console.log(`frame ${f}/${total}`);
  }
  console.log(`done: ${total} frames in ${outDir}`);
} finally {
  await browser.close();
}
