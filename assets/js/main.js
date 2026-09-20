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

  /* ---------- 히어로 사진 슬라이더 (3초 자동 전환) ---------- */
  (function heroSlider() {
    var track = document.getElementById('heroTrack');
    var dotsBox = document.getElementById('heroDots');
    if (!track) return;

    var slides = Array.prototype.slice.call(track.children);
    if (slides.length < 2) return;

    var INTERVAL = 3000;
    var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    // 마지막 -> 처음이 끊기지 않도록 첫 장을 복제해 뒤에 붙인다
    var clone = slides[0].cloneNode(true);
    clone.setAttribute('aria-hidden', 'true');
    var cloneImg = clone.querySelector('img');
    if (cloneImg) { cloneImg.setAttribute('alt', ''); cloneImg.removeAttribute('fetchpriority'); }
    track.appendChild(clone);

    var index = 0;
    var timer = null;
    var dots = [];

    function render(animate) {
      track.style.transition = animate ? '' : 'none';
      track.style.transform = 'translate3d(' + (-index * 100) + '%, 0, 0)';
      var active = index % slides.length;
      dots.forEach(function (d, i) {
        d.classList.toggle('is-active', i === active);
        d.setAttribute('aria-selected', i === active ? 'true' : 'false');
      });
    }

    function next() {
      index += 1;
      render(true);
    }

    function goTo(i) {
      index = i;
      render(true);
      restart();
    }

    // 복제 슬라이드에 도착하면 애니메이션 없이 처음으로 되돌린다
    track.addEventListener('transitionend', function (e) {
      if (e.propertyName !== 'transform') return;
      if (index === slides.length) {
        index = 0;
        render(false);
        void track.offsetWidth; // 리플로우로 transition 복구
        track.style.transition = '';
      }
    });

    function start() {
      if (reduceMotion || timer) return;
      timer = window.setInterval(next, INTERVAL);
    }
    function stop() {
      window.clearInterval(timer);
      timer = null;
    }
    function restart() { stop(); start(); }

    // 인디케이터
    if (dotsBox) {
      slides.forEach(function (_, i) {
        var b = document.createElement('button');
        b.type = 'button';
        b.className = 'slider__dot' + (i === 0 ? ' is-active' : '');
        b.setAttribute('role', 'tab');
        b.setAttribute('aria-label', (i + 1) + '번째 사진');
        b.setAttribute('aria-selected', i === 0 ? 'true' : 'false');
        b.addEventListener('click', function () { goTo(i); });
        dotsBox.appendChild(b);
        dots.push(b);
      });
    }

    // 마우스를 올리거나 포커스가 들어오면 멈춤
    var slider = document.getElementById('heroSlider');
    if (slider) {
      slider.addEventListener('mouseenter', stop);
      slider.addEventListener('mouseleave', start);
      slider.addEventListener('focusin', stop);
      slider.addEventListener('focusout', start);

      // 모바일 스와이프
      var startX = null;
      slider.addEventListener('touchstart', function (e) {
        startX = e.touches[0].clientX;
        stop();
      }, { passive: true });
      slider.addEventListener('touchend', function (e) {
        if (startX === null) return;
        var dx = e.changedTouches[0].clientX - startX;
        if (Math.abs(dx) > 40) {
          if (dx < 0) next();
          else goTo(index === 0 ? slides.length - 1 : index - 1);
        }
        startX = null;
        start();
      });
    }

    // 다른 탭에 있을 때는 돌리지 않는다
    document.addEventListener('visibilitychange', function () {
      if (document.hidden) stop(); else start();
    });

    render(false);
    track.style.transition = '';
    start();
  })();

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
