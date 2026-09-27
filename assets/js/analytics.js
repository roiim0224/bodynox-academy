/* ==========================================================================
   웹 분석 도구  —  ID 를 이 파일 한 곳에서만 관리합니다.

   · Google Analytics 4  : GA_ID
   · 네이버 애널리틱스     : NAVER_ID
   · Meta 픽셀           : META_IDS (여러 개 가능)

   Google Analytics 4  —  측정 ID 한 곳만 바꾸면 전 페이지에 적용됩니다.

   · 측정 ID 는 analytics.google.com > 관리 > 데이터 스트림 에서 확인합니다.
     형식: G- 로 시작하는 11자리 (예: G-ABCD123456)
   · 아래 GA_ID 가 자리표시자인 동안에는 gtag 를 전혀 불러오지 않습니다.
     (쿠키도 심지 않고 네트워크 요청도 보내지 않습니다)
   ========================================================================== */
(function () {
  'use strict';

  var GA_ID = 'G-C2H8VEPDVC';

  /* 자리표시자면 아무것도 하지 않는다 */
  var READY = /^G-[A-Z0-9]{6,12}$/.test(GA_ID) && GA_ID.indexOf('XXXX') === -1;

  window.dataLayer = window.dataLayer || [];
  function gtag() { window.dataLayer.push(arguments); }

  if (READY) {
    var s = document.createElement('script');
    s.async = true;
    s.src = 'https://www.googletagmanager.com/gtag/js?id=' + GA_ID;
    document.head.appendChild(s);

    gtag('js', new Date());
    gtag('config', GA_ID);
  }

  /* ---------- 네이버 애널리틱스 ----------
     GA4 가 주지 않는 네이버 검색 키워드를 보기 위해 함께 씁니다.
     analytics.naver.com > 설정 > 사이트 등록 에서 받은 wa 값입니다. */
  var NAVER_ID = '1221efa822081f0';

  if (/^[0-9a-f]{10,24}$/i.test(NAVER_ID)) {
    var n = document.createElement('script');
    n.async = true;
    n.src = 'https://wcs.pstatic.net/wcslog.js';
    n.onload = function () {
      if (!window.wcs_add) window.wcs_add = {};
      window.wcs_add.wa = NAVER_ID;
      if (window.wcs) window.wcs_do();
    };
    document.head.appendChild(n);
  }

  /* ---------- Meta 픽셀 ----------
     메타 광고의 전환 최적화 · 리타겟팅에 씁니다.
     business.facebook.com > 이벤트 관리자 > 데이터 세트 에서 확인합니다.
     형식: 15~16자리 숫자. 자리표시자면 아무것도 불러오지 않습니다.

     픽셀은 광고를 집행할 광고 계정과 같은 비즈니스 포트폴리오 소속이어야 한다.
     개인 광고 계정 소속으로 만들면 비즈니스 설정 목록에 뜨지 않아 붙일 수 없고,
     신규 포트폴리오는 파트너 공유(Assign partner)가 몇 주간 막혀 있어
     다른 포트폴리오의 광고 계정에 빌려줄 수도 없다. 둘 다 실제로 겪었다.
     그래서 포트폴리오별로 픽셀을 따로 두고 여기에 나란히 싣는다.

       2370021590146728  BPM 코리아      · 광고계정 bpm.bpdynox
       950102224820335   바디녹스 bodynox · 광고계정 877197163504179

     fbq 는 init 한 픽셀 전부로 track 을 보낸다. 배열에 추가만 하면 된다.

     자동 고급 매칭(이메일 · 전화번호를 해싱해 메타로 보내는 기능)은 켜지 않았습니다.
     켜려면 개인정보처리방침 제7조의 이전 항목을 먼저 고쳐야 합니다.

     건강 정보(체형 · 통증 · 질환)는 어떤 경우에도 메타로 보내지 않습니다.
     메타 비즈니스 도구 약관 위반이며 계정 정지 사유입니다. */
  var META_IDS = [
    '2370021590146728',
    '950102224820335'
  ].filter(function (id) { return /^[0-9]{15,16}$/.test(id); });

  var META_READY = META_IDS.length > 0;

  if (META_READY) {
    /* 메타가 제공하는 기본 스니펫 — fbq 스텁을 먼저 만들고 라이브러리는 비동기로 받습니다 */
    !function (f, b, e, v, n, t, s) {
      if (f.fbq) return;
      n = f.fbq = function () {
        n.callMethod ? n.callMethod.apply(n, arguments) : n.queue.push(arguments);
      };
      if (!f._fbq) f._fbq = n;
      n.push = n; n.loaded = !0; n.version = '2.0'; n.queue = [];
      t = b.createElement(e); t.async = !0; t.src = v;
      s = b.getElementsByTagName(e)[0];
      s.parentNode.insertBefore(t, s);
    }(window, document, 'script', 'https://connect.facebook.net/en_US/fbevents.js');

    META_IDS.forEach(function (id) { window.fbq('init', id); });
    window.fbq('track', 'PageView');
  }

  /* GA4 이벤트를 메타 표준 이벤트로 옮겨 함께 보냅니다.
     메타는 표준 이벤트라야 전환 최적화에 쓸 수 있어 이름을 바꿔 전달합니다. */
  function metaSend(name, p) {
    if (!META_READY || !window.fbq) return;
    p = p || {};

    switch (name) {
      case 'apply_click':
        window.fbq('track', 'ViewContent', {
          content_name: '교육 신청 페이지',
          content_category: p.spot || ''
        });
        break;

      case 'form_open':
        window.fbq('track', 'Lead', { content_name: '신청서 열기' });
        break;

      case 'form_submit':
        /* 추정값입니다(main.js 의 finish()). 구글폼이 다른 도메인이라 제출을 직접 읽을 수
           없어 iframe 의 두 번째 load 를 제출로 봅니다.
           구글폼 실제 응답 수와 대조하기 전에는 광고 최적화 기준으로 삼지 마세요. */
        window.fbq('track', 'CompleteRegistration', { content_name: '참가신청서' });
        break;

      case 'contact_click':
        window.fbq('track', 'Contact', { content_category: p.channel || '' });
        break;

      case 'payment_click':
        /* 결제 '시작' 입니다. 토스에서 완료 신호가 돌아오지 않아
           Purchase 는 보내지 않습니다. 보내면 결제하지 않은 클릭까지 매출로 잡힙니다. */
        window.fbq('track', 'InitiateCheckout', {
          value: 789000,
          currency: 'KRW',
          content_name: p.intake || ''
        });
        break;
    }
  }

  /* 다른 스크립트(main.js)에서 쓰는 공용 전송 함수 */
  window.bpmTrack = function (name, params) {
    metaSend(name, params);

    if (!READY) {
      if (window.console && console.debug) {
        console.debug('[bpmTrack] ' + name, params || {});
      }
      return;
    }
    gtag('event', name, params || {});
  };

  /* 버튼이 페이지 어디에 있었는지 — 가까운 조상으로 판별 */
  var SPOTS = [
    ['.nav__cta', '헤더'],
    ['.site-header', '헤더'],
    ['.hero__actions', '히어로'],
    ['.subhero__actions', '상단'],
    ['.cta-inline', '본문 중간 CTA'],
    ['.contact__actions', '문의 섹션'],
    ['#apply', '하단 신청 섹션'],
    ['.intake', '기수 카드'],
    ['.card', '과정 카드'],
    ['.section--dark', '하단 어두운 섹션'],
    ['.site-footer', '푸터']
  ];

  function spotOf(el) {
    for (var i = 0; i < SPOTS.length; i++) {
      if (el.closest(SPOTS[i][0])) return SPOTS[i][1];
    }
    return '기타';
  }

  document.addEventListener('click', function (e) {
    var a = e.target.closest ? e.target.closest('a[href]') : null;
    if (!a) return;

    /* ---------- 토스 결제 버튼 클릭 ---------- */
    if (a.href.indexOf('buy.tosspayments.com') !== -1) {
      /* 어느 기수 카드에서 눌렀는지 — .paypick__no 텍스트를 쓴다 */
      var label = a.querySelector('.paypick__no');
      window.bpmTrack('payment_click', {
        intake: label ? label.textContent.trim() : '(미상)',
        link_url: a.href,
        page_path: location.pathname
      });
      return;
    }

    /* ---------- 상담 채널 클릭 ----------
       카카오톡 · LINE · 전화 · 인스타그램을 channel 로 구분해 한 이벤트로 보냅니다.
       80기(방콕)는 결제 링크가 없어 상담이 유일한 전환 지점이므로 특히 필요합니다. */
    var channel = null;
    if (a.protocol === 'tel:') channel = '전화';
    else if (a.href.indexOf('pf.kakao.com') !== -1) channel = '카카오톡';
    else if (a.href.indexOf('lin.ee') !== -1) channel = 'LINE';
    else if (a.href.indexOf('instagram.com') !== -1) channel = '인스타그램';

    if (channel) {
      window.bpmTrack('contact_click', {
        channel: channel,
        spot: spotOf(a),
        page_path: location.pathname
      });
      return;
    }

    /* ---------- 교육 신청 버튼 클릭 ---------- */
    if (/\/apply\.html(?:[?#]|$)/.test(a.pathname + a.search + a.hash) &&
        !/\/apply\.html$/.test(location.pathname)) {
      window.bpmTrack('apply_click', {
        spot: spotOf(a),
        label: (a.textContent || '').replace(/\s+/g, ' ').trim(),
        page_path: location.pathname
      });
    }
  });
})();
