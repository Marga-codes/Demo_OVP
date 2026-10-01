(function () {
var d = document, $ = function (s) { return d.querySelectorAll(s); };
d.documentElement.classList.add('js');
var header = d.querySelector('.site-header');
var onScroll = function () { header.classList.toggle('is-scrolled', scrollY > 8); };
onScroll(); addEventListener('scroll', onScroll, { passive: true });
var nav = d.getElementById('site-nav'), btn = d.querySelector('.menu-toggle');
function setMenu(open) {
  btn.setAttribute('aria-expanded', open);
  btn.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
  [nav, header].forEach(function (el) { el.classList.toggle('is-open', open); });
  d.body.classList.toggle('menu-open', open);
  $('main, .site-footer').forEach(function (el) { el.inert = open; });
}
btn.onclick = function () { setMenu(btn.getAttribute('aria-expanded') !== 'true'); };
function sub(b, open) {
  b.setAttribute('aria-expanded', open);
  d.getElementById(b.getAttribute('aria-controls')).classList.toggle('is-open', open);
}
$('.sub-toggle').forEach(function (b) {
  b.onclick = function () { sub(b, b.getAttribute('aria-expanded') !== 'true'); };
});
d.addEventListener('click', function (e) {
  if (!e.target.closest('.has-sub')) $('.sub-toggle').forEach(function (b) { sub(b, false); });
});
d.addEventListener('keydown', function (e) {
  if (e.key !== 'Escape') return;
  var open = d.querySelector('.sub-toggle[aria-expanded="true"]');
  if (open) { sub(open, false); open.focus(); }
  else if (nav.classList.contains('is-open')) { setMenu(false); btn.focus(); }
});
var items = $('.reveal');
if ('IntersectionObserver' in window && !matchMedia('(prefers-reduced-motion: reduce)').matches) {
  var io = new IntersectionObserver(function (es) {
    es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('is-visible'); io.unobserve(e.target); } });
  }, { rootMargin: '0px 0px -8% 0px' });
  items.forEach(function (el) { io.observe(el); });
} else items.forEach(function (el) { el.classList.add('is-visible'); });
$('form[data-local]').forEach(function (form) {
  var fields = form.querySelectorAll('[required]');
  function check(el) {
    var bad = !el.checkValidity(), msg = d.getElementById(el.getAttribute('aria-describedby'));
    el.setAttribute('aria-invalid', bad);
    if (msg) msg.textContent = bad ? msg.getAttribute('data-msg') : '';
    return !bad;
  }
  fields.forEach(function (el) {
    el.addEventListener('blur', function () { if (el.value || el.type === 'checkbox') check(el); });
    el.addEventListener('input', function () { if (el.getAttribute('aria-invalid') === 'true') check(el); });
  });
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var first = [].filter.call(fields, function (el) { return !check(el); })[0];
    if (first) return first.focus();
    form.reset();
    fields.forEach(function (el) { el.removeAttribute('aria-invalid'); });
    var s = form.querySelector('.form-status'); s.hidden = false; s.focus();
  });
});
})();
