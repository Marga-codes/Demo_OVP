import { chromium } from 'playwright';
import http from 'http'; import fs from 'fs'; import path from 'path';
const ROOT = new URL('../../ovp-demo-v4', import.meta.url).pathname;
const types = {'.html':'text/html','.css':'text/css','.js':'text/javascript','.webp':'image/webp','.png':'image/png'};
const srv = http.createServer((q, r) => { let f = path.join(ROOT, decodeURIComponent(q.url.split('?')[0].split('#')[0])); if (f.endsWith('/')) f += 'index.html';
  fs.readFile(f, (e, d) => { if (e) { r.writeHead(404); r.end(); return; } r.writeHead(200, {'content-type': types[path.extname(f)] || 'application/octet-stream'}); r.end(d); }); }).listen(4599);
const pages = process.argv[2].split(','); const widths = (process.argv[3] || '375,768,1280,1440').split(',').map(Number);
const out = process.argv[4] || new URL('./shots', import.meta.url).pathname;
fs.mkdirSync(out, {recursive: true});
const b = await chromium.launch();
for (const pg of pages) for (const w of widths) {
  const ctx = await b.newContext({viewport: {width: w, height: 900}, reducedMotion: 'reduce'}); const p = await ctx.newPage();
  const errs = []; p.on('console', m => { if (m.type() === 'error') errs.push(m.text()); }); p.on('pageerror', e => errs.push(e.message));
  await p.goto('http://localhost:4599/' + pg, {waitUntil: 'networkidle'}); await p.evaluate(async () => { for (let y = 0; y < document.body.scrollHeight; y += 600) { window.scrollTo(0, y); await new Promise(r => setTimeout(r, 60)); } window.scrollTo(0, 0); }); await p.waitForTimeout(400);
  const sw = await p.evaluate(() => document.documentElement.scrollWidth);
  const name = pg.replace(/\//g, '_').replace('.html', '') + '-' + w + '.png';
  await p.screenshot({path: path.join(out, name), fullPage: true});
  console.log(name, 'scrollW', sw, sw > w ? 'OVERFLOW' : 'ok', errs.length ? 'ERR ' + errs.join(' | ') : '');
  await ctx.close();
}
await b.close(); srv.close();
