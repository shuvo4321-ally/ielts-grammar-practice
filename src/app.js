(function () {
'use strict';
var $ = function (s, r) { return (r || document).querySelector(s); };
var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }

/* ================================================================ saved state (this browser only) */
var KEY = 'ielts-grammar-lab-v1';
var S = { a: {}, open: {} };
try { var raw = localStorage.getItem(KEY); if (raw) { var got = JSON.parse(raw); if (got.a) S.a = got.a; if (got.open) S.open = got.open; } } catch (e) {}
function save() { try { localStorage.setItem(KEY, JSON.stringify(S)); } catch (e) {} }

/* ================================================================ marking */
function norm(s) {
  return String(s).toLowerCase().replace(/[‘’]/g, "'").replace(/\s+/g, ' ').trim().replace(/[.!]+$/, '').trim();
}
function blank(v) { return v == null || v === '' || (typeof v === 'string' && !v.trim()); }
function mark(qa) {
  var kind = qa.dataset.kind, acc = JSON.parse(qa.dataset.acc), v = S.a[qa.dataset.q];
  if (blank(v)) return 'blank';
  if (kind === 'gap') return acc.some(function (a) { return norm(a) === norm(v); }) ? 'ok' : 'bad';
  if (kind === 'spot') return acc.indexOf(+v) >= 0 ? 'ok' : 'bad';
  return +v === acc ? 'ok' : 'bad';
}
function shown(qa) {
  var v = S.a[qa.dataset.q], kind = qa.dataset.kind;
  if (kind === 'pick') { var b = $('.ch[data-v="' + v + '"]', qa); return b ? b.textContent : ''; }
  if (kind === 'spot') { var t = $('.tok[data-t="' + v + '"]', qa); return t ? t.textContent : ''; }
  return v;
}
function badge(qa) {
  var st = mark(qa), res = $('.res', qa), y = $('.yours', qa);
  var cls = st === 'ok' ? 'r-ok' : 'r-bad';
  res.className = 'res ' + cls; res.textContent = st === 'ok' ? '✓ correct' : st === 'bad' ? '✗ wrong' : 'not answered';
  y.hidden = false; y.className = 'yours ' + cls;
  y.innerHTML = st === 'blank' ? 'You did not answer this one.' :
    (qa.dataset.kind === 'spot' ? 'You tapped: <b>' : 'Your answer: <b>') + esc(shown(qa)) + '</b>. ' + (st === 'ok' ? 'Correct.' : 'Not correct.');
  if (qa.dataset.kind === 'spot') JSON.parse(qa.dataset.acc).forEach(function (i) { var e = $('.tok[data-t="' + i + '"]', qa); if (e) e.classList.add('err'); });
}
function unbadge(qa) {
  var res = $('.res', qa); res.className = 'res'; res.textContent = ''; $('.yours', qa).hidden = true;
  $$('.tok.err', qa).forEach(function (t) { t.classList.remove('err'); });
}
function paint(qa) {
  var v = S.a[qa.dataset.q];
  $$('.ch', qa).forEach(function (b) { b.classList.toggle('on', !blank(v) && b.dataset.v === String(v)); });
  $$('.tok', qa).forEach(function (b) { b.classList.toggle('on', !blank(v) && b.dataset.t === String(v)); });
  var inp = $('.ain', qa); if (inp) inp.value = v == null ? '' : v;
}
function refresh(qa) { if ($('details.afold', qa).open) badge(qa); }

var QAS = $$('.qa[data-q]');
QAS.forEach(function (qa) { paint(qa); if (S.open[qa.dataset.q]) { $('details.afold', qa).open = true; badge(qa); } });

document.addEventListener('click', function (e) {
  var b = e.target.closest && e.target.closest('.qa .ch, .qa .tok'); if (!b) return;
  var qa = b.closest('.qa'), id = qa.dataset.q, v = b.dataset.v != null ? b.dataset.v : b.dataset.t;
  S.a[id] = String(S.a[id]) === v ? '' : +v;
  save(); paint(qa); refresh(qa); updateToc();
});
document.addEventListener('input', function (e) {
  var t = e.target; if (!t.classList || !t.classList.contains('ain')) return;
  var qa = t.closest('.qa'); S.a[qa.dataset.q] = t.value; save(); refresh(qa); updateToc();
});
document.addEventListener('toggle', function (e) {
  var d = e.target; if (!d.classList || !d.classList.contains('afold')) return;
  var qa = d.closest('.qa'), id = qa.dataset.q;
  if (d.open) { S.open[id] = true; badge(qa); } else { delete S.open[id]; unbadge(qa); }
  save(); updateToc();
}, true);

/* ================================================================ per-unit buttons */
document.addEventListener('click', function (e) {
  var b = e.target.closest && e.target.closest('[data-showall], [data-clear]'); if (!b) return;
  var sec = document.getElementById(b.dataset.showall || b.dataset.clear);
  $$('.qa[data-q]', sec).forEach(function (qa) {
    var d = $('details.afold', qa);
    if (b.dataset.showall) { d.open = true; }
    else { delete S.a[qa.dataset.q]; delete S.open[qa.dataset.q]; paint(qa); d.open = false; unbadge(qa); }
  });
  save(); updateToc();
});

/* ================================================================ contents status + error-hunt score */
function updateToc() {
  $$('.sheetpage.unit').forEach(function (sec) {
    var el = document.getElementById('toc-' + sec.id); if (!el) return;
    var qs = $$('.qa[data-q]', sec), opened = qs.filter(function (qa) { return S.open[qa.dataset.q]; });
    var ok = opened.filter(function (qa) { return mark(qa) === 'ok'; }).length;
    el.textContent = opened.length === qs.length ? ok + '/' + qs.length + ' correct' : '';
  });
  $$('.sheetpage.hunt').forEach(function (sec) {
    var hunt = $$('.qa[data-q]', sec), done = hunt.filter(function (qa) { return S.open[qa.dataset.q]; });
    var hok = done.filter(function (qa) { return mark(qa) === 'ok'; }).length;
    var ts = document.getElementById('toc-' + sec.id); if (ts) ts.textContent = done.length ? hok + '/' + done.length + ' correct' : '';
    var hs = $('.huntscore', sec); if (!hs) return;
    if (done.length < hunt.length) { hs.innerHTML = ''; return; }
    var missed = hunt.filter(function (qa) { return mark(qa) !== 'ok'; });
    var units = {};
    missed.forEach(function (qa) { var a = $('.unitref', qa); if (a) units[a.getAttribute('href')] = a.textContent.replace('→ ', ''); });
    hs.innerHTML = '<div class="result"><div class="rscore"><div class="big">' + hok + '<span>/' + hunt.length + '</span></div><div>' +
      (sec.id === 'shunt' ? 'misspelled words found' : 'errors found') + '</div></div>' +
      (missed.length ? '<p style="margin:0"><b>Your checklist.</b> Go back to these units, then check for these errors in your next essay:</p><p style="margin:0">' +
        Object.keys(units).map(function (h) { return '<a href="' + h + '">' + esc(units[h]) + '</a>'; }).join('<br>') + '</p>'
        : '<p style="margin:0"><b>All ' + hunt.length + ' found.</b> Your accuracy on these points is at band 8–9 level.</p>') + '</div>';
  });
}
updateToc();

var totop = $('#totop');
function tt() { totop.hidden = window.scrollY < 900; }
window.addEventListener('scroll', tt, { passive: true }); tt();
})();
