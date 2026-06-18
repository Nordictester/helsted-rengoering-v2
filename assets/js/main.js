(function () {
  'use strict';

  var toggle = document.getElementById('navToggle');
  var nav = document.getElementById('mainNav');
  var overlay = document.getElementById('navOverlay');

  function closeNav() {
    if (!nav) return;
    nav.classList.remove('open');
    if (overlay) overlay.classList.remove('show');
    if (toggle) toggle.setAttribute('aria-expanded', 'false');
    document.body.style.overflow = '';
  }

  function openNav() {
    if (!nav) return;
    nav.classList.add('open');
    if (overlay) overlay.classList.add('show');
    if (toggle) toggle.setAttribute('aria-expanded', 'true');
    document.body.style.overflow = 'hidden';
  }

  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      if (nav.classList.contains('open')) closeNav();
      else openNav();
    });
  }

  if (overlay) overlay.addEventListener('click', closeNav);

  if (nav) {
    nav.querySelectorAll('a').forEach(function (a) {
      a.addEventListener('click', closeNav);
    });
  }

  var scrollBtn = document.getElementById('scrollTop');
  if (scrollBtn) {
    window.addEventListener('scroll', function () {
      scrollBtn.classList.toggle('show', window.scrollY > 400);
    });
    scrollBtn.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  var form = document.getElementById('contactForm');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var btn = form.querySelector('button[type="submit"]');
      var success = document.getElementById('formSuccess');
      if (btn) {
        btn.textContent = 'Sender...';
        btn.disabled = true;
      }
      fetch('/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
        body: new URLSearchParams(new FormData(form)).toString()
      })
        .then(function () {
          if (success) success.style.display = 'block';
          form.reset();
          if (btn) {
            btn.textContent = 'Sendt!';
            btn.disabled = true;
          }
        })
        .catch(function () {
          if (btn) {
            btn.textContent = 'Send besked';
            btn.disabled = false;
          }
          alert('Kunne ikke sende — ring til os på 20 80 18 50');
        });
    });
  }

  /* Tema (lys / mørk) */
  var THEME_KEY = 'helsted-theme';
  var root = document.documentElement;
  var themeBtn = document.getElementById('themeToggle');

  function getTheme() {
    return localStorage.getItem(THEME_KEY) || 'light';
  }

  function updateThemeButton(theme) {
    if (!themeBtn) return;
    themeBtn.textContent = theme === 'dark' ? '☀️' : '🌙';
    themeBtn.setAttribute(
      'aria-label',
      theme === 'dark' ? 'Skift til lyst tema' : 'Skift til mørkt tema'
    );
  }

  function applyTheme(theme) {
    if (theme === 'dark') root.setAttribute('data-theme', 'dark');
    else root.removeAttribute('data-theme');
    localStorage.setItem(THEME_KEY, theme);
    updateThemeButton(theme);
  }

  applyTheme(getTheme());

  if (themeBtn) {
    themeBtn.addEventListener('click', function () {
      applyTheme(getTheme() === 'dark' ? 'light' : 'dark');
    });
  }

  /* Scroll-animationer */
  var reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (!reduced) {
    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (e) {
          if (e.isIntersecting) {
            e.target.classList.add('visible');
            observer.unobserve(e.target);
          }
        });
      },
      { threshold: 0.1, rootMargin: '0px 0px -40px 0px' }
    );
    document.querySelectorAll('.fade-in').forEach(function (el) {
      observer.observe(el);
    });
  } else {
    document.querySelectorAll('.fade-in').forEach(function (el) {
      el.classList.add('visible');
    });
  }
})();