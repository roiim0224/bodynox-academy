/* ==========================================================================
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

  /* 다른 스크립트(main.js)에서 쓰는 공용 전송 함수 */
  window.bpmTrack = function (name, params) {
    if (!READY) {
      if (window.console && console.debug) {
        console.debug('[bpmTrack] ' + name, params || {});
      }
      return;
    }
    gtag('event', name, params || {});
  };

  /* ---------- 토스 결제 버튼 클릭 ---------- */
  document.addEventListener('click', function (e) {
    var a = e.target.closest ? e.target.closest('a[href]') : null;
    if (!a) return;
    if (a.href.indexOf('buy.tosspayments.com') === -1) return;

    /* 어느 기수 카드에서 눌렀는지 — .paypick__no 텍스트를 쓴다 */
    var label = a.querySelector('.paypick__no');
    var intake = label ? label.textContent.trim() : '(미상)';

    window.bpmTrack('payment_click', {
      intake: intake,
      link_url: a.href,
      page_path: location.pathname
    });
  });
})();
