/* ==========================================================================
   BODYNOX ACADEMY — main.js
   의존성 없음. index.html을 파일로 직접 열어도 동작합니다.
   ========================================================================== */
(function () {
  'use strict';

  var header = document.getElementById('siteHeader');
  var nav = document.getElementById('nav');
  var navToggle = document.getElementById('navToggle');
  var floatCta = document.querySelector('.float-cta');
  var navLinks = nav ? nav.querySelectorAll('.nav__list a') : [];

  /* ---------- 모바일 메뉴 ---------- */
  function closeNav() {
    if (!nav || !navToggle) return;
    nav.classList.remove('is-open');
    navToggle.setAttribute('aria-expanded', 'false');
    navToggle.setAttribute('aria-label', '메뉴 열기');
    document.body.classList.remove('is-locked');
  }

  function openNav() {
    if (!nav || !navToggle) return;
    nav.classList.add('is-open');
    navToggle.setAttribute('aria-expanded', 'true');
    navToggle.setAttribute('aria-label', '메뉴 닫기');
    document.body.classList.add('is-locked');
  }

  if (navToggle) {
    navToggle.addEventListener('click', function () {
      if (nav.classList.contains('is-open')) closeNav();
      else openNav();
    });
  }

  if (nav) {
    nav.addEventListener('click', function (e) {
      if (e.target.closest('a')) closeNav();
    });
  }

  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') closeNav();
  });

  // 데스크톱 폭으로 넓어지면 드로어 상태 해제
  var desktopMq = window.matchMedia('(min-width: 900px)');
  var onMqChange = function (e) { if (e.matches) closeNav(); };
  if (desktopMq.addEventListener) desktopMq.addEventListener('change', onMqChange);
  else if (desktopMq.addListener) desktopMq.addListener(onMqChange);

  /* ---------- 스크롤 상태 (헤더 테두리 / 플로팅 CTA) ---------- */
  var ticking = false;

  function onScroll() {
    var y = window.pageYOffset || document.documentElement.scrollTop;

    if (header) header.classList.toggle('is-scrolled', y > 8);
    if (floatCta) floatCta.classList.toggle('is-visible', y > window.innerHeight * 0.7);

    ticking = false;
  }

  window.addEventListener('scroll', function () {
    if (ticking) return;
    ticking = true;
    window.requestAnimationFrame(onScroll);
  }, { passive: true });

  onScroll();

  /* ---------- 스크롤 등장 애니메이션 ---------- */
  var revealItems = document.querySelectorAll('.reveal');

  if ('IntersectionObserver' in window) {
    var revealObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.classList.add('is-in');
        revealObserver.unobserve(entry.target);
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.12 });

    revealItems.forEach(function (el, i) {
      // 같은 그리드 안의 카드들이 순차적으로 나타나도록 약간의 지연
      el.style.transitionDelay = (i % 3) * 90 + 'ms';
      revealObserver.observe(el);
    });
  } else {
    revealItems.forEach(function (el) { el.classList.add('is-in'); });
  }

  /* ---------- 현재 섹션 내비게이션 하이라이트 ---------- */
  var sections = [];
  navLinks.forEach(function (link) {
    var id = link.getAttribute('href');
    if (!id || id.charAt(0) !== '#') return;
    var el = document.querySelector(id);
    if (el) sections.push({ link: link, el: el });
  });

  if (sections.length && 'IntersectionObserver' in window) {
    var navObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        sections.forEach(function (s) {
          s.link.classList.toggle('is-active', s.el === entry.target);
        });
      });
    }, { rootMargin: '-45% 0px -50% 0px', threshold: 0 });

    sections.forEach(function (s) { navObserver.observe(s.el); });
  }

  /* ---------- 푸터 연도 ---------- */
  var yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = String(new Date().getFullYear());

  /* ---------- 아직 연결되지 않은 링크(#) 안내 ---------- */
  document.querySelectorAll('a[href="#"]').forEach(function (a) {
    a.addEventListener('click', function (e) {
      e.preventDefault();
      window.alert('준비 중입니다. 실제 링크로 교체해 주세요.');
    });
  });

})();
