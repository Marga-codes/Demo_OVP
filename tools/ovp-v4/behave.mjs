import { chromium } from 'playwright'; import http from 'http'; import fs from 'fs'; import path from 'path';
const ROOT = new URL('../../ovp-demo-v4', import.meta.url).pathname; const T={'.html':'text/html','.css':'text/css','.js':'text/javascript','.webp':'image/webp','.png':'image/png'};
const srv=http.createServer((q,r)=>{let f=path.join(ROOT,decodeURIComponent(q.url.split('?')[0].split('#')[0]));fs.readFile(f,(e,d)=>{if(e){r.writeHead(404);r.end();return;}r.writeHead(200,{'content-type':T[path.extname(f)]||'x'});r.end(d);});}).listen(4598);
const b=await chromium.launch(); const errs=[];
const S = new URL('./shots/', import.meta.url).pathname;
// desktop keyboard submenu
let p=await b.newPage({viewport:{width:1280,height:900}}); p.on('pageerror',e=>errs.push(e.message)); p.on('console',m=>m.type()==='error'&&errs.push(m.text()));
await p.goto('http://localhost:4598/index.html');
await p.keyboard.press('Tab'); console.log('1st tab:', await p.evaluate(()=>document.activeElement.textContent.trim()));
await p.keyboard.press('Tab'); await p.keyboard.press('Tab'); await p.keyboard.press('Tab');
console.log('focused:', await p.evaluate(()=>document.activeElement.className));
await p.keyboard.press('Enter'); console.log('expanded:', await p.getAttribute('.sub-toggle','aria-expanded'), 'visible:', await p.isVisible('#sub-services'));
await p.screenshot({path:S+'submenu.png',clip:{x:0,y:0,width:1280,height:420}});
await p.keyboard.press('Tab'); console.log('next focus:', await p.evaluate(()=>document.activeElement.textContent.trim().slice(0,30)));
await p.keyboard.press('Escape'); console.log('after esc:', await p.getAttribute('.sub-toggle','aria-expanded'), await p.evaluate(()=>document.activeElement.className));
await p.mouse.wheel(0,600); await p.waitForTimeout(200); console.log('scrolled class:', await p.getAttribute('.site-header','class'));
// contact form
await p.goto('http://localhost:4598/contact.html');
await p.click('button[type=submit]'); console.log('focus after empty submit:', await p.evaluate(()=>document.activeElement.id), '| name err:', await p.textContent('#name-err'));
await p.screenshot({path:S+'form-errors.png',fullPage:false,clip:{x:0,y:250,width:700,height:500}});
await p.fill('#name','Test'); await p.fill('#email','bad'); await p.locator('#email').blur(); console.log('email err:', await p.textContent('#email-err'));
await p.fill('#email','a@b.gov'); await p.selectOption('#sector','Government'); await p.fill('#message','Hi'); await p.check('#consent');
let posted=false; p.on('request',r=>{ if(r.method()==='POST') posted=true; });
await p.click('button[type=submit]'); await p.waitForTimeout(200);
console.log('status visible:', await p.isVisible('.form-status'), 'POST sent:', posted, 'url:', p.url());
// mobile menu
const m=await b.newPage({viewport:{width:375,height:800}}); m.on('pageerror',e=>errs.push(e.message));
await m.goto('http://localhost:4598/services/leadership-change.html'); await m.click('.menu-toggle');
console.log('mobile menu open:', await m.isVisible('#site-nav'), await m.getAttribute('.menu-toggle','aria-label'));
await m.click('.sub-toggle'); await m.screenshot({path:S+'mobile-menu.png'});
await m.keyboard.press('Escape'); await m.keyboard.press('Escape'); console.log('closed:', !(await m.isVisible('#site-nav')));
// targets < 44px
const small=await m.evaluate(()=>[...document.querySelectorAll('a,button,input,select,summary')].filter(e=>{const r=e.getBoundingClientRect();return r.width>0&&(r.height<24||r.width<24)}).map(e=>e.outerHTML.slice(0,80)));
console.log('targets <24px:', small.length, small.slice(0,5));
console.log('ERRORS', errs);
await b.close(); srv.close();
