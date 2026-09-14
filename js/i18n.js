(function () {
  'use strict';

  var STORAGE = 'ris-lang';
  var dict = {};
  var lang = 'en';
  var HOST = 'https://relocateinstyle.swiss';
  var LOCALES = { it: true, de: true };

  function pathParts() {
    return location.pathname.split('/').filter(Boolean);
  }

  function langIndex(parts) {
    parts = parts || pathParts();
    for (var i = 0; i < parts.length; i++) {
      if (LOCALES[parts[i]]) return i;
    }
    return -1;
  }

  function pathLang() {
    var i = langIndex();
    return i >= 0 ? pathParts()[i] : null;
  }

  function onLocalePath() {
    return pathLang() != null;
  }

  function inPreview() {
    return pathParts().indexOf('preview') >= 0;
  }

  function isFileSeg(seg) {
    return /\.[a-z0-9]+$/i.test(seg || '');
  }

  function basePrefix() {
    var parts = pathParts();
    var i = langIndex(parts);
    if (i >= 0) {
      var prefix = parts.slice(0, i).join('/');
      return prefix ? '/' + prefix + '/' : '/';
    }
    if (parts.length && isFileSeg(parts[parts.length - 1])) {
      parts = parts.slice(0, -1);
    }
    return parts.length ? '/' + parts.join('/') + '/' : '/';
  }

  function pageFile() {
    var parts = pathParts();
    var i = langIndex(parts);
    var rest = i >= 0 ? parts.slice(i + 1) : parts;
    var file = rest.length ? rest[rest.length - 1] : '';
    if (!isFileSeg(file)) return 'index.html';
    return file;
  }

  function pageId() {
    var file = pageFile().replace(/\.html$/i, '');
    return file === '' || file === 'index' ? 'home' : file;
  }

  function searchNoLang() {
    var params = new URLSearchParams(location.search);
    params.delete('lang');
    var qs = params.toString();
    return qs ? '?' + qs : '';
  }

  function enPath() {
    var file = pageFile();
    var base = basePrefix();
    return (file === 'index.html' ? base : base + file) + searchNoLang() + location.hash;
  }

  function localePath(code) {
    var file = pageFile();
    var base = basePrefix();
    return (file === 'index.html' ? base + code + '/' : base + code + '/' + file) + searchNoLang() + location.hash;
  }

  function itPath() {
    return localePath('it');
  }

  function dePath() {
    // German site lives only under /preview/de/
    var file = pageFile();
    if (inPreview()) {
      return localePath('de');
    }
    return (file === 'index.html' ? '/preview/de/' : '/preview/de/' + file) + searchNoLang() + location.hash;
  }

  function isBot() {
    return /bot|crawl|slurp|spider|googlebot/i.test(navigator.userAgent || '');
  }

  function detect() {
    var fromPath = pathLang();
    if (fromPath) return fromPath;
    try {
      var saved = (localStorage.getItem(STORAGE) || '').toLowerCase();
      if (saved === 'en' || saved === 'it') return saved;
      // German only under preview — live has no /de/
      if (saved === 'de' && inPreview()) return 'de';
    } catch (e) {}
    var nav = ((navigator.languages && navigator.languages[0]) || navigator.language || '').toLowerCase();
    if (!isBot()) {
      if (nav.indexOf('it') === 0) return 'it';
      if (nav.indexOf('de') === 0 && inPreview()) return 'de';
    }
    return 'en';
  }

  function t(key) {
    if (!key) return '';
    var cur = dict;
    var parts = key.split('.');
    for (var i = 0; i < parts.length; i++) {
      if (cur == null || typeof cur !== 'object' || !(parts[i] in cur)) return '';
      cur = cur[parts[i]];
    }
    return typeof cur === 'string' ? cur : '';
  }

  function apply() {
    document.documentElement.lang = lang;

    document.querySelectorAll('[data-i18n]').forEach(function (el) {
      var val = t(el.getAttribute('data-i18n'));
      if (val) el.textContent = val;
    });

    document.querySelectorAll('[data-i18n-html]').forEach(function (el) {
      var val = t(el.getAttribute('data-i18n-html'));
      if (val) el.innerHTML = val;
    });

    document.querySelectorAll('[data-i18n-aria]').forEach(function (el) {
      var val = t(el.getAttribute('data-i18n-aria'));
      if (val) el.setAttribute('aria-label', val);
    });

    document.querySelectorAll('[data-i18n-alt]').forEach(function (el) {
      var val = t(el.getAttribute('data-i18n-alt'));
      if (val) el.setAttribute('alt', val);
    });

    var meta = t('meta.' + pageId() + '.title');
    if (meta) document.title = meta;
    var desc = t('meta.' + pageId() + '.description');
    var descEl = document.querySelector('meta[name="description"]');
    if (desc && descEl) descEl.setAttribute('content', desc);

    document.querySelectorAll('input[name="_next"]').forEach(function (el) {
      try {
        var next = new URL(el.value, HOST);
        var path = next.pathname
          .replace(/^\/preview(?=\/|$)/, '')
          .replace(/^\/(it|de)(?=\/|$)/, '');
        var underPreview = inPreview();
        var prefix = underPreview ? '/preview' : '';
        if (lang === 'it' || lang === 'de') {
          next.pathname = prefix + '/' + lang + (path === '/' || path === '' ? '/' : path);
        } else {
          next.pathname = prefix + (path === '/' || path === '' ? '/' : path);
        }
        next.searchParams.delete('lang');
        el.value = next.toString();
      } catch (e) {}
    });

    document.querySelectorAll('.lang-switch a[hreflang]').forEach(function (a) {
      var code = a.getAttribute('hreflang');
      a.classList.toggle('is-active', code === lang);
      a.setAttribute('aria-current', code === lang ? 'true' : 'false');
      if (code === 'en') a.setAttribute('href', enPath());
      if (code === 'it') a.setAttribute('href', itPath());
      if (code === 'de') a.setAttribute('href', dePath());
    });

    document.documentElement.classList.remove('i18n-pending');
    document.dispatchEvent(new CustomEvent('ris:i18n', { detail: { lang: lang, t: t } }));
  }

  function switcherLabel() {
    if (lang === 'it') return 'Lingua';
    if (lang === 'de') return 'Sprache';
    return 'Language';
  }

  function injectSwitcher() {
    var nav = document.getElementById('nav');
    if (!nav || nav.querySelector('.lang-switch')) return;
    var wrap = document.createElement('nav');
    wrap.className = 'lang-switch';
    wrap.setAttribute('aria-label', switcherLabel());
    wrap.innerHTML =
      '<a class="lang-switch-opt" href="' + enPath() + '" hreflang="en" lang="en">EN</a>' +
      '<a class="lang-switch-opt" href="' + itPath() + '" hreflang="it" lang="it">IT</a>' +
      '<a class="lang-switch-opt" href="' + dePath() + '" hreflang="de" lang="de">DE</a>';
    var toggle = document.getElementById('nav-toggle');
    if (toggle) nav.insertBefore(wrap, toggle);
    else nav.appendChild(wrap);
  }

  function localeUrl(code) {
    var script = document.querySelector('script[src*="i18n.js"]');
    var base = script ? script.src.replace(/i18n\.js.*$/, '') : 'js/';
    return base + 'locales/' + code + '.json?v=9';
  }

  function load(code) {
    if (code === 'en') {
      dict = {};
      apply();
      return Promise.resolve();
    }
    return fetch(localeUrl(code))
      .then(function (res) {
        if (!res.ok) throw new Error('locale');
        return res.json();
      })
      .then(function (json) {
        dict = json || {};
        apply();
      })
      .catch(function () {
        dict = {};
        document.documentElement.classList.remove('i18n-pending');
      });
  }

  lang = detect();

  // Redirect to locale path when needed (DE only inside /preview/)
  if (lang !== 'en' && !onLocalePath() && !isBot()) {
    if (lang === 'de' && !inPreview()) {
      lang = 'en';
    } else {
      try { localStorage.setItem(STORAGE, lang); } catch (e) {}
      document.documentElement.classList.add('i18n-pending');
      location.replace(localePath(lang));
      return;
    }
  }

  document.documentElement.lang = lang;
  if (lang !== 'en') document.documentElement.classList.add('i18n-pending');

  window.RIS = {
    get lang() { return lang; },
    t: t
  };

  function boot() {
    injectSwitcher();
    document.addEventListener('click', function (e) {
      var a = e.target.closest('.lang-switch a[hreflang]');
      if (!a) return;
      try { localStorage.setItem(STORAGE, a.getAttribute('hreflang')); } catch (err) {}
    });
    load(lang);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
